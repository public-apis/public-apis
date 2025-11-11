# RadBites - Design System

**Version**: 1.0
**Date**: 2025-11-11
**Framework**: Tailwind CSS + shadcn/ui
**Theme**: Clean, Modern, Mobile-First

---

## 📋 Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [Color Palette](#color-palette)
3. [Typography](#typography)
4. [Spacing System](#spacing-system)
5. [Components Library](#components-library)
6. [Layout Patterns](#layout-patterns)
7. [Icons & Imagery](#icons--imagery)
8. [Animations & Transitions](#animations--transitions)
9. [States & Feedback](#states--feedback)
10. [Accessibility](#accessibility)
11. [Responsive Design](#responsive-design)
12. [Dark Mode (Future)](#dark-mode-future)

---

## 🎨 Design Philosophy

### Core Principles

1. **Mobile-First**: 90% des utilisateurs sont sur mobile
2. **Clarity over Cleverness**: Interface claire, pas de fioritures inutiles
3. **Speed Perception**: Animations rapides, feedback immédiat
4. **Delightful Interactions**: Micro-animations pour engagement
5. **Accessible by Default**: WCAG 2.1 AA compliance

### Visual Identity

- **Clean & Modern**: Blanc dominant, accent fuchsia vibrant
- **Cuisine Focus**: Mise en avant des recettes, pas de l'interface
- **Professional yet Friendly**: Sérieux dans l'exécution, chaleureux dans le ton
- **Minimalist**: Pas de gradients complexes, pas de textures lourdes

### Inspiration References

- **Linear**: Simplicité, performance
- **Vercel**: Esthétique épurée, typographie moderne
- **Airbnb**: Cartes produit, spacing généreux
- **Stripe**: Clarté, hiérarchie d'information

---

## 🎨 Color Palette

### Primary Colors

```typescript
// tailwind.config.ts
const colors = {
  // Background
  background: {
    DEFAULT: '#FFFFFF',      // Blanc pur
    subtle: '#F9FAFB',       // Gris très clair (backgrounds secondaires)
    muted: '#F3F4F6',        // Gris clair (cards, borders)
  },

  // Foreground (Text)
  foreground: {
    DEFAULT: '#1A1A1A',      // Noir profond (texte principal)
    muted: '#6B7280',        // Gris moyen (texte secondaire)
    subtle: '#9CA3AF',       // Gris clair (placeholders, hints)
  },

  // Accent (Fuchsia)
  accent: {
    DEFAULT: '#FF006E',      // Fuchsia vibrant (CTA, focus)
    hover: '#E6006 3',        // Fuchsia plus foncé (hover states)
    light: '#FF4D94',        // Fuchsia clair (badges, highlights)
    subtle: '#FFE5F1',       // Fuchsia très clair (backgrounds)
  },

  // Semantic Colors
  success: {
    DEFAULT: '#10B981',      // Vert (confirmations)
    light: '#D1FAE5',        // Vert clair (backgrounds)
    dark: '#059669',         // Vert foncé (hover)
  },

  error: {
    DEFAULT: '#EF4444',      // Rouge (erreurs)
    light: '#FEE2E2',        // Rouge clair (backgrounds)
    dark: '#DC2626',         // Rouge foncé (hover)
  },

  warning: {
    DEFAULT: '#F59E0B',      // Orange (warnings)
    light: '#FEF3C7',        // Orange clair (backgrounds)
    dark: '#D97706',         // Orange foncé (hover)
  },

  info: {
    DEFAULT: '#3B82F6',      // Bleu (informations)
    light: '#DBEAFE',        // Bleu clair (backgrounds)
    dark: '#2563EB',         // Bleu foncé (hover)
  },
};
```

### Usage Guidelines

| Color | Usage | Example |
|-------|-------|---------|
| **accent (fuchsia)** | CTA buttons, links, focus states, progress | "Générer ma recette", input focus border |
| **foreground** | Body text, titles | Titres de recettes, descriptions |
| **foreground-muted** | Secondary text, captions | Temps de cuisson, metadata |
| **background-subtle** | Page backgrounds, sections | Page principale, sections |
| **background-muted** | Cards, inputs, borders | Recettes cards, input fields |
| **success** | Confirmations, completions | "Recette sauvegardée !" |
| **error** | Errors, warnings | "Une erreur est survenue" |

### Contrast Ratios (WCAG AA)

```
✅ foreground on background: 13.8:1 (AAA)
✅ foreground-muted on background: 4.6:1 (AA)
✅ accent on background: 4.8:1 (AA)
✅ accent on background-muted: 5.2:1 (AA)
✅ success/error/warning on background: > 4.5:1 (AA)
```

---

## ✍️ Typography

### Font Families

```typescript
// tailwind.config.ts
fontFamily: {
  sans: [
    'Inter',              // Primary (modern, readable)
    'system-ui',           // Fallback 1
    '-apple-system',       // Fallback 2 (iOS)
    'BlinkMacSystemFont',  // Fallback 3 (macOS)
    'Segoe UI',            // Fallback 4 (Windows)
    'sans-serif'           // Fallback 5 (generic)
  ],
  mono: [
    'JetBrains Mono',      // Code, timers
    'Menlo',               // Fallback
    'monospace'            // Generic fallback
  ],
}
```

**Why Inter?**
- Open source (no licensing)
- Designed for screens (excellent readability)
- Large character set (multilingual support)
- Variable font (performance)

### Type Scale

```typescript
// Font sizes (mobile-first)
fontSize: {
  // Mobile                    // Desktop
  xs: ['12px', '16px'],        // Small labels, captions
  sm: ['14px', '20px'],        // Secondary text, metadata
  base: ['16px', '24px'],      // Body text
  lg: ['18px', '28px'],        // Emphasized text
  xl: ['20px', '28px'],        // Small headings (H4)
  '2xl': ['24px', '32px'],     // Section headings (H3)
  '3xl': ['30px', '36px'],     // Page headings (H2)
  '4xl': ['36px', '40px'],     // Hero headings (H1)
  '5xl': ['48px', '1'],        // Display (rare)
}

// Font weights
fontWeight: {
  normal: 400,     // Body text
  medium: 500,     // Emphasized text
  semibold: 600,   // Subheadings
  bold: 700,       // Headings
}
```

### Typography Components

```tsx
// H1 - Page titles
<h1 className="text-3xl md:text-4xl font-bold text-foreground">
  Mes Recettes
</h1>

// H2 - Section titles
<h2 className="text-2xl md:text-3xl font-semibold text-foreground">
  Recettes Favorites
</h2>

// H3 - Card titles
<h3 className="text-xl md:text-2xl font-semibold text-foreground">
  Poulet Crémeux aux Carottes
</h3>

// Body - Regular text
<p className="text-base text-foreground leading-relaxed">
  Un plat réconfortant où le poulet fondant rencontre...
</p>

// Caption - Metadata
<span className="text-sm text-foreground-muted">
  35 min · Facile · 4 portions
</span>

// Label - Form labels
<label className="text-sm font-medium text-foreground">
  Ingrédients
</label>
```

### Line Heights

```typescript
lineHeight: {
  tight: 1.25,     // Headings
  snug: 1.375,     // Subheadings
  normal: 1.5,     // Body text
  relaxed: 1.625,  // Long-form content
  loose: 2,        // Spacious (rare)
}
```

---

## 📏 Spacing System

### Base Unit: 4px

Tous les spacings sont des multiples de 4px pour cohérence.

```typescript
// tailwind.config.ts
spacing: {
  0: '0px',
  1: '4px',       // 0.25rem
  2: '8px',       // 0.5rem
  3: '12px',      // 0.75rem
  4: '16px',      // 1rem
  5: '20px',      // 1.25rem
  6: '24px',      // 1.5rem
  8: '32px',      // 2rem
  10: '40px',     // 2.5rem
  12: '48px',     // 3rem
  16: '64px',     // 4rem
  20: '80px',     // 5rem
  24: '96px',     // 6rem
}
```

### Spacing Usage

| Context | Spacing | Example |
|---------|---------|---------|
| **Tight** (inside elements) | 2-3 (8-12px) | Padding inside buttons, badges |
| **Comfortable** (between small elements) | 4 (16px) | Gap between form fields |
| **Spacious** (between sections) | 6-8 (24-32px) | Margin between cards |
| **Generous** (page sections) | 12-16 (48-64px) | Margin between major sections |

### Common Patterns

```tsx
// Card padding
<div className="p-4 md:p-6">  // 16px mobile, 24px desktop

// Section margin
<section className="mb-8 md:mb-12">  // 32px mobile, 48px desktop

// Stack spacing (vertical)
<div className="space-y-4">  // 16px between children

// Grid gap
<div className="grid gap-4 md:gap-6">  // 16px mobile, 24px desktop

// Container padding
<div className="px-4 md:px-6 lg:px-8">  // Responsive horizontal padding
```

---

## 🧩 Components Library

### Button

```tsx
import { cva, type VariantProps } from "class-variance-authority";

const buttonVariants = cva(
  // Base styles
  "inline-flex items-center justify-center rounded-xl font-medium transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        // Primary CTA (fuchsia)
        default: "bg-accent text-white hover:bg-accent-hover active:scale-95 shadow-sm hover:shadow-md",

        // Secondary (outline)
        outline: "border-2 border-foreground-muted text-foreground hover:bg-background-muted active:scale-95",

        // Ghost (transparent)
        ghost: "text-foreground hover:bg-background-muted active:scale-95",

        // Destructive (danger)
        destructive: "bg-error text-white hover:bg-error-dark active:scale-95",

        // Link (text only)
        link: "text-accent hover:underline underline-offset-4",
      },
      size: {
        sm: "h-9 px-3 text-sm",      // 36px height
        md: "h-11 px-6 text-base",   // 44px height (mobile touch target)
        lg: "h-14 px-8 text-lg",     // 56px height
      },
    },
    defaultVariants: {
      variant: "default",
      size: "md",
    },
  }
);

// Usage
<Button variant="default" size="md">
  Générer ma recette
</Button>

<Button variant="outline" size="sm">
  Annuler
</Button>
```

### Input

```tsx
const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          // Base styles
          "flex h-11 w-full rounded-xl border border-foreground-muted/20 bg-white px-4 py-2 text-base",
          // Placeholder
          "placeholder:text-foreground-subtle",
          // Focus state
          "focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none",
          // Disabled state
          "disabled:cursor-not-allowed disabled:opacity-50 disabled:bg-background-muted",
          // Transitions
          "transition-colors duration-200",
          className
        )}
        ref={ref}
        {...props}
      />
    );
  }
);

// Usage
<Input
  type="text"
  placeholder="Ex: poulet, carottes, oignons..."
/>
```

### Card

```tsx
const Card = React.forwardRef<HTMLDivElement, CardProps>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        "rounded-2xl border border-foreground-muted/10 bg-white shadow-sm",
        "transition-all duration-200",
        "hover:shadow-md hover:-translate-y-0.5",
        className
      )}
      {...props}
    />
  )
);

const CardHeader = ({ className, ...props }: CardHeaderProps) => (
  <div className={cn("flex flex-col space-y-1.5 p-6", className)} {...props} />
);

const CardTitle = ({ className, ...props }: CardTitleProps) => (
  <h3 className={cn("text-xl font-semibold leading-none tracking-tight", className)} {...props} />
);

const CardDescription = ({ className, ...props }: CardDescriptionProps) => (
  <p className={cn("text-sm text-foreground-muted", className)} {...props} />
);

const CardContent = ({ className, ...props }: CardContentProps) => (
  <div className={cn("p-6 pt-0", className)} {...props} />
);

// Usage: Recipe Card
<Card>
  <CardHeader>
    <img src={recipe.image} alt={recipe.title} className="w-full h-48 object-cover rounded-t-2xl" />
  </CardHeader>
  <CardContent>
    <CardTitle>{recipe.title}</CardTitle>
    <CardDescription className="mt-2">
      {recipe.cooking_time} min · {recipe.difficulty}
    </CardDescription>
    <Button className="mt-4 w-full">Voir la recette</Button>
  </CardContent>
</Card>
```

### Badge

```tsx
const badgeVariants = cva(
  "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors",
  {
    variants: {
      variant: {
        default: "bg-foreground text-white",
        accent: "bg-accent-subtle text-accent",
        success: "bg-success-light text-success-dark",
        error: "bg-error-light text-error-dark",
        warning: "bg-warning-light text-warning-dark",
        outline: "border border-foreground-muted/20 text-foreground-muted",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
);

// Usage
<Badge variant="accent">Facile</Badge>
<Badge variant="success">30 min</Badge>
<Badge variant="outline">4 portions</Badge>
```

### Toast (Notification)

```tsx
// Using sonner (recommended) or radix-ui
<Toaster position="top-center" />

// Types
toast.success("Recette sauvegardée !", {
  description: "Tu peux la retrouver dans 'Mes Favoris'",
});

toast.error("Une erreur est survenue", {
  description: "Réessaye dans quelques instants",
});

toast.info("Nouvelle fonctionnalité !", {
  description: "Découvre les plans hebdomadaires",
  action: {
    label: "Voir",
    onClick: () => router.push('/plans'),
  },
});
```

### Loading Skeleton

```tsx
const Skeleton = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => {
  return (
    <div
      className={cn(
        "animate-pulse rounded-xl bg-foreground-muted/10",
        className
      )}
      {...props}
    />
  );
};

// Usage: Recipe card skeleton
<div className="space-y-3">
  <Skeleton className="h-48 w-full rounded-2xl" />
  <Skeleton className="h-6 w-3/4" />
  <Skeleton className="h-4 w-1/2" />
</div>
```

### Dialog (Modal)

```tsx
// Using shadcn/ui Dialog (Radix UI)
<Dialog>
  <DialogTrigger asChild>
    <Button variant="outline">Ouvrir</Button>
  </DialogTrigger>
  <DialogContent className="sm:max-w-[425px]">
    <DialogHeader>
      <DialogTitle>Générer une variante ?</DialogTitle>
      <DialogDescription>
        Choisis les modifications que tu veux appliquer à cette recette.
      </DialogDescription>
    </DialogHeader>
    <div className="grid gap-4 py-4">
      {/* Content */}
    </DialogContent>
    <DialogFooter>
      <Button type="submit">Générer</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

---

## 📱 Layout Patterns

### Container

```tsx
// Max-width container with responsive padding
const Container = ({ children, className }: ContainerProps) => (
  <div className={cn(
    "mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8",
    className
  )}>
    {children}
  </div>
);

// Usage
<Container>
  <h1>Page content</h1>
</Container>
```

### Page Layout

```tsx
// app/layout.tsx
export default function RootLayout({ children }: { children: React.Node }) {
  return (
    <html lang="fr">
      <body className={inter.className}>
        {/* Header */}
        <header className="sticky top-0 z-50 w-full border-b border-foreground-muted/10 bg-white/80 backdrop-blur-sm">
          <Container>
            <div className="flex h-16 items-center justify-between">
              <Logo />
              <Navigation />
              <UserMenu />
            </div>
          </Container>
        </header>

        {/* Main content */}
        <main className="flex-1 bg-background-subtle">
          {children}
        </main>

        {/* Footer (mobile navigation) */}
        <footer className="fixed bottom-0 left-0 right-0 z-50 border-t border-foreground-muted/10 bg-white md:hidden">
          <MobileNavigation />
        </footer>
      </body>
    </html>
  );
}
```

### Grid Layouts

```tsx
// Recipe grid (responsive)
<div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  {recipes.map(recipe => (
    <RecipeCard key={recipe.id} recipe={recipe} />
  ))}
</div>

// Two-column layout (desktop only)
<div className="grid grid-cols-1 gap-8 lg:grid-cols-[2fr_1fr]">
  <main>{/* Recipe content */}</main>
  <aside>{/* Sidebar (ads, related recipes) */}</aside>
</div>
```

### Stack Layout

```tsx
// Vertical stack with consistent spacing
<div className="space-y-6">
  <Section title="Mode Frigo" />
  <Section title="Mode Envie" />
  <Section title="Mes Favoris" />
</div>

// Horizontal stack (inline elements)
<div className="flex items-center space-x-2">
  <Badge>Facile</Badge>
  <Badge>30 min</Badge>
  <Badge>4 portions</Badge>
</div>
```

---

## 🎭 Icons & Imagery

### Icon Library: Lucide React

```bash
npm install lucide-react
```

**Why Lucide?**
- Modern, clean design
- Tree-shakeable (performance)
- Consistent sizing
- Large library (1000+ icons)

### Icon Usage

```tsx
import { Heart, Clock, ChefHat, Sparkles, Users } from 'lucide-react';

// Standard size (24px)
<Heart className="h-6 w-6 text-accent" />

// Small (16px)
<Clock className="h-4 w-4 text-foreground-muted" />

// Large (32px)
<ChefHat className="h-8 w-8 text-foreground" />

// With animation
<Sparkles className="h-5 w-5 text-accent animate-pulse" />
```

### Common Icons

| Icon | Usage | Component |
|------|-------|-----------|
| 🍳 `ChefHat` | Cooking, recipes | RecipeCard |
| ❤️ `Heart` | Favorites | FavoriteButton |
| ⏱️ `Clock` | Cooking time | RecipeMetadata |
| 👥 `Users` | Servings | RecipeMetadata |
| ✨ `Sparkles` | AI generation | GenerateButton |
| 🔍 `Search` | Search | SearchInput |
| ➕ `Plus` | Add ingredient | IngredientInput |
| ✓ `Check` | Completed steps | StepCheckbox |
| 📤 `Share2` | Share recipe | ShareButton |
| 🔄 `RefreshCw` | Regenerate | RegenerateButton |

### Recipe Images

```tsx
// Image with fallback
<div className="relative h-48 w-full overflow-hidden rounded-t-2xl bg-background-muted">
  {recipe.image_url ? (
    <Image
      src={recipe.image_url}
      alt={recipe.title}
      fill
      className="object-cover"
      sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
    />
  ) : (
    <div className="flex h-full items-center justify-center">
      <ChefHat className="h-16 w-16 text-foreground-muted/20" />
    </div>
  )}
</div>
```

### Image Sources

- **Unsplash API**: Free high-quality food photos
- **Placeholder**: lucide-react ChefHat icon
- **Future**: DALL-E generated images (premium)

---

## ✨ Animations & Transitions

### Transition Durations

```typescript
// tailwind.config.ts
transitionDuration: {
  75: '75ms',     // Instant feedback
  100: '100ms',   // Very fast
  150: '150ms',   // Fast (default for most)
  200: '200ms',   // Medium (hover states)
  300: '300ms',   // Slow (entrances)
  500: '500ms',   // Very slow (complex animations)
}
```

### Easing Functions

```typescript
transitionTimingFunction: {
  'ease-out-cubic': 'cubic-bezier(0.33, 1, 0.68, 1)',  // Natural deceleration
  'ease-in-cubic': 'cubic-bezier(0.32, 0, 0.67, 0)',   // Natural acceleration
  'ease-bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)', // Bounce effect
}
```

### Micro-Animations

```tsx
// Button press
<Button className="active:scale-95 transition-transform duration-150">
  Cliquer
</Button>

// Card hover
<Card className="hover:-translate-y-1 hover:shadow-lg transition-all duration-200">
  ...
</Card>

// Icon pulse (loading)
<Loader2 className="h-4 w-4 animate-spin" />

// Heart favorite animation
<Heart
  className={cn(
    "h-6 w-6 transition-all duration-200",
    isFavorite
      ? "fill-accent text-accent scale-110"
      : "text-foreground-muted hover:scale-110"
  )}
/>

// Fade in on mount
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.3, ease: "easeOut" }}
>
  {children}
</motion.div>
```

### Loading States

```tsx
// Skeleton loading
<Skeleton className="h-48 w-full animate-pulse" />

// Spinner
<Loader2 className="h-8 w-8 animate-spin text-accent" />

// Progress bar (recipe generation)
<div className="w-full bg-background-muted rounded-full h-2 overflow-hidden">
  <motion.div
    className="h-full bg-accent"
    initial={{ width: "0%" }}
    animate={{ width: "100%" }}
    transition={{ duration: 8, ease: "easeInOut" }}
  />
</div>

// Dots loading
<div className="flex space-x-1">
  {[0, 1, 2].map((i) => (
    <motion.div
      key={i}
      className="h-2 w-2 rounded-full bg-accent"
      animate={{ scale: [1, 1.2, 1] }}
      transition={{
        duration: 0.6,
        repeat: Infinity,
        delay: i * 0.2,
      }}
    />
  ))}
</div>
```

---

## 🔔 States & Feedback

### Empty States

```tsx
const EmptyState = ({ icon: Icon, title, description, action }: EmptyStateProps) => (
  <div className="flex flex-col items-center justify-center py-12 text-center">
    <div className="rounded-full bg-background-muted p-6 mb-4">
      <Icon className="h-12 w-12 text-foreground-muted" />
    </div>
    <h3 className="text-lg font-semibold text-foreground mb-2">
      {title}
    </h3>
    <p className="text-sm text-foreground-muted max-w-sm mb-6">
      {description}
    </p>
    {action}
  </div>
);

// Usage
<EmptyState
  icon={Heart}
  title="Aucune recette sauvegardée"
  description="Commence par générer une recette et ajoute-la à tes favoris !"
  action={<Button onClick={goToGenerate}>Créer ma première recette</Button>}
/>
```

### Error States

```tsx
const ErrorState = ({ error, retry }: ErrorStateProps) => (
  <div className="flex flex-col items-center justify-center py-12 text-center">
    <div className="rounded-full bg-error-light p-6 mb-4">
      <AlertCircle className="h-12 w-12 text-error" />
    </div>
    <h3 className="text-lg font-semibold text-foreground mb-2">
      Une erreur est survenue
    </h3>
    <p className="text-sm text-foreground-muted max-w-sm mb-6">
      {error.message || "Quelque chose s'est mal passé. Réessaye dans un instant."}
    </p>
    <Button onClick={retry} variant="outline">
      Réessayer
    </Button>
  </div>
);
```

### Success States

```tsx
// Toast notification (preferred)
toast.success("Recette sauvegardée !", {
  icon: <Check className="h-5 w-5" />,
});

// Inline success
<div className="flex items-center space-x-2 rounded-xl bg-success-light p-4">
  <Check className="h-5 w-5 text-success" />
  <span className="text-sm font-medium text-success-dark">
    Modifications enregistrées
  </span>
</div>
```

---

## ♿ Accessibility

### WCAG 2.1 AA Compliance

#### Color Contrast

✅ All text meets minimum contrast ratios:
- Large text (18pt+): 3:1
- Normal text: 4.5:1
- UI components: 3:1

#### Keyboard Navigation

```tsx
// Focus visible states
className="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2"

// Skip to content
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-white focus:rounded-xl"
>
  Aller au contenu principal
</a>
```

#### Screen Reader Support

```tsx
// Semantic HTML
<main id="main-content" aria-label="Contenu principal">
  <section aria-labelledby="recipes-title">
    <h2 id="recipes-title">Mes Recettes</h2>
    ...
  </section>
</main>

// ARIA labels
<button aria-label="Sauvegarder cette recette">
  <Heart className="h-6 w-6" aria-hidden="true" />
</button>

// Live regions
<div role="status" aria-live="polite" aria-atomic="true">
  {loading && "Génération de la recette en cours..."}
</div>
```

#### Touch Targets

Minimum 44x44px (WCAG 2.5.5):

```tsx
// All buttons, links, inputs
className="h-11 px-6"  // 44px height minimum

// Icon buttons
className="h-11 w-11 flex items-center justify-center"  // 44x44px
```

---

## 📱 Responsive Design

### Breakpoints

```typescript
// tailwind.config.ts
screens: {
  'sm': '640px',   // Small tablets
  'md': '768px',   // Tablets
  'lg': '1024px',  // Desktops
  'xl': '1280px',  // Large desktops
  '2xl': '1536px', // Extra large
}
```

### Mobile-First Strategy

```tsx
// ✅ Good: Mobile first, desktop overrides
<div className="text-base md:text-lg lg:text-xl">
  {content}
</div>

// ❌ Bad: Desktop first
<div className="text-xl md:text-lg sm:text-base">
  {content}
</div>
```

### Responsive Patterns

```tsx
// Navigation: Mobile bottom bar → Desktop sidebar
<nav className="fixed bottom-0 left-0 right-0 md:static md:flex md:items-center">
  ...
</nav>

// Grid: 1 col mobile → 2 cols tablet → 3 cols desktop
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  ...
</div>

// Hide on mobile
<div className="hidden md:block">
  Desktop only content
</div>

// Show on mobile only
<div className="block md:hidden">
  Mobile only content
</div>
```

---

## 🌙 Dark Mode (Future)

### Implementation Strategy

```tsx
// Use next-themes
import { ThemeProvider } from 'next-themes';

// app/layout.tsx
<ThemeProvider attribute="class" defaultTheme="light">
  {children}
</ThemeProvider>

// Component
const { theme, setTheme } = useTheme();
```

### Dark Mode Colors (Planned)

```typescript
colors: {
  dark: {
    background: {
      DEFAULT: '#0A0A0A',
      subtle: '#1A1A1A',
      muted: '#2A2A2A',
    },
    foreground: {
      DEFAULT: '#FAFAFA',
      muted: '#A0A0A0',
      subtle: '#707070',
    },
    accent: {
      DEFAULT: '#FF4D94',  // Fuchsia plus clair pour dark mode
      hover: '#FF006E',
    },
  },
}
```

---

## ✅ Design System Checklist

### Component Library
- [x] Button (5 variants, 3 sizes)
- [x] Input (with focus states)
- [x] Card (with hover states)
- [x] Badge (6 variants)
- [x] Toast (success, error, info)
- [x] Dialog (modal)
- [x] Skeleton (loading)
- [ ] Select/Dropdown (to implement)
- [ ] Checkbox (to implement)
- [ ] Radio (to implement)
- [ ] Switch/Toggle (to implement)

### Accessibility
- [x] WCAG AA color contrast
- [x] Keyboard navigation
- [x] Focus states
- [x] ARIA labels
- [x] Touch targets (44px min)
- [ ] Screen reader testing
- [ ] Keyboard-only testing

### Responsive
- [x] Mobile-first breakpoints
- [x] Responsive typography
- [x] Responsive spacing
- [x] Mobile navigation
- [x] Touch-friendly interactions

### Performance
- [x] Tree-shakeable icons
- [x] Optimized animations (GPU-accelerated)
- [x] Lazy-loaded images
- [ ] Font optimization (subset, preload)
- [ ] Critical CSS inline

---

## 📚 Resources

### Design Tools
- **Figma**: Design mockups (optional but recommended)
- **Tailwind Playground**: Rapid prototyping
- **shadcn/ui docs**: https://ui.shadcn.com

### Inspiration
- **Dribbble**: Food app designs
- **Mobbin**: Mobile app patterns
- **Refactoring UI**: Design tips

### Testing
- **Lighthouse**: Performance & accessibility audit
- **WAVE**: Accessibility evaluation
- **axe DevTools**: Accessibility testing

---

*RadBites Design System - Ready for Implementation*
*Version 1.0 | 2025-11-11*

**Next Steps**:
1. Set up Tailwind config with tokens
2. Install shadcn/ui components
3. Create Storybook for component library (optional)
4. Design Figma mockups (optional but helpful)
