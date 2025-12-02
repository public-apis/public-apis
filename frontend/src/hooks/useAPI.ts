import { useState, useEffect, useMemo } from 'react';
import type { APIEntry, FilterOptions, PaginationInfo } from '../types/api';

// 收藏存储键名
const FAVORITES_STORAGE_KEY = 'api-favorites';

export function useAPI() {
  // API 数据状态
  const [apiData, setApiData] = useState<APIEntry[]>([]);
  // 加载状态
  const [loading, setLoading] = useState(true);
  // 收藏列表
  const [favorites, setFavorites] = useState<Set<string>>(new Set());
  // 过滤选项
  const [filters, setFilters] = useState<FilterOptions>({
    searchTerm: '',
    selectedCategory: 'all',
    onlyHttps: false,
    authType: 'all'
  });
  // 分页信息
  const [pagination, setPagination] = useState<PaginationInfo>({
    currentPage: 1,
    itemsPerPage: 20,
    totalItems: 0
  });

  // 从 localStorage 加载收藏列表
  useEffect(() => {
    const savedFavorites = localStorage.getItem(FAVORITES_STORAGE_KEY);
    if (savedFavorites) {
      try {
        setFavorites(new Set(JSON.parse(savedFavorites)));
      } catch (error) {
        console.error('Failed to load favorites:', error);
      }
    }
  }, []);

  // 保存收藏列表到 localStorage
  useEffect(() => {
    localStorage.setItem(FAVORITES_STORAGE_KEY, JSON.stringify(Array.from(favorites)));
  }, [favorites]);

  // 加载 API 数据
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // 从本地 public 目录加载数据
        const response = await fetch('/apis.json');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        // 为每个 API 添加唯一 ID
        const apiEntries: APIEntry[] = (data.entries || []).map((entry: Omit<APIEntry, 'id'>, index: number) => ({
          ...entry,
          id: `${entry.Category}-${entry.API}-${index}`
        })).slice(0, 80); // 只取前 80 条
        
        setApiData(apiEntries);
        setPagination(prev => ({ ...prev, totalItems: apiEntries.length }));
      } catch (error) {
        console.error('Failed to fetch API data:', error);
        // 如果加载失败，使用模拟数据
        setApiData(getMockData());
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // 过滤和分页处理
  const filteredAndPaginatedData = useMemo(() => {
    let result = [...apiData];

    // 搜索过滤
    if (filters.searchTerm.trim()) {
      const term = filters.searchTerm.toLowerCase();
      result = result.filter(
        entry => 
          entry.API.toLowerCase().includes(term) || 
          entry.Description.toLowerCase().includes(term)
      );
    }

    // 分类过滤
    if (filters.selectedCategory !== 'all') {
      result = result.filter(entry => entry.Category === filters.selectedCategory);
    }

    // HTTPS 过滤
    if (filters.onlyHttps) {
      result = result.filter(entry => entry.HTTPS);
    }

    // 认证方式过滤
    if (filters.authType !== 'all') {
      if (filters.authType === 'none') {
        result = result.filter(entry => entry.Auth === null || entry.Auth === '');
      } else {
        result = result.filter(entry => entry.Auth === filters.authType);
      }
    }

    // 更新总条目数
    setPagination(prev => ({ ...prev, totalItems: result.length, currentPage: 1 }));

    // 分页处理
    const startIndex = (pagination.currentPage - 1) * pagination.itemsPerPage;
    const endIndex = startIndex + pagination.itemsPerPage;
    
    return result.slice(startIndex, endIndex);
  }, [apiData, filters, pagination.currentPage, pagination.itemsPerPage]);

  // 获取所有分类
  const categories = useMemo(() => {
    const categorySet = new Set(apiData.map(entry => entry.Category));
    return ['all', ...Array.from(categorySet).sort()];
  }, [apiData]);

  // 切换收藏状态
  const toggleFavorite = (id: string) => {
    setFavorites(prev => {
      const newFavorites = new Set(prev);
      if (newFavorites.has(id)) {
        newFavorites.delete(id);
      } else {
        newFavorites.add(id);
      }
      return newFavorites;
    });
  };

  // 检查是否已收藏
  const isFavorite = (id: string) => favorites.has(id);

  // 更新过滤选项
  const updateFilters = (newFilters: Partial<FilterOptions>) => {
    setFilters(prev => ({ ...prev, ...newFilters }));
    setPagination(prev => ({ ...prev, currentPage: 1 }));
  };

  // 更新分页
  const updatePagination = (newPagination: Partial<PaginationInfo>) => {
    setPagination(prev => ({ ...prev, ...newPagination }));
  };

  return {
    data: filteredAndPaginatedData,
    loading,
    favorites,
    categories,
    filters,
    pagination,
    isFavorite,
    toggleFavorite,
    updateFilters,
    updatePagination
  };
}

// 生成模拟数据，以防加载失败
function getMockData(): APIEntry[] {
  const mockCategories = ['Animals', 'Books', 'Business', 'Calendar', 'Cloud Storage', 'Cryptocurrency', 'Data Validation', 'Development'];
  const mockEntries: APIEntry[] = [];

  for (let i = 0; i < 80; i++) {
    const category = mockCategories[Math.floor(i / 10)];
    mockEntries.push({
      id: `mock-${i}`,
      API: `Mock API ${i + 1}`,
      Description: `This is a mock ${category.toLowerCase()} API for testing purposes. Provides access to ${category.toLowerCase()} related data.`,
      Category: category,
      Link: `https://api.example.com/${category.toLowerCase()}/${i + 1}`,
      HTTPS: i % 3 !== 0,
      Auth: i % 4 === 0 ? 'apiKey' : i % 4 === 1 ? 'OAuth' : null,
      Cors: i % 5 === 0 ? 'yes' : 'no'
    });
  }

  return mockEntries;
}
