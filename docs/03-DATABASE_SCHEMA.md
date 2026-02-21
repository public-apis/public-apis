# RadBites - Database Schema

**Version**: 1.0
**Date**: 2025-11-11
**Database**: Supabase (PostgreSQL 15)
**Extensions**: pgvector (RAG embeddings)

---

## 📋 Overview

RadBites utilise **Supabase** (PostgreSQL) avec l'extension **pgvector** pour :
- Stockage utilisateurs & authentification (Supabase Auth)
- Recettes générées & favoris
- **RAG (Retrieval-Augmented Generation)** : Embeddings vectoriels pour améliorer qualité LLM
- Analytics & usage tracking

---

## 🏗️ Schema Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Supabase Auth                            │
│  (Géré automatiquement par Supabase)                        │
│  • auth.users (table système)                               │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                   public.users                               │
│  Extension du profil utilisateur                            │
│  • subscription_tier, quotas, préférences                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ↓             ↓             ↓
┌──────────────┐ ┌───────────┐ ┌──────────────┐
│user_preferences recipes    │usage_events  │
│(1:1)         │ │(1:N)      │ │(1:N)         │
└──────────────┘ └───────────┘ └──────────────┘
                       │
                       ↓ (pgvector)
                 ┌──────────────┐
                 │ Embeddings   │
                 │ (RAG search) │
                 └──────────────┘
```

---

## 📊 Tables Détaillées

### 1. `public.users`

Extension du profil utilisateur (complète `auth.users`).

```sql
CREATE TABLE public.users (
  -- Primary Key (sync avec auth.users)
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,

  -- Subscription & Billing
  subscription_tier TEXT NOT NULL DEFAULT 'free'
    CHECK (subscription_tier IN ('free', 'trial', 'premium')),
  subscription_id TEXT UNIQUE, -- Stripe subscription ID
  subscription_ends_at TIMESTAMPTZ, -- Pour abonnements non-récurrents
  trial_ends_at TIMESTAMPTZ, -- Date fin trial
  has_used_trial BOOLEAN NOT NULL DEFAULT false, -- 1 trial par user

  -- Freemium Quota Management
  weekly_generations_count INTEGER NOT NULL DEFAULT 0,
  last_quota_reset_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  -- Metadata
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  last_login_at TIMESTAMPTZ,

  -- Analytics
  total_recipes_generated INTEGER NOT NULL DEFAULT 0,
  total_recipes_saved INTEGER NOT NULL DEFAULT 0
);

-- Indexes
CREATE INDEX idx_users_subscription_tier ON public.users(subscription_tier);
CREATE INDEX idx_users_trial_ends_at ON public.users(trial_ends_at)
  WHERE subscription_tier = 'trial';

-- Row Level Security (RLS)
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

-- Policy : Users can only read/update their own data
CREATE POLICY "Users can view own profile"
  ON public.users FOR SELECT
  USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
  ON public.users FOR UPDATE
  USING (auth.uid() = id);

-- Trigger : Auto-update updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_updated_at
  BEFORE UPDATE ON public.users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

---

### 2. `public.user_preferences`

Préférences culinaires de l'utilisateur (allergies, régimes, etc.).

```sql
CREATE TABLE public.user_preferences (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,

  -- Dietary Restrictions
  allergies TEXT[] DEFAULT '{}', -- Ex: ['gluten', 'lactose', 'nuts']
  diet_type TEXT, -- 'omnivore' | 'vegetarian' | 'vegan' | 'pescatarian' | 'keto' | 'paleo'

  -- Cooking Preferences
  skill_level TEXT DEFAULT 'intermediate'
    CHECK (skill_level IN ('beginner', 'intermediate', 'expert')),
  max_cooking_time INTEGER DEFAULT 45, -- minutes
  favorite_cuisines TEXT[] DEFAULT '{}', -- Ex: ['italian', 'asian', 'french']

  -- Goals
  goals TEXT[] DEFAULT '{}', -- Ex: ['save_time', 'eat_healthy', 'discover', 'impress']

  -- Metadata
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  -- Constraint : 1 preference per user
  UNIQUE(user_id)
);

-- Indexes
CREATE INDEX idx_user_preferences_user_id ON public.user_preferences(user_id);

-- RLS
ALTER TABLE public.user_preferences ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can manage own preferences"
  ON public.user_preferences
  USING (auth.uid() = user_id);

-- Trigger : Auto-update updated_at
CREATE TRIGGER update_user_preferences_updated_at
  BEFORE UPDATE ON public.user_preferences
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

---

### 3. `public.recipes`

Recettes générées par l'IA (core data).

```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE public.recipes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,

  -- Recipe Content
  title TEXT NOT NULL,
  description TEXT, -- Optional short description
  image_url TEXT, -- Unsplash ou placeholder

  -- Ingredients (JSONB for flexibility)
  ingredients JSONB NOT NULL, -- [{name, quantity, unit}, ...]
  /*
  Example:
  [
    {"name": "poulet", "quantity": 500, "unit": "g"},
    {"name": "carottes", "quantity": 3, "unit": "pièce"},
    {"name": "crème", "quantity": 200, "unit": "ml"}
  ]
  */

  -- Steps (JSONB array)
  steps JSONB NOT NULL, -- ["Step 1", "Step 2", ...]
  /*
  Example:
  [
    "Préchauffer le four à 180°C",
    "Couper les carottes en rondelles",
    "Faire revenir le poulet 5 min",
    ...
  ]
  */

  -- Recipe Metadata
  difficulty TEXT NOT NULL DEFAULT 'medium'
    CHECK (difficulty IN ('easy', 'medium', 'hard')),
  cooking_time INTEGER NOT NULL, -- minutes
  prep_time INTEGER, -- minutes (optional)
  servings INTEGER NOT NULL DEFAULT 4,
  dish_type TEXT, -- 'starter' | 'main' | 'side' | 'dessert'

  -- Nutrition Info (JSONB)
  nutrition JSONB,
  /*
  Example:
  {
    "calories": 450,
    "protein": 38,
    "carbs": 25,
    "fat": 18,
    "fiber": 4
  }
  */

  -- Tips & Variations
  tips TEXT, -- Chef's tips (1-2 phrases LLM)
  variations JSONB, -- Optional variations suggérées
  /*
  Example:
  [
    {"name": "Version épicée", "changes": "Ajouter piment"},
    {"name": "Version légère", "changes": "Crème → yaourt grec"}
  ]
  */

  -- Generation Context
  generation_mode TEXT NOT NULL
    CHECK (generation_mode IN ('fridge', 'mood')),
  input_data JSONB NOT NULL,
  /*
  For 'fridge': {"ingredients": ["poulet", "carottes"], "constraints": {...}}
  For 'mood': {"mood": "réconfortant et épicé", "constraints": {...}}
  */

  -- User Interaction
  is_favorite BOOLEAN NOT NULL DEFAULT false,
  quality_rating INTEGER CHECK (quality_rating BETWEEN 1 AND 5),
  user_feedback TEXT, -- Optional feedback si problème

  -- RAG : Vector Embedding (for semantic search)
  embedding vector(1536), -- OpenAI ada-002 = 1536 dimensions

  -- Metadata
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_recipes_user_id ON public.recipes(user_id);
CREATE INDEX idx_recipes_is_favorite ON public.recipes(user_id, is_favorite)
  WHERE is_favorite = true;
CREATE INDEX idx_recipes_created_at ON public.recipes(created_at DESC);
CREATE INDEX idx_recipes_generation_mode ON public.recipes(generation_mode);

-- Vector Index (HNSW pour performance)
CREATE INDEX idx_recipes_embedding ON public.recipes
  USING hnsw (embedding vector_cosine_ops);

-- Full-text search index (recherche par titre/description)
CREATE INDEX idx_recipes_search ON public.recipes
  USING gin(to_tsvector('french', title || ' ' || COALESCE(description, '')));

-- RLS
ALTER TABLE public.recipes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own recipes"
  ON public.recipes FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can create own recipes"
  ON public.recipes FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own recipes"
  ON public.recipes FOR UPDATE
  USING (auth.uid() = user_id);

CREATE POLICY "Users can delete own recipes"
  ON public.recipes FOR DELETE
  USING (auth.uid() = user_id);

-- Public recipe sharing (optional, future feature)
-- Allow reading shared recipes
CREATE POLICY "Anyone can view shared recipes"
  ON public.recipes FOR SELECT
  USING (is_favorite = true); -- Example : favoris = publics (à adapter)

-- Trigger : Auto-update updated_at
CREATE TRIGGER update_recipes_updated_at
  BEFORE UPDATE ON public.recipes
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

---

### 4. `public.usage_events`

Analytics & tracking des événements utilisateur.

```sql
CREATE TABLE public.usage_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES public.users(id) ON DELETE SET NULL, -- Nullable (anonymous events)

  -- Event Data
  event_type TEXT NOT NULL, -- 'recipe_generated' | 'recipe_saved' | 'paywall_shown' | etc.
  event_data JSONB, -- Contexte additionnel (mode, tier, etc.)
  /*
  Example:
  {
    "generation_mode": "fridge",
    "user_tier": "free",
    "ingredients_count": 5
  }
  */

  -- Metadata
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_usage_events_user_id ON public.usage_events(user_id);
CREATE INDEX idx_usage_events_type ON public.usage_events(event_type);
CREATE INDEX idx_usage_events_created_at ON public.usage_events(created_at DESC);

-- RLS : Analytics table, lecture restreinte aux admins
ALTER TABLE public.usage_events ENABLE ROW LEVEL SECURITY;

-- Users can create their own events
CREATE POLICY "Users can create own events"
  ON public.usage_events FOR INSERT
  WITH CHECK (auth.uid() = user_id OR user_id IS NULL);

-- Only admins can read (ou service role)
-- (Pas de policy SELECT = only service_role/postgres can read)
```

---

### 5. `public.culinary_knowledge` (RAG Knowledge Base)

Base de connaissances culinaires pour enrichir le RAG.

```sql
CREATE TABLE public.culinary_knowledge (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Knowledge Entry
  category TEXT NOT NULL, -- 'technique' | 'ingredient_pairing' | 'substitution' | 'cuisine_style'
  title TEXT NOT NULL,
  content TEXT NOT NULL, -- Description détaillée

  -- Examples
  examples JSONB, -- Exemples concrets
  /*
  Example pour 'substitution':
  {
    "original": "beurre",
    "alternatives": [
      {"name": "huile d'olive", "ratio": "0.75", "note": "Plus sain"},
      {"name": "compote de pommes", "ratio": "1", "note": "Version vegan"}
    ]
  }
  */

  -- Tags for filtering
  tags TEXT[] DEFAULT '{}',

  -- Vector Embedding
  embedding vector(1536),

  -- Metadata
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_culinary_knowledge_category ON public.culinary_knowledge(category);
CREATE INDEX idx_culinary_knowledge_embedding ON public.culinary_knowledge
  USING hnsw (embedding vector_cosine_ops);

-- RLS : Read-only for users
ALTER TABLE public.culinary_knowledge ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can read culinary knowledge"
  ON public.culinary_knowledge FOR SELECT
  TO authenticated
  USING (true);

-- Only service_role can insert/update (seed data)
```

---

## 🔍 RAG Functions

### Vector Similarity Search

Fonction pour rechercher des recettes similaires (RAG).

```sql
-- Function: Match recipes by embedding similarity
CREATE OR REPLACE FUNCTION match_recipes(
  query_embedding vector(1536),
  match_threshold float DEFAULT 0.7,
  match_count int DEFAULT 5,
  filter_user_id uuid DEFAULT NULL
)
RETURNS TABLE (
  id uuid,
  title text,
  similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    r.id,
    r.title,
    1 - (r.embedding <=> query_embedding) AS similarity
  FROM public.recipes r
  WHERE
    (filter_user_id IS NULL OR r.user_id = filter_user_id)
    AND r.embedding IS NOT NULL
    AND 1 - (r.embedding <=> query_embedding) > match_threshold
  ORDER BY r.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;

-- Usage example:
/*
SELECT * FROM match_recipes(
  query_embedding := embedding_from_openai('poulet carottes'),
  match_threshold := 0.75,
  match_count := 3,
  filter_user_id := auth.uid()
);
*/
```

### Match Culinary Knowledge

```sql
CREATE OR REPLACE FUNCTION match_culinary_knowledge(
  query_embedding vector(1536),
  category_filter text DEFAULT NULL,
  match_threshold float DEFAULT 0.7,
  match_count int DEFAULT 5
)
RETURNS TABLE (
  id uuid,
  title text,
  content text,
  category text,
  similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    ck.id,
    ck.title,
    ck.content,
    ck.category,
    1 - (ck.embedding <=> query_embedding) AS similarity
  FROM public.culinary_knowledge ck
  WHERE
    (category_filter IS NULL OR ck.category = category_filter)
    AND ck.embedding IS NOT NULL
    AND 1 - (ck.embedding <=> query_embedding) > match_threshold
  ORDER BY ck.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
```

---

## ⚙️ Database Functions & Triggers

### 1. Reset Weekly Quotas (Cron Job)

```sql
-- Function to reset freemium quotas (called by cron every Monday 00:00)
CREATE OR REPLACE FUNCTION reset_weekly_quotas()
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE public.users
  SET
    weekly_generations_count = 0,
    last_quota_reset_at = NOW()
  WHERE
    subscription_tier = 'free'
    AND EXTRACT(DOW FROM NOW()) = 1 -- Monday
    AND EXTRACT(HOUR FROM NOW()) = 0;
END;
$$;

-- Schedule via Supabase Edge Function + Cron (or Vercel Cron)
```

### 2. Expire Trials

```sql
-- Function to expire trials (called daily)
CREATE OR REPLACE FUNCTION expire_trials()
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE public.users
  SET
    subscription_tier = 'free',
    trial_ends_at = NULL
  WHERE
    subscription_tier = 'trial'
    AND trial_ends_at < NOW();
END;
$$;
```

### 3. Auto-increment counters

```sql
-- Trigger : Increment total_recipes_generated after insert
CREATE OR REPLACE FUNCTION increment_recipe_count()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE public.users
  SET total_recipes_generated = total_recipes_generated + 1
  WHERE id = NEW.user_id;
  RETURN NEW;
END;
$$;

CREATE TRIGGER increment_recipe_count_trigger
  AFTER INSERT ON public.recipes
  FOR EACH ROW
  EXECUTE FUNCTION increment_recipe_count();

-- Trigger : Increment total_recipes_saved when favorited
CREATE OR REPLACE FUNCTION increment_saved_count()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  IF NEW.is_favorite = true AND (OLD.is_favorite = false OR OLD.is_favorite IS NULL) THEN
    UPDATE public.users
    SET total_recipes_saved = total_recipes_saved + 1
    WHERE id = NEW.user_id;
  ELSIF NEW.is_favorite = false AND OLD.is_favorite = true THEN
    UPDATE public.users
    SET total_recipes_saved = total_recipes_saved - 1
    WHERE id = NEW.user_id;
  END IF;
  RETURN NEW;
END;
$$;

CREATE TRIGGER increment_saved_count_trigger
  AFTER UPDATE ON public.recipes
  FOR EACH ROW
  WHEN (OLD.is_favorite IS DISTINCT FROM NEW.is_favorite)
  EXECUTE FUNCTION increment_saved_count();
```

---

## 🌱 Seed Data

### Culinary Knowledge (Example)

```sql
-- Seed : Techniques culinaires
INSERT INTO public.culinary_knowledge (category, title, content, tags, examples) VALUES
(
  'technique',
  'Caramélisation',
  'La caramélisation est le processus de cuisson du sucre à haute température pour obtenir une couleur dorée et un goût complexe. Applicable aux légumes (oignons, carottes) et aux viandes.',
  ARRAY['technique', 'cuisson', 'sucre'],
  '{"examples": ["Oignons caramélisés", "Carottes confites", "Crème brûlée"]}'::jsonb
),
(
  'substitution',
  'Remplacer le beurre',
  'Le beurre peut être remplacé par de l''huile d''olive (3/4 de la quantité), de la compote de pommes (même quantité, version vegan), ou de l''avocat écrasé (même quantité, plus sain).',
  ARRAY['substitution', 'beurre', 'vegan'],
  '{"original": "beurre", "alternatives": [{"name": "huile d''olive", "ratio": "0.75"}, {"name": "compote de pommes", "ratio": "1"}]}'::jsonb
),
(
  'ingredient_pairing',
  'Poulet et agrumes',
  'Le poulet se marie exceptionnellement bien avec les agrumes (citron, orange, pamplemousse) qui apportent de la fraîcheur et de l''acidité pour équilibrer le gras.',
  ARRAY['accord', 'poulet', 'agrumes'],
  '{"pairings": ["Poulet au citron", "Poulet à l''orange", "Poulet mariné au pamplemousse"]}'::jsonb
);

-- Generate embeddings for these entries (via API call OpenAI)
-- Example in application code:
/*
const embedding = await openai.embeddings.create({
  model: 'text-embedding-ada-002',
  input: `${title}: ${content}`
});

await supabase
  .from('culinary_knowledge')
  .update({ embedding: embedding.data[0].embedding })
  .eq('id', id);
*/
```

---

## 📈 Views (Optional)

### User Stats View

```sql
CREATE OR REPLACE VIEW user_stats AS
SELECT
  u.id,
  u.subscription_tier,
  u.weekly_generations_count,
  u.total_recipes_generated,
  u.total_recipes_saved,
  COUNT(r.id) AS total_recipes,
  COUNT(r.id) FILTER (WHERE r.is_favorite = true) AS favorite_count,
  AVG(r.quality_rating) AS avg_rating
FROM public.users u
LEFT JOIN public.recipes r ON r.user_id = u.id
GROUP BY u.id;

-- Usage: SELECT * FROM user_stats WHERE id = auth.uid();
```

---

## 🔒 Row Level Security (RLS) Summary

| Table | Policy | Description |
|-------|--------|-------------|
| **users** | SELECT/UPDATE own | Users can only access leur propre profil |
| **user_preferences** | Full access own | CRUD complet sur leurs préférences |
| **recipes** | Full access own | CRUD complet sur leurs recettes |
| **recipes** | SELECT shared | Lecture des recettes partagées publiquement (future) |
| **usage_events** | INSERT own | Users peuvent logger leurs événements |
| **culinary_knowledge** | SELECT all | Lecture seule pour tous users authentifiés |

---

## 🚀 Migration Strategy

### Initial Setup

```sql
-- 1. Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- 2. Create tables in order
-- (users → user_preferences → recipes → usage_events → culinary_knowledge)

-- 3. Create indexes

-- 4. Enable RLS & policies

-- 5. Create functions & triggers

-- 6. Seed culinary_knowledge

-- 7. (Optional) Create views
```

### Supabase CLI

```bash
# Initialize Supabase
supabase init

# Link to project
supabase link --project-ref your-project-ref

# Create migration
supabase migration new initial_schema

# Apply migration
supabase db push

# Generate TypeScript types
supabase gen types typescript --local > types/database.types.ts
```

---

## 📊 Database Monitoring

### Key Metrics

- **Table sizes** : Monitor `recipes` growth (embeddings = heavy)
- **Query performance** : EXPLAIN ANALYZE on vector searches
- **Index usage** : pg_stat_user_indexes
- **RLS performance** : Ensure policies optimisées

### Optimization Tips

1. **Vector indexes** : HNSW est rapide mais consomme mémoire
2. **JSONB indexes** : GIN indexes si recherche fréquente dans JSONB
3. **Partitioning** : Partitionner `usage_events` par date si volume élevé
4. **Archive old data** : Archiver recettes > 1 an (cold storage)

---

## 🔐 Backup Strategy

- **Supabase** : Daily automatic backups (7 jours retention)
- **Critical data** : `users`, `recipes` (embeddings = recréables)
- **Manual backups** : Export régulier via `pg_dump`

```bash
# Backup via Supabase CLI
supabase db dump -f backup_$(date +%Y%m%d).sql

# Restore
psql -h db.your-project.supabase.co -U postgres -f backup.sql
```

---

## ✅ Schema Validation Checklist

- [ ] All tables created
- [ ] pgvector extension enabled
- [ ] Indexes created (standard + vector)
- [ ] RLS enabled on all tables
- [ ] RLS policies configured
- [ ] Triggers functional (updated_at, counters)
- [ ] Functions tested (match_recipes, quotas)
- [ ] Seed data inserted (culinary_knowledge)
- [ ] TypeScript types generated
- [ ] Backup strategy configured

---

## 📚 TypeScript Types (Auto-generated)

```typescript
// types/database.types.ts (generated via supabase gen types)
export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      users: {
        Row: {
          id: string
          subscription_tier: 'free' | 'trial' | 'premium'
          subscription_id: string | null
          weekly_generations_count: number
          // ...
        }
        Insert: {
          id: string
          subscription_tier?: 'free' | 'trial' | 'premium'
          // ...
        }
        Update: {
          subscription_tier?: 'free' | 'trial' | 'premium'
          // ...
        }
      }
      recipes: {
        Row: {
          id: string
          user_id: string
          title: string
          ingredients: Json
          steps: Json
          difficulty: 'easy' | 'medium' | 'hard'
          cooking_time: number
          // ...
        }
        // ...
      }
      // ...
    }
    Views: {
      user_stats: {
        Row: {
          id: string
          total_recipes: number
          avg_rating: number | null
          // ...
        }
      }
    }
    Functions: {
      match_recipes: {
        Args: {
          query_embedding: number[]
          match_threshold?: number
          match_count?: number
          filter_user_id?: string
        }
        Returns: {
          id: string
          title: string
          similarity: number
        }[]
      }
    }
  }
}
```

---

## 🎯 Next Steps

1. **Apply schema** : Run migrations via Supabase CLI
2. **Test queries** : Validate RLS, vector search performance
3. **Seed data** : Insert culinary_knowledge with embeddings
4. **Generate types** : TypeScript types for frontend
5. **Setup monitoring** : Supabase dashboard + custom alerts

---

*RadBites Database Schema - Production Ready*
*Version 1.0 | 2025-11-11*
