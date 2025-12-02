// API 数据类型定义
export interface APIEntry {
  // API 唯一标识
  id: string;
  // API 名称
  API: string;
  // API 描述
  Description: string;
  // API 分类
  Category: string;
  // API 端点地址
  Link: string;
  // 是否需要 HTTPS
  HTTPS: boolean;
  // 认证方式
  Auth: string | null;
  // 是否需要 CORS
  Cors: string;
  // 示例请求地址
  Example?: string;
}

// 过滤选项类型
export interface FilterOptions {
  // 搜索关键词
  searchTerm: string;
  // 选中的分类
  selectedCategory: string;
  // 是否只显示 HTTPS API
  onlyHttps: boolean;
  // 认证方式过滤
  authType: string;
}

// 分页信息类型
export interface PaginationInfo {
  currentPage: number;
  itemsPerPage: number;
  totalItems: number;
}
