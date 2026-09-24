import { Module } from "@nestjs/common";
import { ApisService } from "./apis.service";
import { ApisController } from "./apis.controller";
import { PrismaService } from "src/prisma/prisma.service";

@Module({
  controllers: [ApisController],
  providers: [ApisService, PrismaService],
})
export class ApisModule {}
