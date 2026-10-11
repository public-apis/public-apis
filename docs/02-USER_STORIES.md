# RadBites - User Stories

**Version**: 1.0
**Date**: 2025-11-11
**Sprint Planning**: MVP (Sprints 1-4)

---

## 📋 Story Format

Chaque user story suit ce format :

```
En tant que [type d'utilisateur],
Je veux [objectif],
Afin de [bénéfice].

Acceptance Criteria:
- [ ] Critère 1
- [ ] Critère 2

Technical Notes: [Détails d'implémentation]
Priority: [P0 = Critique | P1 = Important | P2 = Nice-to-have]
Story Points: [1, 2, 3, 5, 8, 13]
Sprint: [1, 2, 3, 4]
```

---

## 🎯 Epic 1 : Authentification & Onboarding

### US-001 : Inscription utilisateur

**En tant que** nouvel utilisateur,
**Je veux** créer un compte rapidement,
**Afin de** commencer à utiliser RadBites.

**Acceptance Criteria:**
- [ ] Formulaire inscription avec email + password
- [ ] Validation email (format)
- [ ] Password minimum 8 caractères
- [ ] Bouton "Sign up with Google" fonctionnel
- [ ] Bouton "Sign up with Apple" (si iOS)
- [ ] Redirection vers onboarding après inscription
- [ ] Message erreur clair si email déjà utilisé
- [ ] Envoi email de confirmation (Supabase)
- [ ] Auto-login après inscription

**Technical Notes:**
```typescript
// Supabase Auth
const { data, error } = await supabase.auth.signUp({
  email: email,
  password: password,
  options: {
    data: {
      subscription_tier: 'free',
      weekly_generations_count: 0
    }
  }
});
```

**Priority:** P0 (Critique)
**Story Points:** 5
**Sprint:** 1

---

### US-002 : Connexion utilisateur

**En tant qu'** utilisateur existant,
**Je veux** me connecter à mon compte,
**Afin d'** accéder à mes recettes sauvegardées.

**Acceptance Criteria:**
- [ ] Formulaire login email + password
- [ ] Social login (Google, Apple)
- [ ] "Forgot password?" link fonctionnel
- [ ] Message erreur clair si credentials invalides
- [ ] Redirection vers dashboard après login
- [ ] Session persistante (remember me)
- [ ] Rate limiting (max 5 tentatives/min)

**Technical Notes:**
```typescript
const { data, error } = await supabase.auth.signInWithPassword({
  email,
  password
});

// Social auth
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: {
    redirectTo: `${window.location.origin}/auth/callback`
  }
});
```

**Priority:** P0
**Story Points:** 3
**Sprint:** 1

---

### US-003 : Onboarding questionnaire

**En tant que** nouvel utilisateur,
**Je veux** renseigner mes préférences culinaires,
**Afin de** recevoir des recettes personnalisées.

**Acceptance Criteria:**
- [ ] Écran 1 : "Allergies/Intolérances ?" (multi-select)
  - Options : Gluten, Lactose, Noix, Fruits de mer, Œufs, Soja, Aucune
- [ ] Écran 2 : "Régime alimentaire ?" (single select)
  - Options : Omnivore, Végétarien, Vegan, Pescatarien, Keto, Paleo, Aucun
- [ ] Écran 3 : "Niveau de cuisine ?" (single select)
  - Débutant, Intermédiaire, Expert
- [ ] Écran 4 : "Temps de cuisson préféré ?" (slider)
  - 15min, 30min, 45min, 1h, 1h30+
- [ ] Écran 5 : "Objectifs ?" (multi-select)
  - Gagner du temps, Manger sain, Découvrir, Impressionner
- [ ] Progress bar (1/5, 2/5, etc.)
- [ ] Bouton "Skip" visible
- [ ] Sauvegarde dans `user_preferences` table
- [ ] Animation de transition entre écrans
- [ ] Écran final : "🎉 Prêt ! Tu as 5 générations gratuites cette semaine"

**Technical Notes:**
```typescript
// Save preferences
await supabase.from('user_preferences').insert({
  user_id: user.id,
  allergies: ['gluten', 'lactose'],
  diet_type: 'vegetarian',
  skill_level: 'intermediate',
  max_cooking_time: 30,
  goals: ['save_time', 'eat_healthy']
});
```

**Priority:** P1
**Story Points:** 5
**Sprint:** 1

---

## 🥕 Epic 2 : Mode Frigo (Core Feature)

### US-004 : Input ingrédients

**En tant qu'** utilisateur,
**Je veux** saisir les ingrédients que j'ai,
**Afin de** générer une recette personnalisée.

**Acceptance Criteria:**
- [ ] Champ input avec placeholder "Ex: poulet, carottes, oignons..."
- [ ] Autocomplete basé sur liste ingrédients communs (locale + API)
- [ ] Ajout d'ingrédient par "Enter" ou clic sur suggestion
- [ ] Display des ingrédients sélectionnés (pills/chips)
- [ ] Bouton "×" pour retirer un ingrédient
- [ ] Minimum 2 ingrédients pour activer bouton "Générer"
- [ ] Maximum 10 ingrédients (éviter surcharge)
- [ ] Message guidant si < 2 ingrédients
- [ ] Sauvegarde temporaire (localStorage) si refresh page

**Technical Notes:**
```typescript
// Autocomplete ingrédients
const commonIngredients = [
  'poulet', 'boeuf', 'porc', 'saumon', 'tofu',
  'carottes', 'oignons', 'tomates', 'ail', 'pommes de terre',
  'riz', 'pâtes', 'crème', 'lait', 'œufs', 'beurre'
  // ... ~200 ingrédients communs
];

// Composant shadcn/ui : Command ou Combobox
<Command>
  <CommandInput placeholder="Ajouter un ingrédient..." />
  <CommandList>
    <CommandGroup>
      {filteredIngredients.map(ing => (
        <CommandItem onSelect={() => addIngredient(ing)}>
          {ing}
        </CommandItem>
      ))}
    </CommandGroup>
  </CommandList>
</Command>
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 1

---

### US-005 : Contraintes optionnelles (Mode Frigo)

**En tant qu'** utilisateur,
**Je veux** spécifier des contraintes de temps/difficulté,
**Afin d'** avoir une recette adaptée à ma situation.

**Acceptance Criteria:**
- [ ] Section "Options" (collapsible/expandable)
- [ ] Temps max : Slider (15, 30, 45, 60, 90+ min)
- [ ] Difficulté : Select (Facile, Intermédiaire, Difficile, Peu importe)
- [ ] Type de plat : Select (Entrée, Plat principal, Accompagnement, Dessert, Peu importe)
- [ ] Nombre de portions : Input number (1-12, default 4)
- [ ] Ces contraintes sont optionnelles (defaults raisonnables)
- [ ] Persistance des préférences (user_preferences)

**Technical Notes:**
```typescript
interface RecipeConstraints {
  maxCookingTime?: number; // minutes
  difficulty?: 'easy' | 'medium' | 'hard';
  dishType?: 'starter' | 'main' | 'side' | 'dessert';
  servings?: number;
}
```

**Priority:** P1
**Story Points:** 3
**Sprint:** 2

---

### US-006 : Génération de recette (Mode Frigo)

**En tant qu'** utilisateur,
**Je veux** générer une recette à partir de mes ingrédients,
**Afin de** savoir quoi cuisiner.

**Acceptance Criteria:**
- [ ] Clic sur "Générer" déclenche appel API
- [ ] Loading state avec animation engageante (8-10s)
  - Ex: "🔍 Analyse de tes ingrédients...", "🧑‍🍳 Création de ta recette...", "✨ Finalisation..."
- [ ] Génération < 10s (P95)
- [ ] Affichage recette complète :
  - Titre créatif
  - Photo (Unsplash fallback ou placeholder)
  - Tags (difficulté, temps, portions)
  - Liste ingrédients avec quantités
  - Steps numérotés
  - Tips du chef (1-2 phrases)
  - Nutrition (calories, protéines, glucides, lipides)
- [ ] Recette cohérente (pas d'hallucinations graves)
- [ ] Gestion erreurs (timeout, API error)
- [ ] Décompte quota freemium (5/5 → 4/5 → ...)
- [ ] Affichage quota restant après génération

**Technical Notes:**
```typescript
// API Route: /api/recipes/generate
async function POST(req: Request) {
  const { ingredients, constraints, userId } = await req.json();

  // 1. Check quota (freemium)
  const user = await getUser(userId);
  if (user.weekly_generations_count >= 5 && user.tier === 'free') {
    return Response.json({ error: 'Quota exceeded' }, { status: 429 });
  }

  // 2. Enrichment
  const [nutrition, substitutions, inspiration] = await Promise.all([
    edamam.getNutrition(ingredients),
    spoonacular.getSubstitutions(ingredients),
    mealDB.getSimilarRecipes(ingredients)
  ]);

  // 3. RAG context
  const ragContext = await supabase.rpc('match_recipes', {
    query_embedding: await getEmbedding(ingredients.join(' ')),
    match_threshold: 0.7,
    match_count: 5
  });

  // 4. LLM generation
  const recipe = await groq.chat.completions.create({
    model: 'llama-3-70b-8192',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: buildPrompt({ ingredients, constraints, nutrition, ragContext }) }
    ],
    temperature: 0.8,
    max_tokens: 2000
  });

  // 5. Parse & validate
  const structuredRecipe = parseRecipe(recipe.choices[0].message.content);

  // 6. Save
  const saved = await supabase.from('recipes').insert({
    user_id: userId,
    ...structuredRecipe,
    generation_mode: 'fridge',
    input_data: { ingredients, constraints }
  });

  // 7. Update quota
  await incrementGenerationCount(userId);

  return Response.json(structuredRecipe);
}
```

**Priority:** P0
**Story Points:** 13
**Sprint:** 2

---

### US-007 : Affichage de la recette

**En tant qu'** utilisateur,
**Je veux** lire la recette générée de manière claire,
**Afin de** pouvoir la suivre en cuisinant.

**Acceptance Criteria:**
- [ ] Layout mobile-optimized (lecture facile)
- [ ] Header :
  - Titre (H1, prominent)
  - Photo recette (si disponible)
  - Tags (badges) : Difficulté, Temps, Portions
- [ ] Section Ingrédients :
  - Liste à puces
  - Quantités + unités
  - Checkbox par ingrédient (optionnel, pour cocher au fur et à mesure)
- [ ] Section Instructions :
  - Steps numérotés
  - Texte clair, court par step
  - Timer intégré (si mention de temps dans step)
- [ ] Section Nutrition :
  - Calories, Protéines, Glucides, Lipides
  - Visual (progress bars ou pie chart simple)
- [ ] Section Tips :
  - Encadré distinct
  - Ton pédagogique
- [ ] Actions (sticky bottom bar ou floating) :
  - ❤️ Sauvegarder
  - 🔄 Régénérer (variante)
  - 📤 Partager
- [ ] Scroll smooth, lisible en cuisinant (texte assez gros)

**Technical Notes:**
```typescript
// Component structure
<RecipeDetail recipe={recipe}>
  <RecipeHeader title={title} image={image} tags={tags} />
  <RecipeIngredients ingredients={ingredients} />
  <RecipeSteps steps={steps} />
  <RecipeNutrition nutrition={nutrition} />
  <RecipeTips tips={tips} />
  <RecipeActions onSave={handleSave} onRegenerate={handleRegenerate} onShare={handleShare} />
</RecipeDetail>
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 2

---

## 🌟 Epic 3 : Mode Envie

### US-008 : Input envie en langage naturel

**En tant qu'** utilisateur,
**Je veux** décrire mon envie culinaire librement,
**Afin de** recevoir une recette appropriée.

**Acceptance Criteria:**
- [ ] Textarea pour input libre
- [ ] Placeholder inspirant : "Ex: Quelque chose de réconfortant et épicé pour ce soir..."
- [ ] Minimum 10 caractères pour activer bouton "Générer"
- [ ] Suggestions d'envies prédéfinies (pills cliquables) :
  - "Réconfortant et chaleureux"
  - "Léger et frais"
  - "Épicé et exotique"
  - "Impressionner mes invités"
  - "Rapide et facile"
- [ ] Clic sur suggestion = pre-fill textarea
- [ ] Mêmes contraintes optionnelles que Mode Frigo
- [ ] Bouton "Générer" prominent

**Technical Notes:**
```typescript
// Analyze mood avec LLM
const moodAnalysis = await groq.chat.completions.create({
  model: 'llama-3-70b-8192',
  messages: [{
    role: 'system',
    content: `Analyze this culinary mood and extract:
    - dish_type (starter/main/side/dessert)
    - flavors (spicy/sweet/savory/tangy/etc)
    - comfort_level (comforting/light/fancy)
    - cuisine_style (italian/asian/french/etc)
    - suggested_ingredients (list)`
  }, {
    role: 'user',
    content: userMood
  }],
  temperature: 0.3, // Plus déterministe pour l'analyse
  response_format: { type: 'json_object' }
});
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 2

---

### US-009 : Génération recette depuis envie

**En tant qu'** utilisateur,
**Je veux** obtenir une recette basée sur mon envie,
**Afin de** satisfaire mes désirs culinaires du moment.

**Acceptance Criteria:**
- [ ] Analyse de l'envie (LLM NLP)
- [ ] Extraction des caractéristiques (saveurs, type, confort)
- [ ] Recherche RAG de recettes similaires
- [ ] Génération recette cohérente avec l'envie
- [ ] Même format de recette que Mode Frigo
- [ ] Affichage des ingrédients nécessaires
- [ ] Même gestion quota freemium
- [ ] Loading state : "🔮 Analyse de ton envie...", "✨ Création de la recette parfaite..."

**Technical Notes:**
```typescript
// Le prompt doit incorporer le mood analysis
const prompt = `
Tu es un chef créatif. L'utilisateur a cette envie : "${userMood}"

Analyse de l'envie :
${JSON.stringify(moodAnalysis)}

Recettes similaires (inspiration) :
${JSON.stringify(ragSimilarRecipes)}

Crée une recette ORIGINALE qui correspond parfaitement à cette envie.
Format JSON strict : {...}
`;
```

**Priority:** P0
**Story Points:** 8
**Sprint:** 2

---

## ❤️ Epic 4 : Sauvegarde & Favoris

### US-010 : Sauvegarder une recette

**En tant qu'** utilisateur,
**Je veux** sauvegarder mes recettes préférées,
**Afin de** les retrouver facilement.

**Acceptance Criteria:**
- [ ] Bouton ❤️ "Sauvegarder" visible sur chaque recette
- [ ] Clic = sauvegarde immédiate (optimistic UI)
- [ ] Toast confirmation "Recette sauvegardée !"
- [ ] Icône ❤️ devient pleine (vs outline)
- [ ] Re-clic = retirer des favoris (toggle)
- [ ] Limite freemium : 3 sauvegardes max
- [ ] Si limite atteinte : Paywall soft
  - "Tu as atteint la limite de 3 favoris. Passe en Premium pour sauvegardes illimitées !"
  - CTA : "Débloquer" → Trial ou Premium
- [ ] Premium : Sauvegardes illimitées
- [ ] Synchro Supabase instantanée

**Technical Notes:**
```typescript
async function toggleFavorite(recipeId: string, userId: string) {
  // Check if already favorited
  const existing = await supabase
    .from('recipes')
    .select('is_favorite')
    .eq('id', recipeId)
    .single();

  if (existing.is_favorite) {
    // Unfavorite
    await supabase
      .from('recipes')
      .update({ is_favorite: false })
      .eq('id', recipeId);
  } else {
    // Check freemium limit
    const favCount = await supabase
      .from('recipes')
      .select('id', { count: 'exact' })
      .eq('user_id', userId)
      .eq('is_favorite', true);

    if (favCount.count >= 3 && user.tier === 'free') {
      throw new Error('Freemium limit reached');
    }

    // Favorite
    await supabase
      .from('recipes')
      .update({ is_favorite: true })
      .eq('id', recipeId);
  }
}
```

**Priority:** P0
**Story Points:** 3
**Sprint:** 3

---

### US-011 : Consulter mes favoris

**En tant qu'** utilisateur,
**Je veux** accéder à la liste de mes recettes favorites,
**Afin de** les consulter même offline.

**Acceptance Criteria:**
- [ ] Menu principal : Onglet "Mes Favoris" (❤️ icon)
- [ ] Liste des recettes sauvegardées (cards)
- [ ] Chaque card affiche :
  - Photo recette (si disponible)
  - Titre
  - Tags (temps, difficulté)
  - Date de sauvegarde
- [ ] Tri par défaut : Plus récent d'abord
- [ ] Option tri : Alphabétique, Temps de cuisson
- [ ] Clic sur card = ouvre recette complète
- [ ] Empty state si aucun favori :
  - Illustration
  - "Aucune recette sauvegardée pour l'instant"
  - CTA : "Créer ma première recette"
- [ ] Offline-capable (PWA cache)
- [ ] Pull-to-refresh pour sync

**Technical Notes:**
```typescript
// Fetch favorites
const { data: favorites } = await supabase
  .from('recipes')
  .select('*')
  .eq('user_id', userId)
  .eq('is_favorite', true)
  .order('created_at', { ascending: false });

// PWA cache strategy (service worker)
self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/recipes/favorites')) {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request).then((fetchResponse) => {
          return caches.open('recipes-v1').then((cache) => {
            cache.put(event.request, fetchResponse.clone());
            return fetchResponse;
          });
        });
      })
    );
  }
});
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 3

---

### US-012 : Supprimer un favori

**En tant qu'** utilisateur,
**Je veux** supprimer une recette de mes favoris,
**Afin de** garder seulement celles que j'aime vraiment.

**Acceptance Criteria:**
- [ ] Swipe left sur card → reveal bouton "Supprimer" (mobile)
- [ ] Ou menu "..." → "Retirer des favoris"
- [ ] Confirmation avant suppression :
  - "Retirer cette recette de tes favoris ?"
  - Boutons : "Annuler" / "Retirer"
- [ ] Suppression avec animation (slide out)
- [ ] Toast confirmation "Recette retirée des favoris"
- [ ] Undo possible (5 secondes) : "Annuler" dans toast
- [ ] Si undo : restauration immédiate

**Technical Notes:**
```typescript
// Soft delete (ou toggle is_favorite)
async function removeFavorite(recipeId: string) {
  await supabase
    .from('recipes')
    .update({ is_favorite: false })
    .eq('id', recipeId);
}

// Undo implementation
let undoTimeout: NodeJS.Timeout;
function showUndoToast(recipeId: string) {
  toast({
    title: 'Recette retirée',
    action: (
      <Button onClick={() => {
        clearTimeout(undoTimeout);
        undoRemove(recipeId);
      }}>
        Annuler
      </Button>
    )
  });

  undoTimeout = setTimeout(() => {
    // Permanent après 5s
  }, 5000);
}
```

**Priority:** P1
**Story Points:** 3
**Sprint:** 3

---

## 💰 Epic 5 : Freemium & Monétisation

### US-013 : Tracking quota freemium

**En tant qu'** utilisateur gratuit,
**Je veux** voir combien de générations il me reste,
**Afin de** gérer mon usage.

**Acceptance Criteria:**
- [ ] Badge quota visible dans header :
  - "✨ 5/5 cette semaine" (full)
  - "✨ 2/5 cette semaine" (medium)
  - "✨ 0/5 cette semaine" (empty, couleur warning)
- [ ] Tooltip au hover : "Ton quota se remet à zéro tous les lundis"
- [ ] Après chaque génération : Toast "Il te reste X générations cette semaine"
- [ ] Reset automatique tous les lundis 00h00 (timezone user)
- [ ] Persistance précise (DB `weekly_generations_count` + `last_reset_at`)

**Technical Notes:**
```typescript
// Cron job (Vercel Cron ou Supabase Edge Function)
// Runs every Monday 00:00 UTC
export async function resetWeeklyQuotas() {
  await supabase
    .from('users')
    .update({
      weekly_generations_count: 0,
      last_reset_at: new Date().toISOString()
    })
    .eq('subscription_tier', 'free');
}

// Check quota before generation
async function checkQuota(userId: string) {
  const user = await getUser(userId);

  // Check if reset needed (edge case: cron failed)
  const lastReset = new Date(user.last_reset_at);
  const now = new Date();
  const daysSinceReset = (now - lastReset) / (1000 * 60 * 60 * 24);

  if (daysSinceReset >= 7) {
    await resetQuota(userId);
    return { remaining: 5, canGenerate: true };
  }

  if (user.weekly_generations_count >= 5) {
    return { remaining: 0, canGenerate: false };
  }

  return {
    remaining: 5 - user.weekly_generations_count,
    canGenerate: true
  };
}
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 3

---

### US-014 : Paywall soft (quota épuisé)

**En tant qu'** utilisateur freemium ayant épuisé son quota,
**Je veux** comprendre comment débloquer plus de générations,
**Afin de** continuer à utiliser l'app.

**Acceptance Criteria:**
- [ ] Quand quota = 0/5 et user clique "Générer" :
  - Modal paywall (non-bloquant, peut fermer)
  - Titre : "✨ Tu as utilisé tes 5 générations gratuites cette semaine !"
  - Message : "Débloquer dès maintenant avec un essai gratuit de 7 jours"
  - Liste avantages Premium :
    - ✅ Générations illimitées
    - ✅ Sauvegardes illimitées
    - ✅ Plans hebdomadaires
    - ✅ Liste de courses auto
  - CTA principal : "Essayer 7 jours gratuits" (prominent, fuchsia)
  - CTA secondaire : "Passer en Premium" (outline)
  - Mention : "Ton quota se remet à zéro lundi prochain"
  - Lien : "Fermer" (discret)
- [ ] Tracking événement "paywall_shown"

**Technical Notes:**
```typescript
// Paywall component
<Dialog open={showPaywall}>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>✨ Tu as utilisé tes 5 générations gratuites cette semaine !</DialogTitle>
    </DialogHeader>
    <div className="space-y-4">
      <p>Débloquer dès maintenant avec un essai gratuit de 7 jours</p>
      <ul>
        <li>✅ Générations illimitées</li>
        <li>✅ Sauvegardes illimitées</li>
        <li>✅ Plans hebdomadaires</li>
        <li>✅ Liste de courses auto</li>
      </ul>
      <Button onClick={startTrial}>Essayer 7 jours gratuits</Button>
      <Button variant="outline" onClick={goToPremium}>Passer en Premium</Button>
      <p className="text-sm text-muted-foreground">
        Ton quota se remet à zéro lundi prochain
      </p>
    </div>
  </DialogContent>
</Dialog>
```

**Priority:** P0
**Story Points:** 3
**Sprint:** 3

---

### US-015 : Activation trial 7 jours

**En tant qu'** utilisateur freemium,
**Je veux** essayer le premium gratuitement pendant 7 jours,
**Afin de** tester avant de payer.

**Acceptance Criteria:**
- [ ] Bouton "Essayer 7 jours gratuits" → Activation immédiate
- [ ] Pas de carte bancaire requise (trust-building)
- [ ] Update user tier : `free` → `trial`
- [ ] Set `trial_ends_at` : Now + 7 days
- [ ] Toast confirmation : "🎉 Essai Premium activé ! Profite de toutes les fonctionnalités jusqu'au [date]"
- [ ] Badge dans header : "Premium (Essai)" avec countdown
- [ ] Toutes features premium débloquées
- [ ] Email de bienvenue trial (Supabase trigger)
- [ ] 1 seul trial par user (check avant activation)

**Technical Notes:**
```typescript
async function startTrial(userId: string) {
  // Check if already had trial
  const user = await getUser(userId);
  if (user.has_used_trial) {
    throw new Error('Trial already used');
  }

  const trialEndsAt = new Date();
  trialEndsAt.setDate(trialEndsAt.getDate() + 7);

  await supabase
    .from('users')
    .update({
      subscription_tier: 'trial',
      trial_ends_at: trialEndsAt.toISOString(),
      has_used_trial: true
    })
    .eq('id', userId);

  // Send welcome email
  await sendTrialWelcomeEmail(user.email, trialEndsAt);
}
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 3

---

### US-016 : Conversion trial → premium

**En tant qu'** utilisateur en trial,
**Je veux** souscrire au premium avant la fin du trial,
**Afin de** continuer à bénéficier des fonctionnalités.

**Acceptance Criteria:**
- [ ] J-2 avant fin trial : Banner persistant
  - "Ton essai se termine dans 2 jours. Passe en Premium maintenant et économise 30% !"
  - CTA : "Profiter de l'offre"
- [ ] J-1 : Email de rappel
- [ ] Jour J : Email "Ton essai se termine aujourd'hui"
- [ ] Page pricing :
  - Option 1 : €4.99/mois (mensuel)
  - Option 2 : €29.99/6 mois (soit €4.16/mois, badge "-17%")
  - Recommandation : 6 mois (highlight)
  - Liste avantages
- [ ] Intégration Stripe Checkout
- [ ] Après paiement :
  - Update tier : `trial` → `premium`
  - Set subscription_id (Stripe)
  - Toast : "🎉 Bienvenue en Premium !"
  - Email confirmation
- [ ] Gestion cas : Trial expire sans conversion
  - Retour à `free`
  - Email : "Ton essai est terminé, on espère te revoir !"
  - Offre de retour (code promo 20%)

**Technical Notes:**
```typescript
// Stripe Checkout Session
async function createCheckoutSession(userId: string, priceId: string) {
  const session = await stripe.checkout.sessions.create({
    customer_email: user.email,
    line_items: [{
      price: priceId, // price_monthly ou price_6months
      quantity: 1
    }],
    mode: 'subscription',
    success_url: `${domain}/premium/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${domain}/premium/cancel`,
    metadata: { userId }
  });

  return session.url;
}

// Webhook Stripe (payment success)
async function handlePaymentSuccess(session: Stripe.Checkout.Session) {
  await supabase
    .from('users')
    .update({
      subscription_tier: 'premium',
      subscription_id: session.subscription,
      subscription_ends_at: null // Recurring
    })
    .eq('id', session.metadata.userId);
}

// Cron: Check trial expiration daily
async function checkTrialExpirations() {
  const expiredTrials = await supabase
    .from('users')
    .select('*')
    .eq('subscription_tier', 'trial')
    .lt('trial_ends_at', new Date().toISOString());

  for (const user of expiredTrials) {
    await supabase
      .from('users')
      .update({ subscription_tier: 'free' })
      .eq('id', user.id);

    await sendTrialExpiredEmail(user.email);
  }
}
```

**Priority:** P0
**Story Points:** 8
**Sprint:** 4

---

## 📱 Epic 6 : PWA & Mobile Experience

### US-017 : Installation PWA

**En tant qu'** utilisateur mobile,
**Je veux** installer RadBites sur mon écran d'accueil,
**Afin d'** y accéder rapidement comme une app native.

**Acceptance Criteria:**
- [ ] Manifest.json configuré :
  - name: "RadBites"
  - short_name: "RadBites"
  - icons (192x192, 512x512)
  - theme_color: "#FF006E" (fuchsia)
  - background_color: "#FFFFFF"
  - display: "standalone"
  - start_url: "/"
- [ ] Service Worker enregistré
- [ ] Prompt d'installation natif (iOS, Android)
- [ ] Custom prompt si natif non affiché :
  - Banner discret : "Installer RadBites pour un accès rapide"
  - Bouton "Installer" → Trigger install prompt
- [ ] Dismiss possible (localStorage, ne plus afficher)
- [ ] Splash screen configuré (blanc + logo fuchsia)
- [ ] Lighthouse PWA score > 90

**Technical Notes:**
```typescript
// next-pwa config (next.config.js)
const withPWA = require('next-pwa')({
  dest: 'public',
  register: true,
  skipWaiting: true,
  disable: process.env.NODE_ENV === 'development'
});

module.exports = withPWA({
  // Next config
});

// Install prompt
useEffect(() => {
  const handleBeforeInstallPrompt = (e) => {
    e.preventDefault();
    setDeferredPrompt(e);
    setShowInstallBanner(true);
  };

  window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);

  return () => {
    window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
  };
}, []);

async function handleInstallClick() {
  if (deferredPrompt) {
    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === 'accepted') {
      setShowInstallBanner(false);
    }
    setDeferredPrompt(null);
  }
}
```

**Priority:** P1
**Story Points:** 5
**Sprint:** 4

---

### US-018 : Offline capability

**En tant qu'** utilisateur,
**Je veux** consulter mes recettes favorites même sans connexion,
**Afin de** cuisiner n'importe où.

**Acceptance Criteria:**
- [ ] Service Worker cache les assets (JS, CSS, fonts, images)
- [ ] Cache des recettes favorites (après première consultation online)
- [ ] Offline : Consultation favoris fonctionne
- [ ] Offline : Génération de recette affiche message clair :
  - "Tu es hors ligne. La génération nécessite une connexion internet."
  - Option : "Consulter mes favoris"
- [ ] Banner "Mode hors ligne" si pas de connexion
- [ ] Auto-sync quand connexion revient (background sync)
- [ ] Indication visuelle si recette pas encore cachée

**Technical Notes:**
```typescript
// Service Worker (sw.js)
const CACHE_NAME = 'radbites-v1';
const urlsToCache = [
  '/',
  '/manifest.json',
  // Dynamic: Recipes favorited
];

// Cache-first strategy for favorites
self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/recipes/favorites')) {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request);
      })
    );
  }
});

// Background Sync (sync favoris quand connexion revient)
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-recipes') {
    event.waitUntil(syncRecipes());
  }
});
```

**Priority:** P1
**Story Points:** 8
**Sprint:** 4

---

## 🔧 Epic 7 : Qualité & Expérience

### US-019 : Régénérer une variante

**En tant qu'** utilisateur,
**Je veux** générer une variante d'une recette,
**Afin de** découvrir d'autres options.

**Acceptance Criteria:**
- [ ] Bouton 🔄 "Régénérer" sur chaque recette
- [ ] Modal de confirmation :
  - "Générer une variante ?"
  - Options :
    - ☐ Plus épicé
    - ☐ Plus léger
    - ☐ Végétarien
    - ☐ Différents ingrédients
  - CTA : "Générer variante"
- [ ] Génération utilise recette originale comme base
- [ ] Prompt : "Crée une variante de cette recette : [original], avec ces modifications : [options]"
- [ ] Décompte quota freemium (compte comme 1 génération)
- [ ] Possibilité de comparer (afficher les 2 côte à côte)

**Technical Notes:**
```typescript
async function generateVariation(
  originalRecipe: Recipe,
  modifications: string[]
) {
  const prompt = `
Tu es un chef créatif. Voici une recette que j'ai aimée :

${JSON.stringify(originalRecipe)}

Crée une VARIANTE de cette recette avec ces modifications :
${modifications.join(', ')}

Garde l'esprit de la recette mais change suffisamment pour que ce soit intéressant.
Format JSON strict.
`;

  const variation = await groq.chat.completions.create({
    model: 'llama-3-70b-8192',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: prompt }
    ],
    temperature: 0.9, // Plus de créativité pour variation
  });

  return parseRecipe(variation.choices[0].message.content);
}
```

**Priority:** P1
**Story Points:** 5
**Sprint:** 4

---

### US-020 : Partage social

**En tant qu'** utilisateur,
**Je veux** partager une recette avec mes amis,
**Afin de** la recommander ou cuisiner ensemble.

**Acceptance Criteria:**
- [ ] Bouton 📤 "Partager" sur chaque recette
- [ ] Native Share API (si disponible) :
  - Titre : "[Nom recette] - RadBites"
  - Text : "Découvre cette recette créée par IA !"
  - URL : Deep link vers la recette
- [ ] Fallback si pas de Share API :
  - Modal avec options : WhatsApp, Instagram, Copier lien
- [ ] Deep link fonctionnel :
  - /recipe/[id] ouvre la recette (même pour non-users)
  - Si non-user : Voir recette + CTA "Créer tes propres recettes"
- [ ] Open Graph tags pour preview :
  - og:title, og:description, og:image
- [ ] Tracking événement "recipe_shared"

**Technical Notes:**
```typescript
async function shareRecipe(recipe: Recipe) {
  const shareData = {
    title: `${recipe.title} - RadBites`,
    text: 'Découvre cette recette créée par IA !',
    url: `https://radbites.app/recipe/${recipe.id}`
  };

  if (navigator.share) {
    try {
      await navigator.share(shareData);
      trackEvent('recipe_shared', { method: 'native' });
    } catch (err) {
      // User cancelled
    }
  } else {
    // Fallback modal
    showShareModal(shareData);
  }
}

// Deep link page (app/recipe/[id]/page.tsx)
export async function generateMetadata({ params }) {
  const recipe = await getRecipe(params.id);

  return {
    title: recipe.title,
    description: recipe.steps[0],
    openGraph: {
      images: [recipe.image || '/default-recipe.jpg']
    }
  };
}
```

**Priority:** P1
**Story Points:** 5
**Sprint:** 4

---

## 🎨 Epic 8 : Design & Polish

### US-021 : Design system cohérent

**En tant qu'** utilisateur,
**Je veux** une interface visuellement cohérente,
**Afin d'** avoir une expérience agréable.

**Acceptance Criteria:**
- [ ] Palette de couleurs respectée partout :
  - Primary : Blanc #FFFFFF
  - Accent : Fuchsia #FF006E
  - Text : #1A1A1A
  - Background : #F9FAFB
- [ ] Typography cohérente :
  - H1 : 32px bold
  - H2 : 24px semibold
  - Body : 16px regular
  - Small : 14px
- [ ] Spacing system (Tailwind) :
  - Gap entre sections : 6-8 (24-32px)
  - Padding containers : 4-6 (16-24px)
- [ ] Components shadcn/ui customisés :
  - Buttons : Fuchsia accent
  - Inputs : Border subtle, focus fuchsia
  - Cards : Shadow soft, rounded-xl
- [ ] Animations subtiles :
  - Transitions 200ms
  - Hover states
  - Loading skeletons
- [ ] Icons cohérents (Lucide React)
- [ ] Responsive breakpoints :
  - Mobile : 320px - 768px
  - Tablet : 768px - 1024px
  - Desktop : 1024px+

**Technical Notes:**
```typescript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#FFFFFF',
          foreground: '#1A1A1A'
        },
        accent: {
          DEFAULT: '#FF006E',
          foreground: '#FFFFFF'
        },
        background: '#F9FAFB',
        foreground: '#1A1A1A'
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif']
      }
    }
  }
};
```

**Priority:** P0
**Story Points:** 8
**Sprint:** 1-4 (continu)

---

### US-022 : Animations & feedback

**En tant qu'** utilisateur,
**Je veux** des retours visuels à mes actions,
**Afin de** savoir que l'app répond.

**Acceptance Criteria:**
- [ ] Loading states pour toutes actions async :
  - Skeletons pour listes
  - Spinners pour boutons
  - Progress bar pour génération (steps)
- [ ] Toasts pour confirmations :
  - Succès (vert) : "Recette sauvegardée !"
  - Erreur (rouge) : "Une erreur est survenue"
  - Info (bleu) : "Copié dans le presse-papiers"
- [ ] Micro-animations :
  - Bouton ❤️ : Scale + bounce au clic
  - Cards : Lift au hover
  - Inputs : Border glow au focus
- [ ] Transitions de page fluides (Framer Motion)
- [ ] Empty states illustrés (non génériques)
- [ ] Error boundaries avec retry

**Technical Notes:**
```typescript
// Framer Motion page transitions
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -20 }}
  transition={{ duration: 0.2 }}
>
  {children}
</motion.div>

// Toast system (shadcn/ui)
import { useToast } from '@/components/ui/use-toast';

const { toast } = useToast();

toast({
  title: 'Recette sauvegardée !',
  description: 'Tu peux la retrouver dans "Mes Favoris"',
  variant: 'success'
});
```

**Priority:** P1
**Story Points:** 5
**Sprint:** 4

---

## 🔒 Epic 9 : Sécurité & Performance

### US-023 : Rate limiting

**En tant que** système,
**Je veux** limiter les appels API par utilisateur,
**Afin de** prévenir les abus et contrôler les coûts.

**Acceptance Criteria:**
- [ ] Rate limit génération recette :
  - Free : 5/semaine (déjà géré par quota)
  - Trial/Premium : 50/jour (protection abuse)
- [ ] Rate limit API endpoints :
  - Auth : 5 tentatives/min
  - Autres : 60 req/min
- [ ] Response 429 si dépassé :
  - Header `Retry-After`
  - Message clair : "Trop de requêtes, réessaie dans [X] secondes"
- [ ] Implémentation avec Upstash Redis ou Vercel KV
- [ ] Tracking IP + user_id (double protection)

**Technical Notes:**
```typescript
// Middleware rate limiting (Upstash Ratelimit)
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(50, '1 d'), // 50 req/day
  analytics: true
});

export async function middleware(req: Request) {
  const ip = req.headers.get('x-forwarded-for');
  const { success, limit, remaining } = await ratelimit.limit(ip);

  if (!success) {
    return new Response('Too Many Requests', {
      status: 429,
      headers: {
        'Retry-After': '3600' // 1 hour
      }
    });
  }

  return NextResponse.next();
}
```

**Priority:** P0
**Story Points:** 5
**Sprint:** 3

---

### US-024 : Gestion des erreurs LLM

**En tant que** système,
**Je veux** gérer les erreurs et hallucinations du LLM,
**Afin de** garantir la qualité des recettes.

**Acceptance Criteria:**
- [ ] Validation du output LLM :
  - JSON parsable
  - Champs requis présents (title, ingredients, steps)
  - Quantités cohérentes (pas de "500kg de sel")
  - Temps de cuisson réaliste (5min - 6h)
- [ ] Si validation échoue :
  - Retry avec prompt ajusté (1 fois)
  - Si échec persiste : Message utilisateur
    "Oups, on a du mal à créer cette recette. Réessaie avec d'autres ingrédients ?"
- [ ] Détection d'hallucinations graves :
  - Ingrédients toxiques/dangereux
  - Instructions contradictoires
  - Blacklist de mots (poison, etc.)
- [ ] Feedback loop :
  - Bouton "Signaler un problème" sur recettes
  - Stockage pour amélioration continue
- [ ] Timeout : Si génération > 30s, erreur

**Technical Notes:**
```typescript
// Validation schema (Zod)
const recipeSchema = z.object({
  title: z.string().min(5).max(100),
  ingredients: z.array(z.object({
    name: z.string(),
    quantity: z.number().positive().max(10000),
    unit: z.enum(['g', 'kg', 'ml', 'l', 'pièce', 'cuillère', 'tasse'])
  })).min(2).max(20),
  steps: z.array(z.string()).min(2).max(15),
  cooking_time: z.number().min(5).max(360),
  difficulty: z.enum(['easy', 'medium', 'hard']),
  nutrition: z.object({
    calories: z.number().min(0).max(5000),
    protein: z.number().min(0).max(500),
    carbs: z.number().min(0).max(500),
    fat: z.number().min(0).max(500)
  })
});

async function validateRecipe(llmOutput: any) {
  try {
    const validated = recipeSchema.parse(llmOutput);

    // Additional checks
    if (containsDangerousIngredient(validated.ingredients)) {
      throw new Error('Dangerous ingredient detected');
    }

    return validated;
  } catch (error) {
    // Log for improvement
    await logValidationError(llmOutput, error);
    throw error;
  }
}
```

**Priority:** P0
**Story Points:** 8
**Sprint:** 2

---

## 📊 Epic 10 : Analytics & Amélioration

### US-025 : Analytics de base

**En tant que** product owner,
**Je veux** tracker les métriques clés,
**Afin d'** optimiser le produit.

**Acceptance Criteria:**
- [ ] Événements trackés (Plausible ou Posthog) :
  - `sign_up` : Nouvelles inscriptions
  - `recipe_generated` : { mode: 'fridge' | 'mood' }
  - `recipe_saved` : Favoris ajoutés
  - `recipe_shared` : Partages
  - `paywall_shown` : Affichage paywall
  - `trial_started` : Activations trial
  - `subscription_created` : Conversions premium
  - `recipe_quality_feedback` : Ratings recettes
- [ ] Dashboard analytics accessible
- [ ] RGPD compliant (Plausible = cookieless)
- [ ] Opt-out possible pour users

**Technical Notes:**
```typescript
// lib/analytics.ts
import { track } from '@/lib/plausible';

export function trackRecipeGenerated(mode: 'fridge' | 'mood', userId: string) {
  track('recipe_generated', {
    props: {
      mode,
      user_tier: user.subscription_tier
    }
  });
}

// Plausible script (app/layout.tsx)
<Script
  defer
  data-domain="radbites.app"
  src="https://plausible.io/js/script.js"
/>
```

**Priority:** P1
**Story Points:** 3
**Sprint:** 4

---

## 📝 Summary

### Total Story Points par Epic :

| Epic | Stories | Story Points | Sprint |
|------|---------|--------------|--------|
| 1. Auth & Onboarding | 3 | 13 | 1 |
| 2. Mode Frigo | 4 | 26 | 1-2 |
| 3. Mode Envie | 2 | 13 | 2 |
| 4. Favoris | 3 | 11 | 3 |
| 5. Monétisation | 4 | 21 | 3-4 |
| 6. PWA | 2 | 13 | 4 |
| 7. Qualité & UX | 2 | 10 | 4 |
| 8. Design | 2 | 13 | 1-4 |
| 9. Sécurité | 2 | 13 | 2-3 |
| 10. Analytics | 1 | 3 | 4 |
| **TOTAL** | **25** | **136** | **4 sprints** |

### Sprint Planning (2 semaines/sprint) :

- **Sprint 1** (Semaines 1-2) : Auth + Onboarding + Mode Frigo (début) = ~30 points
- **Sprint 2** (Semaines 3-4) : Mode Frigo (fin) + Mode Envie + Sécurité = ~35 points
- **Sprint 3** (Semaines 5-6) : Favoris + Monétisation + Rate limiting = ~35 points
- **Sprint 4** (Semaines 7-8) : PWA + Polish + Analytics + Finitions = ~36 points

**Total : 8 semaines pour MVP complet** ✅

---

*RadBites User Stories - Ready for Sprint Planning*
*Version 1.0 | 2025-11-11*
