import { Injectable, BadRequestException } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import axios from "axios";
import { URL } from "url";

export type ApiType = {
  name: string;
  category: string;
  link: string;
  description: string;
  auth: AuthEnum;
  https: boolean;
  cors: CORSEnum;
  postmanLink?: string;
  status?: ApiStatusResult;
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

type ApiStatus = "online" | "offline" | "unknown";

type ApiStatusResult = {
  url: string;
  status: ApiStatus;
  code: number | null;
  responseTimeMs: number | null;
  checkedAt: string;
};

type ApiStatusCacheEntry = {
  data: ApiStatusResult;
  expiresAt: number;
};

@Injectable()
export class ApisService {
  private readonly statusCache = new Map<string, ApiStatusCacheEntry>();

  private readonly cacheTtlMs = 1000 * 60 * 30; 

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

  async checkApiStatus(url: string) {
    const normalizedUrl = this.normalizeUrl(url);

    const cached = this.statusCache.get(normalizedUrl);
    if (cached && cached.expiresAt > Date.now()) {
      return cached.data;
    }

    const start = Date.now();
    let status: ApiStatus = "unknown";
    let code: number | null = null;

    try {
      const head = await axios.head(normalizedUrl, {
        timeout: 5000,
        maxRedirects: 3,
        validateStatus: () => true,
      });
      code = head.status;
      if (code >= 200 && code < 400) {
        status = "online";
      } else if (code >= 400 && code < 600) {
        status = "offline";
      }
    } catch {
      try {
        const get = await axios.get(normalizedUrl, {
          timeout: 5000,
          maxRedirects: 3,
          validateStatus: () => true,
        });
        code = get.status;
        if (code >= 200 && code < 400) {
          status = "online";
        } else if (code >= 400 && code < 600) {
          status = "offline";
        }
      } catch {
        status = "unknown";
      }
    }

    const data: ApiStatusResult = {
      url: normalizedUrl,
      status,
      code,
      responseTimeMs: Date.now() - start,
      checkedAt: new Date().toISOString(),
    };

    this.statusCache.set(normalizedUrl, {
      data,
      expiresAt: Date.now() + this.cacheTtlMs,
    });

    return data;
  }

  private normalizeUrl(input: string): string {
    if (!input || input.trim().length === 0) {
      throw new BadRequestException("URL is required");
    }

    let parsed: URL;
    try {
      parsed = new URL(input);
    } catch {
      throw new BadRequestException("Invalid URL");
    }

    if (!["http:", "https:"].includes(parsed.protocol)) {
      throw new BadRequestException("Only http/https URLs are allowed");
    }

    const hostname = parsed.hostname.toLowerCase();
    if (
      hostname === "localhost" ||
      hostname.startsWith("127.") ||
      hostname.startsWith("192.168.") 
    ) {
      throw new BadRequestException("Private network URLs are not allowed");
    }

    return parsed.toString();
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
