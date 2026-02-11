import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import axios from "axios";

export type ApiType = {
  name: string;
  category: string;
  link: string;
  description: string;
  auth: AuthEnum;
  https: boolean;
  cors: CORSEnum;
  status?: string;
};

export enum AuthEnum {
  OAuth = "OAuth",
  apiKey = "apiKey",
  XMashapeKey = "X-Mashape-Key",
  No = "No",
  UserAgent = "User-Agent",
}

export enum CORSEnum {
  Yes = "Yes",
  No = "No",
  Unknown = "Unknown",
}

@Injectable()
export class ApisService {
  async loadReadme(): Promise<string> {
    const url =
      "https://raw.githubusercontent.com/L3gvccy/public-apis/master/README.md";
    const res = await axios.get<string>(url, { responseType: "text" });
    return res.data;
  }

  getCategories(md: string) {
    const lines = md.split("\n");

    let categories: string[] = [];

    let inIndex = false;

    for (const rawLine of lines) {
      const line = rawLine.trim();

      if (inIndex) {
        if (line === "<br >") {
          break;
        }

        if (line.startsWith("*")) {
          const category = line.split("[")[1].split("]")[0];
          categories.push(category);
        }
      }

      if (line === "## Index") {
        inIndex = true;
      }
    }

    return { categories };
  }

  parseReadme(md: string) {
    const lines = md.split("\n");

    let category = "";
    const apis: ApiType[] = [];

    for (const rawLine of lines) {
      const line = rawLine.trim();

      if (line.startsWith("### ")) {
        category = line.replace("### ", "").trim();
        continue;
      }

      if (
        !category ||
        !line.includes("|") ||
        line.startsWith("|:") ||
        line.startsWith("API |") ||
        line.includes("Back to Index")
      ) {
        continue;
      }

      const cols = line
        .split("|")
        .map((c) => c.trim())
        .filter(Boolean);

      if (cols.length < 5) continue;

      const [apiCol, descCol, authCol, httpsCol, corsCol] = cols;
      const { name, link } = this.extractLink(apiCol);
      const description = this.cleanMarkdown(descCol);
      const auth = this.parseAuth(authCol);
      const https = this.parseHttps(httpsCol);
      const cors = this.parseCors(corsCol);

      apis.push({
        category,
        name,
        description,
        auth,
        https,
        cors,
        link,
      });
    }

    return apis;
  }

  private cleanMarkdown(text: string): string {
    return text
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
      .replace(/\*\*/g, "")
      .replace(/`/g, "")
      .trim();
  }

  private extractLink(text: string): { name: string; link: string } {
    const match = /\[([^\]]+)\]\(([^)]+)\)/.exec(text);
    if (match) {
      return { name: match[1].trim(), link: match[2].trim() };
    }
    const name = this.cleanMarkdown(text);
    return { name, link: "" };
  }

  private parseAuth(text: string): AuthEnum {
    const normalized = this.cleanMarkdown(text).toLowerCase();
    if (!normalized || normalized === "no" || normalized === "none") {
      return AuthEnum.No;
    }
    if (normalized.includes("oauth")) return AuthEnum.OAuth;
    if (normalized.includes("api key") || normalized.includes("apikey"))
      return AuthEnum.apiKey;
    if (normalized.includes("x-mashape-key")) return AuthEnum.XMashapeKey;
    if (normalized.includes("user-agent")) return AuthEnum.UserAgent;
    return AuthEnum.No;
  }

  private parseHttps(text: string): boolean {
    const normalized = this.cleanMarkdown(text).toLowerCase();
    return normalized === "yes" || normalized === "true";
  }

  private parseCors(text: string): CORSEnum {
    const normalized = this.cleanMarkdown(text).toLowerCase();
    if (normalized === "yes" || normalized === "true") return CORSEnum.Yes;
    if (normalized === "no" || normalized === "false") return CORSEnum.No;
    return CORSEnum.Unknown;
  }
}
