import React from 'react';
import type { PaginationInfo } from '../types/api';

interface PaginationProps {
  pagination: PaginationInfo;
  onPageChange: (page: number) => void;
}

export default function Pagination({ pagination, onPageChange }: PaginationProps) {
  const { currentPage, itemsPerPage, totalItems } = pagination;
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  // 没有数据时不显示分页
  if (totalItems === 0) return null;

  // 只有一页时不显示分页
  if (totalPages <= 1) return null;

  // 生成分页页码
  const getPageNumbers = () => {
    const pages = [];
    const maxVisiblePages = 5;

    // 如果总页数小于等于最大可见页数，显示所有页码
    if (totalPages <= maxVisiblePages) {
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
      }
      return pages;
    }

    // 如果当前页在开头
    if (currentPage <= 3) {
      return [1, 2, 3, 4, '...', totalPages];
    }

    // 如果当前页在结尾
    if (currentPage >= totalPages - 2) {
      return [1, '...', totalPages - 3, totalPages - 2, totalPages - 1, totalPages];
    }

    // 如果当前页在中间
    return [
      1,
      '...',
      currentPage - 1,
      currentPage,
      currentPage + 1,
      '...',
      totalPages
    ];
  };

  const pageNumbers = getPageNumbers();

  return (
    <div className="pagination-container">
      <span className="pagination-info">
        共 {totalItems} 条记录，第 {currentPage} / {totalPages} 页
      </span>

      <div className="pagination-buttons">
        {/* 上一页 */}
        <button
          className="pagination-btn"
          onClick={() => onPageChange(currentPage - 1)}
          disabled={currentPage === 1}
        >
          ← 上一页
        </button>

        {/* 页码按钮 */}
        {pageNumbers.map((page, index) => (
          <React.Fragment key={index}>
            {page === '...' ? (
              <span className="pagination-ellipsis">...</span>
            ) : (
              <button
                className={`pagination-btn ${currentPage === page ? 'active' : ''}`}
                onClick={() => onPageChange(page as number)}
              >
                {page}
              </button>
            )}
          </React.Fragment>
        ))}

        {/* 下一页 */}
        <button
          className="pagination-btn"
          onClick={() => onPageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
        >
          下一页 →
        </button>
      </div>
    </div>
  );
}
