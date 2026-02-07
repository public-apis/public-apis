import { Injectable } from "@nestjs/common";
import { User } from "src/generated/prisma/client";
import { PrismaService } from "src/prisma/prisma.service";

@Injectable()
export class UserService {
  constructor(private prisma: PrismaService) {}

  async upsertUser(data: Partial<User>) {
    return await this.prisma.user.upsert({
      where: {
        githubId: data.githubId,
      },
      update: {
        login: data.login,
        avatar: data.avatar,
        githubToken: data.githubToken,
      },
      create: {
        githubId: data.githubId!,
        login: data.login!,
        avatar: data.avatar,
        githubToken: data.githubToken!,
      },
    });
  }

  async findById(id: number) {
    return await this.prisma.user.findUnique({ where: { id } });
  }
}
