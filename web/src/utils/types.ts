export interface API {
  name: string;
  url: string;
  description: string;
  auth: 'No' | 'apiKey' | 'OAuth' | 'X-Mashape-Key' | 'User-Agent';
  https: boolean;
  cors: 'Yes' | 'No' | 'Unknown';
}

export interface Category {
  name: string;
  slug: string;
  apis: API[];
}

export interface APIData {
  categories: Category[];
  totalApis: number;
  lastUpdated: string;
}
