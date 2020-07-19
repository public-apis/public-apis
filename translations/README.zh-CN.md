# 公开 API [![Build Status](https://api.travis-ci.org/public-apis/public-apis.svg)](https://travis-ci.org/public-apis/public-apis)

用于软件和 Web 开发的免费 API 的汇总列表。

可以找到该项目的公共 API [这里](https://github.com/davemachado/public-api)!

有关对该项目做出贡献的信息，请参见 [贡献指南](.github/CONTRIBUTING.md)。

请注意，传递的构建状态表示自上次更新以来所有列出的 API 均可用。生成状态失败表示此刻可能有 1 个或多个服务不可用。

## 指数

- [动物](#animals)
- [日本动漫](#anime)
- [反恶意软件](#anti-malware)
- [艺术与设计](#art--design)
- [图书](#books)
- [商业](#business)
- [日历](#calendar)
- [云存储和文件共享](#cloud-storage--file-sharing)
- [持续集成](#continuous-integration)
- [加密货币](#cryptocurrency)
- [货币兑换](#currency-exchange)
- [资料验证](#data-validation)
- [发展历程](#development)
- [辞典](#dictionaries)
- [文件与生产力](#documents--productivity)
- [环境](#environment)
- [大事记](#events)
- [金融](#finance)
- [食物和饮料](#food--drink)
- [游戏与漫画](#games--comics)
- [地理编码](#geocoding)
- [政府](#government)
- [健康](#health)
- [工作](#jobs)
- [机器学习](#machine-learning)
- [音乐](#music)
- [新闻](#news)
- [公开资料](#open-data)
- [开源项目](#open-source-projects)
- [专利](#patent)
- [个性](#personality)
- [摄影](#photography)
- [科学与数学](#science--math)
- [安全](#security)
- [购物](#shopping)
- [社会的](#social)
- [运动与健身](#sports--fitness)
- [测试数据](#test-data)
- [文字分析](#text-analysis)
- [追踪](#tracking)
- [运输](#transportation)
- [URL 缩短器](#url-shorteners)
- [车辆](#vehicle)
- [视频](#video)
- [天气](#weather)

### 动物

| 火                                                                                     | 描述                        | 验证码   | HTTPS | CORS |
| -------------------------------------------------------------------------------------- | --------------------------- | -------- | ----- | ---- |
| [猫的事实](https://alexwohlbruck.github.io/cat-facts/)                                 | 日常猫的事实                | 没有     | 是    | 没有 |
| [猫](https://docs.thecatapi.com/)                                                      | 猫的图片从 Tumblr           | `apiKey` | 是    | 未知 |
| [小狗](https://dog.ceo/dog-api/)                                                       | 基于斯坦福犬数据集          | 没有     | 是    | 是   |
| [HTTPCat](https://http.cat/)                                                           | 每个 HTTP 状态的猫          | 没有     | 是    | 未知 |
| [自然保护联盟](http://apiv3.iucnredlist.org/api/v3/docs)                               | IUCN 濒危物种红色名录       | `apiKey` | 没有  | 未知 |
| [Movebank](https://github.com/movebank/movebank-api-doc)                               | 动物的运动和迁移数据        | 没有     | 是    | 未知 |
| [寻宝](https://www.petfinder.com/developers/v2/docs/)                                  | 采用                        | `OAuth`  | 是    | 是   |
| [PlaceGOAT](https://placegoat.com/)                                                    | 占位符山羊图像              | 没有     | 是    | 未知 |
| [随机猫](https://aws.random.cat/meow)                                                  | 猫的随机图片                | 没有     | 是    | 是   |
| [狗狗](https://random.dog/woof.json)                                                   | 狗的随机图片                | 没有     | 是    | 是   |
| [狐狸](https://randomfox.ca/floof/)                                                    | 狐狸的随机图片              | 没有     | 是    | 没有 |
| [救援团体](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) | 采用                        | 没有     | 是    | 未知 |
| [Shibe.Online](http://shibe.online/)                                                   | Shibu Inu，猫或鸟的随机图片 | 没有     | 是    | 是   |

**[to 返回索引](#index)**

### 日本动漫

| 火                                                                  | 描述                     | 验证码  | HTTPS | CORS |
| ------------------------------------------------------------------- | ------------------------ | ------- | ----- | ---- |
| [清单](https://github.com/AniList/ApiV2-GraphQL-Docs)               | 动漫发现与追踪           | `OAuth` | 是    | 未知 |
| [动漫新闻网](https://www.animenewsnetwork.com/encyclopedia/api.php) | 动漫行业新闻             | 没有    | 是    | 是   |
| [吉坎](https://jikan.moe)                                           | 非官方的 MyAnimeList API | 没有    | 是    | 是   |
| [Kitsu](http://docs.kitsu.apiary.io/)                               | 动漫发现平台             | `OAuth` | 是    | 未知 |
| [吉卜力工作室](https://ghibliapi.herokuapp.com)                     | 吉卜力工作室电影的资源   | 没有    | 是    | 未知 |

**[to 返回索引](#index)**

### 反恶意软件

| 火                                                                  | 描述                      | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------- | ------------------------- | -------- | ----- | ---- |
| [IPDB 滥用](https://docs.abuseipdb.com/)                            | IP /域/ URL 信誉          | `apiKey` | 是    | 未知 |
| [AlienVault 开放威胁交换（OTX）](https://otx.alienvault.com/api/)   | IP /域/ URL 信誉          | `apiKey` | 是    | 未知 |
| [Google 安全浏览](https://developers.google.com/safe-browsing/)     | Google 链接/域标记        | `apiKey` | 是    | 未知 |
| [元证书](https://metacert.com/)                                     | Metacert 链接标记         | `apiKey` | 是    | 未知 |
| [病毒总数](https://www.virustotal.com/en/documentation/public-api/) | VirusTotal 文件/ URL 分析 | `apiKey` | 是    | 未知 |
| [信任网（WOT）](https://www.mywot.com/en/API)                       | 网站信誉                  | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 艺术与设计

| 火                                                          | 描述               | 验证码   | HTTPS | CORS |
| ----------------------------------------------------------- | ------------------ | -------- | ----- | ---- |
| [行为](https://www.behance.net/dev)                         | 设计               | `apiKey` | 是    | 未知 |
| [库珀·休伊特](https://collection.cooperhewitt.org/api)      | 史密森尼设计博物馆 | `apiKey` | 是    | 未知 |
| [运球](http://developer.dribbble.com/v2/)                   | 设计               | `OAuth`  | 没有  | 未知 |
| [哈佛美术馆](https://github.com/harvardartmuseums/api-docs) | 艺术               | `apiKey` | 没有  | 未知 |
| [图标查找器](https://developer.iconfinder.com)              | 图示               | `apiKey` | 是    | 未知 |
| [图标 8](http://docs.icons8.apiary.io/#reference/0/meta)    | 图示               | `OAuth`  | 是    | 未知 |
| [名词项目](http://api.thenounproject.com/index.html)        | 图示               | `OAuth`  | 没有  | 未知 |
| [国立博物馆](https://www.rijksmuseum.nl/en/api)             | 艺术               | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 图书

| 火                                                              | 描述                     | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------- | ------------------------ | -------- | ----- | ---- |
| [薄伽梵歌](https://bhagavadgita.io/api)                         | 薄伽梵歌文本             | `OAuth`  | 是    | 是   |
| [英国国家书目](http://bnb.data.bl.uk/)                          | 图书                     | 没有     | 没有  | 未知 |
| [好读](https://www.goodreads.com/api)                           | 图书                     | `apiKey` | 是    | 未知 |
| [Google 图书](https://developers.google.com/books/)             | 图书                     | `OAuth`  | 是    | 未知 |
| [图书馆](http://garbage.world/posts/libgen/)                    | 图书馆创世纪搜索引擎     | 没有     | 没有  | 未知 |
| [开放图书馆](https://openlibrary.org/developers/api)            | 书籍，书籍封面和相关数据 | 没有     | 是    | 未知 |
| [企鹅出版](http://www.penguinrandomhouse.biz/webservices/rest/) | 书籍，书籍封面和相关数据 | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 商业

| 火                                                                         | 描述                                         | 验证码   | HTTPS | CORS |
| -------------------------------------------------------------------------- | -------------------------------------------- | -------- | ----- | ---- |
| [慈善搜寻](http://charityapi.orghunter.com/)                               | 非营利慈善机构数据                           | `apiKey` | 没有  | 未知 |
| [Clearbit 徽标](https://clearbit.com/docs#logo-api)                        | 搜索公司徽标并将其嵌入到您的项目中           | `apiKey` | 是    | 未知 |
| [Domainsdb.info](https://domainsdb.info/)                                  | 注册域名搜索                                 | 没有     | 是    | 未知 |
| [自由职业者](https://developers.freelancer.com)                            | 雇用自由职业者完成工作                       | `OAuth`  | 是    | 未知 |
| [邮箱](https://developers.google.com/gmail/api/)                           | 灵活，RESTful 访问用户的收件箱               | `OAuth`  | 是    | 未知 |
| [谷歌分析](https://developers.google.com/analytics/)                       | 收集，配置和分析您的数据以吸引合适的受众     | `OAuth`  | 是    | 未知 |
| [MailboxValidator](https://www.mailboxvalidator.com/api-single-validation) | 验证电子邮件地址以提高可传递性               | `apiKey` | 是    | 未知 |
| [邮枪](https://www.mailgun.com/)                                           | 电邮服务                                     | `apiKey` | 是    | 未知 |
| [标记物](http://www.markerapi.com/)                                        | 商标搜索                                     | 没有     | 没有  | 未知 |
| [ick 虫](https://ticksel.com)                                              | 专为人类设计的友好网站分析                   | 没有     | 是    | 未知 |
| [特雷洛](https://developers.trello.com/)                                   | 板，列表和卡片可帮助您组织和确定项目的优先级 | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 日历

| 火                                                                 | 描述                                             | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------ | ------------------------------------------------ | -------- | ----- | ---- |
| [日历索引](https://www.calendarindex.com/)                         | 全球假期和工作日                                 | `apiKey` | 是    | 是   |
| [教堂日历](http://calapi.inadiutorium.cz/)                         | 天主教礼仪日历                                   | 没有     | 没有  | 未知 |
| [捷克命名日日历](http://svatky.adresa.info/)                       | 查找名称并返回命名日日期                         | 没有     | 没有  | 未知 |
| [Google 日历](https://developers.google.com/google-apps/calendar/) | 显示，创建和修改 Google 日历事件                 | `OAuth`  | 是    | 未知 |
| [希伯来语日历](https://www.hebcal.com/home/developer-apis)         | 在公历和希伯来语之间转换，获取安息日和假日时间等 | 没有     | 没有  | 未知 |
| [假期](https://holidayapi.com/)                                    | 有关假期的历史数据                               | `apiKey` | 是    | 未知 |
| [LectServe](http://www.lectserve.com)                              | 新教礼仪日历                                     | 没有     | 没有  | 未知 |
| [纳格·达特](https://date.nager.at)                                 | 超过 90 个国家/地区的公众假期                    | 没有     | 是    | 没有 |
| [命名日日历](https://api.abalin.net/)                              | 提供多个国家/地区的命名日                        | 没有     | 是    | 是   |
| [非工作日](https://github.com/gadael/icsdb)                        | 非工作日的 ICS 文件数据库                        | 没有     | 是    | 未知 |
| [俄罗斯日历](https://github.com/egno/work-calendar)                | 检查日期是否为俄罗斯假期                         | 没有     | 是    | 没有 |

**[to 返回索引](#index)**

### 云存储和文件共享

| 火                                                                | 描述                                           | 验证码   | HTTPS | CORS |
| ----------------------------------------------------------------- | ---------------------------------------------- | -------- | ----- | ---- |
| [框](https://developer.box.com/)                                  | 文件共享和存储                                 | `OAuth`  | 是    | 未知 |
| [投寄箱](https://www.dropbox.com/developers)                      | 文件共享和存储                                 | `OAuth`  | 是    | 未知 |
| [Google 云端硬碟](https://developers.google.com/drive/)           | 文件共享和存储                                 | `OAuth`  | 是    | 未知 |
| [一个驱动器](https://dev.onedrive.com/)                           | 文件共享和存储                                 | `OAuth`  | 是    | 未知 |
| [Pastebin](https://pastebin.com/api/)                             | 纯文本存储                                     | `apiKey` | 是    | 未知 |
| [颞](https://gateway.temporal.cloud/ipns/docs.api.temporal.cloud) | 基于 IPFS 的文件存储和共享以及可选的 IPNS 命名 | `apiKey` | 是    | 没有 |
| [WeTransfer](https://developers.wetransfer.com)                   | 文件共享                                       | `apiKey` | 是    | 是   |

**[to 返回索引](#index)**

### 持续集成

| 火                                                      | 描述                                                          | 验证码   | HTTPS | CORS |
| ------------------------------------------------------- | ------------------------------------------------------------- | -------- | ----- | ---- |
| [CircleCI](https://circleci.com/docs/api/v1-reference/) | 使用持续集成和持续交付使软件开发过程自动化                    | `apiKey` | 是    | 未知 |
| [代号](https://apidocs.codeship.com/)                   | Codeship 是云中的持续集成平台                                 | `apiKey` | 是    | 未知 |
| [特拉维斯 CI](https://docs.travis-ci.com/api/)          | 将您的 GitHub 项目与 Travis CI 同步，以在几分钟内测试您的代码 | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 加密货币

| 火                                                                    | 描述                                     | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------- | ---------------------------------------- | -------- | ----- | ---- |
| [币安](https://github.com/binance-exchange/binance-official-api-docs) | 交易中国的加密货币                       | `apiKey` | 是    | 未知 |
| [比特币平均](https://apiv2.bitcoinaverage.com/)                       | 区块链行业的数字资产价格数据             | `apiKey` | 是    | 未知 |
| [比特币图表](https://bitcoincharts.com/about/exchanges/)              | 与比特币网络有关的财务和技术数据         | 没有     | 是    | 未知 |
| [比特币](https://docs.bitfinex.com/docs)                              | 加密货币交易平台                         | `apiKey` | 是    | 未知 |
| [比特币](https://www.bitmex.com/app/apiOverview)                      | 总部位于香港的实时加密货币衍生品交易平台 | `apiKey` | 是    | 未知 |
| [Bittrex](https://bittrex.com/Home/Api)                               | 下一代加密交易平台                       | `apiKey` | 是    | 未知 |
| [块](https://www.block.io/docs/basic)                                 | 比特币支付，钱包和交易数据               | `apiKey` | 是    | 未知 |
| [区块链](https://www.blockchain.info/api)                             | 比特币支付，钱包和交易数据               | 没有     | 是    | 未知 |
| [CoinAPI](https://docs.coinapi.io/)                                   | 所有货币兑换都集成在一个 API 下          | `apiKey` | 是    | 没有 |
| [币库](https://developers.coinbase.com)                               | 比特币，比特币现金，莱特币和以太坊价格   | `apiKey` | 是    | 未知 |
| [Coinbase Pro](https://docs.pro.coinbase.com/#api)                    | 加密货币交易平台                         | `apiKey` | 是    | 未知 |
| [硬币台](http://www.coindesk.com/api/)                                | 比特币价格指数                           | 没有     | 没有  | 未知 |
| [壁虎](http://www.coingecko.com/api)                                  | 加密货币的价格，市场和开发商/社交数据    | 没有     | 是    | 是   |
| [Coinigy](https://coinigy.docs.apiary.io)                             | 与 Coinigy 帐户进行交互并直接进行交易    | `apiKey` | 是    | 未知 |
| [硬币层](https://coinlayer.com)                                       | 实时加密货币汇率                         | `apiKey` | 是    | 未知 |
| [Coinlib](https://coinlib.io/apidocs)                                 | 加密货币价格                             | `apiKey` | 是    | 未知 |
| [硬币传说](https://www.coinlore.com/cryptocurrency-data-api)          | 加密货币的价格，数量等等                 | 没有     | 是    | 未知 |
| [币市值](https://coinmarketcap.com/api/)                              | 加密货币价格                             | `apiKey` | 是    | 未知 |
| [Coinpaprika](https://api.coinpaprika.com)                            | 加密货币的价格，数量等等                 | 没有     | 是    | 是   |
| [硬币排名](https://docs.coinranking.com/)                             | 实时加密货币数据                         | 没有     | 是    | 未知 |
| [加密比较](https://www.cryptocompare.com/api#)                        | 加密货币比较                             | 没有     | 是    | 未知 |
| [密码器](https://www.cryptonator.com/api/)                            | 加密货币汇率                             | 没有     | 是    | 未知 |
| [双子座](https://docs.gemini.com/rest-api/)                           | 加密货币交易所                           | 没有     | 是    | 未知 |
| [ICObench](https://icobench.com/developers)                           | 有关列表，评分，统计信息等的各种信息     | `apiKey` | 是    | 未知 |
| [活币](https://www.livecoin.net/api)                                  | 加密货币交易所                           | 没有     | 是    | 未知 |
| [市场比特币](https://www.mercadobitcoin.net/api-doc/)                 | 巴西加密货币信息                         | 没有     | 是    | 未知 |
| [兑换](https://nexchange2.docs.apiary.io/)                            | 自动化的加密货币兑换服务                 | 没有     | 没有  | 是   |
| [尼斯哈希](https://docs.nicehash.com/)                                | 最大的加密货币采矿市场                   | `apiKey` | 是    | 未知 |
| [Poloniex](https://poloniex.com/support/api/)                         | 美国的数字资产交易所                     | `apiKey` | 是    | 未知 |
| [世界币](https://www.worldcoinindex.com/apiservice)                   | 加密货币价格                             | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 货币兑换

| 火                                                                                                    | 描述                     | 验证码   | HTTPS | CORS |
| ----------------------------------------------------------------------------------------------------- | ------------------------ | -------- | ----- | ---- |
| [1 锻造](https://1forge.com/forex-data-api/api-documentation)                                         | 外汇货币市场数据         | `apiKey` | 是    | 未知 |
| [货币层](https://currencylayer.com/documentation)                                                     | 汇率和货币换算           | `apiKey` | 是    | 未知 |
| [捷克国家银行](https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml) | 汇率汇总                 | 没有     | 是    | 未知 |
| [ExchangeRate-API](https://www.exchangerate-api.com)                                                  | 免费货币兑换             | 没有     | 是    | 是   |
| [Exchangeratesapi.io](https://exchangeratesapi.io)                                                    | 汇率与货币换算           | 没有     | 是    | 是   |
| [Fixer.io](http://fixer.io)                                                                           | 汇率和货币换算           | `apiKey` | 是    | 未知 |
| [法兰克福](https://www.frankfurter.app/docs)                                                          | 汇率，货币换算和时间序列 | 没有     | 是    | 是   |
| [Ratesapi](https://ratesapi.io)                                                                       | 免费汇率和历史汇率       | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 资料验证

| 火                                                                       | 描述                                       | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------------ | ------------------------------------------ | -------- | ----- | ---- |
| [Cloudmersive 验证](https://cloudmersive.com/validate-api)               | 验证电子邮件地址，电话号码，增值税号和域名 | `apiKey` | 是    | 是   |
| [语言层](https://languagelayer.com)                                      | 语言检测                                   | 没有     | 是    | 未知 |
| [Lob.com](https://lob.com/)                                              | 美国地址验证                               | `apiKey` | 是    | 未知 |
| [邮箱层](https://mailboxlayer.com)                                       | 电子邮件地址验证                           | 没有     | 是    | 未知 |
| [验证码](https://numvalidate.com)                                        | 开源电话号码验证                           | 没有     | 是    | 未知 |
| [量化](https://numverify.com)                                            | 电话号码验证                               | 没有     | 是    | 未知 |
| [PurgoMalum](http://www.purgomalum.com)                                  | 反对亵渎和淫秽的内容验证器                 | 没有     | 没有  | 未知 |
| [美国自动完成](https://smartystreets.com/docs/cloud/us-autocomplete-api) | 通过实时地址建议快速输入地址数据           | `apiKey` | 是    | 是   |
| [美国提取物](https://smartystreets.com/products/apis/us-extract-api)     | 从包括电子邮件在内的任何文本中提取邮政地址 | `apiKey` | 是    | 是   |
| [美国街地址](https://smartystreets.com/docs/cloud/us-street-api)         | 验证并附加任何美国邮政地址的数据           | `apiKey` | 是    | 是   |
| [瓦特莱现](https://vatlayer.com)                                         | 增值税号码验证                             | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 发展历程

| 火                                                                                              | 描述                                                                   | 验证码          | HTTPS | CORS |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------- | ----- | ---- |
| [24 个拉取请求](https://24pullrequests.com/api)                                                 | 在 12 月促进开源协作的项目                                             | 没有            | 是    | 是   |
| [Agify.io](https://agify.io)                                                                    | 根据名字估算年龄                                                       | 没有            | 是    | 是   |
| [ApiFlash](https://apiflash.com/)                                                               | 针对开发人员的基于 Chrome 的截图 API                                   | `apiKey`        | 是    | 未知 |
| [能力](https://apility.io/apidocs/)                                                             | IP，域和电子邮件反滥用 API 阻止列表                                    | 没有            | 是    | 是   |
| [APIs.guru](https://apis.guru/api-doc/)                                                         | Wikipedia for Web API，公共 API 的 OpenAPI / Swagger 规范              | 没有            | 是    | 未知 |
| [更好的元](http://bettermeta.io)                                                                | 以 JSON 格式返回网站的元标记                                           | `X-Mashape-Key` | 是    | 未知 |
| [比特桶](https://developer.atlassian.com/bitbucket/api/2/reference/)                            | Bitbucket API                                                          | `OAuth`         | 是    | 未知 |
| [无聊](https://www.boredapi.com/)                                                               | 寻找随机活动来对抗无聊                                                 | 没有            | 是    | 未知 |
| [眉毛](https://browshot.com/api/documentation)                                                  | 可以在任何屏幕尺寸和任何设备上轻松制作网页的屏幕截图                   | `apiKey`        | 是    | 未知 |
| [CDNJS](https://api.cdnjs.com/libraries/jquery)                                                 | CDNJS 上的图书馆信息                                                   | 没有            | 是    | 未知 |
| [变更日志](https://changelogs.md)                                                               | 来自开源项目的结构化变更日志元数据                                     | 没有            | 是    | 未知 |
| [计数 API](https://countapi.xyz)                                                                | 免费和简单的计数服务。您可以使用它来跟踪页面点击和特定事件             | 没有            | 是    | 是   |
| [DigitalOcean 状态](https://status.digitalocean.com/api/v1)                                     | 所有 DigitalOcean 服务的状态                                           | 没有            | 是    | 未知 |
| [DomainDb 信息](https://domainsdb.info)                                                         | 域名搜索以查找包含特定单词/短语/等的所有域名                           | 没有            | 是    | 未知 |
| [Faceplusplus](https://www.faceplusplus.com/)                                                   | 面部检测工具                                                           | `OAuth`         | 是    | 未知 |
| [性别化](https://genderize.io)                                                                  | 根据名字估算性别                                                       | 没有            | 是    | 是   |
| [的 GitHub](https://developer.github.com/v3/)                                                   | 以编程方式利用 GitHub 存储库，代码和用户信息                           | `OAuth`         | 是    | 是   |
| [Gitlab](https://docs.gitlab.com/ee/api/)                                                       | 以编程方式自动化 GitLab 交互                                           | `OAuth`         | 是    | 未知 |
| [格](https://developer.gitter.im/docs/welcome)                                                  | 开发人员聊天                                                           | `OAuth`         | 是    | 未知 |
| [HTTP2.Pro](https://http2.pro/doc/api)                                                          | 测试客户端和服务器 HTTP / 2 协议支持的端点                             | 没有            | 是    | 未知 |
| [IBM 文字转语音](https://console.bluemix.net/docs/services/text-to-speech/getting-started.html) | 将文字转换为语音                                                       | `apiKey`        | 是    | 是   |
| [图像图表](https://documentation.image-charts.com/)                                             | 生成图表，QR 码和图形图像                                              | 没有            | 是    | 是   |
| [import.io](http://api.docs.import.io/)                                                         | 从网站或 RSS feed 检索结构化数据                                       | `apiKey`        | 是    | 未知 |
| [IP 化](https://www.ipify.org/)                                                                 | 一个简单的 IP 地址 API                                                 | 没有            | 是    | 未知 |
| [IP 信息](https://ipinfo.io/developers)                                                         | 另一个简单的 IP 地址 API                                               | 没有            | 是    | 未知 |
| [JSON 2 JSONP](https://json2jsonp.com/)                                                         | 使用客户端 JavaScript 将 JSON 即时转换为 JSONP，以轻松进行跨域数据请求 | 没有            | 是    | 未知 |
| [JSONbin.io](https://jsonbin.io)                                                                | 免费的 JSON 存储服务。小型 Web 应用程序，网站和移动应用程序的理想选择  | `apiKey`        | 是    | 是   |
| [裁判 0](https://api.judge0.com/)                                                               | 编译并运行源代码                                                       | 没有            | 是    | 未知 |
| [让我们验证](https://github.com/letsvalidate/api)                                               | 发现网站上使用的技术以及指向缩略图的 URL                               | 没有            | 是    | 未知 |
| [许可证 API](https://github.com/cmccandless/license-api/blob/master/README.md)                  | 非官方的 REST API for Choosealicense.com                               | 没有            | 是    | 没有 |
| [MAC 地址供应商查找](https://macaddress.io)                                                     | 检索有关给定 MAC 地址或 OUI 的供应商详细信息和其他信息                 | `apiKey`        | 是    | 是   |
| [国籍化](https://nationalize.io)                                                                | 估算名字的国籍                                                         | 没有            | 是    | 是   |
| [垃圾邮件](https://oopspam.com/)                                                                | 多种垃圾邮件过滤服务                                                   | 没有            | 是    | 是   |
| [普利诺](https://plino.herokuapp.com/)                                                          | 垃圾邮件过滤系统                                                       | 没有            | 是    | 未知 |
| [邮差](https://docs.api.getpostman.com/)                                                        | 测试 API 的工具                                                        | `apiKey`        | 是    | 未知 |
| [代理搜寻](https://proxycrawl.com)                                                              | 抓取和抓取 anticaptcha 服务                                            | `apiKey`        | 是    | 未知 |
| [公开 API](https://github.com/davemachado/public-api)                                           | 用于 Web 开发的免费 JSON API 的汇总列表                                | 没有            | 是    | 未知 |
| [推杆](https://pusher.com/beams)                                                                | 推送通知适用于 Android 和 iOS                                          | `apiKey`        | 是    | 未知 |
| [二维码](http://qrtag.net/api/)                                                                 | 创建易于阅读的 QR 码和 URL 缩短器                                      | 没有            | 是    | 是   |
| [二维码](http://goqr.me/api/)                                                                   | 生成和解码/读取 QR 码图形                                              | 没有            | 是    | 未知 |
| [快速图表](https://quickchart.io/)                                                              | 生成图表和图形图像                                                     | 没有            | 是    | 是   |
| [要求](https://reqres.in/)                                                                      | 托管的 REST-API 准备响应您的 AJAX 请求                                 | 没有            | 是    | 未知 |
| [ScraperApi](https://www.scraperapi.com)                                                        | 轻松构建可伸缩的网页抓取工具                                           | `apiKey`        | 是    | 未知 |
| [ScreenshotAPI.net](https://screenshotapi.net/)                                                 | 创建像素完美的网站截图                                                 | `apiKey`        | 是    | 是   |
| [喧嚣](http://shoutcloud.io/)                                                                   | 全盖即服务                                                             | 没有            | 没有  | 未知 |
| [StackExchange](https://api.stackexchange.com/)                                                 | 开发人员问答论坛                                                       | `OAuth`         | 是    | 未知 |

**[to 返回索引](#index)**

### 辞典

| 火                                                | 描述                                 | 验证码   | HTTPS | CORS |
| ------------------------------------------------- | ------------------------------------ | -------- | ----- | ---- |
| [机器人语言](https://www.linguarobot.io)          | 单词定义，发音，同义词，反义词及其他 | `apiKey` | 是    | 是   |
| [韦伯斯特](https://dictionaryapi.com/)            | 字典和词库数据                       | `apiKey` | 是    | 未知 |
| [猫头鹰宝](https://owlbot.info/)                  | 带有例句和照片的定义（如果有）       | `apiKey` | 是    | 是   |
| [牛津](https://developer.oxforddictionaries.com/) | 词典数据                             | `apiKey` | 是    | 没有 |
| [Wordnik](http://developer.wordnik.com)           | 词典数据                             | `apiKey` | 没有  | 未知 |
| [话](https://www.wordsapi.com/)                   | 超过 150,000 个单词的定义和同义词    | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 文件与生产力

| 火                                                                  | 描述                                                 | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------- | ---------------------------------------------------- | -------- | ----- | ---- |
| [Cloudmersive 文档和数据转换](https://cloudmersive.com/convert-api) | HTML / URL 到 PDF / PNG，Office 文档到 PDF，图像转换 | `apiKey` | 是    | 是   |
| [File.io](https://www.file.io)                                      | 文件共享                                             | 没有     | 是    | 未知 |
| [汞](https://mercury.postlight.com/web-parser/)                     | 网络解析器                                           | `apiKey` | 是    | 未知 |
| [pdflayer](https://pdflayer.com)                                    | HTML / URL 到 PDF                                    | `apiKey` | 是    | 未知 |
| [口袋](https://getpocket.com/developer/)                            | 书签服务                                             | `OAuth`  | 是    | 未知 |
| [PrexView](https://prexview.com)                                    | 数据从 XML 或 JSON 转换为 PDF，HTML 或图像           | `apiKey` | 是    | 未知 |
| [休息包](https://restpack.io/)                                      | 提供屏幕截图，HTML 到 PDF 以及内容提取 API           | `apiKey` | 是    | 未知 |
| [托多斯](https://developer.todoist.com)                             | 待办事项清单                                         | `OAuth`  | 是    | 未知 |
| [矢量表达](http://vector.express)                                   | 免费矢量文件转换 API                                 | 没有     | 没有  | 是   |
| [瓦卡时间](https://wakatime.com/developers)                         | 程序员的自动时间跟踪排行榜                           | 没有     | 是    | 未知 |
| [奇妙清单](https://developer.wunderlist.com/documentation)          | 待办事项清单                                         | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 环境

| 火                                                                                            | 描述                                    | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------------------------------- | --------------------------------------- | -------- | ----- | ---- |
| [空中视觉](https://airvisual.com/api)                                                         | 空气质量和天气数据                      | `apiKey` | 是    | 未知 |
| [Grünstrom 索引](https://www.corrently.de/hintergrund/gruenstromindex/index.html)             | 德国绿色力量指数（Grünstromindex/ GSI） | 没有     | 没有  | 是   |
| [OpenAQ](https://docs.openaq.org/)                                                            | 露天空气质量数据                        | `apiKey` | 是    | 未知 |
| [PM25.in](http://www.pm25.in/api_doc)                                                         | 中国空气质量                            | `apiKey` | 没有  | 未知 |
| [光伏瓦](https://developer.nrel.gov/docs/solar/pvwatts/v6/)                                   | 能源生产光伏（PV）能源系统              | `apiKey` | 是    | 未知 |
| [英国碳强度](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v1-0-0) | 国家电网开发的英国官方碳强度 API        | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 大事记

| 火                                                                                                                               | 描述                 | 验证码   | HTTPS | CORS |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------- | ----- | ---- |
| [Eventbrite](https://www.eventbrite.com/developer/v3/)                                                                           | 查找活动             | `OAuth`  | 是    | 未知 |
| [皮卡蒂奇](http://developer.picatic.com/?utm_medium=web&utm_source=github&utm_campaign=public-apis%20repo&utm_content=toddmotto) | 在任何地方卖票       | `apiKey` | 是    | 未知 |
| [票务主管](http://developer.ticketmaster.com/products-and-docs/apis/getting-started/)                                            | 搜索事件，景点或场所 | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 金融

| 火                                                         | 描述                                      | 验证码   | HTTPS | CORS |
| ---------------------------------------------------------- | ----------------------------------------- | -------- | ----- | ---- |
| [Alpha Vantage](https://www.alphavantage.co/)              | 实时和历史库存数据                        | `apiKey` | 是    | 未知 |
| [Barchart OnDemand](https://www.barchartondemand.com/free) | 股票，期货和外汇市场数据                  | `apiKey` | 是    | 未知 |
| [IEX 云](https://iexcloud.io/)                             | 实时和历史股票和市场数据                  | `apiKey` | 是    | 是   |
| [IG](https://labs.ig.com/gettingstarted)                   | 点差交易和差价合约市场数据                | `apiKey` | 是    | 未知 |
| [格子布](https://plaid.com/)                               | 连接用户的银行帐户并访问交易数据          | `apiKey` | 是    | 未知 |
| [Razorpay IFSC](https://ifsc.razorpay.com/)                | 印度金融系统代码（银行分支代码）          | 没有     | 是    | 未知 |
| [交易者](https://developer.tradier.com)                    | 美国股票/期权市场数据（延迟，盘中，历史） | `OAuth`  | 是    | 是   |
| [YNAB](https://api.youneedabudget.com/)                    | 预算与计划                                | `OAuth`  | 是    | 是   |

**[to 返回索引](#index)**

### 食物和饮料

| 火                                                                 | 描述                           | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------ | ------------------------------ | -------- | ----- | ---- |
| [毛丹](https://developer.edamam.com/)                              | 配方搜寻                       | `apiKey` | 是    | 未知 |
| [LCBO](https://lcboapi.com/)                                       | 醇                             | `apiKey` | 是    | 未知 |
| [打开啤酒厂数据库](https://www.openbrewerydb.org)                  | 啤酒厂，小百货和手工艺啤酒瓶店 | 没有     | 是    | 是   |
| [公开食物事实](https://world.openfoodfacts.org/data)               | 食品数据库                     | 没有     | 是    | 未知 |
| [朋克 API](https://punkapi.com/)                                   | Brewdog 啤酒食谱               | 没有     | 是    | 未知 |
| [食谱小狗](http://www.recipepuppy.com/about/api/)                  | 餐饮                           | 没有     | 没有  | 未知 |
| [TacoFancy](https://github.com/evz/tacofancy-api)                  | 社区驱动的炸玉米饼数据库       | 没有     | 没有  | 未知 |
| [本周报告](https://github.com/andyklimczak/TheReportOfTheWeek-API) | 餐饮评论                       | 没有     | 是    | 未知 |
| [鸡尾酒数据库](https://www.thecocktaildb.com/api.php)              | 鸡尾酒食谱                     | `apiKey` | 是    | 是   |
| [膳食数据库](https://www.themealdb.com/api.php)                    | 餐食谱                         | `apiKey` | 是    | 是   |
| [菜单上有什么？](http://nypl.github.io/menus-api/)                 | NYPL 人类转录的历史菜单集      | `apiKey` | 没有  | 未知 |
| [佐马托](https://developers.zomato.com/api)                        | 发现餐厅                       | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 游戏与漫画

| 火                                                             | 描述                                                             | 验证码          | HTTPS | CORS |
| -------------------------------------------------------------- | ---------------------------------------------------------------- | --------------- | ----- | ---- |
| [帝国时代 II](https://age-of-empires-2-api.herokuapp.com)      | 获取有关帝国时代 II 资源的信息                                   | 没有            | 是    | 未知 |
| [AmiiboAPI](http://www.amiiboapi.com/)                         | Amiibo 信息                                                      | 没有            | 没有  | 是   |
| [战网](https://dev.battle.net/)                                | 暴雪娱乐                                                         | `apiKey`        | 是    | 未知 |
| [查克·诺里斯数据库](http://www.icndb.com/api/)                 | 笑话                                                             | 没有            | 没有  | 未知 |
| [种族冲突](https://developer.clashofclans.com)                 | 部落冲突游戏信息                                                 | `apiKey`        | 是    | 未知 |
| [皇家冲突](https://developer.clashroyale.com)                  | 大逃杀游戏信息                                                   | `apiKey`        | 是    | 未知 |
| [漫画来了](https://comicvine.gamespot.com/api/documentation)   | 漫画                                                             | 没有            | 是    | 未知 |
| [卡片组](http://deckofcardsapi.com/)                           | 卡片组                                                           | 没有            | 没有  | 未知 |
| [命运游戏](https://github.com/Bungie-net/api)                  | Bungie 平台 API                                                  | `apiKey`        | 是    | 未知 |
| [刀塔 2](https://docs.opendota.com/)                           | 提供有关 Dota 2 的球员统计信息，比赛统计信息，排名的信息         | 没有            | 是    | 未知 |
| [龙与地下城](http://www.dnd5eapi.co/)                          | 第 5 版法术，类，怪物等的参考                                    | 没有            | 没有  | 没有 |
| [平安夜在线](https://esi.evetech.net/ui)                       | 第三方开发者文档                                                 | `OAuth`         | 是    | 未知 |
| [最终幻想十四](https://xivapi.com/)                            | 最终幻想 XIV 游戏数据 API                                        | 没有            | 是    | 是   |
| [堡垒之夜](https://fortnitetracker.com/site-api)               | Fortnite Stats                                                   | `apiKey`        | 是    | 未知 |
| [巨型炸弹](https://www.giantbomb.com/api/documentation)        | 视频游戏                                                         | 没有            | 是    | 未知 |
| [激战 2](https://wiki.guildwars2.com/wiki/API:Main)            | 激战 2 游戏信息                                                  | `apiKey`        | 是    | 未知 |
| [光环](https://developer.haloapi.com/)                         | 光晕 5 和光晕战争 2 信息                                         | `apiKey`        | 是    | 未知 |
| [炉石传说](http://hearthstoneapi.com/)                         | 炉石卡信息                                                       | `X-Mashape-Key` | 是    | 未知 |
| [超像素](https://api.hypixel.net/)                             | Hypixel 播放器统计                                               | `apiKey`        | 是    | 未知 |
| [IGDB.com](https://api.igdb.com/)                              | 电子游戏资料库                                                   | `apiKey`        | 是    | 未知 |
| [笑话 API](https://sv443.net/jokeapi)                          | 编程，其他笑话                                                   | 没有            | 是    | 是   |
| [笑话](https://github.com/15Dkatz/official_joke_api)           | 编程和一般笑话                                                   | 没有            | 是    | 未知 |
| [服务](http://jservice.io)                                     | 危险问题数据库                                                   | 没有            | 没有  | 未知 |
| [魔术聚会](http://magicthegathering.io/)                       | 魔术聚会游戏信息                                                 | 没有            | 没有  | 未知 |
| [奇迹](http://developer.marvel.com)                            | 漫威漫画                                                         | `apiKey`        | 没有  | 未知 |
| [模](https://docs.mod.io)                                      | 跨平台 Mod API                                                   | `apiKey`        | 是    | 未知 |
| [打开琐事](https://opentdb.com/api_config.php)                 | 琐事问题                                                         | 没有            | 是    | 未知 |
| [熊猫分数](https://pandascore.co)                              | 电子竞技游戏和结果                                               | `apiKey`        | 是    | 未知 |
| [PlayerUnknown 的战场](https://pubgtracker.com/site-api)       | PUBG 统计                                                        | `apiKey`        | 是    | 未知 |
| [博卡皮](https://pokeapi.co)                                   | 神奇宝贝信息                                                     | 没有            | 是    | 未知 |
| [神奇宝贝 TCG](https://pokemontcg.io)                          | 神奇宝贝 TCG 信息                                                | 没有            | 是    | 未知 |
| [里克和莫蒂](https://rickandmortyapi.com)                      | 所有瑞克和莫蒂信息，包括图像                                     | 没有            | 是    | 是   |
| [防暴游戏](https://developer.riotgames.com/)                   | 英雄联盟游戏信息                                                 | `apiKey`        | 是    | 未知 |
| [坠落](https://scryfall.com/docs/api)                          | 魔术：聚会数据库                                                 | 没有            | 是    | 是   |
| [蒸汽](https://developer.valvesoftware.com/wiki/Steam_Web_API) | Steam 客户端互动                                                 | `OAuth`         | 是    | 未知 |
| [超级英雄](https://superheroapi.com)                           | 单个 API 下来自所有 Universe 的所有 SuperHeroes 和 Villains 数据 | `apiKey`        | 是    | 未知 |
| [Tronald 转储](https://www.tronalddump.io/)                    | 唐纳德·特朗普曾经说过的最愚蠢的话                                | 没有            | 是    | 未知 |
| [Wargaming.net](https://developers.wargaming.net/)             | Wargaming.net 的信息和统计                                       | `apiKey`        | 是    | 没有 |
| [xkcd](https://xkcd.com/json.html)                             | 以 JSON 格式检索 XKCD 漫画                                       | 没有            | 是    | 没有 |

**[to 返回索引](#index)**

### 地理编码

| 火                                                                                                                     | 描述                                                               | 验证码   | HTTPS | CORS |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------- | ----- | ---- |
| [adresse.data.gouv.fr](https://adresse.data.gouv.fr)                                                                   | 法国的地址数据库，地理编码和反向                                   | 没有     | 是    | 未知 |
| [巴图塔](http://battuta.medunes.net)                                                                                   | （国家/地区/城市）级联位置 API                                     | `apiKey` | 没有  | 未知 |
| [必应地图](https://www.microsoft.com/maps/)                                                                            | 根据必应地图数据创建/自定义数字地图                                | `apiKey` | 是    | 未知 |
| [bng2latlong](https://www.getthedata.com/bng2latlong)                                                                  | 将东西向和北向的英国 OSGB36（英国国家网格）转换为 WGS84 经纬度     | 没有     | 是    | 是   |
| [市 SDK](http://www.citysdk.eu/citysdk-toolkit/)                                                                       | 针对某些欧洲城市的开放 API                                         | 没有     | 是    | 未知 |
| [达姆地图](http://apis.map.daum.net/)                                                                                  | Daum Maps 为韩国地图提供了多个 API                                 | `apiKey` | 没有  | 未知 |
| [FreeGeoIP](https://freegeoip.app/)                                                                                    | 免费的地理 IP 信息，无需注册。 15k /小时的速率限制                 | 没有     | 是    | 是   |
| [GeoApi](https://api.gouv.fr/api/geoapi.html)                                                                          | 法国地理资料                                                       | 没有     | 是    | 未知 |
| [Geocod.io](https://www.geocod.io/)                                                                                    | 批量地址地理编码/反向地理编码                                      | `apiKey` | 是    | 未知 |
| [Geocode.xyz](https://geocode.xyz/)                                                                                    | 提供全球正向/反向地理编码，批处理地理编码和地理解析                | 没有     | 是    | 未知 |
| [GeoDataSource](https://www.geodatasource.com/web-service)                                                             | 使用纬度和经度坐标对城市名称进行地理编码                           | `apiKey` | 是    | 未知 |
| [GeoJS](https://geojs.io/)                                                                                             | 与 ChatOps 集成的 IP 地理位置                                      | 没有     | 是    | 是   |
| [地名](http://www.geonames.org/export/web-services.html)                                                               | 地名和其他地理数据                                                 | 没有     | 没有  | 未知 |
| [geoPlugin](https://www.geoplugin.com)                                                                                 | IP 地理位置和货币换算                                              | 没有     | 是    | 是   |
| [Google Earth Engine](https://developers.google.com/earth-engine/)                                                     | 基于云的行星级环境数据分析平台                                     | `apiKey` | 是    | 未知 |
| [谷歌地图](https://developers.google.com/maps/)                                                                        | 根据 Google 地图数据创建/自定义数字地图                            | `apiKey` | 是    | 未知 |
| [你好萨鲁特](https://www.fourtonfish.com/hellosalut/hello/)                                                            | 根据用户语言获取问候语翻译                                         | 没有     | 是    | 未知 |
| [这里地图](https://developer.here.com)                                                                                 | 根据 HERE Maps 数据创建/自定义数字地图                             | `apiKey` | 是    | 未知 |
| [印度城市](https://indian-cities-api-nocbegfhqg.now.sh/)                                                               | 以干净的 JSON 格式获取所有印度城市                                 | 没有     | 是    | 是   |
| [IP 2 国家](https://ip2country.info)                                                                                   | 将 IP 映射到国家                                                   | 没有     | 是    | 未知 |
| [IP 地址详细信息](https://ipinfo.io/)                                                                                  | 使用 IP 地址查找地理位置                                           | 没有     | 是    | 未知 |
| [IP 位置](http://ip-api.com/)                                                                                          | 使用 IP 地址查找位置                                               | 没有     | 没有  | 未知 |
| [IP 位置](https://ipapi.co/)                                                                                           | 查找 IP 地址位置信息                                               | 没有     | 是    | 未知 |
| [IP 伙伴](https://ipsidekick.com)                                                                                      | 地理位置 API，可返回有关 IP 地址的其他信息                         | `apiKey` | 是    | 未知 |
| [知识产权警卫队](https://www.ipvigilante.com/)                                                                         | 免费的 IP 地理位置 API                                             | 没有     | 是    | 未知 |
| [IP2 位置](https://www.ip2location.com/web-service/ip2location)                                                        | IP 地理位置 Web 服务可获取 55 个以上的参数                         | `apiKey` | 是    | 未知 |
| [IP2 代理](https://www.ip2location.com/web-service/ip2proxy)                                                           | 使用 IP 地址检测代理和 VPN                                         | `apiKey` | 是    | 未知 |
| [IPGeolocationAPI.com](https://ipgeolocationapi.com/)                                                                  | 通过 IP 查找您的访客并提供国家/地区详细信息                        | 没有     | 是    | 是   |
| [IP 信息数据库](https://ipinfodb.com/api)                                                                              | 免费的地理定位工具和 API，用于按 IP 地址查找国家，地区，城市和时区 | `apiKey` | 是    | 未知 |
| [ipstack](https://ipstack.com/)                                                                                        | 通过 IP 地址找到并识别网站访问者                                   | `apiKey` | 是    | 未知 |
| [克鲁维网络](https://www.kwelo.com/network/ip-address)                                                                 | 找到并获取有关 IP 地址的详细信息                                   | 没有     | 是    | 是   |
| [LocationIQ](https://locationiq.org/docs/)                                                                             | 提供正向/反向地理编码和批处理地理编码                              | `apiKey` | 是    | 是   |
| [地图框](https://www.mapbox.com/developers/)                                                                           | 创建/自定义精美的数字地图                                          | `apiKey` | 是    | 未知 |
| [墨西哥](https://github.com/IcaliaLabs/sepomex)                                                                        | 墨西哥 RESTful 邮政编码 API                                        | 没有     | 是    | 未知 |
| [新加坡一地图](https://docs.onemap.sg/)                                                                                | 新加坡土地管理局针对新加坡地址的 REST API 服务                     | `apiKey` | 是    | 未知 |
| [在水上](https://onwater.io/)                                                                                          | 确定纬度/经度是否在水上或陆地上                                    | 没有     | 是    | 未知 |
| [开笼](https://opencagedata.com)                                                                                       | 使用开放数据进行正向和反向地理编码                                 | `apiKey` | 是    | 是   |
| [OpenStreetMap](http://wiki.openstreetmap.org/wiki/API)                                                                | 导航，地理位置和地理数据                                           | `OAuth`  | 没有  | 未知 |
| [PostcodeData.nl](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) | 根据荷兰地址的邮政编码提供地理位置数据                             | 没有     | 没有  | 未知 |
| [Postcodes.io](https://postcodes.io)                                                                                   | 英国的邮政编码查找和地理位置                                       | 没有     | 是    | 是   |
| [REST 国家](https://restcountries.eu)                                                                                  | 通过 RESTful API 获取有关国家的信息                                | 没有     | 是    | 未知 |
| [Uebermaps](https://uebermaps.com/api/v2)                                                                              | 与朋友发现并分享地图                                               | `apiKey` | 是    | 未知 |
| [美国邮政编码](https://smartystreets.com/docs/cloud/us-zipcode-api)                                                    | 验证并附加任何美国邮政编码的数据                                   | `apiKey` | 是    | 是   |
| [犹他州 AGRC](https://api.mapserv.utah.gov)                                                                            | 犹他州 Web API，用于对犹他州地址进行地理编码                       | `apiKey` | 是    | 未知 |
| [ViaCep](https://viacep.com.br)                                                                                        | 巴西 RESTful 邮政编码 API                                          | 没有     | 是    | 未知 |
| [ZipCodeAPI](https://www.zipcodeapi.com)                                                                               | 美国邮政编码的距离，半径和位置 API                                 | `apiKey` | 是    | 未知 |
| [Zippopotam](http://www.zippopotam.us)                                                                                 | 获取有关国家/地区，城市，州等地点的信息                            | 没有     | 没有  | 未知 |

**[to 返回索引](#index)**

### 政府

| 火                                                                          | 描述                                                        | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------------- | ----------------------------------------------------------- | -------- | ----- | ---- |
| [BCLaws](http://www.bclaws.ca/civix/template/complete/api/index.html)       | 查阅不列颠哥伦比亚省的法律                                  | 没有     | 没有  | 未知 |
| [美国商业](https://business.usa.gov/developer)                              | 有关美国计划，活动，服务等的权威信息                        | `apiKey` | 是    | 未知 |
| [人口普查](https://www.census.gov/data/developers/data-sets.html)           | 美国人口普查局提供有关人口统计和企业的各种 API 和数据集     | 没有     | 是    | 未知 |
| [里昂市 Opendata](https://data.beta.grandlyon.com/fr/accueil)               | 里昂市公开数据                                              | `apiKey` | 是    | 未知 |
| [南特市 Opendata](https://data.nantesmetropole.fr/pages/home/)              | 南特（法国）城市开放数据                                    | `apiKey` | 是    | 未知 |
| [布拉格市 Opendata](http://opendata.praha.eu/en)                            | 布拉格（CZ）城市开放数据                                    | 没有     | 没有  | 未知 |
| [Code.gov](https://code.gov)                                                | 美国联邦政府开放源代码共享的主要平台                        | `apiKey` | 是    | 未知 |
| [科罗拉多数据引擎](http://codataengine.org/)                                | 格式化和地理定位的科罗拉多州公共数据                        | 没有     | 是    | 未知 |
| [科罗拉多信息市场](https://data.colorado.gov/)                              | 科罗拉多州政府公开数据                                      | 没有     | 是    | 未知 |
| [美国日期](https://datausa.io/about/api/)                                   | 美国公共数据                                                | 没有     | 是    | 未知 |
| [Data.gov](https://api.data.gov/)                                           | 美国政府数据                                                | `apiKey` | 是    | 未知 |
| [Data.parliament.uk](http://www.data.parliament.uk/developers/)             | 包含实时数据集，包括有关请愿，账单，议员投票，出勤等信息    | 没有     | 没有  | 未知 |
| [哥伦比亚特区开放数据](http://opendata.dc.gov/pages/using-apis)             | 包含哥伦比亚特区政府的公共数据集，包括犯罪，GIS，财务数据等 | 没有     | 是    | 未知 |
| [环保局](https://developer.epa.gov/category/apis/)                          | 来自美国环境保护局的 Web 服务和数据集                       | 没有     | 是    | 未知 |
| [前向纠错](https://api.open.fec.gov/developers/)                            | 有关联邦选举中竞选捐款的信息                                | `apiKey` | 是    | 未知 |
| [联邦公报](https://www.federalregister.gov/reader-aids/developer-resources) | 美国政府日报                                                | 没有     | 是    | 未知 |
| [食品标准局](http://ratings.food.gov.uk/open-data/en-GB)                    | 英国食品卫生等级数据 API                                    | 没有     | 没有  | 未知 |
| [澳大利亚公开政府](https://www.data.gov.au/)                                | 澳大利亚政府公开数据                                        | 没有     | 是    | 未知 |
| [比利时公开政府](https://data.gov.be/)                                      | 比利时政府公开数据                                          | 没有     | 是    | 未知 |
| [加拿大公开政府](http://open.canada.ca/en)                                  | 加拿大政府公开数据                                          | 没有     | 没有  | 未知 |
| [法国公开政府](https://www.data.gouv.fr/)                                   | 法国政府公开数据                                            | `apiKey` | 是    | 未知 |
| [印度公开政府](https://data.gov.in/)                                        | 印度政府公开数据                                            | `apiKey` | 是    | 未知 |
| [意大利公开政府](https://www.dati.gov.it/)                                  | 意大利政府公开数据                                          | 没有     | 是    | 未知 |
| [新西兰公开政府](https://www.data.govt.nz/)                                 | 新西兰政府公开数据                                          | 没有     | 是    | 未知 |
| [罗马尼亚公开政府](http://data.gov.ro/)                                     | 罗马尼亚政府公开数据                                        | 没有     | 没有  | 未知 |
| [台湾公开政府](https://data.gov.tw/)                                        | 台湾政府公开资料                                            | 没有     | 是    | 未知 |
| [美国公开政府](https://www.data.gov/)                                       | 美国政府公开数据                                            | 没有     | 是    | 未知 |
| [法规网](https://regulationsgov.github.io/developers/)                      | 联邦法规材料，以增进对联邦法规制定过程的了解                | `apiKey` | 是    | 未知 |
| [由北方开放代表](https://represent.opennorth.ca/)                           | 寻找加拿大政府代表                                          | 没有     | 是    | 未知 |
| [USAspending.gov](https://api.usaspending.gov/)                             | 美国联邦支出数据                                            | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 健康

| 火                                                          | 描述                                                                   | 验证码   | HTTPS | CORS |
| ----------------------------------------------------------- | ---------------------------------------------------------------------- | -------- | ----- | ---- |
| [更好的医生](https://developer.betterdoctor.com/)           | 有关您所在地区医生的详细信息                                           | `apiKey` | 是    | 未知 |
| [新冠肺炎](https://covid19api.com/)                         | Covid 19 的传播，感染和恢复                                            | 没有     | 是    | 是   |
| [糖尿病](http://predictbgl.com/api/)                        | 记录和检索糖尿病信息                                                   | 没有     | 没有  | 未知 |
| [Flutrack](http://www.flutrack.org/)                        | 地理追踪的流感样症状                                                   | 没有     | 没有  | 未知 |
| [Healthcare.gov](https://www.healthcare.gov/developers/)    | 关于美国健康保险市场的教育内容                                         | 没有     | 是    | 未知 |
| [语法](https://docs.lexigram.io/v1/welcome)                 | NLP 从文本中提取对临床概念的提及，可以访问临床本体                     | `apiKey` | 是    | 未知 |
| [补偿](http://makeup-api.herokuapp.com/)                    | 化妆信息                                                               | 没有     | 没有  | 未知 |
| [医疗保险](https://data.medicare.gov/developers)            | 从 CMS 访问数据-medicare.gov                                           | 没有     | 是    | 未知 |
| [核电厂](https://npiregistry.cms.hhs.gov/registry/help-api) | 国家计划和医疗服务提供方列举系统，有关在美国注册的医疗服务提供方的信息 | 没有     | 是    | 未知 |
| [营养 ix](https://developer.nutritionix.com/)               | 世界上最大的经过验证的营养数据库                                       | `apiKey` | 是    | 未知 |
| [开放 FDA](https://open.fda.gov)                            | FDA 关于药物，设备和食品的公开数据                                     | 没有     | 是    | 未知 |
| [USDA 营养素](https://fdc.nal.usda.gov/)                    | 国家营养数据库标准参考                                                 | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 工作

| 火                                                                                    | 描述                     | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------------------------- | ------------------------ | -------- | ----- | ---- |
| [阿祖纳](https://developer.adzuna.com/overview)                                       | 工作板聚合器             | `apiKey` | 是    | 未知 |
| [职业喷气](https://www.careerjet.com/partners/api/)                                   | 求职引擎                 | `apiKey` | 没有  | 未知 |
| [Github 乔布斯](https://jobs.github.com/api)                                          | 软件开发人员的工作       | 没有     | 是    | 是   |
| [GraphQL 作业](https://api.graphql.jobs)                                              | GraphQL 的工作           | 没有     | 是    | 是   |
| [确实](https://www.indeed.com/publisher)                                              | 工作板聚合器             | `apiKey` | 是    | 未知 |
| [招聘职位](http://api.jobs2careers.com/api/spec.pdf)                                  | 工作汇总器               | `apiKey` | 是    | 未知 |
| [乔布](https://us.jooble.org/api/about)                                               | 求职引擎                 | `apiKey` | 是    | 未知 |
| [枣](http://www.juju.com/publisher/spec/)                                             | 求职引擎                 | `apiKey` | 没有  | 未知 |
| [开放技能](https://github.com/workforce-data-initiative/skills-api/wiki/API-Overview) | 职位，技能和相关职位数据 | 没有     | 没有  | 未知 |
| [芦苇](https://www.reed.co.uk/developers)                                             | 工作板聚合器             | `apiKey` | 是    | 未知 |
| [缪斯](https://www.themuse.com/developers/api/v2)                                     | 工作委员会和公司简介     | `apiKey` | 是    | 未知 |
| [上班](https://developers.upwork.com/)                                                | 自由职业委员会和管理系统 | `OAuth`  | 是    | 未知 |
| [美国乔布斯](https://developer.usajobs.gov/)                                          | 美国政府工作委员会       | `apiKey` | 是    | 未知 |
| [邮递员](https://www.ziprecruiter.com/publishers)                                     | 求职应用和网站           | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 机器学习

| 火                                                                                | 描述                          | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------------------- | ----------------------------- | -------- | ----- | ---- |
| [克拉里菲](https://developer.clarifai.com/)                                       | 计算机视觉                    | `OAuth`  | 是    | 未知 |
| [Cloudmersive](https://www.cloudmersive.com/image-recognition-and-processing-api) | 图像字幕，人脸识别，NSFW 分类 | `apiKey` | 是    | 是   |
| [深码](https://www.deepcode.ai/docs/Overview%252FOverview)                        | 人工智能进行代码审查          | 没有     | 是    | 未知 |
| [对话流程](https://dialogflow.com)                                                | 自然语言处理                  | `apiKey` | 是    | 未知 |
| [肯·艾欧（Keen IO）](https://keen.io/)                                            | 数据分析                      | `apiKey` | 是    | 未知 |
| [Sentim-API](https://sentim-api.herokuapp.com)                                    | 文字情感分析                  | 没有     | 是    | 是   |
| [时间门](https://timedoor.io)                                                     | 时间序列分析 API              | `apiKey` | 是    | 是   |
| [拔掉](https://unplu.gg/test_api.html)                                            | 时间序列数据的预测 API        | `apiKey` | 是    | 未知 |
| [威特](https://wit.ai/)                                                           | 自然语言处理                  | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 音乐

| 火                                                                                                             | 描述                                                   | 验证码   | HTTPS | CORS |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------- | ----- | ---- |
| [AI 掌握](https://aimastering.com/api_docs/)                                                                   | 自动化音乐掌握                                         | `apiKey` | 是    | 是   |
| [Bandsintown](https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0)                                     | 音乐活动                                               | 没有     | 是    | 未知 |
| [迪泽](https://developers.deezer.com/api)                                                                      | 音乐                                                   | `OAuth`  | 是    | 未知 |
| [Discogs](https://www.discogs.com/developers/)                                                                 | 音乐                                                   | `OAuth`  | 是    | 未知 |
| [天才](https://docs.genius.com/)                                                                               | 众包歌词和音乐知识                                     | `OAuth`  | 是    | 未知 |
| [绅士](https://binaryjazz.us/genrenator-api/)                                                                  | 音乐流派发生器                                         | 没有     | 是    | 未知 |
| [iTunes 搜索](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) | 软件产品                                               | 没有     | 是    | 未知 |
| [贾门多](https://developer.jamendo.com/v3.0/docs)                                                              | 音乐                                                   | `OAuth`  | 是    | 未知 |
| [KKBOX](https://developer.kkbox.com)                                                                           | 获取音乐库，播放列表，图表，并在 KKBOX 平台上进行表演  | `OAuth`  | 是    | 未知 |
| [LastFm](https://www.last.fm/api)                                                                              | 音乐                                                   | `apiKey` | 是    | 未知 |
| [歌词库](http://docs.lyricsovh.apiary.io/)                                                                     | 简单的 API 检索歌曲的歌词                              | 没有     | 是    | 未知 |
| [混合云](https://www.mixcloud.com/developers/)                                                                 | 音乐                                                   | `OAuth`  | 是    | 是   |
| [音乐脑](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2)                                    | 音乐                                                   | 没有     | 是    | 未知 |
| [Musixmatch](https://developer.musixmatch.com/)                                                                | 音乐                                                   | `apiKey` | 是    | 未知 |
| [Openwhyd](https://openwhyd.github.io/openwhyd/API)                                                            | 下载流媒体轨道的精选播放列表（YouTube，SoundCloud 等） | `No`     | 是    | 没有 |
| [搜索](https://searchly.asuarez.dev/docs/v1)                                                                   | 基于歌曲歌词的相似度搜索                               | 没有     | 是    | 未知 |
| [颂歌](https://www.songkick.com/developer/)                                                                    | 音乐活动                                               | `OAuth`  | 是    | 未知 |
| [宋斯特](https://www.songsterr.com/a/wa/api/)                                                                  | 提供吉他，贝斯和鼓的乐谱和和弦                         | 没有     | 是    | 未知 |
| [声云](https://developers.soundcloud.com/)                                                                     | 允许用户上传和共享声音                                 | `OAuth`  | 是    | 未知 |
| [Spotify](https://beta.developer.spotify.com/documentation/web-api/)                                           | 查看 Spotify 音乐目录，管理用户的音乐库，获取建议等    | `OAuth`  | 是    | 未知 |
| [品味潜水](https://tastedive.com/read/api)                                                                     | 相似的艺术家 API（也适用于电影和电视节目）             | `apiKey` | 是    | 未知 |
| [音频数据库](https://www.theaudiodb.com/api_guide.php)                                                         | 音乐                                                   | `apiKey` | 是    | 未知 |
| [萤火虫](https://api.vagalume.com.br/docs/)                                                                    | 众包歌词和音乐知识                                     | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 新闻

| 火                                                         | 描述                                         | 验证码   | HTTPS | CORS |
| ---------------------------------------------------------- | -------------------------------------------- | -------- | ----- | ---- |
| [美联社](https://developer.ap.org/)                        | 从美联社搜索新闻和元数据                     | `apiKey` | 是    | 未知 |
| [编年史美国](http://chroniclingamerica.loc.gov/about/api/) | 可从国会图书馆访问数百万页的美国历史报纸     | 没有     | 没有  | 未知 |
| [潮流](https://currentsapi.services/)                      | 在各种新闻来源，博客和论坛中发布的最新新闻   | `apiKey` | 是    | 是   |
| [饲料箱](https://github.com/feedbin/feedbin-api)           | RSS 阅读器                                   | `OAuth`  | 是    | 未知 |
| [纽约时报](https://developer.nytimes.com/)                 | 提供新闻                                     | `apiKey` | 是    | 未知 |
| [新闻](https://newsapi.org/)                               | 当前在各种新闻来源和博客上发布的头条新闻     | `apiKey` | 是    | 未知 |
| [NPR 一](http://dev.npr.org/api/)                          | NPR 的个性化新闻收听体验                     | `OAuth`  | 是    | 未知 |
| [守护者](http://open-platform.theguardian.com/)            | 访问监护人创建的所有内容（按标签和部分分类） | `apiKey` | 是    | 未知 |
| [老读者](https://github.com/theoldreader/api)              | RSS 阅读器                                   | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 公开资料

| 火                                                                    | 描述                                                          | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------- | ------------------------------------------------------------- | -------- | ----- | ---- |
| [18 楼](http://18f.github.io/API-All-the-X/)                          | 非官方的美国联邦政府 API 开发                                 | 没有     | 没有  | 未知 |
| [Archive.org](https://archive.readme.io/docs)                         | 互联网档案馆                                                  | 没有     | 是    | 未知 |
| [卫星](https://datos.arsat.com.ar/developers/)                        | ARSAT 公共数据                                                | `apiKey` | 是    | 未知 |
| [Callook.info](https://callook.info)                                  | 美国火腿无线电呼号                                            | 没有     | 是    | 未知 |
| [卡托](https://carto.com/)                                            | 位置信息预测                                                  | `apiKey` | 是    | 未知 |
| [公民饲料](https://developers.civicfeed.com/)                         | 新闻文章和公共数据集                                          | `apiKey` | 是    | 未知 |
| [谜公众](http://docs.enigma.com/public/public_v20_api_about)          | 最广泛的公共数据收集                                          | `apiKey` | 是    | 是   |
| [FonoApi](https://fonoapi.freshpixl.com/)                             | 行动装置说明                                                  | 没有     | 是    | 未知 |
| [法语地址搜索](https://geo.api.gouv.fr/adresse)                       | 通过法国政府进行地址搜索                                      | 没有     | 是    | 未知 |
| [链接预览](https://www.linkpreview.net)                               | 获取任何请求的 URL 的 JSON 格式的摘要以及标题，描述和预览图像 | `apiKey` | 是    | 是   |
| [大麻菌株](http://strains.evanbusse.com/)                             | 大麻菌株，种族，风味和功效                                    | `apiKey` | 没有  | 未知 |
| [微链接](https://microlink.io)                                        | 从任何网站提取结构化数据                                      | 没有     | 是    | 是   |
| [开放企业](http://api.opencorporates.com/documentation/API-Reference) | 有关许多国家的公司实体和董事的数据                            | `apiKey` | 是    | 未知 |
| [数量](https://www.quandl.com/)                                       | 股市数据                                                      | 没有     | 是    | 未知 |
| [娱乐信息数据库](https://ridb.recreation.gov/)                        | 休闲区，联邦土地，历史遗迹，博物馆和其他景点/资源（美国）     | `apiKey` | 是    | 未知 |
| [舀](http://www.scoop.it/dev)                                         | 内容策划服务                                                  | `apiKey` | 没有  | 未知 |
| [传送](https://developers.teleport.org/)                              | 生活质量数据                                                  | 没有     | 是    | 未知 |
| [大学名单](https://github.com/Hipo/university-domains-list)           | 大学名称，国家和地区                                          | 没有     | 是    | 未知 |
| [奥斯陆大学](https://data.uio.no/)                                    | 奥斯陆大学（挪威）的课程，讲座视频，课程的详细信息等          | 没有     | 是    | 未知 |
| [UPC 数据库](https://upcdatabase.org/api)                             | 来自世界各地的超过 150 万条条形码                             | `apiKey` | 是    | 未知 |
| [维基数据](https://www.wikidata.org/w/api.php?action=help)            | 由 Wikimedia 基金会运营的经过协作编辑的知识库                 | `OAuth`  | 是    | 未知 |
| [维基百科](https://www.mediawiki.org/wiki/API:Main_page)              | Mediawiki 百科全书                                            | 没有     | 是    | 未知 |
| [喊叫](https://www.yelp.com/developers/documentation/v3)              | 寻找本地商家                                                  | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 开源项目

| 火                                                      | 描述           | 验证码   | HTTPS | CORS |
| ------------------------------------------------------- | -------------- | -------- | ----- | ---- |
| [伯爵](https://api.count.ly/reference)                  | 大量的网络分析 | 没有     | 没有  | 未知 |
| [Drupal.org](https://www.drupal.org/drupalorg/docs/api) | Drupal.org     | 没有     | 是    | 未知 |
| [邪恶侮辱发生器](https://evilinsult.com/api)            | 邪恶的侮辱     | 没有     | 是    | 是   |
| [图书馆](https://libraries.io/api)                      | 开源软件库     | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 专利

| 火                                                                                    | 描述                 | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------------------------- | -------------------- | -------- | ----- | ---- |
| [欧洲专利局](https://developers.epo.org/)                                             | 欧洲专利检索系统 API | `OAuth`  | 是    | 未知 |
| [类](https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00)           | 台湾专利检索系统 API | `apiKey` | 是    | 未知 |
| [美国专利商标局](https://www.uspto.gov/learning-and-resources/open-data-and-mobility) | 美国专利 API 服务    | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 个性

| 火                                                              | 描述                                      | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------- | ----------------------------------------- | -------- | ----- | ---- |
| [通知单](http://api.adviceslip.com/)                            | 生成随机建议单                            | 没有     | 是    | 未知 |
| [chucknorris.io](https://api.chucknorris.io)                    | 手工策划的 Chuck Norris 笑话的 JSON API   | 没有     | 是    | 未知 |
| [FavQs.com](https://favqs.com/api)                              | FavQs 允许您收集，发现和分享您喜欢的报价  | `apiKey` | 是    | 未知 |
| [福阿斯](http://www.foaas.com/)                                 | 他妈的服务                                | 没有     | 没有  | 未知 |
| [取笑](http://forismatic.com/en/api/)                           | 励志名言                                  | 没有     | 没有  | 未知 |
| [伊坎哈兹达乔克](https://icanhazdadjoke.com/api)                | 互联网上最多的爸爸笑话                    | 没有     | 是    | 未知 |
| [kanye.rest](https://kanye.rest)                                | REST API 随机引用 Kanye West 报价         | 没有     | 是    | 是   |
| [中](https://github.com/Medium/medium-api-docs)                 | 提供独特观点观点的读者和作家社区          | `OAuth`  | 是    | 未知 |
| [NaMoMemes](https://github.com/theIYD/NaMoMemes)                | 模因                                      | 没有     | 是    | 未知 |
| [编程引号](https://github.com/skolakoda/programming-quotes-api) | 开源项目的 Programming Quotes API         | 没有     | 是    | 未知 |
| [报价花园](https://pprathameshmore.github.io/QuoteGarden/)      | REST API 包含 5000 多个著名的引号         | 没有     | 是    | 未知 |
| [设计报价](https://quotesondesign.com/api/)                     | 励志名言                                  | 没有     | 是    | 未知 |
| [特质化](https://app.traitify.com/developer)                    | 评估，收集和分析人格                      | 没有     | 是    | 未知 |
| [tronalddump.io](https://www.tronalddump.io)                    | Api 和网络存档，了解唐纳德·特朗普所说的话 | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 摄影

| 火                                                   | 描述                               | 验证码   | HTTPS | CORS |
| ---------------------------------------------------- | ---------------------------------- | -------- | ----- | ---- |
| [Flickr](https://www.flickr.com/services/api/)       | Flickr 服务                        | `OAuth`  | 是    | 未知 |
| [盖蒂图片社](http://developers.gettyimages.com/en/)  | 使用世界上最强大的图像构建应用程序 | `OAuth`  | 是    | 未知 |
| [Gfycat](https://developers.gfycat.com/api/)         | 吉菲尔 GIF                         | `OAuth`  | 是    | 未知 |
| [吉菲](https://developers.giphy.com/docs/)           | 获取所有的 GIF                     | `apiKey` | 是    | 未知 |
| [贾佐](https://gyazo.com/api/docs)                   | 上传图片                           | `apiKey` | 是    | 未知 |
| [伊姆古尔](https://apidocs.imgur.com/)               | 图片                               | `OAuth`  | 是    | 未知 |
| [lorem 图片](https://picsum.photos/)                 | 来自 Unsplash 的图像               | 没有     | 是    | 未知 |
| [像素](https://www.pexels.com/api/)                  | 免费图片和视频                     | `apiKey` | 是    | 是   |
| [Pixabay](https://pixabay.com/sk/service/about/api/) | 摄影                               | `apiKey` | 是    | 未知 |
| [小猫咪](https://placekitten.com/)                   | 可调整大小的小猫占位符图像         | 没有     | 是    | 未知 |
| [ScreenShotLayer](https://screenshotlayer.com)       | URL 2 图片                         | 没有     | 是    | 未知 |
| [不飞溅](https://unsplash.com/developers)            | 摄影                               | `OAuth`  | 是    | 未知 |
| [Wallhav](https://wallhaven.cc/help/api)             | 墙纸                               | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 科学与数学

| 火                                                                         | 描述                                            | 验证码   | HTTPS | CORS |
| -------------------------------------------------------------------------- | ----------------------------------------------- | -------- | ----- | ---- |
| [arcsecond.io](https://api.arcsecond.io/)                                  | 多个天文学数据源                                | 没有     | 是    | 未知 |
| [核心](https://core.ac.uk/services#api)                                    | 访问世界上的 Open Access 研究论文               | `apiKey` | 是    | 未知 |
| [GBIF](http://api.gbif.org/v1/)                                            | 全球生物多样性信息设施                          | 没有     | 是    | 是   |
| [iDigBio](https://github.com/idigbio/idigbio-search-api/wiki)              | 获取来自世界各地组织的数百万个博物馆标本        | 没有     | 是    | 未知 |
| [inspirehep.net](https://inspirehep.net/info/hep/api?ln=en)                | 高能物理信息。系统                              | 没有     | 是    | 未知 |
| [它是](https://www.itis.gov/ws_description.html)                           | 综合生物分类信息系统                            | 没有     | 是    | 未知 |
| [启动库](https://launchlibrary.net/docs/1.3/api.html)                      | 即将发射的太空                                  | 没有     | 是    | 未知 |
| [小行星中心](http://www.asterank.com/mpc)                                  | Asterank.com 信息                               | 没有     | 没有  | 未知 |
| [美国宇航局](https://api.nasa.gov)                                         | NASA 数据，包括图像                             | 没有     | 是    | 未知 |
| [NASA APOD（非官方 API）](https://apodapi.herokuapp.com/)                  | 用于获取 APOD（每日天文图像）图像和元数据的 API | 没有     | 是    | 是   |
| [牛顿](https://newton.now.sh/)                                             | 符号和算术数学计算器                            | 没有     | 是    | 未知 |
| [号码](http://numbersapi.com)                                              | 关于数字的事实                                  | 没有     | 没有  | 未知 |
| [开启通知](http://open-notify.org/Open-Notify-API/)                        | ISS 宇航员，当前位置等                          | 没有     | 没有  | 未知 |
| [开放科学框架](https://developer.osf.io)                                   | 研究设计，研究材料，数据，手稿等的资料库和档案  | 没有     | 是    | 未知 |
| [分享](https://share.osf.io/api/v2/)                                       | 关于研究和学术活动的免费，开放的数据集          | 没有     | 是    | 未知 |
| [太空 X](https://github.com/r-spacex/SpaceX-API)                           | 公司，车辆，发射台和发射数据                    | 没有     | 是    | 未知 |
| [日出和日落](https://sunrise-sunset.org/api)                               | 给定纬度和经度的日落和日出时间                  | 没有     | 是    | 未知 |
| [三叶草](https://trefle.io/)                                               | 植物物种的植物数据                              | `apiKey` | 是    | 未知 |
| [USGS 地震危害计划](https://earthquake.usgs.gov/fdsnws/event/1/)           | 实时地震数据                                    | 没有     | 是    | 未知 |
| [USGS 供水服务](https://waterservices.usgs.gov/)                           | 河流和湖泊的水质和水位信息                      | 没有     | 是    | 未知 |
| [世界银行](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) | 世界数据                                        | 没有     | 没有  | 未知 |

**[to 返回索引](#index)**

### 安全

| 火                                                                          | 描述                                                     | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------------- | -------------------------------------------------------- | -------- | ----- | ---- |
| [Censys.io](https://censys.io/api)                                          | 互联网连接的主机和设备的搜索引擎                         | `apiKey` | 是    | 没有 |
| [CRXcavator](https://crxcavator.io/apidocs)                                 | Chrome 扩展程序风险评分                                  | `apiKey` | 是    | 未知 |
| [筛选清单](https://filterlists.com)                                         | adblocker 和防火墙的过滤器列表                           | 没有     | 是    | 未知 |
| [欺诈实验室专业版](https://www.fraudlabspro.com/developer/api/screen-order) | 使用 AI 筛选订单信息以检测欺诈                           | `apiKey` | 是    | 未知 |
| [HaveIBeenPwned](https://haveibeenpwned.com/API/v3)                         | 以前在数据泄露中公开的密码                               | `apiKey` | 是    | 未知 |
| [国家漏洞数据库](https://nvd.nist.gov/vuln/Data-Feeds/JSON-feed-changelog)  | 美国国家漏洞数据库                                       | 没有     | 是    | 未知 |
| [安全足迹](https://securitytrails.com/corp/apidocs)                         | 与域和 IP 相关的信息，例如当前和历史的 WHOIS 和 DNS 记录 | `apiKey` | 是    | 未知 |
| [Shodan](https://developer.shodan.io/)                                      | 互联网连接设备的搜索引擎                                 | `apiKey` | 是    | 未知 |
| [英国警察](https://data.police.uk/docs/)                                    | 英国警察数据                                             | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 购物

| 火                                                                  | 描述                                   | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------------- | -------------------------------------- | -------- | ----- | ---- |
| [百思买](https://bestbuyapis.github.io/api-documentation/#overview) | 产品，购买选项，类别，推荐，商店和商业 | `apiKey` | 是    | 未知 |
| [Bratabase](https://developers.bratabase.com/)                      | 不同类型文胸尺寸的数据库               | `OAuth`  | 是    | 未知 |
| [易趣](https://go.developer.ebay.com/)                              | 在 eBay 上买卖                         | `OAuth`  | 是    | 未知 |
| [沃尔玛](https://developer.walmartlabs.com/docs)                    | 物品价格和可用性                       | `apiKey` | 是    | 未知 |
| [韦格曼斯](https://dev.wegmans.io)                                  | 韦格曼食品市场                         | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**

### 社会的

| 火                                                              | 描述                                                                   | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------- | ---------------------------------------------------------------------- | -------- | ----- | ---- |
| [缓冲](https://buffer.com/developers/api)                       | 访问缓冲区中的待处理和已发送的更新                                     | `OAuth`  | 是    | 未知 |
| [思科 Spark](https://developer.ciscospark.com)                  | 团队协作软件                                                           | `OAuth`  | 是    | 未知 |
| [不和谐](https://discordapp.com/developers/docs/intro)          | 为 Discord 制作机器人，将 Discord 集成到外部平台上                     | `OAuth`  | 是    | 未知 |
| [领英](https://disqus.com/api/docs/auth/)                       | 与 Disqus 数据通信                                                     | `OAuth`  | 是    | 未知 |
| [脸书](https://developers.facebook.com/)                        | Facebook 登录，在 FB 上共享，社交插件，分析等                          | `OAuth`  | 是    | 未知 |
| [四方](https://developer.foursquare.com/)                       | 与 Foursquare 用户和地点互动（基于地理位置的签到，照片，提示，事件等） | `OAuth`  | 是    | 未知 |
| [他妈的服务](https://www.foaas.com)                             | 让某人他妈的                                                           | 没有     | 是    | 未知 |
| [完全联系](https://www.fullcontact.com/developer/docs/)         | 获取社交媒体个人资料和联系信息                                         | `OAuth`  | 是    | 未知 |
| [黑客新闻](https://github.com/HackerNews/API)                   | CS 和创业的社会新闻                                                    | 没有     | 是    | 未知 |
| [Instagram 的](https://www.instagram.com/developer/)            | Instagram 登录，在 Instagram 上共享，社交插件等                        | `OAuth`  | 是    | 未知 |
| [领英](https://developer.linkedin.com/docs/rest-api)            | 与 LinkedIn 进行所有数字集成的基础                                     | `OAuth`  | 是    | 未知 |
| [Meetup.com](https://www.meetup.com/meetup_api/)                | 来自 Meetup.com 的关于聚会的数据                                       | `apiKey` | 是    | 未知 |
| [混合器](https://dev.mixer.com/)                                | 游戏流 API                                                             | `OAuth`  | 是    | 未知 |
| [MySocialApp](https://mysocialapp.io)                           | 无缝的社交网络功能，API，SDK 到任何应用程序                            | `apiKey` | 是    | 未知 |
| [开放集体](https://docs.opencollective.com/help/developers/api) | 获取公开的集体数据                                                     | 没有     | 是    | 未知 |
| [Pinterest 的](https://developers.pinterest.com/)               | 世界思想目录                                                           | `OAuth`  | 是    | 未知 |
| [PWR 电报机器人](https://pwrtelegram.xyz)                       | Telegram 机器人 API 的增强版                                           | `apiKey` | 是    | 未知 |
| [Reddit](https://www.reddit.com/dev/api)                        | 互联网首页                                                             | `OAuth`  | 是    | 未知 |
| [松弛](https://api.slack.com/)                                  | 团队即时通讯                                                           | `OAuth`  | 是    | 未知 |
| [电报机器人](https://core.telegram.org/bots/api)                | 适用于机器人的 MTProto API 的简化 HTTP 版本                            | `apiKey` | 是    | 未知 |
| [电报 MTProto](https://core.telegram.org/api#getting-started)   | 读写电报数据                                                           | `OAuth`  | 是    | 未知 |
| [没垃圾](https://trashnothing.com/developer)                    | 一个免费自行车社区，每天发布数千个免费物品                             | `OAuth`  | 是    | 是   |
| [Tumblr](https://www.tumblr.com/docs/en/api/v2)                 | 读取和写入 Tumblr 数据                                                 | `OAuth`  | 是    | 未知 |
| [抽搐](https://dev.twitch.tv/docs)                              | 游戏流 API                                                             | `OAuth`  | 是    | 未知 |
| [推特](https://developer.twitter.com/en/docs)                   | 读写 Twitter 数据                                                      | `OAuth`  | 是    | 没有 |
| [vk](https://vk.com/dev/sites)                                  | 读取和写入 vk 数据                                                     | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 运动与健身

| 火                                                                   | 描述                                                      | 验证码          | HTTPS | CORS |
| -------------------------------------------------------------------- | --------------------------------------------------------- | --------------- | ----- | ---- |
| [Balldontlie](https://balldontlie.io)                                | Ballldontlie 提供对 NBA 统计数据的访问                    | 没有            | 是    | 是   |
| [BikeWise](https://www.bikewise.org/documentation/api_v2)            | Bikewise 是一个了解和报告自行车碰撞，危害和盗窃的地方     | 没有            | 是    | 未知 |
| [加拿大足球联赛（CFL）](http://api.cfl.ca/)                          | 官方 JSON API 提供有关 CFL 的实时联赛，球队和球员统计信息 | `apiKey`        | 是    | 没有 |
| [城市自行车](http://api.citybik.es/v2/)                              | 世界各地的城市自行车                                      | 没有            | 没有  | 未知 |
| [埃尔加斯特 F1](http://ergast.com/mrd/)                              | 1950 年世界锦标赛开始时的 F1 数据                         | 没有            | 是    | 未知 |
| [Fitbit](https://dev.fitbit.com/)                                    | Fitbit 信息                                               | `OAuth`         | 是    | 未知 |
| [足球（足球）视频](https://www.scorebat.com/video-api/)              | 嵌入英超联赛，德甲联赛，意甲联赛以及更多进球和进球的代码  | 没有            | 是    | 是   |
| [足球预测](https://boggio-analytics.com/fp-api/)                     | 对即将到来的足球比赛，赔率，结果和统计数据的预测          | `X-Mashape-Key` | 是    | 未知 |
| [Football-Data.org](http://api.football-data.org/index)              | 足球数据                                                  | 没有            | 没有  | 未知 |
| [JCDecaux 自行车](https://developer.jcdecaux.com/)                   | 德高集团的自助自行车                                      | `apiKey`        | 是    | 未知 |
| [NBA 统计](https://any-api.com/nba_com/nba_com/docs/API_Description) | 当前和历史的 NBA 统计数据                                 | 没有            | 是    | 未知 |
| [NFL 逮捕](http://nflarrest.com/api/)                                | NFL 逮捕数据                                              | 没有            | 没有  | 未知 |
| [NHL 记录和统计](https://gitlab.com/dword4/nhlapi)                   | NHL 历史数据和统计                                        | 没有            | 是    | 未知 |
| [饮食](https://strava.github.io/api/)                                | 与运动员，活动等联系                                      | `OAuth`         | 是    | 未知 |
| [SuredBits](https://suredbits.com/api/)                              | 查询体育数据，包括球队，球员，比赛，比分和统计数据        | 没有            | 没有  | 没有 |
| [体育数据库](https://www.thesportsdb.com/api.php)                    | 人群来源的运动数据和艺术品                                | `apiKey`        | 是    | 是   |
| [威格](https://wger.de/en/software/api)                              | 锻炼管理器数据，例如锻炼，肌肉或设备                      | `apiKey`        | 是    | 未知 |

**[to 返回索引](#index)**

### 测试数据

| 火                                                      | 描述                                                   | 验证码   | HTTPS | CORS |
| ------------------------------------------------------- | ------------------------------------------------------ | -------- | ----- | ---- |
| [可爱的化身](http://avatars.adorable.io)                | 生成随机卡通头像                                       | 没有     | 是    | 未知 |
| [非常培根](https://baconipsum.com/json-api/)            | 更强大的 Lorem ipsum 生成器                            | 没有     | 是    | 未知 |
| [骰熊头像](https://avatars.dicebear.com/)               | 生成随机像素艺术头像                                   | 没有     | 是    | 没有 |
| [伪 JSON](https://fakejson.com)                         | 生成测试和伪造数据的服务                               | `apiKey` | 是    | 是   |
| [身份图标](https://www.kwelo.com/media/identicon/)      | 生成抽象头像图像                                       | 没有     | 是    | 是   |
| [JSONPlaceholder](http://jsonplaceholder.typicode.com/) | 伪造数据以进行测试和原型制作                           | 没有     | 没有  | 未知 |
| [牛至](http://loripsum.net/)                            | 不烂的“ lorem ipsum”生成器                             | 没有     | 没有  | 未知 |
| [PIPL](https://pipl.ir/)                                | 免费和公共的 API，可在 JSON 中生成随机和伪造的人的数据 | 没有     | 是    | 没有 |
| [随机用户](https://randomuser.me)                       | 生成随机用户数据                                       | 没有     | 是    | 未知 |
| [机器人哈希](https://robohash.org/)                     | 生成随机机器人/异形头像                                | 没有     | 是    | 未知 |
| [此人不存在](https://thispersondoesnotexist.com)        | 产生不存在的人的真实面孔                               | 没有     | 是    | 未知 |
| [UI 名称](https://github.com/thm/uinames)               | 生成随机的假名                                         | 没有     | 是    | 未知 |
| [是否](https://yesno.wtf/api)                           | 随机生成是或否                                         | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 文字分析

| 火                                                                                                              | 描述                                       | 验证码   | HTTPS | CORS |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | -------- | ----- | ---- |
| [艾琳文本分析](http://docs.aylien.com/)                                                                         | 信息检索和自然语言 API 的集合              | `apiKey` | 是    | 未知 |
| [Cloudmersive 自然语言处理](https://www.cloudmersive.com/nlp-api)                                               | 自然语言处理和文本分析                     | `apiKey` | 是    | 是   |
| [检测语言](https://detectlanguage.com/)                                                                         | 检测文字语言                               | `apiKey` | 是    | 未知 |
| [Google Cloud Natural](https://cloud.google.com/natural-language/docs/)                                         | 自然语言理解技术，包括情感，实体和语法分析 | `apiKey` | 是    | 未知 |
| [塞曼提拉](https://semantria.readme.io/docs)                                                                    | 文本分析，带有情感分析，分类和命名实体提取 | `OAuth`  | 是    | 未知 |
| [沃森自然语言理解](https://cloud.ibm.com/apidocs/natural-language-understanding/natural-language-understanding) | 用于高级文本分析的自然语言处理             | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 追踪

| 火                                              | 描述                                           | 验证码   | HTTPS | CORS |
| ----------------------------------------------- | ---------------------------------------------- | -------- | ----- | ---- |
| [邮差](http://postmon.com.br)                   | 方便，快速，免费地查询巴西邮政编码和订单的 API | 没有     | 没有  | 未知 |
| [瑞典](https://developer.postnord.com/docs2)    | 提供有关运输中包裹的信息                       | `apiKey` | 没有  | 未知 |
| [UPS](https://www.ups.com/upsdeveloperkit)      | 发货和地址信息                                 | `apiKey` | 是    | 未知 |
| [什么脉冲](https://whatpulse.org/pages/webapi/) | 衡量键盘/鼠标使用情况的小型应用程序            | 没有     | 是    | 未知 |

**[to 返回索引](#index)**

### 运输

| 火                                                                                                                      | 描述                                                     | 验证码   | HTTPS | CORS |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------- | ----- | ---- |
| [ADS-B 交换](https://www.adsbexchange.com/data/)                                                                        | 访问任何和所有机载飞机的实时和历史数据                   | 没有     | 是    | 未知 |
| [AIS 集线器](http://www.aishub.net/api)                                                                                 | 配备 AIS 跟踪系统的任何海事和内河船舶的实时数据          | `apiKey` | 没有  | 未知 |
| [AIS 网站](http://www.aisweb.aer.mil.br/api/doc/index.cfm)                                                              | 空域控制部（DECEA）制作的数字媒体中的航空信息            | `apiKey` | 没有  | 未知 |
| [艾玛迪斯旅行创新沙盒](https://sandbox.amadeus.com/)                                                                    | 旅行搜索-使用受限                                        | `apiKey` | 是    | 未知 |
| [湾区捷运](http://api.bart.gov)                                                                                         | BART 的站点和预计到达                                    | `apiKey` | 没有  | 未知 |
| [布拉布拉车](https://dev.blablacar.com)                                                                                 | 搜索乘车旅行                                             | `apiKey` | 是    | 未知 |
| [社区交通](https://github.com/transitland/transitland-datastore/blob/master/README.md#api-endpoints)                    | Transitland API                                          | 没有     | 是    | 未知 |
| [戈比波](https://developer.goibibo.com/docs)                                                                            | 旅行搜索 API                                             | `apiKey` | 是    | 未知 |
| [GraphHopper](https://graphhopper.com/api/1/docs/)                                                                      | 带有转弯指示的 A 到 B 路由                               | `apiKey` | 是    | 未知 |
| [冰岛语 API](http://docs.apis.is/)                                                                                      | 提供在冰岛或与冰岛有关的服务的开放 API                   | 没有     | 是    | 未知 |
| [印度铁路](http://api.erail.in/)                                                                                        | 印度铁路信息                                             | `apiKey` | 没有  | 未知 |
| [伊豆](http://api-docs.izi.travel/)                                                                                     | 旅行者语音指南                                           | `apiKey` | 是    | 未知 |
| [里斯本地铁](http://app.metrolisboa.pt/status/getLinhas.php)                                                            | 地铁线路的延误                                           | 没有     | 没有  | 没有 |
| [纳维蒂](https://api.navitia.io/)                                                                                       | 开放的 API，用于使用传输数据构建很酷的东西               | `apiKey` | 是    | 未知 |
| [洗手间](https://www.refugerestrooms.org/api/docs/#!/restrooms)                                                         | 为跨性别，双性恋和性别不符合规定的人提供安全的洗手间通道 | 没有     | 是    | 未知 |
| [史基浦机场](https://developer.schiphol.nl/)                                                                            | 史基浦                                                   | `apiKey` | 是    | 未知 |
| [过境土地](https://transit.land/documentation/datastore/api-endpoints.html)                                             | 公交汇总                                                 | 没有     | 是    | 未知 |
| [美国亚特兰大的交通工具](http://www.itsmarta.com/app-developer-resources.aspx)                                          | 玛莎                                                     | 没有     | 没有  | 未知 |
| [新西兰奥克兰的交通](https://api.at.govt.nz/)                                                                           | 奥克兰交通                                               | 没有     | 是    | 未知 |
| [比利时运输](https://hello.irail.be/api/)                                                                               | 比利时运输 API                                           | 没有     | 是    | 未知 |
| [德国柏林运输](https://github.com/derhuerst/vbb-rest/blob/3/docs/index.md)                                              | 第三方 VBB API                                           | 没有     | 是    | 未知 |
| [法国波尔多运输](https://opendata.bordeaux-metropole.fr/explore/)                                                       | 波尔多大都会公共交通及更多（法国）                       | `apiKey` | 是    | 未知 |
| [美国波士顿交通](https://mbta.com/developers/v3-api)                                                                    | MBTA API                                                 | 没有     | 没有  | 未知 |
| [匈牙利布达佩斯的交通](https://bkkfutar.docs.apiary.io)                                                                 | 布达佩斯公共交通 API                                     | 没有     | 是    | 未知 |
| [美国芝加哥运输](http://www.transitchicago.com/developers/)                                                             | CTA                                                      | 没有     | 没有  | 未知 |
| [捷克共和国运输](https://www.chaps.cz/eng/products/idos-internet)                                                       | 捷克运输 API                                             | 没有     | 是    | 未知 |
| [美国丹佛运输](http://www.rtd-denver.com/gtfs-developer-guide.shtml)                                                    | 热电阻                                                   | 没有     | 没有  | 未知 |
| [芬兰运输](https://digitransit.fi/en/developers/)                                                                       | 芬兰运输 API                                             | 没有     | 是    | 未知 |
| [德国运输](http://data.deutschebahn.com/dataset/api-fahrplan)                                                           | 德国铁路（DB）API                                        | `apiKey` | 没有  | 未知 |
| [法国格勒诺布尔运输](https://www.metromobilite.fr/pages/opendata/OpenDataApi.html)                                      | 格勒诺布尔公共交通                                       | 没有     | 没有  | 没有 |
| [美国火奴鲁鲁的交通](http://hea.thebus.org/api_info.asp)                                                                | 火奴鲁鲁交通信息                                         | `apiKey` | 没有  | 未知 |
| [印度运输](https://data.gov.in/sector/transport)                                                                        | 印度公共交通 API                                         | `apiKey` | 是    | 未知 |
| [葡萄牙里斯本运输](https://emel.city-platform.com/opendata/)                                                            | 有关公交路线，停车和交通的数据                           | `apiKey` | 是    | 未知 |
| [英国伦敦运输](https://api.tfl.gov.uk)                                                                                  | TfL API                                                  | 没有     | 是    | 未知 |
| [英格兰曼彻斯特的交通](https://developer.tfgm.com/)                                                                     | TfGM 传输网络数据                                        | `apiKey` | 是    | 没有 |
| [美国纽约市的交通](http://datamine.mta.info/)                                                                           | MTA                                                      | `apiKey` | 没有  | 未知 |
| [挪威运输](http://reisapi.ruter.no/help)                                                                                | 挪威运输 API                                             | 没有     | 没有  | 未知 |
| [法国巴黎运输](http://restratpws.azurewebsites.net/swagger/)                                                            | 实时时间表变得简单                                       | 没有     | 没有  | 未知 |
| [法国巴黎运输](http://data.ratp.fr/api/v1/console/datasets/1.0/search/)                                                 | RATP 开放数据 API                                        | 没有     | 没有  | 未知 |
| [美国费城运输](http://www3.septa.org/hackathon/)                                                                        | SEPTA API                                                | 没有     | 没有  | 未知 |
| [巴西圣保罗的交通工具](http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/documentacao-api/) | SPTrans                                                  | `OAuth`  | 没有  | 未知 |
| [瑞典运输](https://www.trafiklab.se/api)                                                                                | 公共交通消费者                                           | `OAuth`  | 是    | 未知 |
| [瑞士运输](https://opentransportdata.swiss/en/)                                                                         | 瑞士官方公共交通开放数据                                 | `apiKey` | 是    | 未知 |
| [瑞士运输](https://transport.opendata.ch/)                                                                              | 瑞士公共交通 API                                         | 没有     | 是    | 未知 |
| [荷兰运输](http://www.ns.nl/reisinformatie/ns-api)                                                                      | NS，仅火车                                               | `apiKey` | 没有  | 未知 |
| [荷兰运输](https://github.com/skywave/KV78Turbo-OVAPI/wiki)                                                             | OVAPI，全国范围的公共交通                                | 没有     | 是    | 未知 |
| [加拿大多伦多运输](https://myttc.ca/developers)                                                                         | 含税                                                     | 没有     | 是    | 未知 |
| [美国运输](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf)                                                       | NextBus API                                              | 没有     | 没有  | 未知 |
| [加拿大温哥华运输](https://developer.translink.ca/)                                                                     | 传联                                                     | `OAuth`  | 是    | 未知 |
| [美国华盛顿运输](https://developer.wmata.com/)                                                                          | 华盛顿地铁运输 API                                       | `OAuth`  | 是    | 未知 |
| [优步](https://developer.uber.com/products)                                                                             | 优步乘车要求和价格估算                                   | `OAuth`  | 是    | 是   |
| [我的交通在哪里](https://developer.whereismytransport.com/)                                                             | 新兴城市公共交通数据平台                                 | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### URL 缩短器

| 火                                                                         | 描述                                | 验证码   | HTTPS | CORS |
| -------------------------------------------------------------------------- | ----------------------------------- | -------- | ----- | ---- |
| [有点](http://dev.bitly.com/get_started.html)                              | URL 缩短器和链接管理                | `OAuth`  | 是    | 未知 |
| [CleanURI](https://cleanuri.com/docs)                                      | URL 缩短服务                        | `No`     | 是    | 是   |
| [ClickMeter](https://support.clickmeter.com/hc/en-us/categories/201474986) | 监控，比较和优化您的营销链接        | `apiKey` | 是    | 未知 |
| [更名](https://developers.rebrandly.com/v1/docs)                           | 自定义 URL 缩短器，用于共享品牌链接 | `apiKey` | 是    | 未知 |
| [重新连结](https://rel.ink)                                                | 免费和安全的 URL 缩短器             | 没有     | 是    | 是   |

**[to 返回索引](#index)**

### 车辆

| 火                                                            | 描述                                                           | 验证码   | HTTPS | CORS |
| ------------------------------------------------------------- | -------------------------------------------------------------- | -------- | ----- | ---- |
| [巴西车辆和价格](https://deividfortuna.github.io/fipe/)       | 经济研究所基金会提供的车辆信息-Fipe                            | 没有     | 是    | 未知 |
| [凯利蓝皮书](http://developer.kbb.com/#!/data/1-Default)      | 车辆信息，价格，配置等                                         | `apiKey` | 是    | 没有 |
| [梅赛德斯奔驰](https://developer.mercedes-benz.com/apis)      | 远程信息处理数据，远程访问车辆功能，汽车配置器，查找服务经销商 | `apiKey` | 是    | 没有 |
| [美国国家公路交通安全管理局](https://vpic.nhtsa.dot.gov/api/) | NHTSA 产品信息目录和车辆清单                                   | 没有     | 是    | 未知 |
| [智能车](https://smartcar.com/docs/)                          | 锁定和解锁车辆，并获取里程表读数和位置等数据。适用于大多数新车 | `OAuth`  | 是    | 是   |

**[to 返回索引](#index)**

### 视频

| 火                                                                                              | 描述                                | 验证码   | HTTPS | CORS |
| ----------------------------------------------------------------------------------------------- | ----------------------------------- | -------- | ----- | ---- |
| [冰与火的 API](https://anapioficeandfire.com/)                                                  | 权力游戏 API                        | 没有     | 是    | 未知 |
| [绝命毒师](https://breakingbadapi.com/documentation)                                            | 打破不良 API                        | 没有     | 是    | 未知 |
| [破烂报价](https://github.com/shevabam/breaking-bad-quotes)                                     | 一些坏的坏报价                      | 没有     | 是    | 未知 |
| [捷克电视台](http://www.ceskatelevize.cz/xml/tv-program/)                                       | 捷克电视台的电视节目                | 没有     | 没有  | 未知 |
| [Dailymotion](https://developer.dailymotion.com/)                                               | Dailymotion 开发人员 API            | `OAuth`  | 是    | 未知 |
| [哈利·波特](https://www.potterapi.com/)                                                         | 哈利·波特 API                       | `apiKey` | 是    | 是   |
| [打开电影数据库](http://www.omdbapi.com/)                                                       | 电影信息                            | `apiKey` | 是    | 未知 |
| [罗恩·斯旺森行情](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api) | 电视                                | 没有     | 是    | 未知 |
| [STAPI](http://stapi.co)                                                                        | 关于星际迷航的所有信息              | 没有     | 没有  | 没有 |
| [指环王](https://the-one-api.herokuapp.com/)                                                    | 指环王 API                          | `apiKey` | 是    | 未知 |
| [TMDb](https://www.themoviedb.org/documentation/api)                                            | 基于社区的电影数据                  | `apiKey` | 是    | 未知 |
| [道](https://trakt.tv/b/api-docs)                                                               | 影视数据                            | `apiKey` | 是    | 是   |
| [TVDB](https://api.thetvdb.com/swagger)                                                         | 电视数据                            | `apiKey` | 是    | 未知 |
| [电视迷宫](http://www.tvmaze.com/api)                                                           | 电视节目数据                        | 没有     | 没有  | 未知 |
| [Vimeo](https://developer.vimeo.com/)                                                           | Vimeo 开发人员 API                  | `OAuth`  | 是    | 未知 |
| [的 YouTube](https://developers.google.com/youtube/)                                            | 将 YouTube 功能添加到您的网站和应用 | `OAuth`  | 是    | 未知 |

**[to 返回索引](#index)**

### 天气

| 火                                                      | 描述                       | 验证码   | HTTPS | CORS |
| ------------------------------------------------------- | -------------------------- | -------- | ----- | ---- |
| [7 计时器！](http://www.7timer.info/doc.php?lang=en)    | 天气，尤其是 Astroweather  | 没有     | 没有  | 未知 |
| [APIXU](https://www.apixu.com/doc/request.aspx)         | 天气                       | `apiKey` | 是    | 未知 |
| [元天气](https://www.metaweather.com/api/)              | 天气                       | 没有     | 是    | 没有 |
| [气象学系](https://api.met.no/weatherapi/documentation) | 天气和气候数据             | 没有     | 是    | 未知 |
| [NOAA 气候数据](https://www.ncdc.noaa.gov/cdo-web/)     | 天气和气候数据             | `apiKey` | 是    | 未知 |
| [OD 天气](http://api.oceandrivers.com/static/docs.html) | 天气和天气网络摄像头       | 没有     | 没有  | 未知 |
| [OpenUV](https://www.openuv.io)                         | 实时紫外线指数预测         | `apiKey` | 是    | 未知 |
| [OpenWeatherMap](http://openweathermap.org/api)         | 天气                       | `apiKey` | 没有  | 未知 |
| [风暴玻璃](https://stormglass.io/)                      | 来自多种来源的全球海洋天气 | `apiKey` | 是    | 是   |
| [气象位](https://www.weatherbit.io/api)                 | 天气                       | `apiKey` | 是    | 未知 |
| [雅虎！天气](https://developer.yahoo.com/weather/)      | 天气                       | `apiKey` | 是    | 未知 |

**[to 返回索引](#index)**
