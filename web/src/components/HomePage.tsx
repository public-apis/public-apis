'use client';

import { useState, useMemo } from 'react';
import Fuse from 'fuse.js';
import { APIData, API, Category } from '@/utils/types';
import Header from './Header';
import SearchBar from './SearchBar';
import Filters, { FilterState } from './Filters';
import CategorySidebar from './CategorySidebar';
import MobileNav from './MobileNav';
import APICard from './APICard';

interface HomePageProps {
  data: APIData;
}

export default function HomePage({ data }: HomePageProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [filters, setFilters] = useState<FilterState>({
    auth: '',
    https: '',
    cors: '',
  });

  // Create a flat list of all APIs with category info for searching
  const allApis = useMemo(() => {
    return data.categories.flatMap((category) =>
      category.apis.map((api) => ({
        ...api,
        categoryName: category.name,
        categorySlug: category.slug,
      }))
    );
  }, [data.categories]);

  // Set up Fuse.js for fuzzy search (including category names)
  const fuse = useMemo(() => {
    return new Fuse(allApis, {
      keys: [
        { name: 'name', weight: 2 },
        { name: 'description', weight: 1 },
        { name: 'categoryName', weight: 1.5 },
      ],
      threshold: 0.3,
      includeScore: true,
    });
  }, [allApis]);

  // Filter and search APIs
  const filteredApis = useMemo(() => {
    let results = allApis;

    // Apply search
    if (searchQuery.trim()) {
      const searchResults = fuse.search(searchQuery);
      results = searchResults.map((r) => r.item);
    }

    // Apply category filter
    if (selectedCategory) {
      results = results.filter((api) => api.categorySlug === selectedCategory);
    }

    // Apply auth filter
    if (filters.auth) {
      results = results.filter((api) => api.auth === filters.auth);
    }

    // Apply HTTPS filter
    if (filters.https) {
      results = results.filter((api) =>
        filters.https === 'yes' ? api.https : !api.https
      );
    }

    // Apply CORS filter
    if (filters.cors) {
      results = results.filter((api) => api.cors === filters.cors);
    }

    return results;
  }, [allApis, searchQuery, selectedCategory, filters, fuse]);

  // Group filtered APIs by category for display
  const groupedApis = useMemo(() => {
    const groups: Record<string, typeof filteredApis> = {};

    for (const api of filteredApis) {
      if (!groups[api.categorySlug]) {
        groups[api.categorySlug] = [];
      }
      groups[api.categorySlug].push(api);
    }

    return groups;
  }, [filteredApis]);

  // Calculate API counts per category (for sidebar)
  const apiCounts = useMemo(() => {
    const counts: Record<string, number> = {};
    for (const category of data.categories) {
      counts[category.slug] = category.apis.length;
    }
    return counts;
  }, [data.categories]);

  // Get category order for display
  const categoryOrder = useMemo(() => {
    return data.categories.map((c) => c.slug);
  }, [data.categories]);

  const getCategoryName = (slug: string) => {
    return data.categories.find((c) => c.slug === slug)?.name || slug;
  };

  return (
    <div className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      <Header totalApis={data.totalApis} totalCategories={data.categories.length} />

      <div className="flex">
        <CategorySidebar
          categories={data.categories}
          selectedCategory={selectedCategory}
          onSelectCategory={setSelectedCategory}
          apiCounts={apiCounts}
        />

        <main className="flex-1 min-w-0">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {/* Hero Section */}
            <div className="text-center mb-8">
              <h2 className="text-3xl sm:text-4xl font-bold mb-3" style={{ color: 'var(--foreground)' }}>
                Discover Public APIs
              </h2>
              <p className="text-lg" style={{ color: 'var(--muted)' }}>
                A curated collection of {data.totalApis.toLocaleString()} free APIs for your next project
              </p>
            </div>

            {/* Search */}
            <div className="max-w-2xl mx-auto mb-6">
              <SearchBar
                value={searchQuery}
                onChange={setSearchQuery}
                placeholder="Search APIs, categories, or descriptions..."
              />
            </div>

            {/* Filters */}
            <div className="flex justify-center mb-8">
              <Filters filters={filters} onChange={setFilters} />
            </div>

            {/* Mobile Category Nav */}
            <MobileNav
              categories={data.categories}
              selectedCategory={selectedCategory}
              onSelectCategory={setSelectedCategory}
              apiCounts={apiCounts}
            />

            {/* Results Count */}
            <div className="mb-6">
              <p className="text-sm" style={{ color: 'var(--muted)' }}>
                Showing {filteredApis.length.toLocaleString()} of {data.totalApis.toLocaleString()} APIs
                {selectedCategory && (
                  <span> in <strong style={{ color: 'var(--accent)' }}>{getCategoryName(selectedCategory)}</strong></span>
                )}
                {searchQuery && (
                  <span> matching &quot;<strong style={{ color: 'var(--accent)' }}>{searchQuery}</strong>&quot;</span>
                )}
              </p>
            </div>

            {/* API Grid - Grouped by Category */}
            {filteredApis.length > 0 ? (
              <div className="space-y-10">
                {categoryOrder
                  .filter((slug) => groupedApis[slug]?.length > 0)
                  .map((categorySlug) => (
                    <section key={categorySlug}>
                      <div className="flex items-center gap-3 mb-4">
                        <h3 className="text-xl font-semibold" style={{ color: 'var(--foreground)' }}>
                          {getCategoryName(categorySlug)}
                        </h3>
                        <span
                          className="text-sm px-2 py-0.5 rounded-full"
                          style={{
                            backgroundColor: 'var(--card-bg)',
                            color: 'var(--muted)',
                          }}
                        >
                          {groupedApis[categorySlug].length}
                        </span>
                      </div>
                      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                        {groupedApis[categorySlug].map((api, index) => (
                          <APICard key={`${categorySlug}-${api.name}-${index}`} api={api} />
                        ))}
                      </div>
                    </section>
                  ))}
              </div>
            ) : (
              <div className="text-center py-16">
                <div className="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center"
                  style={{ backgroundColor: 'var(--card-bg)' }}>
                  <svg className="w-8 h-8" style={{ color: 'var(--muted)' }} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                      d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h3 className="text-lg font-medium mb-2" style={{ color: 'var(--foreground)' }}>
                  No APIs found
                </h3>
                <p style={{ color: 'var(--muted)' }}>
                  Try adjusting your search or filters
                </p>
                <button
                  onClick={() => {
                    setSearchQuery('');
                    setSelectedCategory(null);
                    setFilters({ auth: '', https: '', cors: '' });
                  }}
                  className="mt-4 px-4 py-2 rounded-lg font-medium transition-colors"
                  style={{
                    backgroundColor: 'var(--accent)',
                    color: 'white'
                  }}
                >
                  Clear all filters
                </button>
              </div>
            )}
          </div>

          {/* Footer */}
          <footer className="border-t mt-16 py-8" style={{ borderColor: 'var(--card-border)' }}>
            <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
              <p className="text-sm" style={{ color: 'var(--muted)' }}>
                A curated list of free APIs from the{' '}
                <a
                  href="https://github.com/public-apis/public-apis"
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{ color: 'var(--accent)' }}
                  className="hover:underline"
                >
                  public-apis
                </a>
                {' '}project. MIT License.
              </p>
            </div>
          </footer>
        </main>
      </div>
    </div>
  );
}
