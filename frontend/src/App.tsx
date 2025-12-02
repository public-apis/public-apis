import { useState } from 'react';
import { useAPI } from './hooks/useAPI';
import Filter from './components/Filter';
import APICard from './components/APICard';
import DetailModal from './components/DetailModal';
import Pagination from './components/Pagination';
import type { APIEntry } from './types/api';
import './App.css';

function App() {
  const {
    data: filteredAPIs,
    loading,
    categories,
    filters,
    pagination,
    isFavorite,
    toggleFavorite,
    updateFilters,
    updatePagination
  } = useAPI();

  // 详情弹窗状态
  const [selectedAPI, setSelectedAPI] = useState<APIEntry | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  // 打开详情弹窗
  const handleViewDetails = (api: APIEntry) => {
    setSelectedAPI(api);
    setIsModalOpen(true);
  };

  // 关闭详情弹窗
  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedAPI(null);
  };

  return (
    <div className="app">
      {/* 页面头部 */}
      <header className="app-header">
        <h1>🌐 公共 API 浏览器</h1>
        <p>发现并使用免费的公共 API</p>
      </header>

      {/* 主内容区 */}
      <main className="app-main">
        {/* 过滤器 */}
        <Filter
          filters={filters}
          categories={categories}
          onFilterChange={updateFilters}
        />

        {/* API 卡片列表 */}
        {loading ? (
          <div className="loading-container">
            <div className="loading-spinner">加载中...</div>
          </div>
        ) : filteredAPIs.length === 0 ? (
          <div className="empty-state">
            <h3>😔 没有找到匹配的 API</h3>
            <p>请尝试调整搜索条件或过滤选项</p>
          </div>
        ) : (
          <>
            <div className="api-grid">
              {filteredAPIs.map((api) => (
                <APICard
                  key={api.id}
                  api={api}
                  isFavorite={isFavorite(api.id)}
                  onToggleFavorite={() => toggleFavorite(api.id)}
                  onViewDetails={() => handleViewDetails(api)}
                />
              ))}
            </div>

            {/* 分页组件 */}
            <Pagination
              pagination={pagination}
              onPageChange={(page) => updatePagination({ currentPage: page })}
            />
          </>
        )}
      </main>

      {/* 详情弹窗 */}
      <DetailModal
        api={selectedAPI}
        isOpen={isModalOpen}
        onClose={handleCloseModal}
      />

      {/* 页面底部 */}
      <footer className="app-footer">
        <p>
          数据来自 public-apis 项目 | 收藏功能使用 localStorage 存储
        </p>
      </footer>
    </div>
  );
}

export default App;
