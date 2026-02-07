import { Module } from "@nestjs/common";
import { ApisModule } from "./apis/apis.module";
import { PrismaService } from './prisma/prisma.service';
import { AuthModule } from './auth/auth.module';

@Module({
  imports: [ApisModule, AuthModule],
  controllers: [],
  providers: [PrismaService],
})
export class AppModule {}
