import React from 'react';
import type { APIEntry } from '../types/api';

interface DetailModalProps {
  api: APIEntry | null;
  isOpen: boolean;
  onClose: () => void;
}

export default function DetailModal({ api, isOpen, onClose }: DetailModalProps) {
  if (!isOpen || !api) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        {/* 弹窗头部 */}
        <div className="modal-header">
          <h2>{api.API}</h2>
          <button className="close-btn" onClick={onClose}>
            ×
          </button>
        </div>

        {/* 弹窗主体 */}
        <div className="modal-body">
          {/* 基本信息 */}
          <div className="detail-section">
            <h3>基本信息</h3>
            <div className="detail-row">
              <span className="detail-label">分类:</span>
              <span className="detail-value">{api.Category}</span>
            </div>
            <div className="detail-row">
              <span className="detail-label">描述:</span>
              <span className="detail-value">{api.Description}</span>
            </div>
          </div>

          {/* 连接信息 */}
          <div className="detail-section">
            <h3>连接信息</h3>
            <div className="detail-row">
              <span className="detail-label">API 地址:</span>
              <a
                href={api.Link}
                target="_blank"
                rel="noopener noreferrer"
                className="detail-value link"
              >
                {api.Link}
              </a>
            </div>
            {api.Example && (
              <div className="detail-row">
                <span className="detail-label">示例地址:</span>
                <a
                  href={api.Example}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="detail-value link"
                >
                  {api.Example}
                </a>
              </div>
            )}
          </div>

          {/* 安全信息 */}
          <div className="detail-section">
            <h3>安全信息</h3>
            <div className="detail-row">
              <span className="detail-label">协议:</span>
              <span className={`detail-value badge ${api.HTTPS ? 'success' : 'warning'}`}>
                {api.HTTPS ? 'HTTPS' : 'HTTP'}
              </span>
            </div>
            <div className="detail-row">
              <span className="detail-label">认证方式:</span>
              <span className={`detail-value badge ${api.Auth ? 'info' : 'success'}`}>
                {api.Auth ? api.Auth : '无需认证'}
              </span>
            </div>
            <div className="detail-row">
              <span className="detail-label">CORS:</span>
              <span className={`detail-value badge ${api.Cors === 'yes' ? 'success' : 'danger'}`}>
                {api.Cors === 'yes' ? '支持' : '不支持'}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
