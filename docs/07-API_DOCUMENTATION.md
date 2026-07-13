# RadBites - API Documentation

**Version**: 1.0
**Date**: 2025-11-11
**Base URL**: https://radbites.app/api (production) | http://localhost:3000/api (development)

---

## 📋 Table of Contents

### Internal APIs
1. [Authentication](#authentication)
2. [Recipes API](#recipes-api)
3. [User API](#user-api)
4. [Subscription API](#subscription-api)
5. [Webhooks](#webhooks)

### External APIs
6. [TheMealDB](#themealdb)
7. [Edamam Nutrition](#edamam-nutrition)
8. [Spoonacular](#spoonacular)
9. [Unsplash](#unsplash)
10. [Groq (LLM)](#groq-llm)
11. [Together AI (LLM Fallback)](#together-ai-llm-fallback)

---

## 🔐 Authentication

All internal API routes require authentication via Supabase Auth.

### Headers

```http
Authorization: Bearer <supabase_access_token>
Content-Type: application/json
```

### Getting Access Token (Client-Side)

```typescript
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';

const supabase = createClientComponentClient();
const { data: { session } } = await supabase.auth.getSession();
const accessToken = session?.access_token;

// Use in fetch
fetch('/api/recipes', {
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json',
  }
});
```

### Errors

```json
// 401 Unauthorized
{
  "error": "Unauthorized",
  "message": "Missing or invalid authentication token"
}

// 403 Forbidden
{
  "error": "Forbidden",
  "message": "Insufficient permissions"
}
```

---

## 🍽️ Recipes API

### 1. Generate Recipe

Generate a new recipe using AI.

**Endpoint**: `POST /api/recipes/generate`

**Request Body**:
```json
{
  "mode": "fridge" | "mood",

  // For Mode Frigo
  "ingredients": ["poulet", "carottes", "oignons"],

  // For Mode Envie
  "mood": "Quelque chose de réconfortant et épicé",

  // Optional constraints
  "constraints": {
    "difficulty": "easy" | "medium" | "hard",
    "maxCookingTime": 45,        // minutes
    "servings": 4,
    "dishType": "main" | "starter" | "side" | "dessert"
  }
}
```

**Response** (201 Created):
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user-uuid",
  "title": "Poulet Crémeux aux Carottes Confites",
  "description": "Un plat réconfortant...",
  "difficulty": "easy",
  "prep_time": 10,
  "cooking_time": 30,
  "servings": 4,
  "dish_type": "main",
  "ingredients": [
    {
      "name": "poulet (blancs)",
      "quantity": 600,
      "unit": "g"
    },
    {
      "name": "carottes",
      "quantity": 4,
      "unit": "pièce"
    }
  ],
  "steps": [
    "Couper le poulet en morceaux...",
    "Faire chauffer l'huile..."
  ],
  "tips": "Le secret : ne pas cuire le poulet à feu trop fort...",
  "variations": [
    {
      "name": "Version épicée",
      "description": "Ajouter 1 c.à.c de paprika fumé"
    }
  ],
  "nutrition": {
    "calories": 385,
    "protein": 35,
    "carbs": 12,
    "fat": 22,
    "fiber": 3
  },
  "is_favorite": false,
  "generation_mode": "fridge",
  "input_data": { "ingredients": [...], "constraints": {...} },
  "created_at": "2025-11-11T10:30:00Z",
  "updated_at": "2025-11-11T10:30:00Z"
}
```

**Errors**:
```json
// 429 Too Many Requests (Quota exceeded)
{
  "error": "Quota exceeded",
  "message": "Tu as utilisé tes 5 générations gratuites cette semaine",
  "remaining": 0,
  "resetAt": "2025-11-18T00:00:00Z"
}

// 429 Too Many Requests (Rate limit)
{
  "error": "Too many requests",
  "message": "Trop de requêtes, réessaye dans quelques instants",
  "retryAfter": 60  // seconds
}

// 500 Internal Server Error (Generation failed)
{
  "error": "Generation failed",
  "message": "Impossible de générer la recette. Réessaye avec d'autres ingrédients."
}
```

---

### 2. Get Recipe by ID

Retrieve a single recipe.

**Endpoint**: `GET /api/recipes/[id]`

**Response** (200 OK):
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Poulet Crémeux aux Carottes",
  // ... (same structure as generation response)
}
```

**Errors**:
```json
// 404 Not Found
{
  "error": "Not found",
  "message": "Recipe not found"
}

// 403 Forbidden (not owner)
{
  "error": "Forbidden",
  "message": "You don't have access to this recipe"
}
```

---

### 3. List User Recipes

Get all recipes for current user.

**Endpoint**: `GET /api/recipes`

**Query Parameters**:
```
?favorite=true          // Filter favorites only
&generation_mode=fridge // Filter by mode
&difficulty=easy        // Filter by difficulty
&limit=20              // Max results (default 50)
&offset=0              // Pagination offset
&sort=created_at       // Sort field
&order=desc            // Sort direction (asc/desc)
```

**Response** (200 OK):
```json
{
  "recipes": [
    { /* recipe object */ },
    { /* recipe object */ }
  ],
  "total": 45,
  "limit": 20,
  "offset": 0
}
```

---

### 4. Update Recipe

Update recipe metadata (favorite status, rating, etc.).

**Endpoint**: `PATCH /api/recipes/[id]`

**Request Body**:
```json
{
  "is_favorite": true,
  "quality_rating": 5,      // 1-5
  "user_feedback": "Délicieux !"
}
```

**Response** (200 OK):
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "is_favorite": true,
  "quality_rating": 5,
  // ... rest of recipe
}
```

---

### 5. Delete Recipe

Delete a recipe.

**Endpoint**: `DELETE /api/recipes/[id]`

**Response** (204 No Content): _Empty body_

---

### 6. Generate Variation

Generate a variation of an existing recipe.

**Endpoint**: `POST /api/recipes/[id]/variation`

**Request Body**:
```json
{
  "modifications": ["plus épicé", "version végétarienne"]
}
```

**Response** (201 Created):
```json
{
  // New recipe object (variation)
  "title": "Tofu Crémeux aux Carottes Épicé (Variation)",
  // ... adapted recipe
}
```

---

## 👤 User API

### 1. Get User Profile

**Endpoint**: `GET /api/user/profile`

**Response** (200 OK):
```json
{
  "id": "user-uuid",
  "email": "user@example.com",
  "subscription_tier": "free" | "trial" | "premium",
  "trial_ends_at": "2025-11-18T00:00:00Z",
  "weekly_generations_count": 3,
  "last_quota_reset_at": "2025-11-11T00:00:00Z",
  "total_recipes_generated": 28,
  "total_recipes_saved": 12,
  "created_at": "2025-10-01T00:00:00Z"
}
```

---

### 2. Get User Preferences

**Endpoint**: `GET /api/user/preferences`

**Response** (200 OK):
```json
{
  "allergies": ["gluten", "lactose"],
  "diet_type": "vegetarian",
  "skill_level": "intermediate",
  "max_cooking_time": 45,
  "favorite_cuisines": ["italian", "asian"],
  "goals": ["save_time", "eat_healthy"]
}
```

---

### 3. Update User Preferences

**Endpoint**: `PUT /api/user/preferences`

**Request Body**:
```json
{
  "allergies": ["gluten"],
  "diet_type": "vegan",
  "skill_level": "expert",
  "max_cooking_time": 60
}
```

**Response** (200 OK):
```json
{
  "allergies": ["gluten"],
  "diet_type": "vegan",
  // ... updated preferences
}
```

---

## 💳 Subscription API

### 1. Start Trial

**Endpoint**: `POST /api/subscription/trial`

**Response** (200 OK):
```json
{
  "success": true,
  "subscription_tier": "trial",
  "trial_ends_at": "2025-11-18T00:00:00Z"
}
```

**Errors**:
```json
// 409 Conflict (already used trial)
{
  "error": "Trial already used",
  "message": "Tu as déjà utilisé ton essai gratuit"
}
```

---

### 2. Create Checkout Session (Stripe)

**Endpoint**: `POST /api/subscription/checkout`

**Request Body**:
```json
{
  "priceId": "price_monthly" | "price_6months"
}
```

**Response** (200 OK):
```json
{
  "sessionId": "cs_test_...",
  "url": "https://checkout.stripe.com/pay/cs_test_..."
}
```

---

### 3. Get Subscription Status

**Endpoint**: `GET /api/subscription/status`

**Response** (200 OK):
```json
{
  "tier": "premium",
  "status": "active" | "cancelled" | "past_due",
  "currentPeriodEnd": "2025-12-11T00:00:00Z",
  "cancelAtPeriodEnd": false
}
```

---

### 4. Cancel Subscription

**Endpoint**: `POST /api/subscription/cancel`

**Response** (200 OK):
```json
{
  "success": true,
  "cancelAtPeriodEnd": true,
  "currentPeriodEnd": "2025-12-11T00:00:00Z"
}
```

---

## 🪝 Webhooks

### Stripe Webhook

**Endpoint**: `POST /api/webhooks/stripe`

**Purpose**: Handle Stripe subscription events (payment success, subscription cancelled, etc.)

**Events Handled**:
- `checkout.session.completed`: Payment successful
- `customer.subscription.updated`: Subscription modified
- `customer.subscription.deleted`: Subscription cancelled
- `invoice.payment_failed`: Payment failed

**Signature Verification**:
```typescript
import { headers } from 'next/headers';
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export async function POST(req: Request) {
  const body = await req.text();
  const signature = headers().get('stripe-signature')!;

  let event: Stripe.Event;

  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err) {
    return new Response('Webhook signature verification failed', { status: 400 });
  }

  // Handle event
  switch (event.type) {
    case 'checkout.session.completed':
      // Upgrade user to premium
      break;
    case 'customer.subscription.deleted':
      // Downgrade user to free
      break;
  }

  return new Response(JSON.stringify({ received: true }));
}
```

---

## 🌐 External APIs

### TheMealDB

**Purpose**: Inspiration de recettes

**Base URL**: `https://www.themealdb.com/api/json/v1/1`

**Endpoints Used**:

#### Search by Ingredient
```
GET /filter.php?i={ingredient}
```

**Example**:
```typescript
async function searchByIngredient(ingredient: string) {
  const response = await fetch(
    `https://www.themealdb.com/api/json/v1/1/filter.php?i=${ingredient}`
  );
  const data = await response.json();
  return data.meals; // Array of {idMeal, strMeal, strMealThumb}
}
```

#### Get Recipe Details
```
GET /lookup.php?i={mealId}
```

**Client Wrapper**:
```typescript
// lib/apis/mealdb.ts
export class MealDBClient {
  private baseURL = 'https://www.themealdb.com/api/json/v1/1';

  async searchByIngredient(ingredient: string) {
    const response = await fetch(
      `${this.baseURL}/filter.php?i=${encodeURIComponent(ingredient)}`
    );

    if (!response.ok) {
      throw new Error('MealDB API error');
    }

    const data = await response.json();
    return data.meals || [];
  }

  async getRecipeDetails(mealId: string) {
    const response = await fetch(`${this.baseURL}/lookup.php?i=${mealId}`);
    const data = await response.json();
    return data.meals?.[0];
  }

  async getSimilarRecipes(ingredients: string[], limit = 3) {
    const results = await Promise.all(
      ingredients.slice(0, 2).map(ing => this.searchByIngredient(ing))
    );

    return results
      .flat()
      .filter((meal, index, self) =>
        index === self.findIndex(m => m.idMeal === meal.idMeal)
      )
      .slice(0, limit);
  }
}

export const mealDB = new MealDBClient();
```

**Rate Limits**: None (free tier)

---

### Edamam Nutrition

**Purpose**: Données nutritionnelles des ingrédients

**Base URL**: `https://api.edamam.com`

**Authentication**: API Key + App ID

**Endpoints Used**:

#### Nutrition Analysis
```
POST /api/nutrition-details?app_id={app_id}&app_key={app_key}
```

**Request Body**:
```json
{
  "ingredients": [
    "1 large apple",
    "2 cups rice"
  ]
}
```

**Client Wrapper**:
```typescript
// lib/apis/edamam.ts
export class EdamamClient {
  private baseURL = 'https://api.edamam.com';
  private appId = process.env.EDAMAM_APP_ID!;
  private appKey = process.env.EDAMAM_APP_KEY!;

  async getNutrition(ingredients: Array<{name: string; quantity: number; unit: string}>) {
    // Format ingredients for Edamam
    const formattedIngredients = ingredients.map(
      ing => `${ing.quantity} ${ing.unit} ${ing.name}`
    );

    const response = await fetch(
      `${this.baseURL}/api/nutrition-details?app_id=${this.appId}&app_key=${this.appKey}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ingredients: formattedIngredients })
      }
    );

    if (!response.ok) {
      console.error('Edamam API error:', await response.text());
      return null; // Non-blocking
    }

    const data = await response.json();

    return {
      calories: Math.round(data.calories),
      protein: Math.round(data.totalNutrients.PROCNT?.quantity || 0),
      carbs: Math.round(data.totalNutrients.CHOCDF?.quantity || 0),
      fat: Math.round(data.totalNutrients.FAT?.quantity || 0),
      fiber: Math.round(data.totalNutrients.FIBTG?.quantity || 0),
    };
  }
}

export const edamam = new EdamamClient();
```

**Rate Limits**: 10,000 calls/month (free tier)

**Cost**: Free

---

### Spoonacular

**Purpose**: Substitutions d'ingrédients

**Base URL**: `https://api.spoonacular.com`

**Authentication**: API Key

**Endpoints Used**:

#### Get Ingredient Substitutes
```
GET /food/ingredients/substitutes?ingredientName={ingredient}&apiKey={apiKey}
```

**Client Wrapper**:
```typescript
// lib/apis/spoonacular.ts
export class SpoonacularClient {
  private baseURL = 'https://api.spoonacular.com';
  private apiKey = process.env.SPOONACULAR_API_KEY!;

  async getSubstitutions(ingredient: string) {
    try {
      const response = await fetch(
        `${this.baseURL}/food/ingredients/substitutes?ingredientName=${encodeURIComponent(ingredient)}&apiKey=${this.apiKey}`
      );

      if (!response.ok) {
        return null;
      }

      const data = await response.json();

      return {
        original: ingredient,
        substitutes: data.substitutes.map((sub: string) => ({
          name: sub,
          ratio: "1:1" // Default
        }))
      };
    } catch (error) {
      console.error('Spoonacular API error:', error);
      return null;
    }
  }
}

export const spoonacular = new SpoonacularClient();
```

**Rate Limits**: 150 calls/day (free tier)

**Cost**: Free (with limits)

---

### Unsplash

**Purpose**: Images de recettes

**Base URL**: `https://api.unsplash.com`

**Authentication**: Access Key

**Endpoints Used**:

#### Search Photos
```
GET /search/photos?query={query}&per_page=1&client_id={access_key}
```

**Client Wrapper**:
```typescript
// lib/apis/unsplash.ts
export class UnsplashClient {
  private baseURL = 'https://api.unsplash.com';
  private accessKey = process.env.UNSPLASH_ACCESS_KEY!;

  async getRecipeImage(recipeName: string) {
    try {
      // Search for food-related image
      const query = `${recipeName} food`;

      const response = await fetch(
        `${this.baseURL}/search/photos?query=${encodeURIComponent(query)}&per_page=1&orientation=landscape&client_id=${this.accessKey}`
      );

      if (!response.ok) {
        return null;
      }

      const data = await response.json();

      if (data.results.length === 0) {
        return null;
      }

      const photo = data.results[0];

      return {
        url: photo.urls.regular,
        thumb: photo.urls.thumb,
        photographer: photo.user.name,
        photographerUrl: photo.user.links.html,
        downloadLocation: photo.links.download_location // MUST trigger download endpoint
      };
    } catch (error) {
      console.error('Unsplash API error:', error);
      return null;
    }
  }

  async triggerDownload(downloadLocation: string) {
    // Required by Unsplash API guidelines
    await fetch(`${downloadLocation}?client_id=${this.accessKey}`);
  }
}

export const unsplash = new UnsplashClient();
```

**Rate Limits**: 50 calls/hour (free tier)

**Cost**: Free

**Important**: Must trigger download endpoint when using photo (Unsplash requirement)

---

### Groq (LLM - Primary)

**Purpose**: Génération de recettes (LLM primary)

**Base URL**: `https://api.groq.com/openai/v1`

**Authentication**: API Key (Bearer token)

**Model**: `llama-3-70b-8192` (Llama 3 70B Instruct)

**Client Wrapper**:
```typescript
// lib/llm/groq.ts
import Groq from 'groq-sdk';

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY!
});

export async function generateWithGroq(
  systemPrompt: string,
  userPrompt: string,
  options = {}
) {
  const response = await groq.chat.completions.create({
    model: 'llama-3-70b-8192',
    messages: [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: userPrompt }
    ],
    temperature: 0.8,
    max_tokens: 2000,
    top_p: 0.9,
    ...options
  });

  return response.choices[0].message.content;
}
```

**Rate Limits**:
- 30 requests/minute
- 7,000 tokens/minute

**Cost**:
- ~$0.0000004/token (input)
- ~$0.00000054/token (output)
- **Extremely cheap**: ~$0.001 per recipe generation

---

### Together AI (LLM - Fallback)

**Purpose**: Génération de recettes (fallback si Groq fail)

**Base URL**: `https://api.together.xyz/v1`

**Authentication**: API Key

**Model**: `mistralai/Mixtral-8x7B-Instruct-v0.1`

**Client Wrapper**:
```typescript
// lib/llm/together.ts
import Together from 'together-ai';

const together = new Together({
  apiKey: process.env.TOGETHER_API_KEY!
});

export async function generateWithTogether(
  systemPrompt: string,
  userPrompt: string
) {
  const response = await together.chat.completions.create({
    model: 'mistralai/Mixtral-8x7B-Instruct-v0.1',
    messages: [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: userPrompt }
    ],
    temperature: 0.8,
    max_tokens: 2000,
    top_p: 0.9,
    stop: ['</s>']
  });

  return response.choices[0].message.content;
}
```

**Rate Limits**: Variable (generous on free tier)

**Cost**: ~$0.0006/1K tokens

---

## 🔧 Error Handling

### Standard Error Response

```json
{
  "error": "ErrorType",
  "message": "Human-readable error message",
  "code": "ERROR_CODE",
  "details": {} // Optional additional info
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `UNAUTHORIZED` | 401 | Missing or invalid auth token |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `QUOTA_EXCEEDED` | 429 | Freemium quota exceeded |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `VALIDATION_ERROR` | 400 | Invalid request data |
| `GENERATION_FAILED` | 500 | Recipe generation failed |
| `EXTERNAL_API_ERROR` | 502 | External API failure |

---

## 🚦 Rate Limiting

### Implementation (Upstash Redis)

```typescript
// lib/rate-limit.ts
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

export const rateLimit = {
  // Recipe generation: 50/day
  generation: new Ratelimit({
    redis: Redis.fromEnv(),
    limiter: Ratelimit.slidingWindow(50, '1 d'),
    analytics: true,
    prefix: 'radbites:ratelimit:generation'
  }),

  // General API: 60/minute
  api: new Ratelimit({
    redis: Redis.fromEnv(),
    limiter: Ratelimit.slidingWindow(60, '1 m'),
    analytics: true,
    prefix: 'radbites:ratelimit:api'
  }),
};

// Usage in API route
export async function POST(req: Request) {
  const userId = getCurrentUserId();
  const { success, limit, remaining, reset } = await rateLimit.generation.limit(userId);

  if (!success) {
    return NextResponse.json(
      { error: 'Rate limit exceeded' },
      {
        status: 429,
        headers: {
          'X-RateLimit-Limit': limit.toString(),
          'X-RateLimit-Remaining': remaining.toString(),
          'X-RateLimit-Reset': reset.toString()
        }
      }
    );
  }

  // Continue...
}
```

---

## ✅ API Best Practices

### 1. Always Validate Input

```typescript
import { z } from 'zod';

const generateRecipeSchema = z.object({
  mode: z.enum(['fridge', 'mood']),
  ingredients: z.array(z.string()).min(2).max(10).optional(),
  mood: z.string().min(10).max(200).optional(),
  constraints: z.object({
    difficulty: z.enum(['easy', 'medium', 'hard']).optional(),
    maxCookingTime: z.number().min(5).max(360).optional(),
    servings: z.number().min(1).max(12).optional()
  }).optional()
}).refine(
  data => (data.mode === 'fridge' && data.ingredients) || (data.mode === 'mood' && data.mood),
  { message: "Ingredients required for fridge mode, mood for mood mode" }
);

// In API route
const body = await req.json();
const validated = generateRecipeSchema.parse(body); // Throws if invalid
```

### 2. Use Proper HTTP Status Codes

- `200 OK`: Success (GET, PATCH)
- `201 Created`: Resource created (POST)
- `204 No Content`: Success with no body (DELETE)
- `400 Bad Request`: Validation error
- `401 Unauthorized`: Missing auth
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error
- `502 Bad Gateway`: External API failure

### 3. Non-Blocking External APIs

```typescript
// Don't let external API failures block recipe generation
async function enrichRecipe(ingredients: string[]) {
  const [nutrition, substitutions, inspiration] = await Promise.allSettled([
    edamam.getNutrition(ingredients),
    spoonacular.getSubstitutions(ingredients[0]),
    mealDB.getSimilarRecipes(ingredients)
  ]);

  return {
    nutrition: nutrition.status === 'fulfilled' ? nutrition.value : null,
    substitutions: substitutions.status === 'fulfilled' ? substitutions.value : null,
    inspiration: inspiration.status === 'fulfilled' ? inspiration.value : []
  };
}
```

### 4. Log Everything

```typescript
// Structured logging
console.log(JSON.stringify({
  timestamp: new Date().toISOString(),
  level: 'info',
  event: 'recipe_generated',
  userId,
  mode: 'fridge',
  duration: Date.now() - startTime
}));
```

---

## 📚 Environment Variables

```bash
# .env.local

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# LLM
GROQ_API_KEY=gsk_...
TOGETHER_API_KEY=...

# External APIs
EDAMAM_APP_ID=...
EDAMAM_APP_KEY=...
SPOONACULAR_API_KEY=...
UNSPLASH_ACCESS_KEY=...

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Rate Limiting (Upstash Redis)
UPSTASH_REDIS_REST_URL=https://...
UPSTASH_REDIS_REST_TOKEN=...

# Analytics (optional)
NEXT_PUBLIC_PLAUSIBLE_DOMAIN=radbites.app
```

---

*RadBites API Documentation - Production Ready*
*Version 1.0 | 2025-11-11*

**Next Steps:**
1. Test all endpoints with Postman/Insomnia
2. Write API integration tests
3. Set up monitoring (Sentry, Datadog)
4. Document API versioning strategy
