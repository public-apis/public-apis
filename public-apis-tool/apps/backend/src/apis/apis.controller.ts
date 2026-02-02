import { Controller } from "@nestjs/common";
import { ApisService } from "./apis.service";

@Controller("apis")
export class ApisController {
  constructor(private readonly apisService: ApisService) {}
}
