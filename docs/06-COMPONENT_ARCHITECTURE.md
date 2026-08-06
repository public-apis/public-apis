# RadBites - Component Architecture

**Version**: 1.0
**Date**: 2025-11-11
**Framework**: Next.js 14+ (App Router)
**State Management**: Zustand
**Styling**: Tailwind CSS

---

## 📋 Table of Contents

1. [Project Structure](#project-structure)
2. [Naming Conventions](#naming-conventions)
3. [Component Types](#component-types)
4. [Server vs Client Components](#server-vs-client-components)
5. [Data Fetching Patterns](#data-fetching-patterns)
6. [State Management](#state-management)
7. [Custom Hooks](#custom-hooks)
8. [API Routes Structure](#api-routes-structure)
9. [Error Boundaries](#error-boundaries)
10. [Testing Strategy](#testing-strategy)

---

## 📁 Project Structure

```
radbites/
├── app/                          # Next.js 14 App Router
│   ├── (auth)/                   # Auth route group
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── signup/
│   │   │   └── page.tsx
│   │   └── layout.tsx            # Auth layout (centered, no nav)
│   │
│   ├── (main)/                   # Main app route group
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   ├── generate/
│   │   │   ├── frigo/
│   │   │   │   └── page.tsx      # Mode Frigo
│   │   │   ├── mood/
│   │   │   │   └── page.tsx      # Mode Envie
│   │   │   └── layout.tsx
│   │   ├── favorites/
│   │   │   └── page.tsx
│   │   ├── recipe/
│   │   │   └── [id]/
│   │   │       └── page.tsx      # Recipe detail
│   │   ├── premium/
│   │   │   ├── page.tsx
│   │   │   └── success/
│   │   │       └── page.tsx
│   │   └── layout.tsx            # Main layout (with header/footer)
│   │
│   ├── api/                      # API Routes
│   │   ├── recipes/
│   │   │   ├── generate/
│   │   │   │   └── route.ts      # POST /api/recipes/generate
│   │   │   ├── [id]/
│   │   │   │   └── route.ts      # GET/PUT/DELETE /api/recipes/[id]
│   │   │   └── favorites/
│   │   │       └── route.ts      # GET /api/recipes/favorites
│   │   ├── user/
│   │   │   ├── preferences/
│   │   │   │   └── route.ts
│   │   │   └── subscription/
│   │   │       └── route.ts
│   │   └── webhooks/
│   │       └── stripe/
│   │           └── route.ts      # Stripe webhooks
│   │
│   ├── layout.tsx                # Root layout
│   ├── page.tsx                  # Landing page
│   ├── error.tsx                 # Global error boundary
│   ├── not-found.tsx             # 404 page
│   └── loading.tsx               # Global loading UI
│
├── components/                   # React components
│   ├── ui/                       # shadcn/ui base components
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── ...
│   │
│   ├── features/                 # Feature-specific components
│   │   ├── recipe/
│   │   │   ├── RecipeCard.tsx
│   │   │   ├── RecipeDetail.tsx
│   │   │   ├── RecipeIngredients.tsx
│   │   │   ├── RecipeSteps.tsx
│   │   │   ├── RecipeNutrition.tsx
│   │   │   └── RecipeActions.tsx
│   │   │
│   │   ├── generation/
│   │   │   ├── FridgeInput.tsx
│   │   │   ├── MoodInput.tsx
│   │   │   ├── ConstraintsForm.tsx
│   │   │   ├── GenerationLoading.tsx
│   │   │   └── GenerationProgress.tsx
│   │   │
│   │   ├── favorites/
│   │   │   ├── FavoritesList.tsx
│   │   │   ├── FavoriteButton.tsx
│   │   │   └── EmptyFavorites.tsx
│   │   │
│   │   ├── onboarding/
│   │   │   ├── OnboardingFlow.tsx
│   │   │   ├── AllergiesStep.tsx
│   │   │   ├── DietStep.tsx
│   │   │   └── SkillLevelStep.tsx
│   │   │
│   │   └── premium/
│   │       ├── PaywallModal.tsx
│   │       ├── PricingCard.tsx
│   │       ├── TrialBanner.tsx
│   │       └── QuotaBadge.tsx
│   │
│   ├── layout/                   # Layout components
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   ├── MobileNav.tsx
│   │   ├── Sidebar.tsx
│   │   └── Container.tsx
│   │
│   └── shared/                   # Shared/common components
│       ├── Logo.tsx
│       ├── UserAvatar.tsx
│       ├── SearchBar.tsx
│       ├── EmptyState.tsx
│       ├── ErrorState.tsx
│       └── LoadingSpinner.tsx
│
├── lib/                          # Utilities & services
│   ├── supabase/
│   │   ├── client.ts             # Client-side Supabase
│   │   ├── server.ts             # Server-side Supabase
│   │   └── middleware.ts         # Supabase middleware
│   │
│   ├── llm/
│   │   ├── groq.ts               # Groq client
│   │   ├── together.ts           # Together AI client
│   │   ├── prompts.ts            # Prompt templates
│   │   └── validation.ts         # Output validation
│   │
│   ├── apis/                     # External API clients
│   │   ├── edamam.ts             # Edamam Nutrition API
│   │   ├── spoonacular.ts        # Spoonacular API
│   │   ├── mealdb.ts             # TheMealDB API
│   │   └── unsplash.ts           # Unsplash API
│   │
│   ├── stripe/
│   │   ├── client.ts             # Stripe client
│   │   └── webhooks.ts           # Webhook handlers
│   │
│   ├── utils/
│   │   ├── cn.ts                 # Class name merger (clsx + twMerge)
│   │   ├── format.ts             # Formatters (date, time, etc.)
│   │   ├── validation.ts         # Zod schemas
│   │   └── constants.ts          # App constants
│   │
│   └── hooks/                    # Custom React hooks
│       ├── useAuth.ts
│       ├── useRecipe.ts
│       ├── useGeneration.ts
│       ├── useFavorites.ts
│       └── useSubscription.ts
│
├── store/                        # Zustand state management
│   ├── authStore.ts
│   ├── recipeStore.ts
│   ├── generationStore.ts
│   └── uiStore.ts
│
├── types/                        # TypeScript types
│   ├── database.types.ts         # Generated from Supabase
│   ├── recipe.types.ts
│   ├── user.types.ts
│   └── api.types.ts
│
├── config/                       # Configuration files
│   ├── site.ts                   # Site metadata
│   └── prompts.ts                # Prompt configurations
│
├── public/                       # Static assets
│   ├── icons/
│   ├── images/
│   └── manifest.json             # PWA manifest
│
├── middleware.ts                 # Next.js middleware (auth, rate limiting)
├── next.config.js                # Next.js config
├── tailwind.config.ts            # Tailwind config
├── tsconfig.json                 # TypeScript config
└── package.json
```

---

## 🏷️ Naming Conventions

### Files & Folders

```
PascalCase  → Components, Types
camelCase   → Functions, variables, hooks
kebab-case  → Folders (route segments)
```

**Examples:**
```
✅ components/recipe/RecipeCard.tsx
✅ lib/hooks/useRecipe.ts
✅ app/(main)/generate/frigo/page.tsx
✅ types/recipe.types.ts
```

### Components

```typescript
// React Components: PascalCase
export function RecipeCard({ recipe }: RecipeCardProps) { }
export const UserAvatar: React.FC<UserAvatarProps> = ({ user }) => { };

// Component files match component name
RecipeCard.tsx → export function RecipeCard() {}

// Props interface: ComponentName + Props
interface RecipeCardProps {
  recipe: Recipe;
  onFavorite?: (id: string) => void;
}
```

### Functions & Hooks

```typescript
// Functions: camelCase, verb-first
export function generateRecipe(ingredients: string[]) {}
export async function fetchUserPreferences(userId: string) {}

// Hooks: use + PascalCase
export function useRecipe(id: string) {}
export function useAuth() {}

// Event handlers: handle + Event
const handleSubmit = (e: FormEvent) => {}
const handleFavoriteClick = () => {}
```

### Constants

```typescript
// SCREAMING_SNAKE_CASE for true constants
export const MAX_INGREDIENTS = 10;
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

// camelCase for config objects
export const siteConfig = {
  name: "RadBites",
  description: "...",
};
```

---

## 🧩 Component Types

### 1. Server Components (Default in App Router)

**Use for:**
- Data fetching
- SEO-critical content
- Static content

```typescript
// app/(main)/favorites/page.tsx
import { createServerClient } from '@/lib/supabase/server';
import { FavoritesList } from '@/components/features/favorites/FavoritesList';

export default async function FavoritesPage() {
  // Data fetching in Server Component
  const supabase = createServerClient();
  const { data: { user } } = await supabase.auth.getUser();

  if (!user) {
    redirect('/login');
  }

  const { data: recipes } = await supabase
    .from('recipes')
    .select('*')
    .eq('user_id', user.id)
    .eq('is_favorite', true);

  return (
    <div>
      <h1>Mes Favoris</h1>
      <FavoritesList recipes={recipes || []} />
    </div>
  );
}
```

### 2. Client Components

**Use for:**
- Interactivity (onClick, onChange)
- Browser APIs (localStorage, navigator)
- React hooks (useState, useEffect)
- Context providers

```typescript
// components/features/recipe/FavoriteButton.tsx
'use client';

import { useState } from 'react';
import { Heart } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { toast } from 'sonner';

interface FavoriteButtonProps {
  recipeId: string;
  initialFavorite: boolean;
}

export function FavoriteButton({ recipeId, initialFavorite }: FavoriteButtonProps) {
  const [isFavorite, setIsFavorite] = useState(initialFavorite);
  const [isLoading, setIsLoading] = useState(false);

  const handleToggle = async () => {
    setIsLoading(true);

    try {
      const response = await fetch(`/api/recipes/${recipeId}/favorite`, {
        method: 'POST',
      });

      if (!response.ok) throw new Error();

      setIsFavorite(!isFavorite);
      toast.success(isFavorite ? 'Retiré des favoris' : 'Ajouté aux favoris');
    } catch (error) {
      toast.error('Une erreur est survenue');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Button
      variant="ghost"
      size="sm"
      onClick={handleToggle}
      disabled={isLoading}
    >
      <Heart
        className={cn(
          "h-5 w-5 transition-all",
          isFavorite && "fill-accent text-accent"
        )}
      />
    </Button>
  );
}
```

### 3. Shared Components (Composition)

```typescript
// components/features/recipe/RecipeCard.tsx
'use client';

import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { FavoriteButton } from './FavoriteButton';
import type { Recipe } from '@/types/recipe.types';

interface RecipeCardProps {
  recipe: Recipe;
}

export function RecipeCard({ recipe }: RecipeCardProps) {
  return (
    <Card>
      <CardHeader className="p-0">
        <img
          src={recipe.image_url || '/placeholder-recipe.jpg'}
          alt={recipe.title}
          className="w-full h-48 object-cover rounded-t-2xl"
        />
      </CardHeader>
      <CardContent className="p-4">
        <div className="flex items-start justify-between mb-2">
          <h3 className="text-lg font-semibold line-clamp-2">
            {recipe.title}
          </h3>
          <FavoriteButton
            recipeId={recipe.id}
            initialFavorite={recipe.is_favorite}
          />
        </div>

        <div className="flex items-center gap-2 mt-3">
          <Badge variant="outline">{recipe.difficulty}</Badge>
          <Badge variant="outline">{recipe.cooking_time} min</Badge>
          <Badge variant="outline">{recipe.servings} portions</Badge>
        </div>
      </CardContent>
    </Card>
  );
}
```

---

## ⚙️ Server vs Client Components

### Decision Tree

```
Is the component interactive? (useState, useEffect, onClick, etc.)
├─ YES → 'use client'
└─ NO
    ├─ Needs browser APIs? (window, localStorage, etc.)
    │  └─ YES → 'use client'
    └─ NO → Server Component (default)
```

### Composition Pattern

**✅ Good**: Server Component wraps Client Component

```typescript
// app/(main)/recipe/[id]/page.tsx (Server Component)
import { createServerClient } from '@/lib/supabase/server';
import { RecipeDetail } from '@/components/features/recipe/RecipeDetail';

export default async function RecipePage({ params }: { params: { id: string } }) {
  const supabase = createServerClient();
  const { data: recipe } = await supabase
    .from('recipes')
    .select('*')
    .eq('id', params.id)
    .single();

  if (!recipe) notFound();

  return <RecipeDetail recipe={recipe} />; // Client Component
}

// components/features/recipe/RecipeDetail.tsx (Client Component)
'use client';

export function RecipeDetail({ recipe }: { recipe: Recipe }) {
  const [activeStep, setActiveStep] = useState(0); // Interactive!

  return (
    <div>
      {/* Interactive UI */}
    </div>
  );
}
```

**❌ Bad**: Client Component wraps Server Component (impossible)

```typescript
// ❌ This doesn't work
'use client';

export function ClientWrapper() {
  return <ServerComponent />; // Can't use Server Component inside Client
}
```

---

## 📡 Data Fetching Patterns

### 1. Server Components (Preferred)

```typescript
// app/(main)/dashboard/page.tsx
import { createServerClient } from '@/lib/supabase/server';

export default async function DashboardPage() {
  const supabase = createServerClient();

  // Parallel fetching
  const [
    { data: { user } },
    { data: recentRecipes },
    { data: stats }
  ] = await Promise.all([
    supabase.auth.getUser(),
    supabase
      .from('recipes')
      .select('*')
      .order('created_at', { ascending: false })
      .limit(10),
    supabase
      .from('user_stats')
      .select('*')
      .single()
  ]);

  return (
    <div>
      <StatsCards stats={stats} />
      <RecentRecipes recipes={recentRecipes} />
    </div>
  );
}
```

### 2. Client-Side Fetching (SWR Pattern)

```typescript
// lib/hooks/useRecipes.ts
import useSWR from 'swr';
import type { Recipe } from '@/types/recipe.types';

const fetcher = (url: string) => fetch(url).then(r => r.json());

export function useRecipes(filters?: RecipeFilters) {
  const params = new URLSearchParams(filters);
  const { data, error, isLoading, mutate } = useSWR<Recipe[]>(
    `/api/recipes?${params}`,
    fetcher,
    {
      revalidateOnFocus: false,
      dedupingInterval: 60000, // 1 min
    }
  );

  return {
    recipes: data,
    isLoading,
    isError: error,
    mutate, // For optimistic updates
  };
}

// Usage in component
'use client';

export function RecipesList() {
  const { recipes, isLoading, isError } = useRecipes({ favorite: true });

  if (isLoading) return <LoadingSkeleton />;
  if (isError) return <ErrorState />;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {recipes?.map(recipe => (
        <RecipeCard key={recipe.id} recipe={recipe} />
      ))}
    </div>
  );
}
```

### 3. Server Actions (Form Submissions)

```typescript
// app/actions/recipe.actions.ts
'use server';

import { revalidatePath } from 'next/cache';
import { createServerClient } from '@/lib/supabase/server';

export async function toggleFavorite(recipeId: string) {
  const supabase = createServerClient();
  const { data: { user } } = await supabase.auth.getUser();

  if (!user) {
    throw new Error('Unauthorized');
  }

  const { data: recipe } = await supabase
    .from('recipes')
    .select('is_favorite')
    .eq('id', recipeId)
    .single();

  await supabase
    .from('recipes')
    .update({ is_favorite: !recipe.is_favorite })
    .eq('id', recipeId);

  revalidatePath('/favorites');
  return { success: true };
}

// Usage in Client Component
'use client';

import { toggleFavorite } from '@/app/actions/recipe.actions';

export function FavoriteButton({ recipeId }: { recipeId: string }) {
  const [pending, startTransition] = useTransition();

  const handleToggle = () => {
    startTransition(async () => {
      await toggleFavorite(recipeId);
      toast.success('Favoris mis à jour');
    });
  };

  return (
    <Button onClick={handleToggle} disabled={pending}>
      {pending ? <Loader2 className="animate-spin" /> : <Heart />}
    </Button>
  );
}
```

---

## 🗃️ State Management

### Zustand Stores

#### Auth Store

```typescript
// store/authStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { User } from '@/types/user.types';

interface AuthState {
  user: User | null;
  subscription: SubscriptionTier;
  setUser: (user: User | null) => void;
  setSubscription: (tier: SubscriptionTier) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      subscription: 'free',
      setUser: (user) => set({ user }),
      setSubscription: (subscription) => set({ subscription }),
      logout: () => set({ user: null, subscription: 'free' }),
    }),
    {
      name: 'auth-storage', // localStorage key
      partialize: (state) => ({ subscription: state.subscription }), // Only persist subscription
    }
  )
);
```

#### Recipe Generation Store

```typescript
// store/generationStore.ts
import { create } from 'zustand';
import type { Recipe, GenerationInput } from '@/types/recipe.types';

interface GenerationState {
  isGenerating: boolean;
  currentRecipe: Recipe | null;
  generationInput: GenerationInput | null;
  progress: number; // 0-100

  startGeneration: (input: GenerationInput) => void;
  setProgress: (progress: number) => void;
  setRecipe: (recipe: Recipe) => void;
  reset: () => void;
}

export const useGenerationStore = create<GenerationState>((set) => ({
  isGenerating: false,
  currentRecipe: null,
  generationInput: null,
  progress: 0,

  startGeneration: (input) => set({
    isGenerating: true,
    generationInput: input,
    progress: 0
  }),

  setProgress: (progress) => set({ progress }),

  setRecipe: (recipe) => set({
    currentRecipe: recipe,
    isGenerating: false,
    progress: 100
  }),

  reset: () => set({
    isGenerating: false,
    currentRecipe: null,
    generationInput: null,
    progress: 0
  }),
}));
```

#### UI Store (Modals, Toasts)

```typescript
// store/uiStore.ts
import { create } from 'zustand';

interface UIState {
  showPaywall: boolean;
  showOnboarding: boolean;
  setShowPaywall: (show: boolean) => void;
  setShowOnboarding: (show: boolean) => void;
}

export const useUIStore = create<UIState>((set) => ({
  showPaywall: false,
  showOnboarding: false,
  setShowPaywall: (showPaywall) => set({ showPaywall }),
  setShowOnboarding: (showOnboarding) => set({ showOnboarding }),
}));
```

---

## 🪝 Custom Hooks

### useAuth

```typescript
// lib/hooks/useAuth.ts
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';
import { useAuthStore } from '@/store/authStore';

export function useAuth() {
  const router = useRouter();
  const { user, setUser, logout: storeLogout } = useAuthStore();
  const supabase = createClientComponentClient();

  useEffect(() => {
    // Listen to auth state changes
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (session?.user) {
        setUser(session.user as any);
      } else {
        setUser(null);
      }

      if (event === 'SIGNED_OUT') {
        router.push('/login');
      }
    });

    return () => {
      subscription.unsubscribe();
    };
  }, []);

  const logout = async () => {
    await supabase.auth.signOut();
    storeLogout();
    router.push('/');
  };

  return {
    user,
    isAuthenticated: !!user,
    logout,
  };
}
```

### useGeneration

```typescript
// lib/hooks/useGeneration.ts
import { useState } from 'react';
import { useGenerationStore } from '@/store/generationStore';
import type { GenerationInput, Recipe } from '@/types/recipe.types';

export function useGeneration() {
  const {
    isGenerating,
    progress,
    currentRecipe,
    startGeneration,
    setProgress,
    setRecipe,
    reset
  } = useGenerationStore();

  const [error, setError] = useState<string | null>(null);

  const generate = async (input: GenerationInput) => {
    startGeneration(input);
    setError(null);

    try {
      // Simulate progress (real progress from EventSource in production)
      const progressInterval = setInterval(() => {
        setProgress(prev => Math.min(prev + 10, 90));
      }, 800);

      const response = await fetch('/api/recipes/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(input),
      });

      clearInterval(progressInterval);

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Generation failed');
      }

      const recipe: Recipe = await response.json();
      setRecipe(recipe);

      return recipe;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
      reset();
      throw err;
    }
  };

  return {
    generate,
    isGenerating,
    progress,
    currentRecipe,
    error,
    reset,
  };
}
```

---

## 🛣️ API Routes Structure

### Recipe Generation Route

```typescript
// app/api/recipes/generate/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { createRouteHandlerClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import { generateRecipe } from '@/lib/llm/generator';
import { checkQuota, incrementQuota } from '@/lib/quota';
import { rateLimit } from '@/lib/rate-limit';

export async function POST(req: NextRequest) {
  try {
    // 1. Auth check
    const supabase = createRouteHandlerClient({ cookies });
    const { data: { user } } = await supabase.auth.getUser();

    if (!user) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    // 2. Rate limiting
    const rateLimitResult = await rateLimit.check(user.id);
    if (!rateLimitResult.success) {
      return NextResponse.json(
        { error: 'Too many requests' },
        {
          status: 429,
          headers: { 'Retry-After': rateLimitResult.reset.toString() }
        }
      );
    }

    // 3. Quota check (freemium)
    const quotaResult = await checkQuota(user.id);
    if (!quotaResult.canGenerate) {
      return NextResponse.json(
        { error: 'Quota exceeded', remaining: 0 },
        { status: 429 }
      );
    }

    // 4. Parse input
    const input = await req.json();
    const { ingredients, mood, constraints } = input;

    // 5. Generate recipe (with RAG)
    const recipe = await generateRecipe({
      userId: user.id,
      ingredients,
      mood,
      constraints,
    });

    // 6. Save to database
    const { data: savedRecipe, error: saveError } = await supabase
      .from('recipes')
      .insert({
        user_id: user.id,
        ...recipe,
        generation_mode: ingredients ? 'fridge' : 'mood',
        input_data: input,
      })
      .select()
      .single();

    if (saveError) throw saveError;

    // 7. Increment quota
    await incrementQuota(user.id);

    // 8. Track event
    await supabase.from('usage_events').insert({
      user_id: user.id,
      event_type: 'recipe_generated',
      event_data: { mode: savedRecipe.generation_mode }
    });

    return NextResponse.json(savedRecipe);

  } catch (error) {
    console.error('Generation error:', error);
    return NextResponse.json(
      { error: 'Generation failed' },
      { status: 500 }
    );
  }
}
```

---

## 🚨 Error Boundaries

### Global Error Boundary

```typescript
// app/error.tsx
'use client';

import { useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { AlertCircle } from 'lucide-react';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    // Log to error reporting service (Sentry, etc.)
    console.error('Global error:', error);
  }, [error]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center">
      <div className="text-center space-y-4">
        <AlertCircle className="h-16 w-16 text-error mx-auto" />
        <h2 className="text-2xl font-bold">Une erreur est survenue</h2>
        <p className="text-foreground-muted max-w-md">
          Quelque chose s'est mal passé. Notre équipe a été notifiée.
        </p>
        <Button onClick={reset}>Réessayer</Button>
      </div>
    </div>
  );
}
```

### Route-Specific Error Boundary

```typescript
// app/(main)/generate/frigo/error.tsx
'use client';

export default function FridgeGenerationError({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div className="p-6">
      <h2>Erreur de génération</h2>
      <p>{error.message}</p>
      <Button onClick={reset}>Réessayer la génération</Button>
    </div>
  );
}
```

---

## 🧪 Testing Strategy

### Unit Tests (Vitest)

```typescript
// components/features/recipe/RecipeCard.test.tsx
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { RecipeCard } from './RecipeCard';
import type { Recipe } from '@/types/recipe.types';

const mockRecipe: Recipe = {
  id: '1',
  title: 'Poulet Crémeux',
  difficulty: 'easy',
  cooking_time: 30,
  servings: 4,
  is_favorite: false,
  // ... other fields
};

describe('RecipeCard', () => {
  it('renders recipe title', () => {
    render(<RecipeCard recipe={mockRecipe} />);
    expect(screen.getByText('Poulet Crémeux')).toBeInTheDocument();
  });

  it('displays cooking time badge', () => {
    render(<RecipeCard recipe={mockRecipe} />);
    expect(screen.getByText('30 min')).toBeInTheDocument();
  });

  it('calls onFavorite when favorite button clicked', async () => {
    const onFavorite = vi.fn();
    render(<RecipeCard recipe={mockRecipe} onFavorite={onFavorite} />);

    const favoriteButton = screen.getByRole('button', { name: /favorite/i });
    fireEvent.click(favoriteButton);

    expect(onFavorite).toHaveBeenCalledWith('1');
  });
});
```

### Integration Tests (Playwright)

```typescript
// tests/e2e/recipe-generation.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Recipe Generation Flow', () => {
  test.beforeEach(async ({ page }) => {
    // Login
    await page.goto('/login');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL('/dashboard');
  });

  test('generates recipe from ingredients', async ({ page }) => {
    // Navigate to Mode Frigo
    await page.goto('/generate/frigo');

    // Input ingredients
    await page.fill('input[placeholder*="ingrédients"]', 'poulet');
    await page.keyboard.press('Enter');
    await page.fill('input[placeholder*="ingrédients"]', 'carottes');
    await page.keyboard.press('Enter');

    // Generate
    await page.click('button:has-text("Générer")');

    // Wait for generation (with loading state)
    await expect(page.locator('text=Génération en cours')).toBeVisible();

    // Check result
    await expect(page.locator('h1')).toContainText(/poulet|carottes/i, {
      timeout: 15000 // 15s max for generation
    });

    // Verify recipe structure
    await expect(page.locator('text=Ingrédients')).toBeVisible();
    await expect(page.locator('text=Instructions')).toBeVisible();
  });
});
```

---

## ✅ Best Practices Summary

### Component Organization

1. **Colocate related files**: Keep components, tests, and styles together
2. **Single Responsibility**: One component = one job
3. **Composition over Inheritance**: Build complex UIs from simple components
4. **Props interface first**: Define interfaces before implementation

### Performance

1. **Server Components by default**: Use 'use client' only when needed
2. **Lazy load heavy components**: Use React.lazy() + Suspense
3. **Memoization**: Use React.memo() for expensive renders
4. **Optimize images**: Use Next.js Image component

### Code Quality

1. **TypeScript strict mode**: No `any` types
2. **ESLint + Prettier**: Consistent formatting
3. **Code reviews**: PR template with checklist
4. **Test coverage**: Aim for 80%+ on critical paths

---

*RadBites Component Architecture - Production Ready*
*Version 1.0 | 2025-11-11*

**Next Steps:**
1. Set up Next.js 14 project
2. Install dependencies (Supabase, Zustand, shadcn/ui)
3. Create folder structure
4. Implement auth flow
5. Build recipe generation feature
