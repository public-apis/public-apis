import { Body, Controller, Post, UseGuards } from "@nestjs/common";
import { GithubService } from "./github.service";
import { ApisService } from "src/apis/apis.service";
import { UserId } from "src/auth/user-id.decorator";
import { UserService } from "src/user/user.service";
import { JwtAuthGuard } from "src/auth/jwt.guard";
import type { ApiType } from "@repo/shared";

@Controller("github")
export class GithubController {
  constructor(
    private readonly githubService: GithubService,
    private userService: UserService,
  ) {}

  @UseGuards(JwtAuthGuard)
  @Post("add-api")
  async addApi(@UserId() userId: number, @Body() api: ApiType) {
    const user = await this.userService.findById(userId);

    if (user) {
      return await this.githubService.createPR(user, api);
    }
  }
}
