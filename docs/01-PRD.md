# RadBites - Product Requirements Document (PRD)

**Version**: 1.0
**Date**: 2025-11-11
**Product Owner**: [Your Name]
**Status**: Draft → Review → Approved

---

## 📋 Executive Summary

**RadBites** est une PWA mobile-first qui révolutionne la cuisine quotidienne en utilisant l'IA générative pour créer des recettes personnalisées à partir des ingrédients disponibles ou des envies culinaires de l'utilisateur.

### Vision Produit
Transformer chaque repas en expérience créative en combinant :
- **APIs publiques** pour des données nutritionnelles fiables
- **RAG (Retrieval-Augmented Generation)** pour l'apprentissage continu
- **LLM open source** (Groq/Together AI) pour la créativité culinaire

### Problème Résolu
- 40% des français ne savent pas quoi cuisiner chaque soir
- Gaspillage alimentaire : 30kg/personne/an
- 2h/semaine perdues à planifier les repas
- Apps existantes = bases de données statiques, pas de créativité

### Solution
RadBites **invente** des recettes originales adaptées à vos ingrédients, contraintes et envies, plutôt que de chercher dans une base de données figée.

---

## 🎯 Objectifs Produit

### Objectifs Business (6 mois)
- **10,000 utilisateurs** actifs mensuels
- **15% conversion** free → premium (trial 7j)
- **<30% churn** mensuel (engagement 6 mois)
- **CAC < €5** (acquisition organique + viralité)
- **LTV > €35** (6 mois @ €4.99/mois)

### Objectifs Utilisateur
- **Génération recette < 10 secondes** (expérience fluide)
- **3+ recettes générées/utilisateur/semaine** (engagement)
- **NPS > 50** (satisfaction)
- **80% des recettes jugées "excellentes" ou "bonnes"** (qualité)

### Objectifs Techniques
- **PWA installable** sur iOS/Android
- **Offline-capable** (consultation recettes sauvegardées)
- **Performance** : Lighthouse > 90 (mobile)
- **Coût LLM < €0.02/recette** (open source Groq/Together)

---

## 👥 Target Users

### Persona Primaire : "Sarah, 32 ans, Working Mom"
- **Contexte** : Travaille, 2 enfants, manque de temps
- **Pain points** : Ne sait jamais quoi cuisiner, gaspille des aliments
- **Goals** : Gagner du temps, cuisiner varié, réduire budget courses
- **Usage** : 4-5x/semaine, soir après le travail
- **Freemium → Premium** : Oui, si gain temps réel

### Persona Secondaire : "Tom, 25 ans, Foodie Créatif"
- **Contexte** : Célibataire, aime cuisiner, partage sur Instagram
- **Pain points** : Manque d'inspiration, veut être original
- **Goals** : Découvrir techniques, impressionner amis
- **Usage** : Week-end, événements spéciaux
- **Freemium → Premium** : Oui, si recettes vraiment uniques

### Persona Tertiaire : "Marie, 45 ans, Régime Spécifique"
- **Contexte** : Diabétique, doit contrôler glucides
- **Pain points** : Difficile de trouver recettes adaptées
- **Goals** : Manger sain sans frustration
- **Usage** : Quotidien, planification hebdo
- **Freemium → Premium** : Oui, besoin adaptations précises

---

## 🚀 Product Strategy

### Phase 1 : MVP (Semaines 1-4)
**Objectif** : Valider le concept "AI Recipe Generation"

**Features** :
- ✅ Mode Frigo (input ingrédients → recette)
- ✅ Mode Envie (description envie → recette)
- ✅ Sauvegarde favoris (3 max en free, illimité premium)
- ✅ Authentification Supabase (email/password + social)
- ✅ Freemium : 5 générations/semaine
- ✅ Trial 7 jours (accès complet)

**Success Metrics** :
- 100 beta users
- 3+ recettes/user/semaine
- 10% activation (génère au moins 1 recette)

### Phase 2 : Growth Features (Semaines 5-8)
**Objectif** : Augmenter engagement et conversion

**Features** :
- Plans hebdomadaires (premium)
- Liste de courses auto-générée (premium)
- Adaptations allergies/régimes (premium)
- Mode famille (ajustement portions)
- Partage social (recettes)
- Variations de recettes (remix)

**Success Metrics** :
- 1,000 users
- 15% conversion trial → paid
- <40% churn mensuel

### Phase 3 : Scale & Retention (Semaines 9-16)
**Objectif** : Optimiser rétention et viralité

**Features** :
- Community (partage/like recettes users)
- Défis culinaires hebdomadaires
- Intégration courses en ligne (Carrefour API)
- Mode batch cooking (meal prep)
- Analytics nutrition (suivi hebdo)
- Mode coach (progression culinaire)

**Success Metrics** :
- 10,000 users
- <30% churn
- NPS > 50
- Viralité K-factor > 0.3

---

## 🏗️ Core Features (MVP)

### Feature 1 : Mode Frigo 🥕

**Description** :
L'utilisateur input les ingrédients disponibles, l'IA génère une recette créative.

**User Flow** :
```
1. User clique "Mode Frigo"
2. Tape ou sélectionne ingrédients (autocomplete)
   → Ex: "Poulet, carottes, crème, oignons"
3. (Optionnel) Ajoute contraintes :
   - Temps de cuisson max
   - Difficulté
   - Préférences (épicé, léger, etc.)
4. Clique "Générer"
5. Loading (8-10s) avec animation fun
6. Recette apparaît :
   - Titre créatif
   - Photo générée (Unsplash API ou DALL-E si budget)
   - Temps / Difficulté / Portions
   - Liste ingrédients + quantités
   - Steps numérotés
   - Tips du chef (insight LLM)
   - Nutrition (calories, macros)
7. Actions :
   - ❤️ Sauvegarder
   - 🔄 Régénérer (variante)
   - 📤 Partager
```

**Acceptance Criteria** :
- ✅ Génération < 10 secondes (95e percentile)
- ✅ Recette complète (titre, ingrédients, steps, nutrition)
- ✅ Recette cohérente (pas d'hallucinations graves)
- ✅ Sauvegarde persistante (Supabase)
- ✅ Freemium : Max 5 générations/semaine
- ✅ Paywall clair après quota épuisé

**Technical Implementation** :
```typescript
// Architecture RAG Hybrid
async function generateRecipeFromFridge(
  ingredients: string[],
  constraints: RecipeConstraints,
  userContext: UserContext
) {
  // 1. Enrichment via APIs
  const nutritionData = await edamam.getNutrition(ingredients);
  const substitutions = await spoonacular.getSubstitutions(ingredients);
  const inspiration = await mealDB.getSimilarRecipes(ingredients);

  // 2. Build RAG context
  const ragContext = await supabase.vectorSearch({
    query: ingredients.join(' '),
    filters: userContext.preferences
  });

  // 3. LLM Generation
  const prompt = buildPrompt({
    ingredients,
    nutritionData,
    substitutions,
    inspiration,
    ragContext,
    constraints
  });

  const recipe = await groq.generate(prompt, {
    model: 'llama-3-70b',
    temperature: 0.8, // Créativité
    maxTokens: 2000
  });

  // 4. Structure & Validate
  const structuredRecipe = parseAndValidate(recipe);

  // 5. Save to DB + Vector Store
  await saveRecipe(structuredRecipe, userContext);

  return structuredRecipe;
}
```

---

### Feature 2 : Mode Envie 🌟

**Description** :
L'utilisateur décrit son envie en langage naturel, l'IA génère une recette appropriée.

**User Flow** :
```
1. User clique "Mode Envie"
2. Décrit son envie :
   → "Quelque chose de réconfortant et épicé"
   → "Un plat léger pour ce soir"
   → "Impressionner mes invités"
3. (Optionnel) Ajoute contraintes (temps, ingrédients à éviter)
4. Génération recette (même process que Mode Frigo)
```

**Acceptance Criteria** :
- ✅ Comprend langage naturel (NLP)
- ✅ Interprète émotions/contexte ("réconfortant", "impressionner")
- ✅ Génération cohérente avec l'envie
- ✅ Suggestion d'ingrédients nécessaires

**Technical Implementation** :
```typescript
// Le LLM analyse l'envie et détermine les caractéristiques
async function generateRecipeFromMood(
  mood: string,
  constraints: RecipeConstraints
) {
  // 1. LLM analyse le mood
  const analysis = await groq.analyze(mood);
  // → Extrait: type de plat, saveurs, niveau confort, etc.

  // 2. Cherche dans RAG des recettes similaires
  const similarRecipes = await vectorSearch(analysis.embedding);

  // 3. Génère recette originale
  const recipe = await generateRecipe({
    characteristics: analysis,
    inspiration: similarRecipes,
    constraints
  });

  return recipe;
}
```

---

### Feature 3 : Sauvegarde & Favoris ❤️

**Description** :
Les utilisateurs peuvent sauvegarder leurs recettes préférées pour consultation future (offline-capable).

**User Flow** :
```
1. Après génération, user clique ❤️
2. Recette sauvegardée dans "Mes Favoris"
3. Accessible depuis menu principal
4. Consultation offline (PWA cache)
5. Actions :
   - Régénérer variation
   - Supprimer
   - Partager
```

**Limits** :
- Free : 3 sauvegardes max
- Premium : Illimité

**Acceptance Criteria** :
- ✅ Sauvegarde instantanée (optimistic UI)
- ✅ Synchro Supabase
- ✅ Offline access (service worker)
- ✅ Paywall clair si limite atteinte

---

### Feature 4 : Authentification & Onboarding 🔐

**Description** :
Supabase Auth pour gérer utilisateurs et préférences.

**Onboarding Flow** :
```
1. Landing page
   → "Génère des recettes uniques avec l'IA"
   → CTA : "Commencer gratuitement"

2. Sign Up (Supabase Auth)
   → Email/Password
   → Google OAuth
   → Apple Sign In (iOS)

3. Questionnaire rapide (5 questions)
   → Allergies/intolérances ?
   → Régimes spécifiques ? (vegan, keto, etc.)
   → Niveau cuisine ? (débutant, intermédiaire, expert)
   → Temps moyen dispo ? (15min, 30min, 1h+)
   → Objectifs ? (gagner temps, manger sain, découvrir)

4. Confirmation
   → "Tu as 5 générations gratuites cette semaine !"
   → CTA : "Créer ma première recette"
```

**Acceptance Criteria** :
- ✅ Social auth (Google, Apple)
- ✅ Onboarding < 2min
- ✅ Préférences sauvegardées
- ✅ Skip onboarding possible

---

### Feature 5 : Freemium & Trial System 💰

**Freemium Limits** :
- 5 générations/semaine
- 3 sauvegardes max
- Recettes basiques (pas de plans hebdo, pas d'adaptations avancées)

**Trial 7 jours** :
- Accès complet à toutes les features premium
- Banner : "Il te reste X jours de trial"
- Prompt conversion J6 : Offre -30% si souscription maintenant

**Premium (€4.99/mois ou €29.99/6 mois)** :
- Générations illimitées
- Sauvegardes illimitées
- Plans hebdomadaires
- Liste courses auto
- Adaptations allergies/régimes avancées
- Mode famille (portions auto-ajustées)
- Historique complet
- Support prioritaire

**Acceptance Criteria** :
- ✅ Quota tracking précis (weekly reset)
- ✅ Paywall clair et non-intrusif
- ✅ Trial activation automatique (1 clic)
- ✅ Gestion abonnement Stripe
- ✅ Offre engagement 6 mois (-17%)

---

## 🎨 Design Principles

### Visual Identity
- **Mobile-first** : Optimisé pour smartphone (90% des usages)
- **Clean & Modern** : Interface épurée, focus sur le contenu
- **Color Palette** :
  - Primary : Blanc (#FFFFFF)
  - Accent : Fuchsia (#E91E63 ou #FF006E)
  - Text : Gris foncé (#1A1A1A)
  - Background : Blanc cassé (#F9FAFB)
  - Success : Vert (#10B981)
  - Warning : Orange (#F59E0B)
- **Typography** :
  - Headings : Inter ou Geist (modern, clean)
  - Body : System font stack (performance)
  - Monospace : JetBrains Mono (code/timers)

### UX Principles
1. **Rapidité** : Chaque action < 300ms (perceived)
2. **Clarté** : Pas de jargon, langage naturel
3. **Feedback** : Loading states, confirmations visuelles
4. **Forgiveness** : Undo actions, pas de destructive sans confirmation
5. **Delight** : Micro-animations, easter eggs culinaires

### Accessibility
- WCAG 2.1 AA compliance
- Contraste suffisant (4.5:1 text, 3:1 UI)
- Touch targets ≥ 44x44px
- Screen reader support
- Keyboard navigation

---

## 🏛️ Technical Architecture

### Stack
```
Frontend:
├─ Next.js 14+ (App Router)
├─ React 18+ (Server Components where possible)
├─ TypeScript (strict mode)
├─ Tailwind CSS + shadcn/ui
├─ PWA (next-pwa)
└─ Zustand (state management, lightweight)

Backend:
├─ Supabase (Auth, Database, Storage)
├─ Supabase pgvector (RAG embeddings)
├─ Vercel Edge Functions (API routes)
└─ Stripe (payments)

AI/ML:
├─ Groq API (primary LLM - Llama 3 70B)
├─ Together AI (fallback - Mixtral 8x7B)
├─ OpenAI Embeddings (pour RAG, ada-002)
└─ Langchain (orchestration)

External APIs:
├─ TheMealDB (inspiration recettes)
├─ Edamam Nutrition API (données nutritionnelles)
├─ Spoonacular (substitutions ingrédients)
└─ Unsplash (photos recettes)

Hosting:
├─ Vercel (frontend + serverless)
├─ Supabase Cloud (database)
└─ Cloudflare CDN (assets)
```

### Architecture RAG Hybride

```
┌─────────────────────────────────────────────┐
│          User Input (Ingredients/Mood)       │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         API Enrichment Layer                 │
│  • TheMealDB (inspiration)                   │
│  • Edamam (nutrition)                        │
│  • Spoonacular (substitutions)               │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         RAG Context Builder                  │
│  Supabase pgvector:                          │
│  • Previous recipes (successful)             │
│  • User preferences                          │
│  • Culinary techniques DB                    │
│  • Ingredient pairings                       │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         LLM Orchestration                    │
│  Primary: Groq (Llama 3 70B)                 │
│  Fallback: Together AI (Mixtral 8x7B)        │
│  → Generate creative recipe                  │
│  → Adapt to constraints                      │
│  → Format structured output                  │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         Structured Recipe Output             │
│  • Title, ingredients, steps                 │
│  • Nutrition, timing, difficulty             │
│  • Tips & variations                         │
└─────────────────────────────────────────────┘
```

### Database Schema (Preview)
```sql
-- Users
users (
  id uuid PRIMARY KEY,
  email text UNIQUE,
  created_at timestamp,
  subscription_tier text, -- 'free' | 'trial' | 'premium'
  trial_ends_at timestamp,
  weekly_generations_count integer,
  last_reset_at timestamp
)

-- User Preferences
user_preferences (
  user_id uuid REFERENCES users,
  allergies text[],
  diet_type text, -- 'vegan', 'keto', 'vegetarian', etc.
  skill_level text,
  max_cooking_time integer,
  favorite_cuisines text[]
)

-- Recipes
recipes (
  id uuid PRIMARY KEY,
  user_id uuid REFERENCES users,
  title text,
  ingredients jsonb,
  steps jsonb,
  nutrition jsonb,
  difficulty text,
  cooking_time integer,
  servings integer,
  created_at timestamp,
  is_favorite boolean,
  generation_mode text, -- 'fridge' | 'mood'
  input_data jsonb,
  embedding vector(1536) -- pour RAG
)

-- Usage Analytics
usage_events (
  id uuid PRIMARY KEY,
  user_id uuid REFERENCES users,
  event_type text, -- 'generation', 'save', 'share', etc.
  metadata jsonb,
  created_at timestamp
)
```

---

## 📊 Success Metrics & KPIs

### Acquisition Metrics
- **Sign-ups** : 1,000/mois (M3)
- **Activation rate** : 60% (génère ≥1 recette)
- **CAC** : < €5 (organique + viralité)
- **Viral coefficient (K-factor)** : > 0.3

### Engagement Metrics
- **DAU/MAU ratio** : > 30% (sticky product)
- **Recipes per user per week** : > 3
- **Session length** : > 5min
- **Return rate D1/D7/D30** : 40%/25%/15%

### Conversion Metrics
- **Free → Trial** : 30%
- **Trial → Paid** : 15%
- **Overall conversion** : 4.5%
- **LTV** : > €35 (7 mois rétention moyenne)

### Retention Metrics
- **Churn mensuel** : < 30%
- **Cohort retention M1/M3/M6** : 70%/50%/40%
- **NPS** : > 50

### Quality Metrics
- **Recipe quality rating** : > 4.2/5
- **LLM hallucinations** : < 2% (grave), < 10% (mineure)
- **Generation speed P95** : < 10s
- **App crashes** : < 0.1%

### Revenue Metrics
- **MRR** : €5,000 (M6)
- **ARPU** : €4.50
- **CAC payback** : < 2 mois
- **Gross margin** : > 70% (après coûts LLM/infra)

---

## 🚧 Technical Constraints & Trade-offs

### Performance
- **Target** : Lighthouse score > 90 (mobile)
- **Trade-off** : PWA = plus lourd qu'app native, mais 1 codebase
- **Mitigation** : Code splitting, lazy loading, image optimization

### Cost LLM
- **Target** : < €0.02/génération
- **Trade-off** : Open source moins "créatif" que GPT-4
- **Mitigation** : Groq ultra-rapide + cheap, RAG pour améliorer qualité

### Data Privacy
- **Contrainte** : RGPD compliance
- **Trade-off** : Moins de data tracking = moins d'insights
- **Mitigation** : Anonymisation, consent clair, Supabase EU region

### Offline Capability
- **Target** : Consultation recettes offline
- **Trade-off** : Pas de génération offline (nécessite LLM)
- **Mitigation** : Caching intelligent, fallback messages clairs

---

## 🔮 Future Roadmap (Post-MVP)

### Q1 2026 : Community & Social
- Partage public de recettes
- Système de like/commentaires
- Profils utilisateurs
- Défis culinaires hebdomadaires

### Q2 2026 : Advanced Features
- Génération d'images de recettes (DALL-E)
- Mode vidéo (steps en vidéo courte)
- Intégration courses en ligne (Carrefour, Auchan)
- Mode batch cooking (meal prep week-end)

### Q3 2026 : B2B
- API pour restaurants (test nouvelles recettes)
- Partenariats marques alimentaires
- White-label pour supermarchés

### Q4 2026 : Intelligence
- Prédiction des envies (ML sur historique)
- Analyse nutrition long-terme
- Coach culinaire (progression skills)
- Assistant vocal (génération mains-libres)

---

## 🎯 Go-to-Market Strategy

### Pre-Launch (Semaines -2 à 0)
- Landing page + waitlist
- Teasing sur ProductHunt
- Contenu social (TikTok, Instagram)
- Beta privée (50 users)

### Launch (Semaine 1)
- ProductHunt launch
- Posts Reddit (r/Cooking, r/EatCheapAndHealthy)
- Campagne Instagram/TikTok (influenceurs micro)
- PR tech (TechCrunch, TheNextWeb)

### Growth (Semaines 2-12)
- Content marketing (blog recettes IA)
- SEO (recettes + IA keywords)
- Referral program (parrainer = +5 générations)
- Partenariats (blogs food, nutritionnistes)

### Pricing Strategy
- **Free** : Acquisition maximale
- **Trial 7j** : Tester avant d'acheter
- **Premium €4.99** : Prix psychologique (< €5)
- **Engagement 6 mois €29.99** : -17%, réduit churn

---

## ✅ Acceptance Criteria (MVP Launch)

### Must-Have (Bloquant)
- ✅ Mode Frigo opérationnel (génération < 10s)
- ✅ Mode Envie opérationnel
- ✅ Sauvegarde favoris (3 max free)
- ✅ Auth Supabase (email + Google)
- ✅ Freemium (5 générations/semaine)
- ✅ Trial 7 jours fonctionnel
- ✅ Paywall Stripe (abonnement)
- ✅ PWA installable (iOS/Android)
- ✅ Offline consultation favoris
- ✅ Performance Lighthouse > 85
- ✅ RGPD compliant
- ✅ Mobile responsive (320px → 768px)

### Should-Have (Important)
- ✅ Onboarding interactif
- ✅ Variations de recettes (régénérer)
- ✅ Partage social (native share API)
- ✅ Analytics basiques (Plausible)
- ✅ Error handling robuste
- ✅ Loading states agréables

### Could-Have (Nice-to-have)
- ⭕ Photos recettes (Unsplash)
- ⭕ Mode sombre
- ⭕ Animations micro-interactions
- ⭕ Easter eggs culinaires
- ⭕ Notifications push (trial ending)

### Won't-Have (MVP)
- ❌ Community features
- ❌ Plans hebdomadaires (premium future)
- ❌ Liste courses auto
- ❌ Génération d'images IA
- ❌ Mode vidéo
- ❌ Intégration courses en ligne

---

## 📞 Stakeholders & Responsibilities

| Rôle | Nom | Responsabilités |
|------|-----|-----------------|
| Product Owner | [Your Name] | Vision produit, roadmap, arbitrages |
| Tech Lead | [Your Name] | Architecture, stack, code review |
| Designer | [TBD/Freelance] | UI/UX, design system, prototypes |
| Marketing | [TBD/Vous] | GTM, growth, content |
| Legal | [TBD] | RGPD, CGU/CGV, mentions légales |

---

## 📚 Appendices

### A. Competitive Analysis

| Competitor | Forces | Faiblesses | Différenciation RadBites |
|------------|--------|------------|--------------------------|
| **Supercook** | Gratuit, simple | Recettes statiques, pas d'IA | IA créative vs DB statique |
| **Yummly** | Grosse DB recettes | Pas de génération custom | Personnalisation LLM |
| **Tasty** | Vidéos engageantes | Pas d'adaptation perso | Génération sur-mesure |
| **Mealime** | Plans hebdo | Pas créatif | Créativité IA |
| **ChatGPT/Claude** | Génération texte | Pas d'app dédiée, pas de save | Expérience dédiée cuisine |

**Positionnement** : "Midjourney de la cuisine - l'IA créative pour tes repas"

### B. Risk Analysis

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Qualité recettes (hallucinations) | Moyenne | Critique | RAG + validation, feedback users |
| Coûts LLM explosent | Faible | Élevé | Groq cheap, caching, rate limiting |
| Acquisition difficile | Moyenne | Élevé | Viralité, content marketing, referral |
| Churn élevé | Moyenne | Élevé | Engagement features, trial 7j |
| Concurrence (ChatGPT plugin) | Élevée | Moyenne | Expérience dédiée > généraliste |
| RGPD/Legal | Faible | Critique | Avocat, compliance dès J1 |

### C. API Cost Estimates (1000 users actifs)

```
LLM (Groq Llama 3 70B):
- 1000 users × 3 recettes/semaine × 4 semaines = 12,000 générations/mois
- 12,000 × 2,000 tokens avg × $0.0000004/token = $9.60/mois
- Avec caching 50% : ~$5/mois ✅ Ultra cheap

Embeddings (OpenAI ada-002):
- 12,000 × 500 tokens × $0.0000001/token = $0.60/mois ✅

External APIs (tous gratuits):
- TheMealDB : Free tier ✅
- Edamam : Free tier 10,000 calls/mois ✅
- Spoonacular : Free tier 150 calls/day ✅
- Unsplash : Free tier 50 calls/hour ✅

Infrastructure:
- Vercel Pro : $20/mois
- Supabase Pro : $25/mois
- Stripe : 1.4% + €0.25/transaction

Total coût fixe : ~$50/mois
Coût variable : ~$6/1000 users
```

**Break-even** : ~100 utilisateurs premium @ €4.99/mois

---

## ✍️ Sign-off

| Nom | Rôle | Signature | Date |
|-----|------|-----------|------|
| [Your Name] | Product Owner | _________ | 2025-11-11 |
| [Tech Lead] | Tech Lead | _________ | ______ |
| [Stakeholder] | [Role] | _________ | ______ |

---

**Document Status** : ✅ Ready for Development

**Next Steps** :
1. Review & approve PRD
2. Create User Stories (detailed)
3. Design Database Schema
4. Create Prompt Engineering Guide
5. Start MVP development (Sprint 1)

---

*RadBites - Transforming everyday cooking with AI creativity*
*Version 1.0 | 2025-11-11*
