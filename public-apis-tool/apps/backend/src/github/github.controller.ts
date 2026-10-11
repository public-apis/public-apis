import { Body, Controller, Get, Post, UseGuards } from "@nestjs/common";
import { GithubService } from "./github.service";
import { ApisService, type ApiType } from "src/apis/apis.service";
import { UserId } from "src/auth/user-id.decorator";
import { UserService } from "src/user/user.service";
import { JwtAuthGuard } from "src/auth/jwt.guard";

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

  @UseGuards(JwtAuthGuard)
  @Get("pr-history")
  async PRHistory(@UserId() userId: number) {
    const user = await this.userService.findById(userId);

    if (user) {
      return await this.githubService.PRHistory(user);
    }
  }
}
