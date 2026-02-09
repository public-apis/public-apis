import { Controller } from "@nestjs/common";
import { ApisService } from "./apis.service";
import { Get } from "@nestjs/common";

@Controller("apis")
export class ApisController {
  constructor(private readonly apisService: ApisService) {}

  @Get()
  async getApis() {
    const md = await this.apisService.loadReadme();
    return this.apisService.parseReadme(md);
  }

  @Get("get-categories")
  async getCategories() {
    const md = await this.apisService.loadReadme();
    return this.apisService.getCategories(md);
  }
}
