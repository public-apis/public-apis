# RadBites - PWA Configuration Guide

**Version**: 1.0
**Date**: 2025-11-11
**Framework**: Next.js 14+ with next-pwa
**Target**: iOS Safari 15+ & Android Chrome 90+

---

## 📋 Table of Contents

1. [PWA Overview](#pwa-overview)
2. [Setup & Installation](#setup--installation)
3. [Manifest Configuration](#manifest-configuration)
4. [Service Worker Strategy](#service-worker-strategy)
5. [Offline Capabilities](#offline-capabilities)
6. [Installation Prompts](#installation-prompts)
7. [iOS Specific Configuration](#ios-specific-configuration)
8. [Android Specific Configuration](#android-specific-configuration)
9. [Push Notifications (Future)](#push-notifications-future)
10. [Performance Optimization](#performance-optimization)
11. [Testing & Debugging](#testing--debugging)

---

## 🎯 PWA Overview

### What is a PWA?

A Progressive Web App (PWA) is a web application that uses modern web capabilities to deliver an app-like experience to users.

### RadBites PWA Goals

1. **Installable**: Users can add RadBites to their home screen
2. **Offline-capable**: View saved recipes without internet
3. **Fast**: Instant loading with caching strategies
4. **Engaging**: Push notifications for trial expiry, new features (future)
5. **Native-like**: Full-screen, no browser UI

### Benefits for RadBites

- ✅ **Retention**: Installed apps have 3x higher retention
- ✅ **Engagement**: Home screen icon = easy access
- ✅ **Offline**: View favorites even without connection
- ✅ **Performance**: Cached assets = instant load
- ✅ **Cross-platform**: One codebase for iOS & Android

---

## 🛠️ Setup & Installation

### 1. Install Dependencies

```bash
npm install next-pwa
npm install --save-dev @types/serviceworker
```

### 2. Configure next.config.js

```javascript
// next.config.js
const withPWA = require('next-pwa')({
  dest: 'public',
  register: true,
  skipWaiting: true,
  disable: process.env.NODE_ENV === 'development',
  buildExcludes: [/middleware-manifest\.json$/],
  runtimeCaching: [
    {
      urlPattern: /^https:\/\/fonts\.(?:googleapis|gstatic)\.com\/.*/i,
      handler: 'CacheFirst',
      options: {
        cacheName: 'google-fonts',
        expiration: {
          maxEntries: 4,
          maxAgeSeconds: 365 * 24 * 60 * 60 // 1 year
        }
      }
    },
    {
      urlPattern: /^https:\/\/images\.unsplash\.com\/.*/i,
      handler: 'CacheFirst',
      options: {
        cacheName: 'unsplash-images',
        expiration: {
          maxEntries: 50,
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 days
        }
      }
    },
    {
      urlPattern: /\.(?:jpg|jpeg|gif|png|svg|ico|webp)$/i,
      handler: 'CacheFirst',
      options: {
        cacheName: 'static-images',
        expiration: {
          maxEntries: 100,
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 days
        }
      }
    },
    {
      urlPattern: /\/api\/recipes\/favorites/,
      handler: 'NetworkFirst',
      options: {
        cacheName: 'api-favorites',
        expiration: {
          maxEntries: 1,
          maxAgeSeconds: 24 * 60 * 60 // 1 day
        },
        networkTimeoutSeconds: 10
      }
    }
  ]
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  // ... other Next.js config
};

module.exports = withPWA(nextConfig);
```

### 3. TypeScript Configuration

```typescript
// types/serviceworker.d.ts
/// <reference lib="webworker" />

declare const self: ServiceWorkerGlobalScope;

export {};
```

---

## 📱 Manifest Configuration

### 1. Create manifest.json

```json
// public/manifest.json
{
  "name": "RadBites - AI Recipe Generator",
  "short_name": "RadBites",
  "description": "Génère des recettes créatives avec l'IA à partir de tes ingrédients",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFFFFF",
  "theme_color": "#FF006E",
  "orientation": "portrait-primary",
  "scope": "/",
  "icons": [
    {
      "src": "/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ],
  "categories": ["food", "lifestyle", "productivity"],
  "shortcuts": [
    {
      "name": "Générer une recette",
      "short_name": "Générer",
      "description": "Créer une nouvelle recette avec l'IA",
      "url": "/generate/frigo",
      "icons": [
        {
          "src": "/icons/shortcut-generate.png",
          "sizes": "96x96"
        }
      ]
    },
    {
      "name": "Mes Favoris",
      "short_name": "Favoris",
      "description": "Voir mes recettes favorites",
      "url": "/favorites",
      "icons": [
        {
          "src": "/icons/shortcut-favorites.png",
          "sizes": "96x96"
        }
      ]
    }
  ],
  "screenshots": [
    {
      "src": "/screenshots/home.png",
      "sizes": "540x720",
      "type": "image/png",
      "form_factor": "narrow"
    },
    {
      "src": "/screenshots/recipe.png",
      "sizes": "540x720",
      "type": "image/png",
      "form_factor": "narrow"
    },
    {
      "src": "/screenshots/home-wide.png",
      "sizes": "1920x1080",
      "type": "image/png",
      "form_factor": "wide"
    }
  ],
  "related_applications": [],
  "prefer_related_applications": false
}
```

### 2. Link Manifest in Layout

```tsx
// app/layout.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'RadBites - AI Recipe Generator',
  description: 'Génère des recettes créatives avec l\'IA',
  manifest: '/manifest.json',
  themeColor: '#FF006E',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'default',
    title: 'RadBites',
  },
  formatDetection: {
    telephone: false,
  },
  openGraph: {
    type: 'website',
    siteName: 'RadBites',
    title: 'RadBites - AI Recipe Generator',
    description: 'Génère des recettes créatives avec l\'IA',
  },
  twitter: {
    card: 'summary',
    title: 'RadBites - AI Recipe Generator',
    description: 'Génère des recettes créatives avec l\'IA',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <head>
        {/* PWA Meta Tags */}
        <meta name="application-name" content="RadBites" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="default" />
        <meta name="apple-mobile-web-app-title" content="RadBites" />
        <meta name="format-detection" content="telephone=no" />
        <meta name="mobile-web-app-capable" content="yes" />
        <meta name="msapplication-TileColor" content="#FF006E" />
        <meta name="msapplication-tap-highlight" content="no" />
        <meta name="theme-color" content="#FF006E" />

        {/* Apple Touch Icons */}
        <link rel="apple-touch-icon" href="/icons/icon-152x152.png" />
        <link rel="apple-touch-icon" sizes="152x152" href="/icons/icon-152x152.png" />
        <link rel="apple-touch-icon" sizes="180x180" href="/icons/icon-192x192.png" />
        <link rel="apple-touch-icon" sizes="167x167" href="/icons/icon-192x192.png" />

        {/* Favicon */}
        <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png" />
        <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png" />
        <link rel="shortcut icon" href="/favicon.ico" />

        {/* Apple Splash Screens (optional but recommended) */}
        <link
          rel="apple-touch-startup-image"
          href="/splash/apple-splash-2048-2732.jpg"
          media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
        />
        {/* Add more splash screens for different devices */}
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### 3. Generate Icons

Use a tool like [PWA Asset Generator](https://github.com/elegantapp/pwa-asset-generator):

```bash
npx pwa-asset-generator logo.svg public/icons --background "#FFFFFF" --padding "20%" --scrape false --manifest public/manifest.json
```

Or use [RealFaviconGenerator](https://realfavicongenerator.net/)

---

## ⚙️ Service Worker Strategy

### Cache Strategies

RadBites uses different caching strategies for different resources:

#### 1. **Cache First** (Static Assets)
- **Use for**: Images, fonts, CSS, JS bundles
- **Logic**: Check cache first, fallback to network
- **Best for**: Immutable assets

```typescript
// Automatically configured by next-pwa
{
  urlPattern: /\.(?:jpg|jpeg|png|svg|webp)$/i,
  handler: 'CacheFirst',
  options: {
    cacheName: 'static-images',
    expiration: {
      maxEntries: 100,
      maxAgeSeconds: 30 * 24 * 60 * 60 // 30 days
    }
  }
}
```

#### 2. **Network First** (API Calls)
- **Use for**: API endpoints (recipes, user data)
- **Logic**: Try network first, fallback to cache if offline
- **Best for**: Dynamic data that needs to be fresh

```typescript
{
  urlPattern: /\/api\/recipes/,
  handler: 'NetworkFirst',
  options: {
    cacheName: 'api-cache',
    networkTimeoutSeconds: 10, // Fallback to cache after 10s
    expiration: {
      maxEntries: 50,
      maxAgeSeconds: 24 * 60 * 60 // 1 day
    }
  }
}
```

#### 3. **Stale While Revalidate** (User Profile)
- **Use for**: User preferences, profile data
- **Logic**: Return cached version immediately, update in background
- **Best for**: Data that changes infrequently

```typescript
{
  urlPattern: /\/api\/user/,
  handler: 'StaleWhileRevalidate',
  options: {
    cacheName: 'user-cache',
    expiration: {
      maxEntries: 5,
      maxAgeSeconds: 7 * 24 * 60 * 60 // 7 days
    }
  }
}
```

### Custom Service Worker (Advanced)

For more control, create a custom service worker:

```typescript
// public/sw.js (if needed for custom logic)
const CACHE_NAME = 'radbites-v1';
const OFFLINE_URL = '/offline';

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll([
        '/',
        '/offline',
        '/icons/icon-192x192.png',
        // Add critical assets
      ]);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Custom fetch logic
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => {
        return caches.match(OFFLINE_URL);
      })
    );
  }
});
```

---

## 📴 Offline Capabilities

### What Works Offline

1. **Viewing favorite recipes** ✅
2. **Browsing previously viewed recipes** ✅
3. **Viewing user profile** ✅
4. **UI navigation** ✅

### What Doesn't Work Offline

1. **Generating new recipes** ❌ (requires LLM API)
2. **Saving new favorites** ❌ (requires DB write)
3. **Authentication** ❌ (requires network)

### Offline UX Implementation

#### 1. Detect Offline State

```typescript
// lib/hooks/useOnline.ts
import { useEffect, useState } from 'react';

export function useOnline() {
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {
    // Initial check
    setIsOnline(navigator.onLine);

    // Listen for changes
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  return isOnline;
}
```

#### 2. Offline Banner

```tsx
// components/shared/OfflineBanner.tsx
'use client';

import { useOnline } from '@/lib/hooks/useOnline';
import { WifiOff } from 'lucide-react';

export function OfflineBanner() {
  const isOnline = useOnline();

  if (isOnline) return null;

  return (
    <div className="fixed top-0 left-0 right-0 z-50 bg-warning py-2 px-4 flex items-center justify-center gap-2">
      <WifiOff className="h-5 w-5" />
      <span className="text-sm font-medium">
        Tu es hors ligne. Certaines fonctionnalités sont limitées.
      </span>
    </div>
  );
}

// Add to layout
// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <OfflineBanner />
        {children}
      </body>
    </html>
  );
}
```

#### 3. Disable Actions When Offline

```tsx
// components/features/generation/GenerateButton.tsx
'use client';

import { useOnline } from '@/lib/hooks/useOnline';
import { Button } from '@/components/ui/button';
import { Sparkles, WifiOff } from 'lucide-react';

export function GenerateButton({ onClick }: { onClick: () => void }) {
  const isOnline = useOnline();

  return (
    <Button
      onClick={onClick}
      disabled={!isOnline}
      className="w-full"
    >
      {isOnline ? (
        <>
          <Sparkles className="mr-2 h-5 w-5" />
          Générer ma recette
        </>
      ) : (
        <>
          <WifiOff className="mr-2 h-5 w-5" />
          Connexion requise
        </>
      )}
    </Button>
  );
}
```

#### 4. Offline Page

```tsx
// app/offline/page.tsx
import { WifiOff } from 'lucide-react';
import Link from 'next/link';
import { Button } from '@/components/ui/button';

export default function OfflinePage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-6">
      <WifiOff className="h-24 w-24 text-foreground-muted mb-6" />
      <h1 className="text-3xl font-bold mb-4">Tu es hors ligne</h1>
      <p className="text-foreground-muted text-center max-w-md mb-8">
        Certaines pages nécessitent une connexion internet. Tu peux consulter tes recettes favorites hors ligne.
      </p>
      <Button asChild>
        <Link href="/favorites">Voir mes favoris</Link>
      </Button>
    </div>
  );
}
```

---

## 📲 Installation Prompts

### Browser Default Prompt

Browsers show an install prompt automatically when PWA criteria are met:
- ✅ Served over HTTPS
- ✅ Has manifest.json with required fields
- ✅ Has service worker registered
- ✅ User has engaged with the site

### Custom Install Prompt

Provide a better UX with a custom install button:

```tsx
// components/features/pwa/InstallPrompt.tsx
'use client';

import { useEffect, useState } from 'react';
import { Button } from '@/components/ui/button';
import { Download, X } from 'lucide-react';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
}

export function InstallPrompt() {
  const [deferredPrompt, setDeferredPrompt] = useState<BeforeInstallPromptEvent | null>(null);
  const [showPrompt, setShowPrompt] = useState(false);
  const [isInstalled, setIsInstalled] = useState(false);

  useEffect(() => {
    // Check if already installed
    if (window.matchMedia('(display-mode: standalone)').matches) {
      setIsInstalled(true);
      return;
    }

    // Check if dismissed before
    const dismissed = localStorage.getItem('pwa-install-dismissed');
    if (dismissed) {
      const dismissedDate = new Date(dismissed);
      const daysSince = (Date.now() - dismissedDate.getTime()) / (1000 * 60 * 60 * 24);
      if (daysSince < 30) return; // Don't show for 30 days
    }

    // Listen for install prompt
    const handleBeforeInstallPrompt = (e: Event) => {
      e.preventDefault();
      setDeferredPrompt(e as BeforeInstallPromptEvent);
      setShowPrompt(true);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);

    // Listen for app installed
    window.addEventListener('appinstalled', () => {
      setIsInstalled(true);
      setShowPrompt(false);
    });

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    };
  }, []);

  const handleInstall = async () => {
    if (!deferredPrompt) return;

    // Show install prompt
    deferredPrompt.prompt();

    // Wait for user choice
    const { outcome } = await deferredPrompt.userChoice;

    if (outcome === 'accepted') {
      console.log('PWA installed');
    }

    setDeferredPrompt(null);
    setShowPrompt(false);
  };

  const handleDismiss = () => {
    localStorage.setItem('pwa-install-dismissed', new Date().toISOString());
    setShowPrompt(false);
  };

  if (isInstalled || !showPrompt) return null;

  return (
    <div className="fixed bottom-20 md:bottom-6 left-4 right-4 md:left-auto md:right-6 md:max-w-sm bg-white border-2 border-accent rounded-2xl shadow-lg p-4 z-40 animate-in slide-in-from-bottom-5">
      <button
        onClick={handleDismiss}
        className="absolute top-2 right-2 p-1 hover:bg-background-muted rounded-lg"
      >
        <X className="h-4 w-4" />
      </button>

      <div className="flex items-start gap-3">
        <div className="flex-shrink-0">
          <img src="/icons/icon-96x96.png" alt="RadBites" className="h-12 w-12 rounded-xl" />
        </div>
        <div className="flex-1">
          <h3 className="font-semibold text-sm mb-1">Installer RadBites</h3>
          <p className="text-xs text-foreground-muted mb-3">
            Accède rapidement à tes recettes depuis ton écran d'accueil
          </p>
          <Button onClick={handleInstall} size="sm" className="w-full">
            <Download className="mr-2 h-4 w-4" />
            Installer
          </Button>
        </div>
      </div>
    </div>
  );
}

// Add to layout
// app/layout.tsx
import { InstallPrompt } from '@/components/features/pwa/InstallPrompt';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        {children}
        <InstallPrompt />
      </body>
    </html>
  );
}
```

---

## 🍎 iOS Specific Configuration

### 1. iOS Install Instructions

iOS doesn't support the standard install prompt. Show custom instructions:

```tsx
// components/features/pwa/IOSInstallInstructions.tsx
'use client';

import { useEffect, useState } from 'react';
import { Dialog, DialogContent } from '@/components/ui/dialog';
import { Share, Plus, Home } from 'lucide-react';

export function IOSInstallInstructions() {
  const [show, setShow] = useState(false);
  const [isIOS, setIsIOS] = useState(false);
  const [isInstalled, setIsInstalled] = useState(false);

  useEffect(() => {
    // Detect iOS
    const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
    setIsIOS(iOS);

    // Check if already installed
    const standalone = window.matchMedia('(display-mode: standalone)').matches;
    setIsInstalled(standalone);

    // Show instructions after 30 seconds if not installed
    if (iOS && !standalone) {
      const timer = setTimeout(() => {
        const dismissed = localStorage.getItem('ios-install-dismissed');
        if (!dismissed) {
          setShow(true);
        }
      }, 30000);

      return () => clearTimeout(timer);
    }
  }, []);

  if (!isIOS || isInstalled) return null;

  return (
    <Dialog open={show} onOpenChange={setShow}>
      <DialogContent className="sm:max-w-md">
        <div className="text-center">
          <h2 className="text-xl font-bold mb-4">Installer RadBites sur iOS</h2>

          <div className="space-y-4 text-left">
            <div className="flex items-start gap-3">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-accent text-white flex items-center justify-center font-bold">
                1
              </div>
              <div>
                <p className="font-medium mb-1">Appuie sur le bouton Partager</p>
                <div className="flex items-center gap-2 text-sm text-foreground-muted">
                  <Share className="h-4 w-4" />
                  <span>En bas de Safari</span>
                </div>
              </div>
            </div>

            <div className="flex items-start gap-3">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-accent text-white flex items-center justify-center font-bold">
                2
              </div>
              <div>
                <p className="font-medium mb-1">Sélectionne "Sur l'écran d'accueil"</p>
                <div className="flex items-center gap-2 text-sm text-foreground-muted">
                  <Plus className="h-4 w-4" />
                  <span>Dans le menu de partage</span>
                </div>
              </div>
            </div>

            <div className="flex items-start gap-3">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-accent text-white flex items-center justify-center font-bold">
                3
              </div>
              <div>
                <p className="font-medium mb-1">Confirme l'ajout</p>
                <div className="flex items-center gap-2 text-sm text-foreground-muted">
                  <Home className="h-4 w-4" />
                  <span>L'app apparaîtra sur ton écran d'accueil</span>
                </div>
              </div>
            </div>
          </div>

          <button
            onClick={() => {
              localStorage.setItem('ios-install-dismissed', 'true');
              setShow(false);
            }}
            className="mt-6 text-sm text-foreground-muted hover:text-foreground"
          >
            Ne plus afficher
          </button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
```

### 2. iOS Splash Screens

Generate splash screens for all iOS devices:

```html
<!-- In app/layout.tsx <head> -->
<!-- iPhone X, XS, 11 Pro -->
<link rel="apple-touch-startup-image" href="/splash/apple-splash-1125-2436.jpg"
  media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)" />

<!-- iPhone XR, 11 -->
<link rel="apple-touch-startup-image" href="/splash/apple-splash-828-1792.jpg"
  media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)" />

<!-- iPhone XS Max, 11 Pro Max -->
<link rel="apple-touch-startup-image" href="/splash/apple-splash-1242-2688.jpg"
  media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)" />

<!-- iPad Pro 12.9" -->
<link rel="apple-touch-startup-image" href="/splash/apple-splash-2048-2732.jpg"
  media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)" />

<!-- Add more for other devices -->
```

---

## 🤖 Android Specific Configuration

### 1. Android Install Banner

Android Chrome shows a native install banner automatically. Customize appearance in manifest.json:

```json
{
  "theme_color": "#FF006E",
  "background_color": "#FFFFFF",
  "display": "standalone"
}
```

### 2. Android Shortcuts

Enable app shortcuts (long-press on icon):

```json
// Already in manifest.json
"shortcuts": [
  {
    "name": "Générer une recette",
    "url": "/generate/frigo",
    "icons": [{"src": "/icons/shortcut-generate.png", "sizes": "96x96"}]
  }
]
```

---

## 🔔 Push Notifications (Future)

### Setup (When Ready)

```typescript
// lib/push-notifications.ts
export async function subscribeUserToPush() {
  if (!('serviceWorker' in navigator) || !('PushManager' in window)) {
    console.log('Push notifications not supported');
    return null;
  }

  const registration = await navigator.serviceWorker.ready;

  // Request permission
  const permission = await Notification.requestPermission();

  if (permission !== 'granted') {
    return null;
  }

  // Subscribe to push
  const subscription = await registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(
      process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!
    )
  });

  // Send subscription to server
  await fetch('/api/push/subscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(subscription)
  });

  return subscription;
}

function urlBase64ToUint8Array(base64String: string) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}
```

---

## ⚡ Performance Optimization

### 1. Lighthouse Score Goals

| Metric | Target | Current |
|--------|--------|---------|
| Performance | > 90 | TBD |
| Accessibility | > 95 | TBD |
| Best Practices | 100 | TBD |
| SEO | 100 | TBD |
| PWA | ✅ Installable | TBD |

### 2. Performance Checklist

- [ ] **Service Worker**: Caching static assets
- [ ] **Image Optimization**: next/image for all images
- [ ] **Font Optimization**: Preload Inter font, subset if possible
- [ ] **Code Splitting**: Dynamic imports for heavy components
- [ ] **Bundle Size**: Keep JS bundle < 200KB gzipped
- [ ] **First Paint**: < 1.5s
- [ ] **Time to Interactive**: < 3s
- [ ] **Cumulative Layout Shift**: < 0.1

### 3. Service Worker Update Strategy

```typescript
// components/features/pwa/UpdatePrompt.tsx
'use client';

import { useEffect, useState } from 'react';
import { Button } from '@/components/ui/button';

export function UpdatePrompt() {
  const [showUpdate, setShowUpdate] = useState(false);
  const [registration, setRegistration] = useState<ServiceWorkerRegistration | null>(null);

  useEffect(() => {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.ready.then((reg) => {
        setRegistration(reg);

        // Check for updates
        reg.addEventListener('updatefound', () => {
          const newWorker = reg.installing;

          newWorker?.addEventListener('statechange', () => {
            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
              // New version available
              setShowUpdate(true);
            }
          });
        });
      });
    }
  }, []);

  const handleUpdate = () => {
    if (registration?.waiting) {
      registration.waiting.postMessage({ type: 'SKIP_WAITING' });
      window.location.reload();
    }
  };

  if (!showUpdate) return null;

  return (
    <div className="fixed bottom-4 left-4 right-4 md:left-auto md:right-4 md:max-w-sm bg-accent text-white rounded-2xl shadow-lg p-4 z-50">
      <p className="font-medium mb-3">Nouvelle version disponible !</p>
      <Button onClick={handleUpdate} variant="secondary" size="sm" className="w-full">
        Mettre à jour
      </Button>
    </div>
  );
}
```

---

## 🧪 Testing & Debugging

### 1. Chrome DevTools

#### Test PWA Criteria
1. Open DevTools
2. Application tab → Manifest
3. Check all fields are correct
4. Application tab → Service Workers
5. Verify SW is registered and active

#### Test Offline
1. Application tab → Service Workers
2. Check "Offline"
3. Navigate the app
4. Verify cached resources load

#### Lighthouse Audit
1. DevTools → Lighthouse tab
2. Select "Progressive Web App"
3. Run audit
4. Fix any issues

### 2. Testing Checklist

- [ ] **Install**: Can install on iOS Safari
- [ ] **Install**: Can install on Android Chrome
- [ ] **Offline**: View favorites works offline
- [ ] **Offline**: Appropriate error messages when offline
- [ ] **Icons**: All icon sizes present and correct
- [ ] **Splash**: iOS splash screens show correctly
- [ ] **Theme**: Theme color matches app
- [ ] **Updates**: Update prompt shows when new version deployed
- [ ] **Performance**: Lighthouse score > 90
- [ ] **Shortcuts**: App shortcuts work (Android)

### 3. Testing on Real Devices

#### iOS
```bash
# Use ngrok to test on real device
npx ngrok http 3000

# Open ngrok URL in iOS Safari
# Test install flow
```

#### Android
```bash
# Same with ngrok or use local network IP
# Open in Chrome on Android device
```

---

## ✅ PWA Launch Checklist

### Pre-Launch
- [ ] manifest.json complete and valid
- [ ] All required icons generated (72px - 512px)
- [ ] Service worker registered
- [ ] Offline page created
- [ ] Install prompt implemented
- [ ] iOS install instructions added
- [ ] HTTPS enabled (required for PWA)
- [ ] Meta tags in <head>
- [ ] Lighthouse PWA audit passing

### Testing
- [ ] Tested on iOS Safari (iPhone)
- [ ] Tested on Android Chrome
- [ ] Tested offline functionality
- [ ] Tested install flow
- [ ] Tested update flow
- [ ] Performance audit > 90

### Monitoring
- [ ] Analytics tracking installs
- [ ] Error monitoring (Sentry)
- [ ] Service worker logs
- [ ] User feedback on PWA experience

---

*RadBites PWA Configuration - Production Ready*
*Version 1.0 | 2025-11-11*

**Next Steps:**
1. Generate all required icons
2. Test install flow on iOS and Android
3. Run Lighthouse audit
4. Deploy to HTTPS
5. Monitor PWA metrics (installs, offline usage)
