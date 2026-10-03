import { Module } from "@nestjs/common";
import { GithubService } from "./github.service";
import { GithubController } from "./github.controller";
import { PrismaService } from "src/prisma/prisma.service";
import { JwtService } from "@nestjs/jwt";
import { UserService } from "src/user/user.service";

@Module({
  controllers: [GithubController],
  providers: [GithubService, PrismaService, JwtService, UserService],
})
export class GithubModule {}
