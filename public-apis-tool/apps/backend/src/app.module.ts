import { Module } from "@nestjs/common";
import { ApisModule } from "./apis/apis.module";
import { PrismaService } from "./prisma/prisma.service";
import { AuthModule } from "./auth/auth.module";
import { UserService } from "./user/user.service";
import { AuthService } from "./auth/auth.service";
import { JwtService } from "@nestjs/jwt";

@Module({
  imports: [ApisModule, AuthModule],
  controllers: [],
  providers: [PrismaService, UserService, AuthService, JwtService],
})
export class AppModule {}
