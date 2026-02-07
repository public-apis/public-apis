import { AuthEnum, CORSEnum } from "./enums";

export type ApiEntry = {
  name: string;
  description: string;
  category: string;
  auth: "None" | "API Key" | "OAuth" | "Basic";
  https: boolean;
  cors: "Yes" | "No" | "Unknown";
  link: string;
};

export type ApiType = {
  name: string;
  category: string;
  link: string;
  description: string;
  auth: AuthEnum;
  https: boolean;
  cors: CORSEnum;
  postmanLink?: string;
};
