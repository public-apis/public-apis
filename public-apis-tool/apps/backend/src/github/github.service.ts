import { Injectable } from "@nestjs/common";
import { User } from "src/generated/prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { Octokit } from "@octokit/rest";
import { ApiType } from "src/apis/apis.service";

@Injectable()
export class GithubService {
  constructor(private prisma: PrismaService) {}

  async createPR(user: User, api: ApiType) {
    const octokit = new Octokit({ auth: user.githubToken });

    const upstream = {
      owner: "L3gvccy",
      repo: "public-apis",
    };

    let forkExists = true;
    try {
      await octokit.repos.get({
        owner: user.login,
        repo: upstream.repo,
      });
    } catch (error) {
      forkExists = false;
    }

    if (!forkExists) {
      await octokit.repos.createFork(upstream);
      for (let i = 0; i < 20; i++) {
        try {
          await octokit.repos.get({ owner: user.login, repo: upstream.repo });
          break;
        } catch {
          await new Promise((r) => setTimeout(r, 1500));
        }
      }
    }

    const base = await octokit.repos.getBranch({
      ...upstream,
      branch: "master",
    });

    const branch = `add-api-${Date.now()}`;

    await octokit.git.createRef({
      owner: user.login,
      repo: upstream.repo,
      ref: `refs/heads/${branch}`,
      sha: base.data.commit.sha,
    });

    const readme = (await octokit.repos.getContent({
      owner: user.login,
      repo: upstream.repo,
      path: "README.md",
      ref: branch,
    })) as any;

    const content = Buffer.from(readme.data.content, "base64").toString();
    const updated = this.insertAPI(content, api);

    await octokit.repos.createOrUpdateFileContents({
      owner: user.login,
      repo: upstream.repo,
      path: "README.md",
      message: `Add ${api.name} API to ${api.category} category`,
      content: Buffer.from(updated).toString("base64"),
      sha: readme.data.sha,
      branch,
    });

    const pr = await octokit.pulls.create({
      ...upstream,
      title: `Add ${api.name} API to ${api.category} category`,
      head: `${user.login}:${branch}`,
      base: "master",
      body: `Submitted with Public APIs Tool`,
    });

    return pr.data.html_url;
  }

  insertAPI(content: string, api: ApiType): string {
    const rawLines = content.split("\n");

    const entry = `| [${api.name}](${api.link}) | ${api.description} | ${api.auth} | ${api.https} | ${api.cors} |`;

    let inCategory = false;
    let inserted = false;
    let output: string[] = [];

    for (let i = 0; i < rawLines.length; i++) {
      const line = rawLines[i].trim();
      const nextLine = rawLines[i + 1]?.trim() || "";

      if (line === `### ${api.category}`) {
        inCategory = true;
        output.push(line);
        continue;
      }

      if (inCategory && !inserted) {
        if (line === "|:---|:---|:---|:---|:---|" || !line.startsWith("|")) {
          output.push(rawLines[i]);
          continue;
        }
        const currentMatch = line.match(/\[(.*?)\]/);
        const nextMatch = nextLine.match(/\[(.*?)\]/);

        if (!nextMatch || nextLine.startsWith("### ")) {
          if (!currentMatch) {
            output.push(entry);
            inserted = true;
            output.push(rawLines[i]);
            continue;
          }
          const currentName = currentMatch[1].toLowerCase();
          const newName = api.name.toLowerCase();
          if (currentName > newName) {
            output.push(entry);
            inserted = true;
          }
          output.push(rawLines[i]);
          continue;
        }

        if (currentMatch && nextMatch) {
          const currentName = currentMatch[1].toLowerCase();
          const nextName = nextMatch[1].toLowerCase();
          const newName = api.name.toLowerCase();

          if (currentName <= newName && newName <= nextName) {
            output.push(rawLines[i]);
            output.push(entry);
            inserted = true;
            continue;
          }
        }
      }

      output.push(rawLines[i]);
    }

    if (!inserted && inCategory) {
      output.push(entry);
    }

    return output.join("\n");
  }
}
