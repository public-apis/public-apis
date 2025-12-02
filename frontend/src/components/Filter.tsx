import React from 'react';
import type { FilterOptions } from '../types/api';

interface FilterProps {
  filters: FilterOptions;
  categories: string[];
  onFilterChange: (filters: Partial<FilterOptions>) => void;
}

export default function Filter({ filters, categories, onFilterChange }: FilterProps) {
  return (
    <div className="filter-container">
      {/* 搜索框 */}
      <div className="search-group">
        <label htmlFor="search">搜索:</label>
        <input
          id="search"
          type="text"
          placeholder="按API名称或描述搜索..."
          value={filters.searchTerm}
          onChange={(e) => onFilterChange({ searchTerm: e.target.value })}
          className="search-input"
        />
      </div>

      {/* 分类筛选 */}
      <div className="select-group">
        <label htmlFor="category">分类:</label>
        <select
          id="category"
          value={filters.selectedCategory}
          onChange={(e) => onFilterChange({ selectedCategory: e.target.value })}
          className="select-input"
        >
          {categories.map((category) => (
            <option key={category} value={category}>
              {category === 'all' ? '所有分类' : category}
            </option>
          ))}
        </select>
      </div>

      {/* HTTPS 过滤 */}
      <div className="checkbox-group">
        <label>
          <input
            type="checkbox"
            checked={filters.onlyHttps}
            onChange={(e) => onFilterChange({ onlyHttps: e.target.checked })}
          />
          仅显示 HTTPS API
        </label>
      </div>

      {/* 认证方式过滤 */}
      <div className="select-group">
        <label htmlFor="auth">认证方式:</label>
        <select
          id="auth"
          value={filters.authType}
          onChange={(e) => onFilterChange({ authType: e.target.value })}
          className="select-input"
        >
          <option value="all">所有认证方式</option>
          <option value="none">无需认证</option>
          <option value="apiKey">API Key</option>
          <option value="OAuth">OAuth</option>
          <option value="X-Mashape-Key">X-Mashape-Key</option>
        </select>
      </div>
    </div>
  );
}
