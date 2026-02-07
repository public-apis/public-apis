export type ApiEntry = {
  name: string;
  description: string;
  category: string;
  auth: "None" | "API Key" | "OAuth" | "Basic";
  https: boolean;
  cors: "Yes" | "No" | "Unknown";
  link: string;
};
