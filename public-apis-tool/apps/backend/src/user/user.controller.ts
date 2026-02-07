import { Controller, Get, Res, UseGuards } from "@nestjs/common";
import { UserService } from "./user.service";
import { JwtAuthGuard } from "src/auth/jwt.guard";
import { UserId } from "src/auth/user-id.decorator";
import type { Response } from "express";

@Controller("user")
export class UserController {
  constructor(private userService: UserService) {}

  @UseGuards(JwtAuthGuard)
  @Get("me")
  async getMe(@UserId() userId: number) {
    const user = await this.userService.findById(userId);

    return { user };
  }

  @Get("logout")
  async logout(@Res() res: Response) {
    res.cookie("jwt", "", {
      httpOnly: true,
      secure: true,
      sameSite: "none",
      maxAge: 1,
    });

    return true;
  }
}
