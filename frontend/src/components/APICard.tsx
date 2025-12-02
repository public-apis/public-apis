import React from 'react';
import type { APIEntry } from '../types/api';

interface APICardProps {
  api: APIEntry;
  isFavorite: boolean;
  onToggleFavorite: () => void;
  onViewDetails: () => void;
}

export default function APICard({ api, isFavorite, onToggleFavorite, onViewDetails }: APICardProps) {
  return (
    <div className="api-card">
      {/* 收藏按钮 */}
      <button
        className={`favorite-btn ${isFavorite ? 'favorited' : ''}`}
        onClick={onToggleFavorite}
        title={isFavorite ? '取消收藏' : '收藏'}
      >
        {isFavorite ? '★' : '☆'}
      </button>

      <div className="api-content">
        {/* API 标题 */}
        <h3 className="api-name">{api.API}</h3>

        {/* API 分类标签 */}
        <span className="category-tag">{api.Category}</span>

        {/* API 描述 */}
        <p className="api-description">{api.Description}</p>

        {/* API 属性标签 */}
        <div className="api-properties">
          <span className={`property-tag ${api.HTTPS ? 'https' : 'http'}`}>
            {api.HTTPS ? '🔒 HTTPS' : '📶 HTTP'}
          </span>
          
          <span className={`property-tag ${api.Auth ? 'auth' : 'no-auth'}`}>
            {api.Auth ? `🔑 ${api.Auth}` : '🚫 无需认证'}
          </span>

          <span className={`property-tag ${api.Cors === 'yes' ? 'cors' : 'no-cors'}`}>
            {api.Cors === 'yes' ? '✅ CORS' : '❌ 无CORS'}
          </span>
        </div>

        {/* 操作按钮 */}
        <div className="api-actions">
          <a
            href={api.Link}
            target="_blank"
            rel="noopener noreferrer"
            className="action-btn primary"
          >
            访问 API
          </a>
          <button className="action-btn secondary" onClick={onViewDetails}>
            查看详情
          </button>
        </div>
      </div>
    </div>
  );
}
