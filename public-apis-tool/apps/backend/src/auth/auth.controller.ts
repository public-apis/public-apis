import { Controller, Get, Query, Res } from "@nestjs/common";
import { AuthService } from "./auth.service";
import { UserService } from "src/user/user.service";
import type { Response } from "express";

@Controller("auth")
export class AuthController {
  constructor(
    private readonly authService: AuthService,
    private readonly userService: UserService,
  ) {}

  @Get("github")
  githubLogin(@Res() res: Response) {
    const params = new URLSearchParams({
      client_id: process.env.GITHUB_CLIENT_ID ?? "",
      scope: "public_repo read:user",
      prompt: "consent",
    });

    const redirectUrl = `https://github.com/login/oauth/authorize?${params.toString()}`;

    return res.redirect(redirectUrl);
  }

  @Get("github/callback")
  async githubCallback(@Query("code") code: string, @Res() res: Response) {
    const accessToken = await this.authService.getAccessToken(code);
    const profile = await this.authService.getUserProfile(accessToken);

    const user = await this.userService.upsertUser({
      githubId: profile.id,
      login: profile.login,
      avatar: profile.avatar_url,
      githubToken: accessToken,
    });

    const jwt = this.authService.generateJwt({ sub: user.id });

    res.cookie("jwt", jwt, {
      httpOnly: true,
      secure: true,
      sameSite: "none",
      maxAge: 1000 * 60 * 60 * 24,
    });

    res.redirect(`${process.env.ORIGIN}/auth-success`);
  }
}
