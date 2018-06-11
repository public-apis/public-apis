# Public APIs [![Build Status](https://api.travis-ci.org/toddmotto/public-apis.svg)](https://travis-ci.org/toddmotto/public-apis)

A collective list of free APIs for use in web development.

A public API for this project can be found [here](https://github.com/davemachado/public-api) - thanks to [DigitalOcean](https://www.digitalocean.com/) for helping us provide this service!

For information on contributing to this project, please see the [contributing guide](.github/CONTRIBUTING.md).

Please note a passing build status indicates all listed APIs are available since the last update. A failing build status indicates that 1 or more services may be unavailable at the moment.

## Index

* [Animals](#animals)
* [Anime](#anime)
* [Anti-Malware](#anti-malware)
* [Art & Design](#art--design)
* [Books](#books)
* [Business](#business)
* [Calendar](#calendar)
* [Cloud Storage & File Sharing](#cloud-storage--file-sharing)
* [Continuous Integration](#continuous-integration)
* [Cryptocurrency](#cryptocurrency)
* [Currency Exchange](#currency-exchange)
* [Data Validation](#data-validation)
* [Development](#development)
* [Dictionaries](#dictionaries)
* [Documents & Productivity](#documents--productivity)
* [Environment](#environment)
* [Events](#events)
* [Finance](#finance)
* [Food & Drink](#food--drink)
* [Fraud Prevention](#fraud-prevention)
* [Games & Comics](#games--comics)
* [Geocoding](#geocoding)
* [Government](#government)
* [Health](#health)
* [Jobs](#jobs)
* [Machine Learning](#machine-learning)
* [Music](#music)
* [News](#news)
* [Open Data](#open-data)
* [Open Source Projects](#open-source-projects)
* [Patent](#patent)
* [Personality](#personality)
* [Photography](#photography)
* [Science & Math](#science--math)
* [Security](#security)
* [Shopping](#shopping)
* [Social](#social)
* [Sports & Fitness](#sports--fitness)
* [Test Data](#test-data)
* [Text Analysis](#text-analysis)
* [Tracking](#tracking)
* [Transportation](#transportation)
* [URL Shorteners](#url-shorteners)
* [Vehicle](#vehicle)
* [Video](#video)
* [Weather](#weather)

### Animals
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Cats | Pictures of cats from Tumblr | No | Yes | Unknown | [Go!](https://thecatapi.com/docs.html) |
| Dogs | Based on the Stanford Dogs Dataset | No | Yes | Unknown | [Go!](https://dog.ceo/dog-api/) |
| HTTPCat | Cat for every HTTP Status | No | Yes | Unknown | [Go!](https://http.cat/) |
| IUCN | IUCN Red List of Threatened Species | `apiKey` | No | Unknown | [Go!](http://apiv3.iucnredlist.org/api/v3/docs) |
| Movebank | Movement and Migration data of animals | No | Yes | Unknown | [Go!](https://github.com/movebank/movebank-api-doc) |
| Petfinder | Adoption | `apiKey` | Yes | Unknown | [Go!](https://www.petfinder.com/developers/api-docs/) |
| RandomCat | Random pictures of cats | No | Yes | Yes | [Go!](https://aws.random.cat/meow) |
| RandomDog | Random pictures of dogs | No | Yes | Yes | [Go!](https://random.dog/woof.json) |
| RandomFox | Random pictures of foxes | No | Yes | Yes | [Go!](https://randomfox.ca/floof/) |
| RescueGroups | Adoption | No | Yes | Unknown | [Go!](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) |
| Shibe.Online | Random pictures of Shibu Inu, cats or birds | No | No | Unknown | [Go!](http://shibe.online/) |

### Anime
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| AniList | Anime discovery & tracking | `OAuth` | Yes | Unknown | [Go!](https://github.com/AniList/ApiV2-GraphQL-Docs) |
| Jikan | Unofficial MyAnimeList API | No | Yes | Yes | [Go!](https://jikan.moe) |
| Kitsu | Anime discovery platform | `OAuth` | Yes | Unknown | [Go!](http://docs.kitsu.apiary.io/) |
| Studio Ghibli | Resources from Studio Ghibli films | No | Yes | Unknown | [Go!](https://ghibliapi.herokuapp.com) |

### Anti-Malware
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| AlienVault Open Threat Exchange (OTX) | IP/domain/URL reputation | `apiKey` | Yes | Unknown | [Go!](https://otx.alienvault.com/api/) |
| Certly | Certly Link/Domain Flagging | `apiKey` | Yes | Unknown | [Go!](https://guard.certly.io/) |
| Google Safe Browsing | Google Link/Domain Flagging | `apiKey` | Yes | Unknown | [Go!](https://developers.google.com/safe-browsing/) |
| Metacert | Metacert Link Flagging | `apiKey` | Yes | Unknown | [Go!](https://metacert.com/) |
| VirusTotal | VirusTotal File/URL Analysis | `apiKey` | Yes | Unknown | [Go!](https://www.virustotal.com/en/documentation/public-api/) |
| Web Of Trust (WOT) | Website reputation | `apiKey` | Yes | Unknown | [Go!](https://www.mywot.com/wiki/API) |

### Art & Design
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Behance | Design | `apiKey` | Yes | Unknown | [Go!](https://www.behance.net/dev) |
| Cooper Hewitt | Smithsonian Design Museum | `apiKey` | Yes | Unknown | [Go!](https://collection.cooperhewitt.org/api) |
| Dribbble | Design | `OAuth` | No | Unknown | [Go!](http://developer.dribbble.com/v1/) |
| Harvard Art Museums | Art | `apiKey` | No | Unknown | [Go!](https://github.com/harvardartmuseums/api-docs) |
| Iconfinder | Icons | `apiKey` | Yes | Unknown | [Go!](https://developer.iconfinder.com) |
| Icons8 | Icons | `OAuth` | Yes | Unknown | [Go!](http://docs.icons8.apiary.io/#reference/0/meta) |
| Noun Project | Icons | `OAuth` | No | Unknown | [Go!](http://api.thenounproject.com/index.html) |
| Rijksmuseum | Art | `apiKey` | Yes | Unknown | [Go!](https://www.rijksmuseum.nl/en/api) |

### Books
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Bhagavad Gita | Bhagavad Gita text | `OAuth` | Yes | Yes | [Go!](https://bhagavadgita.io/api) |
| BookNomads | Books published in the Netherlands and Flanders (about 2.5 million), book covers, and related data | No | Yes | Unknown | [Go!](https://www.booknomads.com/dev) |
| British National Bibliography | Books | No | No | Unknown | [Go!](http://bnb.data.bl.uk/) |
| Goodreads | Books | `apiKey` | Yes | Unknown | [Go!](https://www.goodreads.com/api) |
| Google Books | Books | `OAuth` | Yes | Unknown | [Go!](https://developers.google.com/books/) |
| Open Library | Books, book covers, and related data | No | Yes | Unknown | [Go!](https://openlibrary.org/developers/api) |
| Penguin Publishing | Books, book covers, and related data | No | Yes | Unknown | [Go!](http://www.penguinrandomhouse.biz/webservices/rest/) |

### Business
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Charity Search | Non-profit charity data | `apiKey` | No | Unknown | [Go!](http://charityapi.orghunter.com/) |
| Clearbit Logo | Search for company logos and embed them in your projects | No | Yes | Unknown | [Go!](https://clearbit.com/docs#logo-api) |
| Domainsdb.info | Registered Domain Names Search | No | Yes | Unknown | [Go!](https://domainsdb.info/) |
| Gmail | Flexible, RESTful access to the user's inbox | `OAuth` | Yes | Unknown | [Go!](https://developers.google.com/gmail/api/) |
| Google Analytics | Collect, configure, and analyze your data to reach the right audience | `OAuth` | Yes | Unknown | [Go!](https://developers.google.com/analytics/) |
| mailgun | Email Service | `apiKey` | Yes | Unknown | [Go!](https://www.mailgun.com/) |
| markerapi | Trademark Search | No | No | Unknown | [Go!](http://www.markerapi.com/) |
| Ticksel | Friendly website analytics made for humans | No | Yes | Unknown | [Go!](https://ticksel.com) |
| Trello | Boards, lists, and cards to help you organize and prioritize your projects | `OAuth` | Yes | Unknown | [Go!](https://developers.trello.com/) |

### Calendar
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Church Calendar | Catholic liturgical calendar | No | No | Unknown | [Go!](http://calapi.inadiutorium.cz/) |
| Czech Namedays Calendar | Lookup for a name and returns nameday date | No | No | Unknown | [Go!](http://svatky.adresa.info/) |
| Google Calendar | Display, create and modify Google calendar events | `OAuth` | Yes | Unknown | [Go!](https://developers.google.com/google-apps/calendar/) |
| Hebrew Calendar | Convert between Gregarian and Hebrew, fetch Shabbat and Holiday times, etc | No | No | Unknown | [Go!](https://www.hebcal.com/home/developer-apis) |
| Holidays | Historical data regarding holidays | `apiKey` | Yes | Unknown | [Go!](https://holidayapi.com/) |
| LectServe | Protestant liturgical calendar | No | No | Unknown | [Go!](http://www.lectserve.com) |
| Namedays Calendar | Provides namedays for multiple countries | No | Yes | Yes | [Go!](https://api.abalin.net/) |
| Non-Working Days | Database of ICS files for non working days | No | Yes | Unknown | [Go!](https://github.com/gadael/icsdb) |

### Cloud Storage & File Sharing
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Box | File Sharing and Storage | `OAuth` | Yes | Unknown | [Go!](https://developer.box.com/) |
| Dropbox | File Sharing and Storage | `OAuth` | Yes | Unknown | [Go!](https://www.dropbox.com/developers) |
| Google Drive | File Sharing and Storage | `OAuth` | Yes | Unknown | [Go!](https://developers.google.com/drive/) |
| OneDrive | File Sharing and Storage | `OAuth` | Yes | Unknown | [Go!](https://dev.onedrive.com/) |
| Pastebin | Plain Text Storage | `apiKey` | Yes | Unknown | [Go!](https://pastebin.com/api/) |

### Continuous Integration
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| CircleCI | Automate the software development process using continuous integration and continuous delivery | `apiKey` | Yes | Unknown | [Go!](https://circleci.com/docs/api/v1-reference/) |
| Codeship | Codeship is a Continuous Integration Platform in the cloud | `apiKey` | Yes | Unknown | [Go!](https://apidocs.codeship.com/) |
| Travis CI | Sync your GitHub projects with Travis CI to test your code in minutes | `apiKey` | Yes | Unknown | [Go!](https://docs.travis-ci.com/api/) |

### Cryptocurrency
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Binance | Exchange for Trading Cryptocurrencies based in China | `apiKey` | Yes | Unknown | [Go!](https://github.com/binance-exchange/binance-official-api-docs) |
| BitcoinCharts | Financial and Technical Data related to the Bitcoin Network | No | Yes | Unknown | [Go!](https://bitcoincharts.com/about/exchanges/) |
| Bitfinex | Cryptocurrency Trading Platform | `apiKey` | Yes | Unknown | [Go!](https://docs.bitfinex.com/docs/introduction) |
| Bitmex | Real-Time Cryptocurrency derivatives trading platform based in Hong Kong | `apiKey` | Yes | Unknown | [Go!](https://www.bitmex.com/app/apiOverview) |
| Bittrex | Next Generation Crypto Trading Platform | `apiKey` | Yes | Unknown | [Go!](https://bittrex.com/Home/Api) |
| Block | Bitcoin Payment, Wallet & Transaction Data | `apiKey` | Yes | Unknown | [Go!](https://www.block.io/docs/basic) |
| Blockchain | Bitcoin Payment, Wallet & Transaction Data | No | Yes | Unknown | [Go!](https://www.blockchain.info/api) |
| CoinAPI | All Currency Exchanges integrate under a single api | `apiKey` | Yes | No | [Go!](https://docs.coinapi.io/) |
| Coinbase | Bitcoin, Litecoin and Ethereum Prices | `apiKey` | Yes | Unknown | [Go!](https://developers.coinbase.com) |
| CoinBin | Cryptocurrency information | No | Yes | Unknown | [Go!](https://coinbin.org/) |
| CoinDesk | Bitcoin Price Index | No | No | Unknown | [Go!](http://www.coindesk.com/api/) |
| CoinMarketCap | Cryptocurrencies Prices | No | Yes | Unknown | [Go!](https://coinmarketcap.com/api/) |
| CryptoCompare | Cryptocurrencies Comparison | No | Yes | Unknown | [Go!](https://www.cryptocompare.com/api#) |
| Cryptonator | Cryptocurrencies Exchange Rates | No | Yes | Unknown | [Go!](https://www.cryptonator.com/api/) |
| GDAX | Cryptocurrency Trading Platform | `apiKey` | Yes | Unknown | [Go!](https://docs.gdax.com/#api) |
| Livecoin | Cryptocurrency Exchange | No | Yes | Unknown | [Go!](https://www.livecoin.net/api) |
| MercadoBitcoin | Brazilian Cryptocurrency Information | No | Yes | Unknown | [Go!](https://www.mercadobitcoin.net/api-doc/) |
| Nexchange | Automated cryptocurrency exchange service | No | No | Yes | [Go!](https://nexchange2.docs.apiary.io/) |
| Poloniex | US based digital asset exchange | `apiKey` | Yes | Unknown | [Go!](https://poloniex.com/support/api/) |
| WorldCoinIndex | Cryptocurrencies Prices | `apiKey` | Yes | Unknown | [Go!](https://www.worldcoinindex.com/apiservice) |

### Currency Exchange
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| 1Forge | Forex currency market data | `apiKey` | Yes | Unknown | [Go!](https://1forge.com/forex-data-api/api-documentation) |
| Currencylayer | Exchange rates and currency conversion | `apiKey` | Yes | Unknown | [Go!](https://currencylayer.com/documentation) |
| Czech National Bank | A collection of exchange rates | No | Yes | Unknown | [Go!](https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml) |
| Exchangeratesapi.io | Exchange rates with currency conversion | No | Yes | Yes | [Go!](https://exchangeratesapi.io) |
| Fixer.io | Exchange rates and currency conversion | `apiKey` | Yes | Unknown | [Go!](http://fixer.io) |
| LabStack | Accurate and reliable live currency exchange rates for over 150 symbols | `apiKey` | Yes | Yes | [Go!](https://labstack.com/docs/api/currency) |

### Data Validation
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| LabStack | Check email address for syntax error, disposable mail server and valid SMTP mailbox | `apiKey` | Yes | Yes | [Go!](https://labstack.com/docs/api/email) |
| languagelayer | Language detection | No | Yes | Unknown | [Go!](https://languagelayer.com) |
| Lob.com | US Address Verification | `apiKey` | Yes | Unknown | [Go!](https://lob.com/) |
| mailboxlayer | Email address validation | No | Yes | Unknown | [Go!](https://mailboxlayer.com) |
| NumValidate | Open Source phone number validation | No | Yes | Unknown | [Go!](https://numvalidate.com) |
| numverify | Phone number validation | No | Yes | Unknown | [Go!](https://numverify.com) |
| PurgoMalum | Content validator against profanity & obscenity | No | No | Unknown | [Go!](http://www.purgomalum.com) |
| vatlayer | VAT number validation | No | Yes | Unknown | [Go!](https://vatlayer.com) |

### Development
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| ApiLeap | Make screenshots from web pages and HTML | `apiKey` | Yes | Unknown | [Go!](https://apileap.com/) |
| Apility.io | IP, Domains and Emails anti-abuse API blocklist | No | Yes | Yes | [Go!](https://apility.io/apidocs/) |
| APIs.guru | Wikipedia for Web APIs, OpenAPI/Swagger specs for public APIs | No | Yes | Unknown | [Go!](https://apis.guru/api-doc/) |
| BetterMeta | Return a site's meta tags in JSON format | `X-Mashape-Key` | Yes | Unknown | [Go!](http://bettermeta.io) |
| Bitbucket | Pull public information for a Bitbucket account | No | Yes | Unknown | [Go!](https://api.bitbucket.org/2.0/users/karllhughes) |
| Browshot | Easily make screenshots of web pages in any screen size, as any device | `apiKey` | Yes | Unknown | [Go!](https://browshot.com/api/documentation) |
| CDNJS | Library info on CDNJS | No | Yes | Unknown | [Go!](https://api.cdnjs.com/libraries/jquery) |
| Changelogs.md | Structured changelog metadata from open source projects | No | Yes | Unknown | [Go!](https://changelogs.md) |
| Count.io | Persistent counting and A/B testing | No | Yes | Unknown | [Go!](https://count.io) |
| DigitalOcean Status | Status of all DigitalOcean services | No | Yes | Unknown | [Go!](https://status.digitalocean.com/api/v1) |
| DomainDb Info | Domain name search to find all domains containing particular words/phrases/etc | No | Yes | Unknown | [Go!](https://domainsdb.info/apidomainsdb/index.php) |
| Faceplusplus | A tool to detect face | `OAuth` | Yes | Unknown | [Go!](https://www.faceplusplus.com/) |
| Genderize.io | Determines a gender from a first name | No | Yes | Unknown | [Go!](https://genderize.io) |
| Github | Make use of GitHub repositories, code and user info programmatically | `OAuth` | Yes | Yes | [Go!](https://developer.github.com/v3/) |
| Gitlab | Automate GitLab interaction programmatically | `OAuth` | Yes | Unknown | [Go!](https://docs.gitlab.com/ee/api/) |
| Gitter | Chat for GitHub | `OAuth` | Yes | Unknown | [Go!](https://github.com/gitterHQ/docs) |
| HTTP2.Pro | Test endpoints for client and server HTTP/2 protocol support | No | Yes | Unknown | [Go!](https://http2.pro/doc/api) |
| import.io | Retrieve structured data from a website or RSS feed | `apiKey` | Yes | Unknown | [Go!](http://api.docs.import.io/) |
| IPify | A simple IP Address API | No | Yes | Unknown | [Go!](https://www.ipify.org/) |
| IPinfo | Another simple IP Address API | No | Yes | Unknown | [Go!](https://ipinfo.io/developers) |
| JSON 2 JSONP | Convert JSON to JSONP (on-the-fly) for easy cross-domain data requests using client-side JavaScript | No | Yes | Unknown | [Go!](https://json2jsonp.com/) |
| JSONbin.io | Free JSON storage service. Ideal for small scale Web apps, Websites and Mobile apps | `apiKey` | Yes | Unknown | [Go!](https://jsonbin.io) |
| Judge0 | Compile and run source code | No | Yes | Unknown | [Go!](https://api.judge0.com/) |
| Kairos | Face Recognition and Emotion Analysis | `apiKey` | Yes | Unknown | [Go!](https://www.kairos.com/features) |
| Let's Validate | Uncovers the technologies used on websites and URL to thumbnail | No | Yes | Unknown | [Go!](https://github.com/letsvalidate/api) |
| License-API | Unofficial REST API for choosealicense.com | No | Yes | No | [Go!](https://github.com/cmccandless/license-api/blob/master/README.md) |
| LiveEdu | Live Coding Streaming | `OAuth` | Yes | Unknown | [Go!](https://www.liveedu.tv/developer/applications/) |
| Myjson | A simple JSON store for your web or mobile app | No | No | Unknown | [Go!](http://myjson.com/api) |
| Plino | Spam filtering system | No | Yes | Unknown | [Go!](https://plino.herokuapp.com/) |
| Public APIs | A collective list of free JSON APIs for use in web development | No | Yes | Unknown | [Go!](https://github.com/davemachado/public-api) |
| QR code | Generate and decode / read QR code graphics | No | Yes | Unknown | [Go!](http://goqr.me/api/) |
| ReqRes | A hosted REST-API ready to respond to your AJAX requests | No | Yes | Unknown | [Go!](https://reqres.in/ ) |
| Scrape Website Email | Grabs email addresses from a URL | `X-Mashape-Key` | Yes | Unknown | [Go!](https://market.mashape.com/tommytcchan/scrape-website-email) |
| SHOUTCLOUD | ALL-CAPS AS A SERVICE | No | No | Unknown | [Go!](http://shoutcloud.io/) |
| StackExchange | Q&A forum for developers | `OAuth` | Yes | Unknown | [Go!](https://api.stackexchange.com/) |
| Verse | Check what's the latest version of your favorite open-source project | No | Yes | Unknown | [Go!](https://verse.pawelad.xyz/) |
| XML to JSON | Integration developer utility APIs | No | Yes | Unknown | [Go!](https://developers.wso2apistore.com/) |

### Dictionaries
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Oxford | Dictionary Data | `apiKey` | Yes | Unknown | [Go!](https://developer.oxforddictionaries.com/) |
| Wordnik | Dictionary Data | `apiKey` | No | Unknown | [Go!](http://developer.wordnik.com) |
| Words | Definitions and synonyms for more than 150,000 words | `apiKey` | Yes | Unknown | [Go!](https://www.wordsapi.com/) |

### Documents & Productivity
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Cloudmersive Document and Data Conversion | HTML/URL to PDF/PNG, Office documents to PDF, image conversion | `apiKey` | Yes | Yes | [Go!](https://cloudmersive.com/convert-api) |
| File.io | File Sharing | No | Yes | Unknown | [Go!](https://www.file.io) |
| Mercury | Web parser | `apiKey` | Yes | Unknown | [Go!](https://mercury.postlight.com/web-parser/) |
| pdflayer | HTML/URL to PDF | `apiKey` | Yes | Unknown | [Go!](https://pdflayer.com) |
| Pocket | Bookmarking service | `OAuth` | Yes | Unknown | [Go!](https://getpocket.com/developer/) |
| PrexView | Data from XML or JSON to PDF, HTML or Image | `apiKey` | Yes | Unknown | [Go!](https://prexview.com) |
| Restpack | Provides screenshot, HTML to PDF, and content extraction APIs | `apiKey` | Yes | Unknown | [Go!](https://restpack.io/) |
| Todoist | Todo Lists | `OAuth` | Yes | Unknown | [Go!](https://developer.todoist.com) |
| Vector Express | Free vector file converting API | No | No | Yes | [Go!](http://vector.express) |
| Wunderlist | Todo Lists | `OAuth` | Yes | Unknown | [Go!](https://developer.wunderlist.com/documentation) |

### Environment
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| AirVisual | Air quality and weather data | `apiKey` | Yes | Unknown | [Go!](https://airvisual.com/api) |
| OpenAQ | Open air quality data | `apiKey` | Yes | Unknown | [Go!](https://docs.openaq.org/) |
| PM2.5.in | Air quality of China | `apiKey` | No | Unknown | [Go!](http://www.pm25.in/api_doc) |
| PVWatts | Energy production photovoltaic (PV) energy systems | `apiKey` | Yes | Unknown | [Go!](https://developer.nrel.gov/docs/solar/pvwatts-v5/) |
| UK Carbon Intensity | The Official Carbon Intensity API for Great Britain developed by National Grid | No | Yes | Unknown | [Go!](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v1-0-0) |

### Events
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Eventbrite | Find events | `OAuth` | Yes | Unknown | [Go!](https://www.eventbrite.com/developer/v3/) |
| Picatic | Sell tickets anywhere | `apiKey` | Yes | Unknown | [Go!](http://developer.picatic.com/?utm_medium=web&utm_source=github&utm_campaign=public-apis%20repo&utm_content=toddmotto) |
| Ticketmaster | Search events, attractions, or venues | `apiKey` | Yes | Unknown | [Go!](http://developer.ticketmaster.com/products-and-docs/apis/getting-started/) |

### Finance
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Alpha Vantage | Realtime and historical stock data | `apiKey` | Yes | Unknown | [Go!](https://www.alphavantage.co/) |
| Barchart OnDemand | Stock, Futures, and Forex Market Data | `apiKey` | Yes | Unknown | [Go!](https://www.barchartondemand.com/free) |
| Consumer Financial Protection Bureau | Financial services consumer complaint data | `apiKey` | Yes | Unknown | [Go!](https://data.consumerfinance.gov/resource/jhzv-w97w.json) |
| IEX | Stocks and Market Data | No | Yes | Unknown | [Go!](https://iextrading.com/developer/) |
| IG | Spreadbetting and CFD Market Data | `apiKey` | Yes | Unknown | [Go!](https://labs.ig.com/gettingstarted) |
| Plaid | Connect with users’ bank accounts and access transaction data | `apiKey` | Yes | Unknown | [Go!](https://plaid.com/) |
| Razorpay IFSC | Indian Financial Systems Code (Bank Branch Codes) | No | Yes | Unknown | [Go!](https://ifsc.razorpay.com/) |
| RoutingNumbers.info | ACH/NACHA Bank Routing Numbers | No | Yes | Unknown | [Go!](https://www.routingnumbers.info/api/index.html) |
| VAT Rates | A collection of all VAT rates for EU countries | No | Yes | Unknown | [Go!](https://jsonvat.com/) |

### Food & Drink
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Edamam | Recipe Search | `apiKey` | Yes | Unknown | [Go!](https://developer.edamam.com/) |
| Food2Fork | Recipe Search | `apiKey` | No | Unknown | [Go!](http://food2fork.com/about/api) |
| LCBO | Alcohol | `apiKey` | Yes | Unknown | [Go!](https://lcboapi.com/) |
| Open Food Facts | Food Products Database | No | Yes | Unknown | [Go!](https://world.openfoodfacts.org/data) |
| PunkAPI | Brewdog Beer Recipes | No | Yes | Unknown | [Go!](https://punkapi.com/) |
| Recipe Puppy | Food | No | No | Unknown | [Go!](http://www.recipepuppy.com/about/api/) |
| TacoFancy | Community-driven taco database | No | No | Unknown | [Go!](https://github.com/evz/tacofancy-api) |
| The Report of the Week | Food & Drink Reviews | No | Yes | Unknown | [Go!](https://github.com/andyklimczak/TheReportOfTheWeek-API) |
| TheCocktailDB | Cocktail Recipes | `apiKey` | Yes | Yes | [Go!](https://www.thecocktaildb.com/api.php) |
| TheMealDB | Meal Recipes | `apiKey` | Yes | Yes | [Go!](https://www.themealdb.com/api.php) |
| What's on the menu? | NYPL human-transcribed historical menu collection | `apiKey` | No | Unknown | [Go!](http://nypl.github.io/menus-api/) |
| Yummly | Find food recipes | `apiKey` | Yes | Unknown | [Go!](https://developer.yummly.com/) |
| Zomato | Discover restaurants | `apiKey` | Yes | Unknown | [Go!](https://developers.zomato.com/api) |


### Fraud Prevention
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Whitepages Pro | Global identity verification with phone, address, email, and IP | `apiKey` | Yes | Unknown | [Go!](https://pro.whitepages.com/developer/documentation/identity-check-api/) |
| Whitepages Pro | Phone reputation to detect spammy phones | `apiKey` | Yes | Unknown | [Go!](https://pro.whitepages.com/developer/documentation/phone-reputation-api/) |
| Whitepages Pro | Get an owner’s name, address, demographics based on the phone number | `apiKey` | Yes | Unknown | [Go!](https://pro.whitepages.com/developer/documentation/reverse-phone-api/) |
| Whitepages Pro | Phone number validation, line_type, carrier append | `apiKey` | Yes | Unknown | [Go!](https://pro.whitepages.com/developer/documentation/phone-intelligence-api/) |
| Whitepages Pro | Get normalized physical address, residents, address type, and validity | `apiKey` | Yes | Unknown | [Go!](https://pro.whitepages.com/developer/documentation/reverse-address-api/) |

### Games & Comics
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| AmiiboAPI | Amiibo Information | No | No | Yes | [Go!](http://www.amiiboapi.com/) |
| Battle.net | Blizzard Entertainment | `apiKey` | Yes | Unknown | [Go!](https://dev.battle.net/) |
| Battlefield 4 | Battlefield 4 Information | No | Yes | Unknown | [Go!](https://bf4stats.com/api) |
| Chuck Norris Database | Jokes | No | No | Unknown | [Go!](http://www.icndb.com/api/) |
| Clash of Clans | Clash of Clans Game Information | No | Yes | Unknown | [Go!](https://developer.clashofclans.com) |
| Clash Royale | Clash Royale Game Information | No | Yes | Unknown | [Go!](https://github.com/martincarrera/clash-royale-api) |
| Comic Vine | Comics | No | Yes | Unknown | [Go!](https://comicvine.gamespot.com/api/documentation) |
| Deck of Cards | Deck of Cards | No | No | Unknown | [Go!](http://deckofcardsapi.com/) |
| Destiny The Game | Bungie Platform API | `apiKey` | Yes | Unknown | [Go!](https://github.com/Bungie-net/api) |
| Dota 2 | Provides information about Player stats , Match stats, Rankings for Dota 2 | No | Yes | Unknown | [Go!](https://docs.opendota.com/) |
| Eve Online | Third-Party Developer Documentation | `OAuth` | Yes | Unknown | [Go!](https://eveonline-third-party-documentation.readthedocs.io/en/latest/) |
| Fortnite | Fortnite Stats | `apiKey` | Yes | Unknown | [Go!](https://fortnitetracker.com/site-api) |
| Games | Minecraft and other server info & user info) | No | Yes | Unknown | [Go!](https://docs.gameapis.net/) |
| Giant Bomb | Video Games | No | Yes | Unknown | [Go!](https://www.giantbomb.com/api/documentation) |
| Guild Wars 2 | Guild Wars 2 Game Information | `apiKey` | Yes | Unknown | [Go!](https://wiki.guildwars2.com/wiki/API:Main) |
| Halo | Halo 5 and Halo Wars 2 Information | `apiKey` | Yes | Unknown | [Go!](https://developer.haloapi.com/) |
| Hearthstone | Hearthstone Cards Information | `X-Mashape-Key` | Yes | Unknown | [Go!](http://hearthstoneapi.com/) |
| IGDB.com | Video Game Database | `apiKey` | Yes | Unknown | [Go!](https://api.igdb.com/) |
| Jokes | Programming and general jokes | No | Yes | Unknown | [Go!](https://github.com/15Dkatz/official_joke_api) |
| Jservice | Jeopardy Question Database | No | No | Unknown | [Go!](http://jservice.io) |
| Magic The Gathering | Magic The Gathering Game Information | No | No | Unknown | [Go!](http://magicthegathering.io/) |
| Marvel | Marvel Comics | `apiKey` | No | Unknown | [Go!](http://developer.marvel.com) |
| Open Trivia | Trivia Questions | No | Yes | Unknown | [Go!](https://opentdb.com/api_config.php) |
| PandaScore | E-sports games and results | `apiKey` | Yes | Unknown | [Go!](https://api.pandascore.co) |
| PlayerUnknown's Battlegrounds | PUBG Stats | `apiKey` | Yes | Unknown | [Go!](https://pubgtracker.com/site-api) |
| Pokéapi | Pokémon Information | No | Yes | Unknown | [Go!](https://pokeapi.co) |
| Pokémon TCG | Pokémon TCG Information | No | Yes | Unknown | [Go!](https://pokemontcg.io) |
| Qriusity | Quiz/Trivia Questions | No | Yes | Unknown | [Go!](https://qriusity.com/) |
| Rick and Morty | All the Rick and Morty information, including images | No | Yes | Yes | [Go!](https://rickandmortyapi.com) |
| Riot Games | League of Legends Game Information | `apiKey` | Yes | Unknown | [Go!](https://developer.riotgames.com/) |
| Steam | Steam Client Interaction | `OAuth` | Yes | Unknown | [Go!](https://developer.valvesoftware.com/wiki/Steam_Web_API) |
| Wargaming.net | Wargaming.net info and stats | `apiKey` | Yes | No | [Go!](https://developers.wargaming.net/) |
| xkcd | Retrieve xkcd comics as JSON | No | Yes | Unknown | [Go!](https://xkcd.com/json.html) |

### Geocoding
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| adresse.data.gouv.fr | Address database of France, geocoding, and reverse | No | Yes | Unknown | [Go!](https://adresse.data.gouv.fr) |
| Battuta | A (country/region/city) in-cascade location API | `apiKey` | Yes | Unknown | [Go!](https://battuta.medunes.net) |
| Bing Maps | Create/customize digital maps based on Bing Maps data | `apiKey` | Yes | Unknown | [Go!](https://www.microsoft.com/maps/) |
| City Context | Crime, school, and transportation data for US cities | `apiKey` | Yes | Unknown | [Go!](https://www.citycontext.com/api-reference#/) |
| CitySDK | Open APIs for select European cities | No | Yes | Unknown | [Go!](http://www.citysdk.eu/citysdk-toolkit/) |
| Daum Maps | Daum Maps provide multiple APIs for Korean maps | `apiKey` | No | Unknown | [Go!](http://apis.map.daum.net/) |
| GeoApi | French geographical data | No | Yes | Unknown | [Go!](https://api.gouv.fr/api/geoapi.html) |
| Geocode.xyz | Provides worldwide forward/reverse geocoding, batch geocoding and geoparsing | No | Yes | Unknown | [Go!](https://geocode.xyz/) |
| GeoNames | Place names and other geographical data | No | No | Unknown | [Go!](http://www.geonames.org/export/web-services.html) |
| Google Earth Engine | A cloud-based platform for planetary-scale environmental data analysis | `apiKey` | Yes | Unknown | [Go!](https://developers.google.com/earth-engine/) |
| Google Maps | Create/customize digital maps based on Google Maps data | `apiKey` | Yes | Unknown | [Go!](https://developers.google.com/maps/) |
| GraphLoc | Free GraphQL IP Geolocation API | No | Yes | Unknown | [Go!](https://www.graphloc.com) |
| HelloSalut | Get hello translation following user language | No | Yes | Unknown | [Go!](https://www.fourtonfish.com/hellosalut/hello/) |
| HERE Maps | Create/customize digital maps based on HERE Maps data | `apiKey` | Yes | Unknown | [Go!](https://developer.here.com) |
| IP 2 Country | Map an IP to a country | No | Yes | Unknown | [Go!](https://ip2country.info) |
| IP Address Details | Find geolocation with ip address | No | Yes | Unknown | [Go!](https://ipinfo.io/) |
| IP Location | Find IP address location information | No | Yes | Unknown | [Go!](https://ipapi.co/) |
| IP Sidekick | Geolocation API that returns extra information about an IP address | `apiKey` | Yes | Unknown | [Go!](https://ipsidekick.com) |
| IP Vigilante | Free IP Geolocation API | No | Yes | Unknown | [Go!](https://www.ipvigilante.com/) |
| ipstack | Locate and identify website visitors by IP address | `apiKey` | Yes | Unknown | [Go!](https://ipstack.com/) |
| LabStack | Find IP to location, location to latitude-longitude and reverse | `apiKey` | Yes | Yes | [Go!](https://labstack.com/docs/api/geocode) |
| LocationIQ | Provides forward/reverse geocoding and batch geocoding | `apiKey` | Yes | Yes | [Go!](https://locationiq.org/docs/) |
| Mapbox | Create/customize beautiful digital maps | `apiKey` | Yes | Unknown | [Go!](https://www.mapbox.com/developers/) |
| Mexico | Mexico RESTful zip codes API | No | Yes | Unknown | [Go!](https://github.com/IcaliaLabs/sepomex) |
| One Map, Singapore | Singapore Land Authority REST API services for Singapore addresses | `apiKey` | Yes | Unknown | [Go!](https://docs.onemap.sg/) |
| OnWater | Determine if a lat/lon is on water or land | No | Yes | Unknown | [Go!](https://onwater.io/) |
| OpenCage | Forward and reverse geocoding using open data | No | Yes | Unknown | [Go!](https://geocoder.opencagedata.com) |
| OpenStreetMap | Navigation, geolocation and geographical data | `OAuth` | No | Unknown | [Go!](http://wiki.openstreetmap.org/wiki/API) |
| PostcodeData.nl | Provide geolocation data based on postcode for Dutch addresses | No | No | Unknown | [Go!](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) |
| Postcodes.io | Postcode lookup & Geolocation for the UK | No | Yes | Unknown | [Go!](https://postcodes.io) |
| REST Countries | Get information about countries via a RESTful API | No | Yes | Unknown | [Go!](https://restcountries.eu) |
| Uebermaps | Discover and share maps with friends | `apiKey` | Yes | Unknown | [Go!](https://uebermaps.com/api/v2) |
| Utah AGRC | Utah Web API for geocoding Utah addresses | `apiKey` | Yes | Unknown | [Go!](https://api.mapserv.utah.gov) |
| ViaCep | Brazil RESTful zip codes API | No | Yes | Unknown | [Go!](https://viacep.com.br) |
| Zippopotam | Get information about place such as country, city, state, etc | No | No | Unknown | [Go!](http://www.zippopotam.us) |

### Government
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| BCLaws | Access to the laws of British Columbia | No | No | Unknown | [Go!](http://www.bclaws.ca/civix/template/complete/api/index.html) |
| BusinessUSA | Authoritative information on U.S. programs, events, services and more | `apiKey` | Yes | Unknown | [Go!](https://business.usa.gov/developer) |
| Census.gov | The US Census Bureau provides various APIs and data sets on demographics and businesses | No | Yes | Unknown | [Go!](https://www.census.gov/data/developers/data-sets.html) |
| Colorado Data Engine | Formatted and geolocated Colorado public data | No | Yes | Unknown | [Go!](http://codataengine.org/) |
| Colorado Information Marketplace | Colorado State Government Open Data | No | Yes | Unknown | [Go!](https://data.colorado.gov/) |
| Data USA | US Public Data | No | Yes | Unknown | [Go!](https://datausa.io/about/api/) |
| EPA | Web services and data sets from the US Environmental Protection Agency | No | Yes | Unknown | [Go!](https://developer.epa.gov/category/api/) |
| FEC | Information on campaign donations in federal elections | `apiKey` | Yes | Unknown | [Go!](https://api.open.fec.gov/developers/) |
| Federal Register | The Daily Journal of the United States Government | No | Yes | Unknown | [Go!](https://www.federalregister.gov/reader-aids/developer-resources) |
| Food Standards Agency | UK food hygiene rating data API | No | No | Unknown | [Go!](http://ratings.food.gov.uk/open-data/en-GB) |
| Open Government, Australia | Australian Government Open Data | No | Yes | Unknown | [Go!](https://www.data.gov.au/) |
| Open Government, Belgium | Belgium Government Open Data | No | Yes | Unknown | [Go!](https://data.gov.be/) |
| Open Government, Canada | Canadian Government Open Data | No | No | Unknown | [Go!](http://open.canada.ca/en) |
| Open Government, France | French Government Open Data | `apiKey` | Yes | Unknown | [Go!](https://www.data.gouv.fr/) |
| Open Government, India | Indian Government Open Data | `apiKey` | Yes | Unknown | [Go!](https://data.gov.in/) |
| Open Government, New Zealand | New Zealand Government Open Data | No | Yes | Unknown | [Go!](https://www.data.govt.nz/) |
| Open Government, Taiwan | Taiwan Government Open Data | No | Yes | Unknown | [Go!](https://data.gov.tw/) |
| Open Government, USA | United States Government Open Data | No | Yes | Unknown | [Go!](https://www.data.gov/) |
| Prague Opendata | Prague City Open Data | No | No | Unknown | [Go!](http://opendata.praha.eu/en) |
| Regulations.gov | Federal regulatory materialsto increase understanding of the Federal rule making process | `apiKey` | Yes | Unknown | [Go!](https://regulationsgov.github.io/developers/) |
| Represent by Open North | Find Canadian Government Representatives | No | Yes | Unknown | [Go!](https://represent.opennorth.ca/) |

### Health
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| BetterDoctor | Detailed information about doctors in your area | `apiKey` | Yes | Unknown | [Go!](https://developer.betterdoctor.com/) |
| Diabetes | Logging and retrieving diabetes information | No | No | Unknown | [Go!](http://predictbgl.com/api/) |
| Flutrack | Influenza-like symptoms with geotracking | No | No | Unknown | [Go!](http://www.flutrack.org/) |
| Healthcare.gov | Educational content about the US Health Insurance Marketplace | No | Yes | Unknown | [Go!](https://www.healthcare.gov/developers/) |
| Lexigram | NLP that extracts mentions of clinical concepts from text, gives access to clinical ontology | `apiKey` | Yes | Unknown | [Go!](https://docs.lexigram.io/v1/welcome) |
| Makeup | Makeup Information | No | No | Unknown | [Go!](http://makeup-api.herokuapp.com/) |
| Medicare | Access to the data from the CMS - medicare.gov | No | Yes | Unknown | [Go!](https://data.medicare.gov/developers) |
| NPPES | National Plan & Provider Enumeration System, info on healthcare providers registered in US | No | Yes | Unknown | [Go!](https://npiregistry.cms.hhs.gov/registry/help-api) |
| Nutritionix | Worlds largest verified nutrition database | `apiKey` | Yes | Unknown | [Go!](https://developer.nutritionix.com/) |
| openFDA | Public FDA data about drugs, devices, and foods | No | Yes | Unknown | [Go!](https://open.fda.gov/api/) |
| USDA Nutrients | National Nutrient Database for Standard Reference | No | Yes | Unknown | [Go!](https://ndb.nal.usda.gov/ndb/doc/index) |

### Jobs
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Adzuna | Job board aggregator | `apiKey` | Yes | Unknown | [Go!](https://developer.adzuna.com/overview) |
| Authentic Jobs | Job board for designers, hackers, and creative pros | `apiKey` | Yes | Unknown | [Go!](https://authenticjobs.com/api/docs) |
| Careerjet | Job search engine | `apiKey` | No | Unknown | [Go!](https://www.careerjet.com/partners/api/) |
| Github Jobs | Jobs for software developers | No | Yes | Unknown | [Go!](https://jobs.github.com/api) |
| Indeed | Job board aggregator | `apiKey` | Yes | Unknown | [Go!](https://www.indeed.com/publisher) |
| Jobs2Careers | Job aggregator | `apiKey` | Yes | Unknown | [Go!](http://api.jobs2careers.com/api/spec.pdf) |
| Jooble | Job search engine | `apiKey` | Yes | Unknown | [Go!](https://us.jooble.org/api/about) |
| Juju | Job search engine | `apiKey` | No | Unknown | [Go!](http://www.juju.com/publisher/spec/) |
| Open Skills | Job titles, skills, and related jobs data | No | No | Unknown | [Go!](https://github.com/workforce-data-initiative/skills-api/wiki/API-Overview) |
| Reed | Job board aggregator | `apiKey` | Yes | Unknown | [Go!](https://www.reed.co.uk/developers) |
| Search.gov Jobs | Tap into a list of current jobs openings with the United States government | No | Yes | Unknown | [Go!](https://search.gov/developer/jobs.html) |
| The Muse | Job board and company profiles | `apiKey` | Yes | Unknown | [Go!](https://www.themuse.com/developers/api/v2) |
| Upwork | Freelance job board and management system | `OAuth` | Yes | Unknown | [Go!](https://developers.upwork.com/) |
| USAJOBS | US government job board | `apiKey` | Yes | Unknown | [Go!](https://developer.usajobs.gov/) |
| ZipRecruiter | Job search app and website | `apiKey` | Yes | Unknown | [Go!](https://www.ziprecruiter.com/publishers) |

### Machine Learning
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Clarifai | Computer Vision | `OAuth` | Yes | Unknown | [Go!](https://developer.clarifai.com/) |
| Cloudmersive | Image captioning, face recognition, NSFW classification | `apiKey` | Yes | Yes | [Go!](https://www.cloudmersive.com/image-recognition-and-processing-api) |
| Dialogflow | Natural Language Processing | `apiKey` | Yes | Unknown | [Go!](https://dialogflow.com) |
| Keen IO | Data Analytics | `apiKey` | Yes | Unknown | [Go!](https://keen.io/) |
| Unplugg | Forecasting API for timeseries data | `apiKey` | Yes | Unknown | [Go!](https://unplu.gg/test_api.html) |
| Wit.ai | Natural Language Processing | `OAuth` | Yes | Unknown | [Go!](https://wit.ai/) |

### Music
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Bandsintown | Music Events | No | Yes | Unknown | [Go!](https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0) |
| Deezer | Music | `OAuth` | Yes | Unknown | [Go!](https://developers.deezer.com/api) |
| Discogs | Music | `OAuth` | Yes | Unknown | [Go!](https://www.discogs.com/developers/) |
| Genius | Crowdsourced lyrics and music knowledge | `OAuth` | Yes | Unknown | [Go!](https://docs.genius.com/) |
| Genrenator | Music genre generator | No | Yes | Unknown | [Go!](https://binaryjazz.us/genrenator-api/) |
| iTunes Search | Software products | No | Yes | Unknown | [Go!](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) |
| Jamendo | Music | `OAuth` | Yes | Unknown | [Go!](https://developer.jamendo.com/v3.0) |
| LastFm | Music | `apiKey` | Yes | Unknown | [Go!](https://www.last.fm/api) |
| Lyrics.ovh | Simple API to retrieve the lyrics of a song | No | Yes | Unknown | [Go!](http://docs.lyricsovh.apiary.io/) |
| Mixcloud | Music | `OAuth` | Yes | Unknown | [Go!](https://www.mixcloud.com/developers/) |
| MusicBrainz | Music | No | Yes | Unknown | [Go!](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2) |
| Musikki | Music | `apiKey` | Yes | Unknown | [Go!](https://music-api.musikki.com/reference) |
| Musixmatch | Music | `apiKey` | Yes | Unknown | [Go!](https://developer.musixmatch.com/) |
| Songkick | Music Events | `OAuth` | Yes | Unknown | [Go!](https://www.songkick.com/developer/) |
| Songsterr | Provides guitar, bass and drums tabs and chords | No | Yes | Unknown | [Go!](https://www.songsterr.com/a/wa/api/) |
| Spotify | View Spotify music catalog, manage users' libraries, get recommendations, and more | `OAuth` | Yes | Unknown | [Go!](https://beta.developer.spotify.com/documentation/web-api/) |
| TasteDive | Similar artist API (also works for movies and TV shows) | `apiKey` | Yes | Unknown | [Go!](https://tastedive.com/read/api) |
| TheAudioDB | Music | `apiKey` | No | Unknown | [Go!](http://www.theaudiodb.com) |
| Vagalume | Crowdsourced lyrics and music knowledge | `apiKey` | Yes | Unknown | [Go!](https://api.vagalume.com.br/docs/) |

### News
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Chronicling America | Provides access to millions of pages of historic US newspapers from the Library of Congress | No | No | Unknown | [Go!](http://chroniclingamerica.loc.gov/about/api/) |
| Feedbin | RSS reader | `OAuth` | Yes | Unknown | [Go!](https://github.com/feedbin/feedbin-api) |
| Feedster | Searchable and categorized collections of RSS feeds | `apiKey` | Yes | Unknown | [Go!](https://api.feedster.me/v1/docs/) |
| New York Times | Provides news | `apiKey` | Yes | Unknown | [Go!](https://developer.nytimes.com/) |
| News | Headlines currently published on a range of news sources and blogs | `apiKey` | Yes | Unknown | [Go!](https://newsapi.org/) |
| NPR One | Personalized news listening experience from NPR | `OAuth` | Yes | Unknown | [Go!](http://dev.npr.org/api/) |
| The Guardian | Access all the content the Guardian creates, categorised by tags and section | `apiKey` | Yes | Unknown | [Go!](http://open-platform.theguardian.com/) |
| The Old Reader | RSS reader | `apiKey` | Yes | Unknown | [Go!](https://github.com/theoldreader/api) |

### Open Data
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| 18F | Unofficial US Federal Government API Development | No | No | Unknown | [Go!](http://18f.github.io/API-All-the-X/) |
| Abbreviation | Get abbreviations and meanings | `X-Mashape-Key` | Yes | Unknown | [Go!](https://market.mashape.com/daxeel/abbreviations) |
| Archive.org | The Internet Archive | No | Yes | Unknown | [Go!](https://archive.readme.io/docs) |
| Callook.info | United States ham radio callsigns | No | Yes | Unknown | [Go!](https://callook.info) |
| CARTO | Location Information Prediction | `apiKey` | Yes | Unknown | [Go!](https://carto.com/) |
| Celebinfo | Celebrity information | `X-Mashape-Key` | Yes | Unknown | [Go!](https://market.mashape.com/daxeel/celebinfo/) |
| Datakick | The open product database | `apiKey` | Yes | Unknown | [Go!](https://www.datakick.org/api) |
| Dronestream | Tracks United States drone strikes | No | Yes | Unknown | [Go!](https://dronestre.am/) |
| Enigma Public | Broadest collection of public data | `apiKey` | Yes | Yes | [Go!](http://docs.enigma.com/public/public_v20_api_about) |
| fonoApi | Mobile Device Description | No | Yes | Unknown | [Go!](https://fonoapi.freshpixl.com/) |
| French Address Search | Address search via the French Government | No | Yes | Unknown | [Go!](https://adresse.data.gouv.fr/api) |
| INQStats | Open demographic data such as population, life expectancy, migration rate, etc | `apiKey` | No | Unknown | [Go!](http://blog.inqubu.com/inqstats-open-api-published-to-get-demographic-data) |
| LinkPreview | Get JSON formatted summary with title, description and preview image for any requested URL | `apiKey` | Yes | Yes | [Go!](https://www.linkpreview.net) |
| Marijuana Strains | Marijuana strains, races, flavors, and effects | `apiKey` | No | Unknown | [Go!](http://strains.evanbusse.com/) |
| Microlink.io | Turns any link into information | No | Yes | Unknown | [Go!](https://docs.microlink.io) |
| Quandl | Stock Market Data | No | Yes | Unknown | [Go!](https://www.quandl.com/) |
| Scoop.it | Content Curation Service | `apiKey` | No | Unknown | [Go!](http://www.scoop.it/dev) |
| Teleport | Quality of Life Data | No | Yes | Unknown | [Go!](https://developers.teleport.org/) |
| Universities List | University names, countries and domains | No | Yes | Unknown | [Go!](https://github.com/Hipo/university-domains-list) |
| UPC database | More than 1.5 million barcode numbers from all around the world | `apiKey` | Yes | Unknown | [Go!](https://upcdatabase.org/api) |
| Wikidata | Collaboratively edited knowledge base operated by the Wikimedia Foundation | `OAuth` | Yes | Unknown | [Go!](https://www.wikidata.org/w/api.php?action=help) |
| Wikipedia | Mediawiki Encyclopedia | No | Yes | Unknown | [Go!](https://www.mediawiki.org/wiki/API:Main_page) |
| Yelp | Find Local Business | `OAuth` | Yes | Unknown | [Go!](https://www.yelp.com/developers/documentation/v3) |

### Open Source Projects
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Countly | Countly web analytics | No | No | Unknown | [Go!](http://resources.count.ly/docs) |
| Drupal.org | Drupal.org | No | Yes | Unknown | [Go!](https://www.drupal.org/drupalorg/docs/api) |
| Libraries.io | Open source software libraries | `apiKey` | Yes | Unknown | [Go!](https://libraries.io/api) |

### Patent
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| EPO | European patent search system api | `OAuth` | Yes | Unknown | [Go!](https://developers.epo.org/) |
| TIPO | Taiwan patent search system api | `apiKey` | Yes | Unknown | [Go!](https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00) |
| USPTO | USA patent api services | No | Yes | Unknown | [Go!](https://www.uspto.gov/learning-and-resources/open-data-and-mobility) |

### Personality
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| chucknorris.io | JSON API for hand curated Chuck Norris jokes | No | Yes | Unknown | [Go!](https://api.chucknorris.io) |
| FavQs.com | FavQs allows you to collect, discover, and share your favorite quotes | `apiKey` | Yes | Unknown | [Go!](https://favqs.com/api) |
| Forismatic | Inspirational Quotes | No | No | Unknown | [Go!](http://forismatic.com/en/api/) |
| icanhazdadjoke | The largest selection of dad jokes on the internet | No | Yes | Unknown | [Go!](https://icanhazdadjoke.com/api) |
| Medium | Community of readers and writers offering unique perspectives on ideas | `OAuth` | Yes | Unknown | [Go!](https://github.com/Medium/medium-api-docs) |
| Quotes on Design | Inspirational Quotes | No | Yes | Unknown | [Go!](https://quotesondesign.com/api-v4-0/) |
| Traitify | Assess, collect, and analyze Personality | No | Yes | Unknown | [Go!](https://app.traitify.com/developer) |
| tronalddump.io | Api & web archive for the things Donald Trump has said | No | Yes | Unknown | [Go!](https://www.tronalddump.io) |

### Photography
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| 500px | Photography Community | `OAuth` | Yes | Unknown | [Go!](https://github.com/500px/api-documentation) |
| Flickr | Flickr Services | `OAuth` | Yes | Unknown | [Go!](https://www.flickr.com/services/api/) |
| Getty Images | Build applications using the world's most powerful imagery | `OAuth` | Yes | Unknown | [Go!](http://developers.gettyimages.com/en/) |
| Gfycat | Jiffier GIFs | `OAuth` | Yes | Unknown | [Go!](https://developers.gfycat.com/api/) |
| Giphy | Get all your gifs | `apiKey` | Yes | Unknown | [Go!](https://developers.giphy.com/docs/) |
| Gyazo | Upload images | `apiKey` | Yes | Unknown | [Go!](https://gyazo.com/api/docs) |
| Imgur | Images | `OAuth` | Yes | Unknown | [Go!](https://apidocs.imgur.com/) |
| Pixabay | Photography | `apiKey` | Yes | Unknown | [Go!](https://pixabay.com/sk/service/about/api/) |
| Pixhost | Upload images, photos, galleries | No | Yes | Unknown | [Go!](https://pixhost.org/api/index.html) |
| PlaceKitten | Resizable kitten placeholder images | No | Yes | Unknown | [Go!](https://placekitten.com/) |
| ScreenShotLayer | URL 2 Image | No | Yes | Unknown | [Go!](https://screenshotlayer.com) |
| Unsplash | Photography | `OAuth` | Yes | Unknown | [Go!](https://unsplash.com/developers) |

### Science & Math
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| arcsecond.io | Multiple astronomy data sources | No | Yes | Unknown | [Go!](https://api.arcsecond.io/) |
| CORE | Access the world's Open Access research papers | `apiKey` | Yes | Unknown | [Go!](https://core.ac.uk/services#api) |
| inspirehep.net | High Energy Physics info. system | No | Yes | Unknown | [Go!](https://inspirehep.net/info/hep/api?ln=en) |
| Launch Library | Upcoming Space Launches | No | Yes | Unknown | [Go!](https://launchlibrary.net/docs/1.3/api.html) |
| Minor Planet Center | Asterank.com Information | No | No | Unknown | [Go!](http://www.asterank.com/mpc) |
| NASA | NASA data, including imagery | No | Yes | Unknown | [Go!](https://api.nasa.gov) |
| Newton | Symbolic and Arithmetic Math Calculator | No | Yes | Unknown | [Go!](https://newton.now.sh/) |
| Numbers | Facts about numbers | No | No | Unknown | [Go!](http://numbersapi.com) |
| Open Notify | ISS astronauts, current location, etc | No | No | Unknown | [Go!](http://open-notify.org/Open-Notify-API/) |
| Open Science Framework | Repository and archive for study designs, research materials, data, manuscripts, etc | No | Yes | Unknown | [Go!](https://developer.osf.io) |
| SHARE | A free, open, dataset about research and scholarly activities | No | Yes | Unknown | [Go!](https://share.osf.io/api/v2/) |
| SpaceX | Company, vehicle, launchpad and launch data | No | Yes | Unknown | [Go!](https://github.com/r-spacex/SpaceX-API) |
| Sunrise and Sunset | Sunset and sunrise times for a given latitude and longitude | No | Yes | Unknown | [Go!](https://sunrise-sunset.org/api) |
| USGS Earthquake Hazards Program | Earthquakes data real-time | No | Yes | Unknown | [Go!](https://earthquake.usgs.gov/fdsnws/event/1/) |
| USGS Water Services | Water quality and level info for rivers and lakes | No | Yes | Unknown | [Go!](https://waterservices.usgs.gov/) |
| World Bank | World Data | No | No | Unknown | [Go!](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) |

### Security
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| AXFR Database | AXFR public database | No | No | Unknown | [Go!](http://api.axfrcheck.com) |
| HaveIBeenPwned | Passwords which have previously been exposed in data breaches | No | Yes | Unknown | [Go!](https://haveibeenpwned.com/API/v2) |
| SecurityTrails | Domain and IP related information such as current and historical WHOIS and DNS records | `apiKey` | Yes | Unknown | [Go!](https://securitytrails.com/corp/apidocs) |
| UK Police | UK Police data | No | Yes | Unknown | [Go!](https://data.police.uk/docs/) |

### Shopping
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Best Buy | Products, Buying Options, Categories, Recommendations, Stores, and Commerce | `apiKey` | Yes | Unknown | [Go!](https://bestbuyapis.github.io/api-documentation/#overview) |
| eBay | Sell and Buy on eBay | `OAuth` | Yes | Unknown | [Go!](https://go.developer.ebay.com/) |
| Wal-Mart | Item price and availability | `apiKey` | Yes | Unknown | [Go!](https://developer.walmartlabs.com/docs) |
| Wegmans | Wegmans Food Markets | `apiKey` | Yes | Unknown | [Go!](https://dev.wegmans.io) |

### Social
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Buffer | Access to pending and sent updates in Buffer | `OAuth` | Yes | Unknown | [Go!](https://buffer.com/developers/api) |
| Cisco Spark | Team Collaboration Software | `OAuth` | Yes | Unknown | [Go!](https://developer.ciscospark.com) |
| Discord | Make bots for Discord, integrate Discord onto an external platform | `OAuth` | Yes | Unknown | [Go!](https://discordapp.com/developers/docs/intro) |
| Disqus | Communicate with Disqus data | `OAuth` | Yes | Unknown | [Go!](https://disqus.com/api/docs/auth/) |
| Facebook | Facebook Login, Share on FB, Social Plugins, Analytics and more | `OAuth` | Yes | Unknown | [Go!](https://developers.facebook.com/) |
| Foursquare | Interact with Foursquare users and places (geolocation-based checkins, photos, tips, events, etc) | `OAuth` | Yes | Unknown | [Go!](https://developer.foursquare.com/) |
| Fuck Off as a Service | Asks someone to fuck off | No | Yes | Unknown | [Go!](https://www.foaas.com) |
| Full Contact | Get Social Media profiles and contact Information | `OAuth` | Yes | Unknown | [Go!](https://www.fullcontact.com/developer/docs/) |
| HackerNews | Social news for CS and entrepreneurship | No | Yes | Unknown | [Go!](https://github.com/HackerNews/API) |
| Instagram | Instagram Login, Share on Instagram, Social Plugins and more | `OAuth` | Yes | Unknown | [Go!](https://www.instagram.com/developer/) |
| Instagram Proxy | Instagram's public data as an API | No | Yes | Yes | [Go!](https://github.com/whizzzkid/instagram-proxy-api) |
| LinkedIn | The foundation of all digital integrations with LinkedIn | `OAuth` | Yes | Unknown | [Go!](https://developer.linkedin.com/docs/rest-api) |
| Meetup.com | Data about Meetups from Meetup.com | `apiKey` | Yes | Unknown | [Go!](https://www.meetup.com/meetup_api/) |
| Pinterest | The world's catalog of ideas | `OAuth` | Yes | Unknown | [Go!](https://developers.pinterest.com/) |
| PWRTelegram bot | Boosted version of the Telegram bot API | `OAuth` | Yes | Unknown | [Go!](https://pwrtelegram.xyz) |
| Reddit | Homepage of the internet | `OAuth` | Yes | Unknown | [Go!](https://www.reddit.com/dev/api) |
| SharedCount | Social media like and share data for any URL | `apiKey` | Yes | Unknown | [Go!](http://docs.sharedcount.com/) |
| Slack | Team Instant Messaging | `OAuth` | Yes | Unknown | [Go!](https://api.slack.com/) |
| Telegram Bot | Simplified HTTP version of the MTProto API for bots | `OAuth` | Yes | Unknown | [Go!](https://core.telegram.org/bots/api) |
| Telegram MTProto | Read and write Telegram data | `OAuth` | Yes | Unknown | [Go!](https://core.telegram.org/api#getting-started) |
| Tumblr | Read and write Tumblr Data | `OAuth` | Yes | Unknown | [Go!](https://www.tumblr.com/docs/en/api/v2) |
| Twitch | Game Streaming API | `OAuth` | Yes | Unknown | [Go!](https://dev.twitch.tv/docs) |
| Twitter | Read and write Twitter data | `OAuth` | Yes | No | [Go!](https://developer.twitter.com/en/docs) |
| vk | Read and write vk data | `OAuth` | Yes | Unknown | [Go!](https://vk.com/dev/sites) |

### Sports & Fitness
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| BikeWise | Bikewise is a place to learn about and report bike crashes, hazards, and thefts | No | Yes | Unknown | [Go!](https://www.bikewise.org/documentation/api_v2) |
| Cartola FC | The Cartola FC API serves to check the partial points of your team | No | Yes | Unknown | [Go!](https://github.com/wgenial/cartrolandofc) |
| City Bikes | City Bikes around the world | No | No | Unknown | [Go!](http://api.citybik.es/v2/) |
| Cricket Live Scores | Live cricket scores | `X-Mashape-Key` | Yes | Unknown | [Go!](https://market.mashape.com/dev132/cricket-live-scores) |
| Ergast F1 | F1 data from the beginning of the world championships in 1950 | No | Yes | Unknown | [Go!](http://ergast.com/mrd/) |
| Fitbit | Fitbit Information | `OAuth` | Yes | Unknown | [Go!](https://dev.fitbit.com/) |
| Football-Data.org | Football Data | No | No | Unknown | [Go!](http://api.football-data.org/index) |
| JCDecaux Bike | JCDecaux's self-service bicycles | `apiKey` | Yes | Unknown | [Go!](https://developer.jcdecaux.com/) |
| NBA Stats | Current and historical NBA Statistics | No | Yes | Unknown | [Go!](https://any-api.com/nba_com/nba_com/docs/API_Description) |
| NFL Arrests | NFL Arrest Data | No | No | Unknown | [Go!](http://nflarrest.com/api/) |
| Pro Motocross | The RESTful AMA Pro Motocross lap times for every racer on the start gate | No | No | Unknown | [Go!](http://promotocrossapi.com) |
| Strava | Connect with athletes, activities and more | `OAuth` | Yes | Unknown | [Go!](https://strava.github.io/api/) |
| SuredBits | Query sports data, including teams, players, games, scores, and statistics | No | No | Unknown | [Go!](https://suredbits.com/api/) |
| TheSportsDB | Crowd-Sourced Sports Data and Artwork | `apiKey` | Yes | Yes | [Go!](https://www.thesportsdb.com/api.php) |
| UFC Data | Ultimate Fighting Championship information for events and fighters | No | No | Unknown | [Go!](http://ufc-data-api.ufc.com/) |
| Wger | Workout manager data as exercises, muscles or equipment | `apiKey` | Yes | Unknown | [Go!](https://wger.de/en/software/api) |

### Test Data
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Adorable Avatars | Generate random cartoon avatars | No | Yes | Unknown | [Go!](http://avatars.adorable.io) |
| Bacon Ipsum | A Meatier Lorem Ipsum Generator | No | Yes | Unknown | [Go!](https://baconipsum.com/json-api/) |
| Dicebear Avatars | Generate random pixel-art avatars | No | Yes | Unknown | [Go!](https://avatars.dicebear.com/) |
| FakeJSON | Service to generate test and fake data | `apiKey` | Yes | Yes | [Go!](https://fakejson.com) |
| FHIR | Fast Healthcare Interoperability Resources test data | No | Yes | Unknown | [Go!](http://fhirtest.uhn.ca/home) |
| Hipster Ipsum | Generates Hipster Ipsum text | No | No | Unknown | [Go!](http://hipsterjesus.com/) |
| JSONPlaceholder | Fake data for testing and prototyping | No | No | Unknown | [Go!](http://jsonplaceholder.typicode.com/) |
| Lorem Text | Generates Lorem Ipsum text | `X-Mashape-Key` | Yes | Unknown | [Go!](https://market.mashape.com/montanaflynn/lorem-text-generator) |
| LoremPicsum | Generate placeholder pictures | No | No | Unknown | [Go!](http://lorempicsum.com) |
| Loripsum | The "lorem ipsum" generator that doesn't suck | No | No | Unknown | [Go!](http://loripsum.net/) |
| RandomUser | Generates random user data | No | Yes | Unknown | [Go!](https://randomuser.me) |
| RoboHash | Generate random robot/alien avatars | No | Yes | Unknown | [Go!](https://robohash.org/) |
| UI Names | Generate random fake names | No | Yes | Unknown | [Go!](https://github.com/thm/uinames) |
| Yes No | Generate yes or no randomly | No | Yes | Unknown | [Go!](https://yesno.wtf/api) |

### Text Analysis
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Aylien Text Analysis | A collection of information retrieval and natural language APIs | `apiKey` | Yes | Unknown | [Go!](http://docs.aylien.com/) |
| Detect Language | Detects text language | `apiKey` | Yes | Unknown | [Go!](https://detectlanguage.com/) |
| Google Cloud Natural | Natural language understanding technology, including sentiment, entity, and syntax analysis | `apiKey` | Yes | Unknown | [Go!](https://cloud.google.com/natural-language/docs/) |
| Semantira | Text Analytics with sentiment analysis, categorization & named entity extraction | `OAuth` | Yes | Unknown | [Go!](https://semantria.readme.io/docs) |
| Watson Natural Language Understanding | Natural language processing for advanced text analysis | `OAuth` | Yes | Unknown | [Go!](https://www.ibm.com/watson/developercloud/natural-language-understanding/api/v1/) |

### Tracking
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Postmon | An API to query Brazilian ZIP codes and orders easily, quickly and free | No | No | Unknown | [Go!](http://postmon.com.br) |
| Sweden | Provides information about parcels in transport | `apiKey` | No | Unknown | [Go!](https://developer.postnord.com/docs2) |
| UPS | Shipment and Address information | `apiKey` | Yes | Unknown | [Go!](https://www.ups.com/upsdeveloperkit) |

### Transportation
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| ADS-B Exchange | Access real-time and historical data of any and all airborne aircraft | No | Yes | Unknown | [Go!](https://www.adsbexchange.com/data/) |
| AIS Hub | Real-time data of any marine and inland vessel equipped with AIS tracking system | `apiKey` | No | Unknown | [Go!](http://www.aishub.net/api) |
| AIS Web | Aeronautical information in digital media produced by the Department of Airspace Control (DECEA) | `apiKey` | No | Unknown | [Go!](http://www.aisweb.aer.mil.br/api/doc/index.cfm) |
| Amadeus Travel Innovation Sandbox | Travel Search - Limited usage | `apiKey` | Yes | Unknown | [Go!](https://sandbox.amadeus.com/) |
| Bay Area Rapid Transit | Stations and predicted arrivals for BART | `apiKey` | No | Unknown | [Go!](http://api.bart.gov) |
| Community Transit | Transitland API | No | Yes | Unknown | [Go!](https://github.com/transitland/transitland-datastore/blob/master/README.md#api-endpoints) |
| Goibibo | API for travel search | `apiKey` | Yes | Unknown | [Go!](https://developer.goibibo.com/docs) |
| GraphHopper | A-to-B routing with turn-by-turn instructions | `apiKey` | Yes | Unknown | [Go!](https://graphhopper.com/api/1/docs/) |
| Icelandic APIs | Open APIs that deliver services in or regarding Iceland | No | Yes | Unknown | [Go!](http://docs.apis.is/) |
| Indian Railways | Indian Railways Information | `apiKey` | No | Unknown | [Go!](http://api.erail.in/) |
| Izi | Audio guide for travellers | `apiKey` | Yes | Unknown | [Go!](http://api-docs.izi.travel/) |
| Navitia | The open API for building cool stuff with transport data | `apiKey` | Yes | Unknown | [Go!](https://api.navitia.io/) |
| REFUGE Restrooms | Provides safe restroom access for transgender, intersex, and gender nonconforming individuals | No | Yes | Unknown | [Go!](https://www.refugerestrooms.org/api/docs/#!/restrooms) |
| Schiphol Airport | Schiphol | `apiKey` | Yes | Unknown | [Go!](https://developer.schiphol.nl/) |
| TransitLand | Transit Aggregation | No | Yes | Unknown | [Go!](https://transit.land/documentation/datastore/api-endpoints.html) |
| Transport for Atlanta, US | Marta | No | No | Unknown | [Go!](http://www.itsmarta.com/app-developer-resources.aspx) |
| Transport for Auckland, New Zealand | Auckland Transport | No | Yes | Unknown | [Go!](https://api.at.govt.nz/) |
| Transport for Belgium | Belgian transport API | No | Yes | Unknown | [Go!](https://hello.irail.be/api/) |
| Transport for Berlin, Germany | Third-party VBB API | No | Yes | Unknown | [Go!](https://github.com/derhuerst/vbb-rest/blob/master/docs/index.md) |
| Transport for Boston, US | MBTA API | No | No | Unknown | [Go!](http://realtime.mbta.com/Portal/Home/Documents) |
| Transport for Budapest, Hungary | Budapest public transport API | No | Yes | Unknown | [Go!](https://apiary.io/) |
| Transport for Chicago, US | CTA | No | No | Unknown | [Go!](http://www.transitchicago.com/developers/) |
| Transport for Czech Republic | Czech transport API | No | Yes | Unknown | [Go!](https://www.chaps.cz/eng/products/idos-internet) |
| Transport for Denver, US | RTD | No | No | Unknown | [Go!](http://www.rtd-denver.com/gtfs-developer-guide.shtml) |
| Transport for Finland | Finnish transport API | No | Yes | Unknown | [Go!](https://digitransit.fi/en/developers/ ) |
| Transport for Germany | Deutsche Bahn (DB) API | `apiKey` | No | Unknown | [Go!](http://data.deutschebahn.com/dataset/api-fahrplan) |
| Transport for India | India Public Transport API | `apiKey` | Yes | Unknown | [Go!](https://data.gov.in/sector/transport) |
| Transport for London, England | TfL API | No | Yes | Unknown | [Go!](https://api.tfl.gov.uk) |
| Transport for Madrid, Spain | Madrid BUS transport API | `apiKey` | No | Unknown | [Go!](http://opendata.emtmadrid.es/Servicios-web/BUS) |
| Transport for Minneapolis, US | NexTrip API | `OAuth` | No | Unknown | [Go!](http://svc.metrotransit.org/) |
| Transport for New York City, US | MTA | `apiKey` | No | Unknown | [Go!](http://datamine.mta.info/) |
| Transport for Norway | Norwegian transport API | No | No | Unknown | [Go!](http://reisapi.ruter.no/help) |
| Transport for Ottawa, Canada | OC Transpo next bus arrival API | No | No | Unknown | [Go!](http://www.octranspo.com/index.php/developers) |
| Transport for Paris, France | RATP Open Data API | No | No | Unknown | [Go!](http://data.ratp.fr/api/v1/console/datasets/1.0/search/) |
| Transport for Paris, France | Live schedules made simple | No | No | Unknown | [Go!](http://restratpws.azurewebsites.net/swagger/) |
| Transport for Philadelphia, US | SEPTA APIs | No | No | Unknown | [Go!](http://www3.septa.org/hackathon/) |
| Transport for Sao Paulo, Brazil | SPTrans | `OAuth` | No | Unknown | [Go!](http://www.sptrans.com.br/desenvolvedores/APIOlhoVivo/Documentacao.aspx) |
| Transport for Sweden | Public Transport consumer | `OAuth` | Yes | Unknown | [Go!](https://www.trafiklab.se/api) |
| Transport for Switzerland | Swiss public transport API | No | Yes | Unknown | [Go!](https://transport.opendata.ch/) |
| Transport for Switzerland | Official Swiss Public Transport Open Data | `apiKey` | Yes | Unknown | [Go!](https://opentransportdata.swiss/en/) |
| Transport for The Netherlands | NS, only trains | `apiKey` | No | Unknown | [Go!](http://www.ns.nl/reisinformatie/ns-api) |
| Transport for The Netherlands | OVAPI, country-wide public transport | No | Yes | Unknown | [Go!](https://github.com/skywave/KV78Turbo-OVAPI/wiki) |
| Transport for Toronto, Canada | TTC | No | Yes | Unknown | [Go!](https://myttc.ca/developers) |
| Transport for United States | NextBus API | No | No | Unknown | [Go!](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf) |
| Transport for Vancouver, Canada | TransLink | `OAuth` | Yes | Unknown | [Go!](https://developer.translink.ca/) |
| Transport for Victoria, AU | PTV API | `apiKey` | Yes | Unknown | [Go!](https://www.ptv.vic.gov.au/about-ptv/ptv-data-and-reports/digital-products/ptv-timetable-api/) |
| Transport for Washington, US | Washington Metro transport API | `OAuth` | Yes | Unknown | [Go!](https://developer.wmata.com/) |
| Uber | Uber ride requests and price estimation | `OAuth` | Yes | Yes | [Go!](https://developer.uber.com/products) |
| WhereIsMyTransport | Platform for public transport data in emerging cities | `OAuth` | Yes | Unknown | [Go!](https://developer.whereismytransport.com/) |

### URL Shorteners
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Bitly | URL shortener and link management | `OAuth` | Yes | Unknown | [Go!](http://dev.bitly.com/get_started.html) |
| ClickMeter | Monitor, compare, and optimize your marketing links | `apiKey` | Yes | Unknown | [Go!](https://support.clickmeter.com/hc/en-us/categories/201474986) |
| Google URL Shortener | Takes long URLs and squeezes them into fewer characters to make a link that is easier to share | `apiKey` | Yes | Unknown | [Go!](https://developers.google.com/url-shortener/v1/getting_started) |
| Rebrandly | Custom URL shortener for sharing branded links | `apiKey` | Yes | Unknown | [Go!](https://developers.rebrandly.com/v1/docs) |

### Vehicle
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| Brazilian Vehicles and Prices | Vehicles information from Fundação Instituto de Pesquisas Econômicas - Fipe | No | Yes | Unknown | [Go!](https://deividfortuna.github.io/fipe/) |
| Kelley Blue Book | Vehicle info, pricing, configuration, plus much more | `apiKey` | Yes | No | [Go!](http://developer.kbb.com/#!/data/1-Default) |
| Mercedes-Benz | Telematics data, remotely access vehicle functions, car configurator, locate service dealers | `apiKey` | Yes | No | [Go!](https://developer.mercedes-benz.com/apis) |
| NHTSA | NHTSA Product Information Catalog and Vehicle Listing | No | Yes | Unknown | [Go!](https://vpic.nhtsa.dot.gov/api/) |

### Video
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| An API of Ice And Fire | Game Of Thrones API | No | Yes | Unknown | [Go!](https://anapioficeandfire.com/) |
| Czech Television | TV programme of Czech TV | No | No | Unknown | [Go!](http://www.ceskatelevize.cz/xml/tv-program/) |
| Dailymotion | Dailymotion Developer API | `OAuth` | Yes | Unknown | [Go!](https://developer.dailymotion.com/) |
| Open Movie Database | Movie information | `apiKey` | Yes | Unknown | [Go!](http://www.omdbapi.com/) |
| Ron Swanson Quotes | Television | No | Yes | Unknown | [Go!](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api) |
| SWAPI | Star Wars Information | No | Yes | Unknown | [Go!](https://swapi.co) |
| TMDb | Community-based movie data | `apiKey` | Yes | Unknown | [Go!](https://www.themoviedb.org/documentation/api) |
| TVDB | Television data | `apiKey` | Yes | Unknown | [Go!](https://api.thetvdb.com/swagger) |
| TVMaze | TV Show Data | No | No | Unknown | [Go!](http://www.tvmaze.com/api) |
| Utelly | Check where a tv show or movie is available | `X-Mashape-Key` | Yes | Unknown | [Go!](https://market.mashape.com/utelly/utelly) |
| Vimeo | Vimeo Developer API | `OAuth` | Yes | Unknown | [Go!](https://developer.vimeo.com/) |
| YouTube | Add YouTube functionality to your sites and apps | `OAuth` | Yes | Unknown | [Go!](https://developers.google.com/youtube/) |

### Weather
API | Description | Auth | HTTPS | CORS | Link |
|---|---|---|---|---|---|
| ClimaCell Micro Weather | Historical, real-time, and nowcast weather data | `apiKey` | Yes | Yes | [Go!](https://developer.climacell.co) |
| Dark Sky | Weather | `apiKey` | Yes | No | [Go!](https://darksky.net/dev/) |
| MetaWeather | Weather | No | Yes | No | [Go!](https://www.metaweather.com/api/) |
| ODWeather | Weather and weather webcams | No | No | Unknown | [Go!](http://api.oceandrivers.com/static/docs.html) |
| OpenUV | Real-time UV Index Forecast | `apiKey` | Yes | Unknown | [Go!](https://www.openuv.io) |
| OpenWeatherMap | Weather | `apiKey` | No | Unknown | [Go!](http://openweathermap.org/api) |
| Storm Glass | Global marine weather from multiple sources | `apiKey` | Yes | Yes | [Go!](https://stormglass.io/) |
| Weatherbit | Weather | `apiKey` | Yes | Unknown | [Go!](https://www.weatherbit.io/api) |
| Yahoo! Weather | Weather | `apiKey` | Yes | Unknown | [Go!](https://developer.yahoo.com/weather/) |
