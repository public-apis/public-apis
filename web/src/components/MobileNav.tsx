'use client';

import { useState } from 'react';
import { Category } from '@/utils/types';

interface MobileNavProps {
  categories: Category[];
  selectedCategory: string | null;
  onSelectCategory: (slug: string | null) => void;
  apiCounts: Record<string, number>;
}

export default function MobileNav({
  categories,
  selectedCategory,
  onSelectCategory,
  apiCounts
}: MobileNavProps) {
  const [isOpen, setIsOpen] = useState(false);
  const totalApis = Object.values(apiCounts).reduce((a, b) => a + b, 0);

  const selectedName = selectedCategory
    ? categories.find(c => c.slug === selectedCategory)?.name || 'Category'
    : 'All APIs';

  return (
    <div className="lg:hidden mb-4">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between px-4 py-3 rounded-xl border transition-theme"
        style={{
          backgroundColor: 'var(--card-bg)',
          borderColor: 'var(--card-border)',
          color: 'var(--foreground)',
        }}
      >
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5" style={{ color: 'var(--accent)' }} fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <span className="font-medium">{selectedName}</span>
        </div>
        <svg
          className={`w-5 h-5 transition-transform ${isOpen ? 'rotate-180' : ''}`}
          style={{ color: 'var(--muted)' }}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {isOpen && (
        <div
          className="mt-2 rounded-xl border overflow-hidden transition-theme"
          style={{
            backgroundColor: 'var(--card-bg)',
            borderColor: 'var(--card-border)',
          }}
        >
          <div className="max-h-64 overflow-y-auto">
            <button
              onClick={() => {
                onSelectCategory(null);
                setIsOpen(false);
              }}
              className={`w-full flex items-center justify-between px-4 py-3 text-left text-sm transition-colors ${
                selectedCategory === null ? 'font-medium' : ''
              }`}
              style={{
                backgroundColor: selectedCategory === null ? 'var(--accent)' : 'transparent',
                color: selectedCategory === null ? 'white' : 'var(--foreground)',
              }}
            >
              <span>All APIs</span>
              <span className="text-xs opacity-70">{totalApis}</span>
            </button>

            {categories.map((category) => (
              <button
                key={category.slug}
                onClick={() => {
                  onSelectCategory(category.slug);
                  setIsOpen(false);
                }}
                className={`w-full flex items-center justify-between px-4 py-3 text-left text-sm transition-colors border-t ${
                  selectedCategory === category.slug ? 'font-medium' : ''
                }`}
                style={{
                  backgroundColor: selectedCategory === category.slug ? 'var(--accent)' : 'transparent',
                  color: selectedCategory === category.slug ? 'white' : 'var(--foreground)',
                  borderColor: 'var(--card-border)',
                }}
              >
                <span>{category.name}</span>
                <span className="text-xs opacity-70">{apiCounts[category.slug] || 0}</span>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
