'use client';

import { Category } from '@/utils/types';

interface CategorySidebarProps {
  categories: Category[];
  selectedCategory: string | null;
  onSelectCategory: (slug: string | null) => void;
  apiCounts: Record<string, number>;
}

export default function CategorySidebar({
  categories,
  selectedCategory,
  onSelectCategory,
  apiCounts
}: CategorySidebarProps) {
  const totalApis = Object.values(apiCounts).reduce((a, b) => a + b, 0);

  return (
    <aside
      className="w-64 flex-shrink-0 overflow-y-auto border-r transition-theme hidden lg:block"
      style={{
        backgroundColor: 'var(--sidebar-bg)',
        borderColor: 'var(--card-border)',
        height: 'calc(100vh - 64px)',
        position: 'sticky',
        top: '64px',
      }}
    >
      <div className="p-4">
        <h2 className="text-sm font-semibold uppercase tracking-wider mb-3" style={{ color: 'var(--muted)' }}>
          Categories
        </h2>

        <nav className="space-y-1">
          <button
            onClick={() => onSelectCategory(null)}
            className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-left text-sm transition-colors ${
              selectedCategory === null ? 'font-medium' : ''
            }`}
            style={{
              backgroundColor: selectedCategory === null ? 'var(--accent)' : 'transparent',
              color: selectedCategory === null ? 'white' : 'var(--foreground)',
            }}
          >
            <span>All APIs</span>
            <span
              className="text-xs px-2 py-0.5 rounded-full"
              style={{
                backgroundColor: selectedCategory === null ? 'rgba(255,255,255,0.2)' : 'var(--card-bg)',
                color: selectedCategory === null ? 'white' : 'var(--muted)',
              }}
            >
              {totalApis}
            </span>
          </button>

          {categories.map((category) => (
            <button
              key={category.slug}
              onClick={() => onSelectCategory(category.slug)}
              className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-left text-sm transition-colors ${
                selectedCategory === category.slug ? 'font-medium' : ''
              }`}
              style={{
                backgroundColor: selectedCategory === category.slug ? 'var(--accent)' : 'transparent',
                color: selectedCategory === category.slug ? 'white' : 'var(--foreground)',
              }}
            >
              <span className="truncate">{category.name}</span>
              <span
                className="text-xs px-2 py-0.5 rounded-full flex-shrink-0 ml-2"
                style={{
                  backgroundColor: selectedCategory === category.slug ? 'rgba(255,255,255,0.2)' : 'var(--card-bg)',
                  color: selectedCategory === category.slug ? 'white' : 'var(--muted)',
                }}
              >
                {apiCounts[category.slug] || 0}
              </span>
            </button>
          ))}
        </nav>
      </div>
    </aside>
  );
}
