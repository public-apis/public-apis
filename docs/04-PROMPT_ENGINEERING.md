# RadBites - Prompt Engineering Guide

**Version**: 1.0
**Date**: 2025-11-11
**LLM Provider**: Groq (Llama 3 70B) + Together AI (Mixtral 8x7B fallback)
**Critical**: Ce document définit la qualité des recettes générées ⭐

---

## 📋 Table of Contents

1. [Principles & Philosophy](#principles--philosophy)
2. [System Prompts](#system-prompts)
3. [Mode Frigo: Recipe Generation](#mode-frigo-recipe-generation)
4. [Mode Envie: Mood-Based Generation](#mode-envie-mood-based-generation)
5. [RAG Context Integration](#rag-context-integration)
6. [LLM Parameters & Configuration](#llm-parameters--configuration)
7. [Output Validation & Parsing](#output-validation--parsing)
8. [Error Handling & Fallbacks](#error-handling--fallbacks)
9. [Prompt Versioning & A/B Testing](#prompt-versioning--ab-testing)
10. [Examples & Test Cases](#examples--test-cases)

---

## 🎯 Principles & Philosophy

### Core Principles

1. **Créativité Contrôlée** : Le LLM doit être créatif mais réaliste
2. **Cohérence Culinaire** : Respecter les règles de base de la cuisine
3. **Safety First** : Pas d'ingrédients dangereux, pas d'instructions risquées
4. **Personnalisation** : Intégrer contexte utilisateur (allergies, niveau, etc.)
5. **Clarté** : Instructions simples, étapes numérotées, langage accessible
6. **Inspiration ≠ Copie** : S'inspirer du RAG mais créer quelque chose d'unique

### Quality Metrics

- **Cohérence** : Ingrédients + steps logiques (pas de "ajouter du poulet" si pas dans ingredients)
- **Réalisabilité** : Temps de cuisson réaliste, techniques adaptées au niveau
- **Originalité** : Pas une copie d'une recette existante
- **Goût** : Combinaisons d'ingrédients qui ont du sens
- **Safety** : Aucun risque sanitaire (cuisson viandes, conservation, etc.)

---

## 🧠 System Prompts

### Base System Prompt (Common)

Ce prompt est utilisé pour **tous** les modes.

```typescript
const BASE_SYSTEM_PROMPT = `Tu es Chef RadBot, un chef cuisinier créatif et pédagogue spécialisé dans la création de recettes originales à partir d'ingrédients disponibles.

## Ton rôle
- Créer des recettes ORIGINALES (pas des copies de recettes existantes)
- Adapter les recettes au niveau de l'utilisateur (débutant, intermédiaire, expert)
- Respecter les contraintes (allergies, régimes alimentaires, temps de cuisson)
- Donner des explications pédagogiques (pourquoi cette technique, ce timing)
- Inspirer confiance et donner envie de cuisiner

## Principes culinaires à respecter
1. **Équilibre des saveurs** : Sucré/salé/acide/amer/umami
2. **Textures variées** : Croquant/fondant/croustillant
3. **Temps de cuisson réalistes** : Pas de "poulet cuit en 5 min"
4. **Techniques adaptées** : Niveau débutant = techniques simples
5. **Quantités cohérentes** : Proportions logiques pour le nombre de portions
6. **Sécurité alimentaire** : Cuisson complète des viandes, conservation correcte

## Ce que tu ne dois JAMAIS faire
- Inventer des ingrédients toxiques ou dangereux
- Donner des instructions contradictoires
- Sous-estimer les temps de cuisson (risque sanitaire)
- Proposer des techniques trop complexes pour débutants
- Copier mot pour mot une recette existante
- Utiliser du jargon incompréhensible

## Ton style
- Ton amical mais professionnel
- Phrases courtes et claires
- Encourageant ("Tu vas adorer !", "Le secret c'est...")
- Pédagogique (explique le "pourquoi")
- Visuel (décris les textures, couleurs, arômes)

## Format de réponse
Tu dois TOUJOURS répondre en JSON strict avec cette structure exacte :

{
  "title": "Titre créatif et appétissant (50 caractères max)",
  "description": "Description courte en 1-2 phrases (150 caractères max)",
  "difficulty": "easy" | "medium" | "hard",
  "prep_time": nombre en minutes,
  "cooking_time": nombre en minutes,
  "servings": nombre de portions (généralement 4),
  "dish_type": "starter" | "main" | "side" | "dessert",
  "ingredients": [
    {
      "name": "nom de l'ingrédient",
      "quantity": nombre (float),
      "unit": "g" | "kg" | "ml" | "l" | "pièce" | "cuillère à soupe" | "cuillère à café" | "tasse" | "pincée"
    }
  ],
  "steps": [
    "Étape 1 : instruction claire et précise",
    "Étape 2 : ...",
    ...
  ],
  "tips": "1-2 phrases avec un conseil de chef ou une astuce",
  "variations": [
    {
      "name": "Nom de la variation",
      "description": "Comment adapter la recette"
    }
  ],
  "nutrition": {
    "calories": nombre par portion,
    "protein": nombre en grammes,
    "carbs": nombre en grammes,
    "fat": nombre en grammes,
    "fiber": nombre en grammes
  }
}

IMPORTANT : Ta réponse doit être du JSON pur, sans markdown, sans \`\`\`json, juste le JSON.`;
```

---

## 🥕 Mode Frigo: Recipe Generation

### Prompt Template

```typescript
interface FridgeGenerationInput {
  ingredients: string[]; // Ex: ["poulet", "carottes", "crème", "oignons"]
  userPreferences: {
    allergies?: string[];
    dietType?: string; // 'vegetarian', 'vegan', etc.
    skillLevel?: 'beginner' | 'intermediate' | 'expert';
    maxCookingTime?: number; // minutes
  };
  constraints?: {
    difficulty?: 'easy' | 'medium' | 'hard';
    dishType?: 'starter' | 'main' | 'side' | 'dessert';
    servings?: number;
  };
  ragContext?: {
    similarRecipes: Array<{title: string; ingredients: string[]}>;
    nutritionData: any;
    substitutions: any;
    culinaryKnowledge: Array<{title: string; content: string}>;
  };
}

function buildFridgePrompt(input: FridgeGenerationInput): string {
  const {
    ingredients,
    userPreferences,
    constraints,
    ragContext
  } = input;

  // Build user context section
  let userContext = "## Contexte utilisateur\n";

  if (userPreferences.allergies?.length) {
    userContext += `- **Allergies** : ${userPreferences.allergies.join(', ')} (IMPORTANT : ne jamais utiliser ces ingrédients)\n`;
  }

  if (userPreferences.dietType && userPreferences.dietType !== 'omnivore') {
    userContext += `- **Régime** : ${userPreferences.dietType}\n`;
  }

  if (userPreferences.skillLevel) {
    const skillDesc = {
      beginner: 'débutant (techniques simples, étapes claires)',
      intermediate: 'intermédiaire (peut gérer plusieurs cuissons simultanées)',
      expert: 'expert (techniques avancées acceptées)'
    };
    userContext += `- **Niveau** : ${skillDesc[userPreferences.skillLevel]}\n`;
  }

  if (userPreferences.maxCookingTime) {
    userContext += `- **Temps max** : ${userPreferences.maxCookingTime} minutes\n`;
  }

  // Build constraints section
  let constraintsSection = "";
  if (constraints) {
    constraintsSection = "## Contraintes\n";
    if (constraints.difficulty) {
      constraintsSection += `- Difficulté souhaitée : ${constraints.difficulty}\n`;
    }
    if (constraints.dishType) {
      constraintsSection += `- Type de plat : ${constraints.dishType}\n`;
    }
    if (constraints.servings) {
      constraintsSection += `- Portions : ${constraints.servings}\n`;
    }
  }

  // Build RAG context
  let ragSection = "";
  if (ragContext) {
    ragSection = "## Inspiration et connaissances culinaires\n\n";

    if (ragContext.similarRecipes?.length) {
      ragSection += "### Recettes similaires (pour inspiration UNIQUEMENT)\n";
      ragContext.similarRecipes.forEach(r => {
        ragSection += `- **${r.title}** : ${r.ingredients.slice(0, 5).join(', ')}\n`;
      });
      ragSection += "\n*Note : Inspire-toi de ces recettes mais crée quelque chose d'ORIGINAL.*\n\n";
    }

    if (ragContext.nutritionData) {
      ragSection += "### Données nutritionnelles des ingrédients\n";
      ragSection += JSON.stringify(ragContext.nutritionData, null, 2) + "\n\n";
    }

    if (ragContext.substitutions) {
      ragSection += "### Substitutions possibles\n";
      ragSection += JSON.stringify(ragContext.substitutions, null, 2) + "\n\n";
    }

    if (ragContext.culinaryKnowledge?.length) {
      ragSection += "### Connaissances culinaires pertinentes\n";
      ragContext.culinaryKnowledge.forEach(k => {
        ragSection += `- **${k.title}** : ${k.content}\n`;
      });
      ragSection += "\n";
    }
  }

  // Build the final user prompt
  const userPrompt = `${userContext}
${constraintsSection}
${ragSection}

## Mission
Crée une recette **originale et créative** en utilisant PRINCIPALEMENT ces ingrédients :
${ingredients.map(ing => `- ${ing}`).join('\n')}

Tu peux ajouter des ingrédients de base courants (huile, sel, poivre, herbes) si nécessaire, mais les ingrédients principaux doivent être ceux listés ci-dessus.

**Rappel CRITIQUE** :
- Vérifie la cohérence : chaque ingrédient dans la liste doit être utilisé dans les steps
- Respecte les allergies et régimes (c'est NON-NÉGOCIABLE)
- Temps de cuisson réalistes (poulet = min 20min, légumes = 10-15min)
- Niveau adapté : ${userPreferences.skillLevel || 'intermédiaire'}

Génère maintenant la recette en JSON (sans markdown).`;

  return userPrompt;
}
```

### Example Input/Output

**Input:**
```typescript
{
  ingredients: ["poulet", "carottes", "crème fraîche", "oignons"],
  userPreferences: {
    skillLevel: "beginner",
    maxCookingTime: 40
  },
  constraints: {
    difficulty: "easy",
    servings: 4
  }
}
```

**Output (JSON):**
```json
{
  "title": "Poulet Crémeux aux Carottes Confites",
  "description": "Un plat réconfortant où le poulet fondant rencontre des carottes caramélisées dans une sauce crémeuse.",
  "difficulty": "easy",
  "prep_time": 10,
  "cooking_time": 30,
  "servings": 4,
  "dish_type": "main",
  "ingredients": [
    {"name": "poulet (blancs)", "quantity": 600, "unit": "g"},
    {"name": "carottes", "quantity": 4, "unit": "pièce"},
    {"name": "crème fraîche", "quantity": 200, "unit": "ml"},
    {"name": "oignons", "quantity": 2, "unit": "pièce"},
    {"name": "huile d'olive", "quantity": 2, "unit": "cuillère à soupe"},
    {"name": "sel", "quantity": 1, "unit": "pincée"},
    {"name": "poivre", "quantity": 1, "unit": "pincée"},
    {"name": "thym", "quantity": 1, "unit": "cuillère à café"}
  ],
  "steps": [
    "Couper le poulet en morceaux de taille moyenne. Éplucher et couper les carottes en rondelles, les oignons en lamelles.",
    "Dans une grande poêle, chauffer l'huile d'olive à feu moyen. Faire dorer les morceaux de poulet 5 minutes de chaque côté. Réserver.",
    "Dans la même poêle, faire revenir les oignons 3 minutes jusqu'à ce qu'ils deviennent translucides.",
    "Ajouter les carottes et laisser cuire 5 minutes en remuant régulièrement.",
    "Remettre le poulet dans la poêle, ajouter la crème fraîche, le thym, le sel et le poivre. Mélanger délicatement.",
    "Couvrir et laisser mijoter 15 minutes à feu doux. Les carottes doivent être tendres et la sauce onctueuse.",
    "Goûter et ajuster l'assaisonnement si nécessaire. Servir chaud avec du riz ou des pâtes."
  ],
  "tips": "Le secret : ne pas faire cuire le poulet à feu trop fort pour qu'il reste moelleux. Tu peux ajouter une cuillère de miel aux carottes pour les caraméliser légèrement.",
  "variations": [
    {
      "name": "Version épicée",
      "description": "Ajouter 1 cuillère à café de paprika fumé et une pincée de piment de Cayenne à l'étape 5"
    },
    {
      "name": "Version légère",
      "description": "Remplacer la crème fraîche par du yaourt grec nature (ajouter hors du feu pour éviter qu'il ne tranche)"
    }
  ],
  "nutrition": {
    "calories": 385,
    "protein": 35,
    "carbs": 12,
    "fat": 22,
    "fiber": 3
  }
}
```

---

## 🌟 Mode Envie: Mood-Based Generation

### Two-Step Process

Mode Envie utilise un **processus en 2 étapes** :

1. **Analyse du mood** : Extraire les caractéristiques de l'envie
2. **Génération de recette** : Créer une recette correspondant au mood

### Step 1: Mood Analysis Prompt

```typescript
const MOOD_ANALYSIS_PROMPT = `Tu es un analyste culinaire expert. Ton rôle est d'analyser une envie exprimée en langage naturel et d'en extraire les caractéristiques culinaires.

Analyse cette envie et extrais les informations suivantes en JSON :

{
  "mood_keywords": ["liste", "de", "mots-clés"],
  "flavor_profile": {
    "dominant": "saveur principale (salé/sucré/acide/amer/umami)",
    "secondary": ["saveurs", "secondaires"],
    "intensity": "light" | "medium" | "strong"
  },
  "texture_preferences": ["croquant", "fondant", "croustillant", "crémeux", ...],
  "comfort_level": "comforting" | "light" | "fancy" | "adventurous",
  "cuisine_style": "french" | "italian" | "asian" | "fusion" | "traditional" | null,
  "suggested_dish_type": "starter" | "main" | "side" | "dessert",
  "suggested_ingredients": ["ingrédients", "recommandés"],
  "cooking_techniques": ["techniques", "suggérées"],
  "atmosphere": "description de l'atmosphère recherchée"
}

Réponds UNIQUEMENT en JSON, sans markdown.`;

function buildMoodAnalysisPrompt(userMood: string): string {
  return `${MOOD_ANALYSIS_PROMPT}

Envie de l'utilisateur : "${userMood}"

Analyse :`;
}
```

**Example Mood Analysis:**

**Input:** "Quelque chose de réconfortant et épicé pour ce soir d'hiver"

**Output:**
```json
{
  "mood_keywords": ["réconfortant", "épicé", "hiver", "soir"],
  "flavor_profile": {
    "dominant": "salé",
    "secondary": ["épicé", "umami"],
    "intensity": "medium"
  },
  "texture_preferences": ["fondant", "crémeux"],
  "comfort_level": "comforting",
  "cuisine_style": "fusion",
  "suggested_dish_type": "main",
  "suggested_ingredients": ["viande mijotée", "légumes racines", "épices chaudes", "bouillon", "crème ou lait de coco"],
  "cooking_techniques": ["mijotage", "braisage", "caramélisation"],
  "atmosphere": "Plat chaleureux et rassurant, parfait pour se réchauffer après une journée froide"
}
```

### Step 2: Recipe Generation from Mood

```typescript
function buildMoodRecipePrompt(
  moodAnalysis: MoodAnalysis,
  userPreferences: UserPreferences,
  ragContext: RAGContext
): string {
  let prompt = `## Contexte utilisateur\n`;

  // Same user context as Mode Frigo
  if (userPreferences.allergies?.length) {
    prompt += `- **Allergies** : ${userPreferences.allergies.join(', ')}\n`;
  }
  // ... (rest of user context)

  prompt += `\n## Analyse de l'envie\n`;
  prompt += `L'utilisateur recherche une recette avec ces caractéristiques :\n`;
  prompt += `- **Ambiance** : ${moodAnalysis.atmosphere}\n`;
  prompt += `- **Profil de saveurs** : ${moodAnalysis.flavor_profile.dominant} (dominant), ${moodAnalysis.flavor_profile.secondary.join(', ')}\n`;
  prompt += `- **Textures** : ${moodAnalysis.texture_preferences.join(', ')}\n`;
  prompt += `- **Niveau de confort** : ${moodAnalysis.comfort_level}\n`;
  prompt += `- **Style de cuisine** : ${moodAnalysis.cuisine_style || 'libre'}\n`;
  prompt += `- **Ingrédients suggérés** : ${moodAnalysis.suggested_ingredients.join(', ')}\n`;
  prompt += `- **Techniques** : ${moodAnalysis.cooking_techniques.join(', ')}\n`;

  // Add RAG context
  if (ragContext) {
    prompt += `\n## Inspiration\n`;
    // ... (similar recipes, culinary knowledge)
  }

  prompt += `\n## Mission\n`;
  prompt += `Crée une recette **originale** qui correspond PARFAITEMENT à cette envie.\n\n`;
  prompt += `La recette doit :\n`;
  prompt += `- Capturer l'atmosphère recherchée\n`;
  prompt += `- Utiliser les techniques et ingrédients suggérés\n`;
  prompt += `- Respecter le profil de saveurs et textures\n`;
  prompt += `- Être réalisable et délicieuse\n\n`;
  prompt += `Génère la recette en JSON (sans markdown).`;

  return prompt;
}
```

---

## 🔄 RAG Context Integration

### When to Use RAG

Le RAG est utilisé pour **enrichir** le prompt avec :
- **Recettes similaires** : Inspiration (pas copie)
- **Connaissances culinaires** : Techniques, accords ingrédients
- **Historique utilisateur** : Recettes qu'il a aimées
- **Données nutritionnelles** : Validation réalisme

### RAG Query Strategy

```typescript
async function buildRAGContext(
  input: string | string[], // mood ou ingredients
  userPreferences: UserPreferences
): Promise<RAGContext> {
  // 1. Generate embedding
  const embedding = await openai.embeddings.create({
    model: 'text-embedding-ada-002',
    input: Array.isArray(input) ? input.join(' ') : input
  });

  // 2. Search similar recipes (user's own + public)
  const similarRecipes = await supabase.rpc('match_recipes', {
    query_embedding: embedding.data[0].embedding,
    match_threshold: 0.75,
    match_count: 3,
    filter_user_id: userPreferences.userId // Optional
  });

  // 3. Search culinary knowledge
  const culinaryKnowledge = await supabase.rpc('match_culinary_knowledge', {
    query_embedding: embedding.data[0].embedding,
    match_threshold: 0.7,
    match_count: 5
  });

  // 4. Get nutrition data from external APIs
  let nutritionData = null;
  if (Array.isArray(input)) {
    // Mode Frigo : get nutrition for ingredients
    nutritionData = await edamam.getNutritionData(input);
  }

  // 5. Get substitutions
  let substitutions = null;
  if (Array.isArray(input) && input.length > 0) {
    substitutions = await spoonacular.getSubstitutions(input[0]); // Main ingredient
  }

  return {
    similarRecipes: similarRecipes.data || [],
    culinaryKnowledge: culinaryKnowledge.data || [],
    nutritionData,
    substitutions
  };
}
```

### RAG Context Balance

⚠️ **Attention à la taille du prompt !**

- **Token limit** : Llama 3 70B = 8192 tokens max
- **RAG context** : ~2000 tokens max
- **User prompt** : ~1000 tokens
- **System prompt** : ~800 tokens
- **Output buffer** : ~2000 tokens

**Strategy** : Limiter le RAG context si trop long (résumer ou sélectionner top 2-3 items).

```typescript
function truncateRAGContext(ragContext: RAGContext, maxTokens: number = 2000): RAGContext {
  // Estimate tokens (rough: 1 token ≈ 4 chars)
  let currentTokens = 0;
  const truncated = { ...ragContext };

  // Priority: culinary knowledge > similar recipes > nutrition > substitutions

  if (truncated.culinaryKnowledge) {
    const knowledgeTokens = JSON.stringify(truncated.culinaryKnowledge).length / 4;
    if (currentTokens + knowledgeTokens > maxTokens) {
      truncated.culinaryKnowledge = truncated.culinaryKnowledge.slice(0, 3);
    }
    currentTokens += JSON.stringify(truncated.culinaryKnowledge).length / 4;
  }

  if (truncated.similarRecipes && currentTokens < maxTokens) {
    // Keep only titles and first 5 ingredients
    truncated.similarRecipes = truncated.similarRecipes.map(r => ({
      title: r.title,
      ingredients: r.ingredients.slice(0, 5)
    })).slice(0, 2);
    currentTokens += JSON.stringify(truncated.similarRecipes).length / 4;
  }

  // Truncate nutrition/substitutions if still too long
  if (currentTokens > maxTokens) {
    truncated.nutritionData = null;
    truncated.substitutions = null;
  }

  return truncated;
}
```

---

## ⚙️ LLM Parameters & Configuration

### Groq Configuration (Primary)

```typescript
const GROQ_CONFIG = {
  model: 'llama-3-70b-8192', // Llama 3 70B Instruct
  temperature: 0.8, // Créativité élevée mais contrôlée
  max_tokens: 2000, // Recette complète
  top_p: 0.9, // Nucleus sampling
  frequency_penalty: 0.3, // Éviter répétitions
  presence_penalty: 0.2, // Encourager diversité
  stop: null, // Pas de stop sequence (JSON complet attendu)
};

// Pour variations (plus créatif)
const GROQ_CONFIG_VARIATION = {
  ...GROQ_CONFIG,
  temperature: 0.9, // Plus de créativité pour variations
};

// Pour mood analysis (plus déterministe)
const GROQ_CONFIG_ANALYSIS = {
  ...GROQ_CONFIG,
  temperature: 0.3, // Moins de créativité, plus de précision
  max_tokens: 500,
};
```

### Together AI Configuration (Fallback)

```typescript
const TOGETHER_CONFIG = {
  model: 'mistralai/Mixtral-8x7B-Instruct-v0.1',
  temperature: 0.8,
  max_tokens: 2000,
  top_p: 0.9,
  repetition_penalty: 1.1, // Together AI param
  stop: ['</s>'], // Mixtral stop token
};
```

### When to Use Fallback

```typescript
async function generateWithFallback(
  systemPrompt: string,
  userPrompt: string,
  config: typeof GROQ_CONFIG
): Promise<string> {
  try {
    // Try Groq first
    const response = await groq.chat.completions.create({
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      ...config
    });
    return response.choices[0].message.content;
  } catch (error) {
    console.error('Groq failed, trying Together AI:', error);

    // Fallback to Together AI
    const response = await together.chat.completions.create({
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      ...TOGETHER_CONFIG
    });
    return response.choices[0].message.content;
  }
}
```

---

## ✅ Output Validation & Parsing

### Parsing Strategy

```typescript
interface RecipeOutput {
  title: string;
  description: string;
  difficulty: 'easy' | 'medium' | 'hard';
  prep_time: number;
  cooking_time: number;
  servings: number;
  dish_type: 'starter' | 'main' | 'side' | 'dessert';
  ingredients: Array<{
    name: string;
    quantity: number;
    unit: string;
  }>;
  steps: string[];
  tips: string;
  variations: Array<{
    name: string;
    description: string;
  }>;
  nutrition: {
    calories: number;
    protein: number;
    carbs: number;
    fat: number;
    fiber: number;
  };
}

function parseRecipeOutput(llmOutput: string): RecipeOutput {
  // 1. Clean output (remove markdown if present)
  let cleaned = llmOutput.trim();

  // Remove ```json and ``` if present
  if (cleaned.startsWith('```json')) {
    cleaned = cleaned.replace(/^```json\n/, '').replace(/\n```$/, '');
  } else if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```\n/, '').replace(/\n```$/, '');
  }

  // 2. Parse JSON
  let parsed: any;
  try {
    parsed = JSON.parse(cleaned);
  } catch (error) {
    // Try to fix common JSON errors
    cleaned = cleaned
      .replace(/,\s*}/g, '}') // Trailing commas
      .replace(/,\s*]/g, ']')
      .replace(/'/g, '"'); // Single quotes to double

    try {
      parsed = JSON.parse(cleaned);
    } catch (retryError) {
      throw new Error('Invalid JSON output from LLM');
    }
  }

  // 3. Validate with Zod schema
  const recipeSchema = z.object({
    title: z.string().min(5).max(100),
    description: z.string().max(200),
    difficulty: z.enum(['easy', 'medium', 'hard']),
    prep_time: z.number().int().min(0).max(180),
    cooking_time: z.number().int().min(0).max(360),
    servings: z.number().int().min(1).max(12),
    dish_type: z.enum(['starter', 'main', 'side', 'dessert']),
    ingredients: z.array(z.object({
      name: z.string().min(1),
      quantity: z.number().positive().max(10000),
      unit: z.string()
    })).min(2).max(20),
    steps: z.array(z.string().min(10)).min(2).max(15),
    tips: z.string().max(300),
    variations: z.array(z.object({
      name: z.string(),
      description: z.string()
    })).optional(),
    nutrition: z.object({
      calories: z.number().min(0).max(5000),
      protein: z.number().min(0).max(500),
      carbs: z.number().min(0).max(500),
      fat: z.number().min(0).max(500),
      fiber: z.number().min(0).max(100)
    })
  });

  const validated = recipeSchema.parse(parsed);

  // 4. Additional semantic validation
  validateRecipeSemantics(validated);

  return validated;
}
```

### Semantic Validation

```typescript
function validateRecipeSemantics(recipe: RecipeOutput): void {
  // 1. Check ingredients are used in steps
  const stepsText = recipe.steps.join(' ').toLowerCase();
  const unusedIngredients = recipe.ingredients.filter(ing => {
    const ingredientName = ing.name.toLowerCase();
    return !stepsText.includes(ingredientName);
  });

  if (unusedIngredients.length > 0) {
    console.warn('Unused ingredients:', unusedIngredients.map(i => i.name));
    // Don't throw, just warn (LLM might use synonyms)
  }

  // 2. Check cooking time is realistic
  const totalTime = recipe.prep_time + recipe.cooking_time;
  if (totalTime < 5) {
    throw new Error('Cooking time too short (< 5 min)');
  }
  if (totalTime > 480) { // 8 hours
    throw new Error('Cooking time unrealistic (> 8 hours)');
  }

  // 3. Check dangerous keywords
  const dangerousKeywords = ['poison', 'toxique', 'cru' /* if meat */, 'non cuit'];
  const allText = JSON.stringify(recipe).toLowerCase();
  const foundDangerous = dangerousKeywords.find(kw => allText.includes(kw));
  if (foundDangerous) {
    throw new Error(`Dangerous keyword found: ${foundDangerous}`);
  }

  // 4. Check quantities are reasonable
  const unreasonableIngredients = recipe.ingredients.filter(ing => {
    if (ing.unit === 'kg' && ing.quantity > 5) return true; // > 5kg
    if (ing.unit === 'l' && ing.quantity > 3) return true; // > 3L
    if (ing.unit === 'g' && ing.quantity > 2000) return true; // > 2kg
    return false;
  });

  if (unreasonableIngredients.length > 0) {
    console.warn('Unreasonable quantities:', unreasonableIngredients);
  }

  // 5. Check nutrition is realistic per serving
  const { calories, protein, carbs, fat } = recipe.nutrition;
  if (calories < 50 || calories > 2000) {
    throw new Error(`Unrealistic calories per serving: ${calories}`);
  }

  // Calories should roughly match macros (4 cal/g for protein/carbs, 9 cal/g for fat)
  const estimatedCalories = (protein * 4) + (carbs * 4) + (fat * 9);
  const caloriesDiff = Math.abs(calories - estimatedCalories);
  if (caloriesDiff > calories * 0.3) { // 30% margin
    console.warn(`Nutrition mismatch: stated ${calories} cal, estimated ${estimatedCalories} cal`);
  }
}
```

---

## 🚨 Error Handling & Fallbacks

### Retry Strategy

```typescript
async function generateRecipeWithRetry(
  systemPrompt: string,
  userPrompt: string,
  maxRetries: number = 2
): Promise<RecipeOutput> {
  let lastError: Error | null = null;

  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      // Generate
      const llmOutput = await generateWithFallback(
        systemPrompt,
        userPrompt,
        GROQ_CONFIG
      );

      // Parse & validate
      const recipe = parseRecipeOutput(llmOutput);

      // Success!
      return recipe;

    } catch (error) {
      lastError = error as Error;
      console.error(`Attempt ${attempt + 1} failed:`, error);

      if (attempt < maxRetries - 1) {
        // Adjust prompt for retry
        if (error.message.includes('Invalid JSON')) {
          userPrompt += '\n\nIMPORTANT: Ta réponse doit être du JSON valide, sans markdown, sans texte additionnel.';
        } else if (error.message.includes('Cooking time')) {
          userPrompt += '\n\nATTENTION: Vérifie que les temps de cuisson sont réalistes.';
        } else if (error.message.includes('Nutrition')) {
          userPrompt += '\n\nATTENTION: Vérifie que les valeurs nutritionnelles sont cohérentes avec les macros.';
        }

        // Wait before retry (exponential backoff)
        await new Promise(resolve => setTimeout(resolve, 1000 * (attempt + 1)));
      }
    }
  }

  // All retries failed
  throw new Error(`Recipe generation failed after ${maxRetries} attempts: ${lastError?.message}`);
}
```

### User-Facing Error Messages

```typescript
function getUserFriendlyError(error: Error): string {
  if (error.message.includes('Invalid JSON')) {
    return "Oups, j'ai eu du mal à créer cette recette. Peux-tu réessayer avec des ingrédients légèrement différents ?";
  }

  if (error.message.includes('Cooking time')) {
    return "Cette recette semble avoir un problème de timing. Réessayons !";
  }

  if (error.message.includes('quota') || error.message.includes('429')) {
    return "Tu as atteint ta limite de générations cette semaine. Passe en Premium pour des générations illimitées !";
  }

  if (error.message.includes('timeout')) {
    return "La génération prend trop de temps. Réessaye dans quelques instants.";
  }

  // Default
  return "Une erreur inattendue est survenue. Notre équipe a été notifiée. Réessaye dans un moment !";
}
```

---

## 🔬 Prompt Versioning & A/B Testing

### Versioning Strategy

```typescript
// Store prompts with versions
const PROMPT_VERSIONS = {
  'base_system_v1.0': BASE_SYSTEM_PROMPT,
  'base_system_v1.1': BASE_SYSTEM_PROMPT_V1_1, // Future iterations
  // ...
};

// Track which version was used for each recipe
interface RecipeGeneration {
  recipeId: string;
  promptVersion: string;
  userRating?: number;
  generatedAt: Date;
}

// Log every generation
async function logGeneration(
  recipeId: string,
  promptVersion: string,
  userId: string
) {
  await supabase.from('recipe_generations').insert({
    recipe_id: recipeId,
    prompt_version: promptVersion,
    user_id: userId,
    generated_at: new Date().toISOString()
  });
}
```

### A/B Testing Framework

```typescript
// Define experiments
interface PromptExperiment {
  name: string;
  variants: {
    control: string; // Prompt version
    treatment: string; // Alternative prompt version
  };
  allocation: number; // % of users in treatment (0-100)
  metrics: string[]; // ['rating', 'favorite_rate', 'completion_rate']
  startDate: Date;
  endDate?: Date;
}

const ACTIVE_EXPERIMENTS: PromptExperiment[] = [
  {
    name: 'exp_creative_temperature',
    variants: {
      control: 'base_system_v1.0', // temp 0.8
      treatment: 'base_system_v1.1_temp_0.9' // temp 0.9
    },
    allocation: 50, // 50% in treatment
    metrics: ['rating', 'favorite_rate'],
    startDate: new Date('2025-11-15'),
    endDate: new Date('2025-12-01')
  }
];

// Assign user to variant
function getPromptVariant(userId: string, experiment: PromptExperiment): string {
  // Stable hash-based assignment
  const hash = simpleHash(userId + experiment.name);
  const bucket = hash % 100;

  if (bucket < experiment.allocation) {
    return experiment.variants.treatment;
  }
  return experiment.variants.control;
}

function simpleHash(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) - hash) + str.charCodeAt(i);
    hash = hash & hash; // Convert to 32bit integer
  }
  return Math.abs(hash);
}

// Usage in generation
async function generateRecipe(/* ... */): Promise<RecipeOutput> {
  // Check active experiments
  const experiment = ACTIVE_EXPERIMENTS[0]; // Simplified
  const promptVersion = experiment
    ? getPromptVariant(userId, experiment)
    : 'base_system_v1.0';

  const systemPrompt = PROMPT_VERSIONS[promptVersion];

  // Generate with assigned variant
  const recipe = await generateRecipeWithRetry(systemPrompt, userPrompt);

  // Log for analysis
  await logGeneration(recipe.id, promptVersion, userId);

  return recipe;
}
```

### Analyzing Results

```sql
-- Query to compare experiment results
SELECT
  rg.prompt_version,
  COUNT(*) as total_recipes,
  AVG(r.quality_rating) as avg_rating,
  SUM(CASE WHEN r.is_favorite THEN 1 ELSE 0 END)::float / COUNT(*) as favorite_rate,
  AVG(EXTRACT(EPOCH FROM (r.updated_at - r.created_at))) as avg_time_to_favorite
FROM recipe_generations rg
JOIN recipes r ON r.id = rg.recipe_id
WHERE rg.generated_at BETWEEN '2025-11-15' AND '2025-12-01'
GROUP BY rg.prompt_version;
```

---

## 📝 Examples & Test Cases

### Test Case 1: Mode Frigo - Beginner

**Input:**
```typescript
{
  ingredients: ["pâtes", "tomates", "basilic", "ail"],
  userPreferences: {
    skillLevel: "beginner",
    maxCookingTime: 20
  },
  constraints: {
    difficulty: "easy"
  }
}
```

**Expected Output Characteristics:**
- Title mentioning "pâtes" et "tomates"
- Difficulty = "easy"
- cooking_time ≤ 20 min
- Steps simples (max 6 steps)
- Techniques de base (faire bouillir, couper, mélanger)
- Pas de jargon technique

---

### Test Case 2: Mode Frigo - Expert avec Allergies

**Input:**
```typescript
{
  ingredients: ["saumon", "asperges", "citron", "beurre"],
  userPreferences: {
    skillLevel: "expert",
    allergies: ["gluten"],
    maxCookingTime: 45
  },
  constraints: {
    difficulty: "hard",
    dishType: "main"
  }
}
```

**Expected Output Characteristics:**
- Difficulty = "hard"
- Techniques avancées (papillote, émulsion, réduction)
- AUCUN ingrédient avec gluten
- Présentation soignée mentionnée
- Tips techniques (température exacte, timing précis)

---

### Test Case 3: Mode Envie - Comfort Food

**Input:**
```typescript
{
  mood: "Quelque chose de réconfortant pour me remonter le moral",
  userPreferences: {
    skillLevel: "intermediate",
    dietType: "vegetarian"
  }
}
```

**Expected Mood Analysis:**
```json
{
  "comfort_level": "comforting",
  "flavor_profile": {
    "dominant": "salé",
    "secondary": ["umami", "crémeux"]
  },
  "suggested_ingredients": ["fromage", "pâtes", "légumes rôtis", "crème"],
  "atmosphere": "Plat chaleureux et rassurant"
}
```

**Expected Recipe Characteristics:**
- Dish_type = "main"
- Ingrédients riches (fromage, crème, féculents)
- Textures réconfortantes (fondant, crémeux)
- Pas de viande (vegetarian)
- Description évocant chaleur et réconfort

---

### Test Case 4: Edge Case - Ingrédients Incompatibles

**Input:**
```typescript
{
  ingredients: ["chocolat", "saumon", "oignons"],
  userPreferences: {
    skillLevel: "intermediate"
  }
}
```

**Expected Behavior:**
Le LLM doit soit :
1. Créer 2 recettes distinctes (une sucrée avec chocolat, une salée avec saumon/oignons)
2. OU demander clarification
3. OU créer une recette fusion audacieuse (rare mais acceptable si expert)

**Validation:** Checker que la recette a du sens (pas de "saumon au chocolat et oignons" sauf si très bien justifié).

---

### Test Case 5: Variations

**Input (après recette générée):**
```typescript
{
  originalRecipe: { /* Poulet Crémeux */ },
  variations: ["plus épicé", "version végétarienne"]
}
```

**Expected Output:**
```json
{
  "title": "Tofu Crémeux aux Carottes Confites (Version Végétarienne Épicée)",
  "ingredients": [
    {"name": "tofu ferme", "quantity": 400, "unit": "g"}, // remplace poulet
    {"name": "piment de Cayenne", "quantity": 0.5, "unit": "cuillère à café"}, // ajout
    // ... rest similar
  ],
  "tips": "Le tofu doit être bien pressé avant cuisson pour absorber les saveurs. Le piment apporte du punch tout en gardant l'aspect réconfortant."
}
```

---

## 🎓 Best Practices Summary

### DO ✅
1. **Toujours valider l'output** avec Zod schema
2. **Tronquer le RAG context** si trop long (> 2000 tokens)
3. **Logger chaque génération** pour analyse
4. **Retry avec prompt ajusté** en cas d'erreur
5. **Tester les edge cases** régulièrement
6. **Versionner les prompts** et A/B test
7. **Monitorer les hallucinations** via user feedback

### DON'T ❌
1. Ne jamais ignorer les allergies (CRITIQUE)
2. Ne pas dépasser token limit (8192 pour Llama 3)
3. Ne pas utiliser température > 1.0 (perte de contrôle)
4. Ne pas générer sans validation
5. Ne pas copier verbatim des recettes existantes (copyright)
6. Ne pas utiliser jargon technique pour débutants
7. Ne pas ignorer les erreurs silencieusement

---

## 📊 Monitoring & Improvement

### Metrics to Track

```typescript
interface PromptMetrics {
  promptVersion: string;

  // Quality
  avgRating: number; // User ratings 1-5
  favoriteRate: number; // % of recipes favorited
  reportRate: number; // % of recipes reported (problems)

  // Performance
  avgGenerationTime: number; // seconds
  errorRate: number; // % of failed generations
  retryRate: number; // % needing retry

  // Usage
  totalGenerations: number;
  uniqueUsers: number;
}
```

### Continuous Improvement Loop

```
1. Deploy new prompt version (A/B test)
2. Collect data (2 weeks)
3. Analyze metrics
4. Iterate prompt
5. Repeat
```

### Red Flags 🚩

- **Error rate > 5%** : Prompt trop complexe ou LLM instable
- **Avg rating < 3.5** : Qualité recettes insuffisante
- **Report rate > 2%** : Hallucinations ou erreurs dangereuses
- **Generation time > 15s** : Prompt trop long ou API lente

---

## ✅ Checklist Before Production

- [ ] System prompt tested on 20+ diverse inputs
- [ ] Validation schema covers all edge cases
- [ ] Error handling tested (timeout, invalid JSON, etc.)
- [ ] RAG context truncation working
- [ ] Fallback to Together AI functional
- [ ] Retry logic tested
- [ ] User-friendly error messages defined
- [ ] Logging & monitoring in place
- [ ] A/B testing framework ready
- [ ] Dangerous keywords blacklist comprehensive
- [ ] Allergy handling tested and validated
- [ ] Token limits respected (< 8000 input tokens)

---

*RadBites Prompt Engineering Guide - Production Ready*
*Version 1.0 | 2025-11-11*

**Next Review**: After 1000 recipes generated (analyze quality metrics)
