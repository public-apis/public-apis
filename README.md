# Public APIs [![Build Status](https://api.travis-ci.org/toddmotto/public-apis.svg)](https://travis-ci.org/toddmotto/public-apis)

A collective list of free JSON APIs for use in web development.

For information on contributing to this project, please see the [contributing guide](CONTRIBUTING.md).

## Index

* [Animals](#animals)
* [Anime](#anime)
* [Anti-Malware](#anti-malware)
* [Art & Design](#art--design)
* [Books](#books)
* [Business](#business)
* [Calendar](#calendar)
* [Cloud Storage & File Sharing](#cloud-storage--file-sharing)
* [Currency Exchange](#currency-exchange)
* [Data Access](#data-access)
* [Data Validation](#data-validation)
* [Development](#development)
* [Documents & Productivity](#documents--productivity)
* [Environment](#environment)
* [Finance](#finance)
* [Food & Drink](#food--drink)
* [Fraud Prevention](#fraud-prevention)
* [Games & Comics](#games--comics)
* [Geocoding](#geocoding)
* [Health](#health)
* [Machine Learning](#machine-learning)
* [Math](#math)
* [Music](#music)
* [News](#news)
* [Open Source projects](#open-source-projects)
* [Personality](#personality)
* [Photography](#photography)
* [Science](#science)
* [Security](#security)
* [Shopping](#shopping)
* [Social](#social)
* [Sports & Fitness](#sports--fitness)
* [Transportation](#transportation)
* [University](#university)
* [Vehicle](#vehicle)
* [Video](#video)
* [Weather](#weather)

### Animals

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| IUCN | IUCN Red List of Threatened Species | `token` | No | [Go!](http://apiv3.iucnredlist.org/api/v3/docs) |
| Petfinder | Adoption | Yes | Yes | [Go!](https://www.petfinder.com/developers/api-docs/) |
| RescueGroups | Adoption | No | Yes | [Go!](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) |

### Anime

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| AniList | AniList Anime | `OAuth` | No | [Go!](http://anilist-api.readthedocs.io/en/latest/) |
| Kitsu | Kitsu Anime | `OAuth` | No | [Go!](http://docs.kitsu17.apiary.io/) |
| Studio Ghibli | Resources from Studio Ghibli films | No | Yes | [Go!](https://ghibliapi.herokuapp.com) |

### Anti-Malware

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Certly | Certly Link/Domain Flagging | `token` | Yes | [Go!](https://guard.certly.io/) |
| Google Safe Browsing | Google Link/Domain Flagging | `token` | Yes | [Go!](https://developers.google.com/safe-browsing/) |
| Metacert | Metacert Link Flagging | `token` | Yes | [Go!](https://metacert.com/) |
| VirusTotal | VirusTotal File/URL Analysis | `token` | Yes | [Go!](https://www.virustotal.com/en/documentation/public-api/) |
| Web Of Trust (WOT) | Website reputation | `key` string | Yes | [Go!](https://www.mywot.com/wiki/API) |

### Art & Design

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Dribbble | Design | `OAuth` | No | [Go!](http://developer.dribbble.com/v1/) |
| Noun Project | Icons | `OAuth` | No | [Go!](http://api.thenounproject.com/index.html) |
| Rijksmuseum| Art | No | Yes | [Go!](https://www.rijksmuseum.nl/en/api) |

### Books

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| British National Bibliography | Books | No | No | [Go!](http://bnb.data.bl.uk/) |
| Good Reads | Books | No | Yes | [Go!](https://www.goodreads.com/api) |
| Google Books | Books | `OAuth` | Yes | [Go!](https://developers.google.com/books/) |

### Business

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| mailgun | Email Service | `apiKey` query string | Yes | [Go!](https://www.mailgun.com/) |
| markerapi | Trademark Search | No | No | [Go!](http://www.markerapi.com/) |

### Calendar

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Church Calendar | Catholic liturgical calendar | No | No | [Go!](http://calapi.inadiutorium.cz/) |
| Holidays | Free API for obtaining information about holidays. | `key` string | Yes | [Go!](https://holidayapi.com/) |
| LectServe | Protestant liturgical calendar | No | No | [Go!](http://www.lectserve.com) |
| Non-Working Days | Database of ICS files for non working days | No | Yes | [Go!](https://github.com/gadael/icsdb) |

### Cloud Storage & File Sharing

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Box | File Sharing and Storage | `OAuth` | Yes | [Go!](https://developer.box.com/) |
| Dropbox | File Sharing and Storage | `OAuth` | Yes | [Go!](https://www.dropbox.com/developers) |
| Google Drive | File Sharing and Storage | `OAuth` | Yes | [Go!](https://developers.google.com/drive/) |
| OneDrive | File Sharing and Storage | `OAuth` | Yes | [Go!](https://dev.onedrive.com/) |

### Currency Exchange

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Currencylayer | Exchange rates and currency conversion | `apiKey` query string | Yes | [Go!](https://currencylayer.com/documentation) |
| Fixer.io | Exchange rates and currency conversion | No | Yes | [Go!](http://fixer.io) |

### Data Access

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| 18F | US Federal Government /Developer Program | No | No | [Go!](http://18f.github.io/API-All-the-X/) |
| Abbreviation | Get abbreviations and meanings | `X-Mashape-Key` as header | Yes | [Go!](https://market.mashape.com/daxeel/abbreviations) |
| CARTO | Location Information Prediction | `apiKey` | Yes | [Go!](https://carto.com/) |
| Callook.info | United States ham radio callsigns | No | Yes | [Go!](https://callook.info) |
| Celebinfo | Celebrity information | `X-Mashape-Key` as header | Yes | [Go!](https://market.mashape.com/daxeel/celebinfo/) |
| Colorado Data Engine | Formatted and geolocated Colorado public data | No | Yes | [Go!](http://codataengine.org/) |
| Colorado Information Marketplace | Colorado State Government Open Data | No | Yes | [Go!](https://data.colorado.gov/) |
| Data USA | US Public Data | No | Yes | [Go!](https://datausa.io/about/api/) |
| Dronestream | Tracks United States drone strikes | No | No | [Go!](http://dronestre.am/) |
| fonoApi | Mobile Device Description | No | Yes | [Go!](https://fonoapi.freshpixl.com/) |
| Open Government, Australia | Australian Government Open Data | No | Yes | [Go!](https://www.data.gov.au/) |
| Open Government, USA | United States Government Open Data | No | Yes | [Go!](https://www.data.gov/) |
| Open Government, Canada | Canadian Government Open Data | No | No | [Go!](http://open.canada.ca/en) |
| Open Government Data, India | Indian Government Open Data | `token` | Yes | [Go!](https://data.gov.in/) |
| Pearson | Dictionary Data | `apiKey` query string | No | [Go!](http://developer.pearson.com/apis/dictionaries) |
| Prague Opendata | Prague City Open Data | No | No | [Go!](http://opendata.praha.eu/en) |
| Quandl | Stock Market Data | No | Yes | [Go!](https://www.quandl.com/) |
| Represent by Open North | Find Canadian Government Representatives | No | Yes | [Go!](https://represent.opennorth.ca/) |
| Scoop.it | Content Curation Service | `apiKey` query string | No | [Go!](http://www.scoop.it/dev) |
| Teleport | Quality of Life Data | No | Yes | [Go!](https://developers.teleport.org/) |
| Wikipedia | Mediawiki Encyclopedia | No | Yes | [Go!](https://www.mediawiki.org/wiki/API:Main_page) |
| Wordnik | Dictionary Data | No | No | [Go!](http://developer.wordnik.com) |
| Yelp | Find Local Business | `OAuth` | Yes | [Go!](https://www.yelp.com/developers) |

### Data Validation

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| languagelayer | Language detection | No | Yes | [Go!](https://languagelayer.com) |
| mailboxlayer | Email address validation | No | Yes | [Go!](https://mailboxlayer.com) |
| numverify | Phone number validation | No | Yes | [Go!](https://numverify.com) |
| vatlayer | VAT number validation | No | Yes | [Go!](https://vatlayer.com) |

### Development

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Adorable Avatars | Generate random cartoon avatars | No | Yes | [Go!](http://avatars.adorable.io) |
| APIs.guru | Wikipedia for Web APIs, OpenAPI/Swagger specs for public APIs | No | Yes | [Go!](https://apis.guru/api-doc/) |
| CDNJS | Library info on CDNJS | No | Yes | [Go!](https://api.cdnjs.com/libraries/jquery) |
| Faceplusplus | A tool to detect face | `OAuth` | Yes | [Go!](https://www.faceplusplus.com/) |
| Genderize.io | Determines a gender from a first name | No | Yes | [Go!](https://genderize.io) |
| Github - User Data | Pull public information for a user's github | No | Yes | [Go!](https://api.github.com/users/hackeryou) |
| Gitter | Chat for GitHub | `OAuth` | Yes | [Go!](https://developer.gitter.im/docs/welcome) |
| Hipster Ipsum | Generates Hipster Ipsum text | No | No | [Go!](http://hipsterjesus.com/) |
| IPify | A simple IP Address API  | No | Yes | [Go!](https://www.ipify.org/) |
| JSONPlaceholder | Fake data for testing and prototyping | No | No | [Go!](http://jsonplaceholder.typicode.com/) |
| LiveEdu | Live Coding Streaming | `OAuth` | Yes | [Go!](https://www.liveedu.tv/developer/applications/) |
| Lorem Text | Generates Lorem Ipsum text | `X-Mashape-Key` as header | Yes | [Go!](https://market.mashape.com/montanaflynn/lorem-text-generator) |
| Loripsum | The "lorem ipsum" generator that doesn't suck | No | No | [Go!](http://loripsum.net/) |
| Myjson | A simple JSON store for your web or mobile app | No | No | [Go!](http://myjson.com/api) |
| Plino | Spam filtering system | No | Yes | [Go!](https://plino.herokuapp.com/) |
| Random Word | Generate random word | No | No | [Go!](http://www.setgetgo.com/randomword/) |
| RandomUser | Generates random user data | No | Yes | [Go!](https://randomuser.me) |
| ReqRes | A hosted REST-API ready to respond to your AJAX requests | No | Yes | [Go!](https://reqres.in/ ) |
| RoboHash | Generate random robot/alien avatars | No | Yes | [Go!](https://robohash.org/) |
| StackExchange | Q&A forum for developers | `OAuth` | Yes | [Go!](https://api.stackexchange.com/) |
| Stormpath | User Authentication | `apiKey` | Yes | [Go!](https://stormpath.com/) |
| UI Names | Generate random fake names | No | Yes | [Go!](https://github.com/thm/uinames) |

### Documents & Productivity

| API | Description | Auth | HTTPS |Link |
|---|---|---|---|---|
| File.io | File Sharing | No | No | [Go!](http://www.file.io) |
| pdflayer API | HTML/URL to PDF | No | Yes | [Go!](https://pdflayer.com) |
| Todoist | Todo Lists | `OAuth` | Yes | [Go!](https://developer.todoist.com) |
| Wunderlist | Todo Lists | `OAuth` | Yes | [Go!](https://developer.wunderlist.com/documentation) |

### Environment

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| PM2.5.in | PM2.5 Data of China | `apiKey` query string | No | [Go!](http://www.pm25.in/api_doc) |

### Finance

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Barchart OnDemand | Stock, Futures, and Forex Market Data | `apiKey` | Yes | [Go!](https://www.barchartondemand.com/free) |

### Food & Drink

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| BigOven | Recipe Search | `X-Mashape-Key` as header | No | [Go!](http://api2.bigoven.com/) |
| BreweryDB | Beer | `apiKey` query string | No | [Go!](http://www.brewerydb.com/developers) |
| Edamam | Recipe Search | `apiKey` query string | Yes | [Go!](https://developer.edamam.com/) |
| Food2Fork | Recipe Search | `apiKey` query string | No | [Go!](http://food2fork.com/about/api) |
| LCBO | Alcohol | `apiKey` query string | Yes | [Go!](https://lcboapi.com/) |
| PunkAPI | Brewdog Beer Recipes | No | Yes | [Go!](https://punkapi.com/) |
| Recipe Puppy | Food | No | No | [Go!](http://www.recipepuppy.com/about/api/) |
| Yummly | Find food recipes | No | Yes | [Go!](https://developer.yummly.com/) |

### Fraud Prevention

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Whitepages Pro | Global identity verification with phone, address, email, and IP | `apiKey` | Yes | [Go!](https://pro.whitepages.com/developer/documentation/identity-check-api/) |
| Whitepages Pro | Phone reputation to detect spammy phones | `apiKey` | Yes | [Go!](https://pro.whitepages.com/developer/documentation/phone-reputation-api/) |
| Whitepages Pro | Get an owner’s name, address, demographics based on the phone number | `apiKey` | Yes | [Go!](https://pro.whitepages.com/developer/documentation/reverse-phone-api/) |
| Whitepages Pro| Phone number validation, line_type, carrier append | `apiKey` | Yes | [Go!](https://pro.whitepages.com/developer/documentation/phone-intelligence-api/) |
| Whitepages Pro| Get normalized physical address, residents, address type, and validity. | `apiKey` | Yes | [Go!](https://pro.whitepages.com/developer/documentation/reverse-address-api/) |

### Games & Comics

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Battle.net | Blizzard Entertainment | No | Yes | [Go!](https://dev.battle.net/)  |
| Chuck Norris Database | Jokes | No | No | [Go!](http://www.icndb.com/api/) |
| Clash of Clans | Clash of Clans Game Information | No | Yes | [Go!](https://developer.clashofclans.com) |
| Clash Royale | Clash Royale Game Information | No | Yes | [Go!](https://github.com/martincarrera/clash-royale-api)  |
| Comic Vine | Comics | No | Yes | [Go!](https://comicvine.gamespot.com/api/documentation) |
| Deck of Cards | Deck of Cards | No | No | [Go!](http://deckofcardsapi.com/)  |
| Eve Online | Third-Party Developer Documentation | `OAuth` required for some parts | Yes | [Go!](https://eveonline-third-party-documentation.readthedocs.io/en/latest/) |
| Giant Bomb | Video Games | No | Yes | [Go!](https://www.giantbomb.com/api/documentation) |
| Guild Wars 2 | Guild Wars 2 Game Information | `apiKey` query string (for some routes) | Yes | [Go!](https://wiki.guildwars2.com/wiki/API:Main) |
| Magic The Gathering | Magic The Gathering Game Information | No | No | [Go!](http://magicthegathering.io/) |
| Marvel | Marvel Comics | No | No | [Go!](http://developer.marvel.com) |
| Minecraft | Minecraft server info & user info) | No | Yes | [Go!](https://mcapi.ca/) |
| Open Trivia | Trivia Questions | No | Yes | [Go!](https://opentdb.com/api_config.php) |
| Pokéapi | Pokémon Information | No | No | [Go!](http://pokeapi.co) |
| Riot Games | League of Legends Game Information | `apiKey` | Yes | [Go!](https://developer.riotgames.com/) |
| Steam | Steam Client Interaction | `OAuth` | Yes | [Go!](https://developer.valvesoftware.com/wiki/Steam_Web_API) |
| SWAPI | Star Wars Information | No | Yes | [Go!](https://swapi.co) |

### Geocoding

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Bing Maps | Create/customize digital maps based on Bing Maps data | `apiKey` | Yes | [Go!](https://www.microsoft.com/maps/choose-your-bing-maps-API.aspx) |
| Geocode.xyz | Provides worldwide forward/reverse geocoding, batch geocoding and geoparsing | No | Yes | [Go!](https://geocode.xyz/) |
| GeoNames | Place names and other geographical data | No | No | [Go!](http://www.geonames.org/export/web-services.html) |
| GéoApi | French geographical data | No | Yes | [Go!](https://api.gouv.fr/api/geoapi.html) |
| Google Maps | Create/customize digital maps based on Google Maps data | `apiKey` query string | Yes | [Go!](https://developers.google.com/maps/) |
| IP 2 Country | Map an IP to a country | No | Yes | [Go!](https://ip2country.info) |
| IP Address Details| Find geolocation with ip address | No | Yes | [Go!](https://ipinfo.io/) |
| IP Vigilante | Free IP Geolocation API | No | Yes | [Go!](https://www.ipvigilante.com/) |
| Mapbox | Create/customize beautiful digital maps | `apiKey` query string | Yes | [Go!](https://www.mapbox.com/developers/) |
| Mapzen Search | Open Source & Open Data Global Geocoding Service | No | Yes | [Go!](https://mapzen.com/products/search/) |
| Mexico | Mexico RESTful zip codes API | No | Yes | [Go!](https://github.com/IcaliaLabs/sepomex) |
| OpenCage | Forward and reverse geocoding using open data | No | Yes | [Go!](https://geocoder.opencagedata.com) |
| OpenStreetMap | Navigation, geolocation and geographical data | `OAuth` | No | [Go!](http://wiki.openstreetmap.org/wiki/API) |
| PostcodeData.nl | Provide geolocation data based on postcode for Dutch addresses | No | No | [Go!](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) |
| Postcodes.io | Postcode lookup & Geolocation for the UK | No | Yes | [Go!](https://postcodes.io) |
| Utah AGRC | Utah Web API for geocoding Utah addresses | `apiKey` | Yes | [Go!](https://api.mapserv.utah.gov) |
| ViaCep | Brazil RESTful zip codes API | No | Yes | [Go!](https://viacep.com.br) |

### Health

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Diabetes | Logging and retrieving diabetes information | No | No | [Go!](http://predictbgl.com/api/) |
| Flutrack | Influenza-like symptoms with geotracking | No | No | [Go!](http://www.flutrack.org/) |
| Makeup | Makeup Information | No | No | [Go!](http://makeup-api.herokuapp.com/) |
| Nutritionix | Worlds largest verified nutrition database | `apiKey` query string | Yes | [Go!](https://developer.nutritionix.com/) |
| openFDA | Public FDA data about drugs, devices, and foods | No | Yes | [Go!](https://open.fda.gov/api/) |
| USDA Nutrients | National Nutrient Database for Standard Reference | No | Yes | [Go!](https://ndb.nal.usda.gov/ndb/doc/index) |

### Machine Learning

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| API.AI | Natural Language Processing | `apikey` | Yes | [Go!](https://api.ai/) |
| Clarifai | Computer Vision | `OAuth` | Yes | [Go!](https://developer.clarifai.com/) |
| Cleverbot | Web chat bot | `apikey` | Yes | [Go!](https://www.cleverbot.com/api/) |
| Unplugg | Forecasting API for timeseries data | `apikey` | Yes | [Go!](https://unplu.gg/test_api.html) |
| Wit.ai | Natural Language Processing | `OAuth` | Yes | [Go!](https://wit.ai/) |

### Math

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Newton | Symbolic and Arithmetic Math Calculator | No | Yes | [Go!](https://newton.now.sh/) |

### Music

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Deezer | Music | `OAuth` | No | [Go!](http://developers.deezer.com/login?redirect=/api) |
| Discogs | Music | `OAuth` | Yes | [Go!](https://www.discogs.com/developers/) |
| Genius | Crowdsourced lyrics and music knowledge | `OAuth` | Yes | [Go!](https://docs.genius.com/) |
| Jamendo | Music | `OAuth` | Yes | [Go!](https://developer.jamendo.com/v3.0) |
| iTunes Search | Software products | No | Yes | [Go!](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) |
| LastFm | Music | No | No | [Go!](http://www.last.fm/api) |
| Mixcloud | Music | No | Yes | [Go!](https://www.mixcloud.com/developers/) |
| MusicBrainz | Music | No | Yes | [Go!](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2) |
| Musikki | Music | No | Yes | [Go!](https://music-api.musikki.com/reference) |
| Musixmatch | Music | `apikey` query string | Yes | [Go!](https://developer.musixmatch.com/) |
| Songsterr | Provides guitar, bass and drums tabs and chords  | No | Yes | [Go!](https://www.songsterr.com/a/wa/api/) |
| Soundcloud | Music | No | Yes | [Go!](https://developers.soundcloud.com/) |
| Spotify | Music | `OAuth` required for some parts | Yes | [Go!](https://developer.spotify.com/web-api/) |
| Vagalume | Crowdsourced lyrics and music knowledge | `apikey` query string | Yes | [Go!](https://api.vagalume.com.br/docs/) |

### News

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| New York Times | Provides news | `apikey` | Yes | [Go!](https://developer.nytimes.com/) |
| News API | headlines currently published on a range of news sources and blogs | `apikey` | Yes | [Go!](https://newsapi.org/) |

### Open Source projects

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Countly  | Countly web analytics | No | No | [Go!](http://resources.count.ly/docs) |
| Drupal.org | Drupal.org | No | Yes | [Go!](https://www.drupal.org/drupalorg/docs/api) |
| Libraries.io | Open source software libraries | `apiKey` query string | Yes | [Go!](https://libraries.io/api) |

### Personality

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| chucknorris.io | JSON API for hand curated Chuck Norris jokes | No | Yes | [Go!](https://api.chucknorris.io) |
| Forismatic | Inspirational Quotes | No | No | [Go!](http://forismatic.com/en/api/) |
| Medium | Community of readers and writers offering unique perspectives on ideas. | `OAuth` | Yes | [Go!](https://github.com/Medium/medium-api-docs) |
| Quotes on Design | Inspirational Quotes | No | Yes | [Go!](https://quotesondesign.com/api-v4-0/) |
| Traitify | Assess, collect, and analyze Personality | No | Yes | [Go!](https://app.traitify.com/developer) |
| tronalddump.io | Api & web archive for the dumbest things Donald Trump has ever said | No | Yes | [Go!](https://www.tronalddump.io) |

### Photography

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| 500px |  Photography Community | `OAuth` | Yes | [Go!](https://github.com/500px/api-documentation) |
| Flickr | Flickr Services | `OAuth` | Yes | [Go!](https://www.flickr.com/services/api/) |
| Gfycat | Jiffier GIFs | `OAuth` | Yes | [Go!](https://developers.gfycat.com/api/) |
| Giphy | Get all your gifs | No | Yes | [Go!](https://github.com/Giphy/GiphyAPI) |
| Imgur | Images | `OAuth` | Yes | [Go!](https://api.imgur.com/#overview) |
| ScreenShotLayer | URL 2 Image | No | Yes | [Go!](https://screenshotlayer.com) |
| Unsplash | Photography | `OAuth` | Yes | [Go!](https://unsplash.com/developers) |

### Science

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Fedger.io | Query machine intelligence data | No | Yes | [Go!](https://dev.fedger.io/docs/) |
| inspirehep.net | High Energy Physics info. system | No | Yes | [Go!](https://inspirehep.net/info/hep/api?ln=en) |
| Launch Library | Upcoming Space Launches | No | Yes | [Go!](https://launchlibrary.net/1.2/docs/api.html) |
| Minor Planet Center | Asterank.com Information | No | No | [Go!](http://www.asterank.com/mpc) |
| NASA | NASA data, including imagery | No | Yes | [Go!](https://api.nasa.gov) |
| Open Notify | ISS astronauts, current location, etc | No | No | [Go!](http://open-notify.org/Open-Notify-API/) |
| Sunrise and Sunset | Sunset and sunrise times for a given latitude and longitude. | No | No | [Go!](http://sunrise-sunset.org/api) |
| USGS Earthquake Hazards Program | Earthquakes data real-time | No | Yes | [Go!](https://earthquake.usgs.gov/fdsnws/event/1/) |
| World Bank | World Data | No | No | [Go!](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) |

### Security

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| AXFR Database | AXFR public database | No | No | [Go!](http://api.axfrcheck.com) |
| UK Police | UK Police data | No | Yes | [Go!](https://data.police.uk/docs/) |

### Shopping

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| eBay | Sell and Buy on eBay | `OAuth` | Yes | [Go!](https://go.developer.ebay.com/) |

### Social

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Discord bot | Make bots for Discord | `OAuth` | Yes | [Go!](https://discordapp.com/developers/docs/intro) |
| Facebook API | Facebook Login, Share on FB, Social Plugins, Analytics and more | `OAuth` | Yes | [Go!](https://developers.facebook.com/) |
| Foursquare | Interact with Foursquare users and places (geolocation-based checkins, photos, tips, events, etc) | `OAuth` | Yes | [Go!](https://developer.foursquare.com/) |
| Fuck Off as a Service | Asks someone to fuck off | No | Yes | [Go!](https://www.foaas.com) |
| Full Contact | Get Social Media profiles and contact Information | `OAuth` | Yes | [Go!](https://www.fullcontact.com/developer/docs/) |
| HackerNews | Social news for CS and entrepreneurship | No | Yes | [Go!](https://github.com/HackerNews/API) |
| Instagram | Instagram Login, Share on Instagram, Social Plugins and more | `OAuth` | Yes | [Go!](https://www.instagram.com/developer/) |
| LinkedIn | The foundation of all digital integrations with LinkedIn | `OAuth` | Yes | [Go!](https://developer.linkedin.com/docs/rest-api) |
| Telegram MTProto | Read and write Telegram data | `OAuth` | Yes | [Go!](https://core.telegram.org/api#getting-started) |
| Telegram bot | Simplified HTTP version of the MTProto API for bots | `OAuth` | Yes | [Go!](https://core.telegram.org/bots/api) |
| Pinterest | The world's catalog of ideas | `OAuth` | Yes | [Go!](https://developers.pinterest.com/) |
| PWRTelegram bot | Boosted version of the Telegram bot API | `OAuth` | Yes | [Go!](https://pwrtelegram.xyz) |
| Reddit | Homepage of the internet | `OAuth` required for some parts | Yes | [Go!](https://www.reddit.com/dev/api) |
| Slack | Team Instant Messaging | `OAuth` | Yes | [Go!](https://api.slack.com/) |
| Tumblr | Read and write Tumblr Data | `OAuth` | Yes | [Go!](https://www.tumblr.com/docs/en/api/v2) |
| Twitch | Game Streaming API | `OAuth` | Yes | [Go!](https://github.com/justintv/Twitch-API) |
| Twitter | Read and write Twitter data | `OAuth` | Yes | [Go!](https://dev.twitter.com/rest/public) |
| vk API | Read and write vk dat | `OAuth` | Yes | [Go!](https://vk.com/dev/sites) |

### Sports & Fitness

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| City Bikes | City Bikes around the world | No | No | [Go!](http://api.citybik.es/v2/) |
| Ergast F1 | F1 data from the beginning of the world championships in 1950 | No | No | [Go!](http://ergast.com/mrd/) |
| Fitbit | Fitbit Information | `OAuth` | Yes | [Go!](https://dev.fitbit.com/) |
| Football-Data.org | Football Data | No | No | [Go!](http://api.football-data.org/index) |
| JCDecaux Bike | JCDecaux's self-service bicycles | `apiKey` query string | Yes | [Go!](https://developer.jcdecaux.com/) |
| Cricket Live Scores | live-score | `X-Mashape-Key` as header | Yes | [Go!](https://market.mashape.com/dev132/cricket-live-scores) |
| NFL Arrests | NFL Arrest Data | No | No | [Go!](http://nflarrest.com/api/) |
| Pro Motocross | The RESTful AMA Pro Motocross lap times for every racer on the start gate | No | No | [Go!](http://promotocrossapi.com) |
| Strava | Connect with athletes, activities and more | [`OAuth`](https://strava.github.io/api/v3/oauth/)| Yes | [Go!](https://strava.github.io/api/) |
| Wger | Workout manager data as exercises, muscles or equipments | `apiKey` query string | Yes | [Go!](https://wger.de/en/software/api) |

### Transportation

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Amadeus Travel Innovation Sandbox | Travel Search - Limited usage | `apikey` query string | Yes | [Go!](https://sandbox.amadeus.com/) |
| Community Transit | Transitland API | No | Yes | [Go!](https://github.com/transitland/transitland-datastore/blob/master/README.md#api-endpoints) |
| Goibibo | API for travel search  | `apiKey` query string | Yes | [Go!](https://developer.goibibo.com/docs) |
| Indian Railways | Indian Railways Information | `token` | No | [Go!](http://api.erail.in/) |
| The Nomad List | A list of the best places to live/work remotely | No | Yes | [Go!](https://nomadlist.com/faq) |
| Schiphol Airport | Schiphol | `OAuth` | Yes | [Go!](https://flight-info.3scale.net/) |
| TransitLand | Transit Aggregation | No | Yes | [Go!](https://transit.land/documentation/datastore/api-endpoints.html) |
| Transport for Atlanta, US | Marta | No | No | [Go!](http://www.itsmarta.com/app-developer-resources.aspx) |
| Transport for Belgium | Belgian transport API | No | Yes | [Go!](https://hello.irail.be/api/) |
| Transport for Boston, MA, USA | MBTA API | No | No | [Go!](http://realtime.mbta.com/Portal/Home/Documents) |
| Transport for Budapest | Budapest public transport API | No | Yes | [Go!](https://apiary.io/) |
| Transport for Chicago, US | CTA | No | No | [Go!](http://www.transitchicago.com/developers/) |
| Transport for Czech Republic | Czech transport API | No | Yes | [Go!](https://www.chaps.cz/eng/products/idos-internet) |
| Transport for Finland | Finnish transport API | No | Yes | [Go!](https://digitransit.fi/en/developers/ ) |
| Transport for Germany | Deutsche Bahn (DB) API | `authKey` query string | No | [Go!](http://data.deutschebahn.com/dataset/api-fahrplan) |
| Transport for Berlin | third-party VBB API | No | Yes | [Go!](https://github.com/derhuerst/vbb-rest/blob/master/docs/index.md) |
| Transport for India | India Public Transport API | Api key | Yes | [Go!](https://data.gov.in/sector/transport) |
| Transport for London, England | TfL API | No | Yes | [Go!](https://api.tfl.gov.uk) |
| Transport for Minneapolis, US | NexTrip API | `OAuth` | No | [Go!](http://svc.metrotransit.org/) |
| Transport for New York City | MTA | api key | No | [Go!](http://datamine.mta.info/) |
| Transport for Norway | Norwegian transport API | No | No | [Go!](http://reisapi.ruter.no/help) |
| Transport for Ottawa, Canada | OC Transpo next bus arrival API | No | No | [Go!](http://www.octranspo.com/index.php/developers) |
| Transport for Paris, France | RATP Open Data API | No | No | [Go!](http://data.ratp.fr/api/v1/console/datasets/1.0/search/) |
| Transport for Philadelphia | SEPTA APIs | No | No | [Go!](http://www3.septa.org/hackathon/) |
| Transport for Rio de Janeiro, Brazil | Prefeitura do Rio (City Hall) | No | No | [Go!](http://data.rio/group/transporte-e-mobilidade) |
| Transport for Sweden | Public Transport consumer | `OAuth` | Yes | [Go!](https://www.trafiklab.se/api) |
| Transport for Switzerland | Swiss public transport API | No | Yes | [Go!](https://transport.opendata.ch/) |
| Transport for Switzerland | Official Swiss Public Transport Open Data | `apikey` | Yes | [Go!](https://opentransportdata.swiss/en/) |
| Transport for São Paulo, Brazil | SPTrans | `OAuth` | No | [Go!](http://www.sptrans.com.br/desenvolvedores/APIOlhoVivo/Documentacao.aspx) |
| Transport for The Netherlands | NS | No | No | [Go!](http://www.ns.nl/reisinformatie/ns-api) |
| Transport for Tokyo, Japan | Tokyo Metro | `apiKey` query string | Yes | [Go!](https://developer.tokyometroapp.jp/info)  |
| Transport for Toronto, Canada | TTC | No | Yes | [Go!](https://myttc.ca/developers) |
| Transport for Vancouver, Canada | TransLink | `OAuth` | Yes | [Go!](https://developer.translink.ca/) |
| Transport for Victoria, AU | PTV API | `authKey` | Yes | [Go!](https://www.ptv.vic.gov.au/about-ptv/ptv-data-and-reports/digital-products/ptv-timetable-api/) |
| Transport for Washington, US | Washington Metro transport API | `OAuth` | Yes | [Go!](https://developer.wmata.com/) |
| Transport for Madrid, Spain | Madrid BUS transport API | `apiKey` query string | No | [Go!](http://opendata.emtmadrid.es/Servicios-web/BUS) |
| Transport for Auckland, New Zealand | Auckland Transport API  | No | Yes | [Go!](https://api.at.govt.nz/) |
| Uber | Request Uber rides, reach riders, transport things, and reward drivers | `OAuth` | Yes | [Go!](https://developer.uber.com/) |
| WhereIsMyTransport | Platform for public transport data in emerging cities  | `OAuth` | Yes | [Go!](https://developer.whereismytransport.com/) |

### University

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Universities List | University names, countries and domains| No | Yes | [Go!](https://github.com/Hipo/university-domains-list) |

### Vehicle

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Vehicles | Lot of vehicles informations | `apiKey` query string | No | [Go!](http://developer.edmunds.com/api-documentation/overview/) |
| Brazilian Vehicles and Prices | Vehicles information from Fundação Instituto de Pesquisas Econômicas - Fipe | No | Yes | [Go!](https://deividfortuna.github.io/fipe/) |
| NHTSA Vehicles | NHTSA Product Information Catalog and Vehicle Listing | No | Yes | [Go!](https://vpic.nhtsa.dot.gov/api/) |

### Video

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| An API of Ice And Fire | Game Of Thrones API | No | Yes | [Go!](https://anapioficeandfire.com/) |
| Dailymotion | Dailymotion Developer API | `OAuth` required for some parts | Yes | [Go!](https://developer.dailymotion.com/) |
| MovieDB | Movie Data | `apiKey` | Yes | [Go!](https://www.themoviedb.org/documentation/api) |
| Netflix Roulette | Netflix database | No | No | [Go!](http://netflixroulette.net/api/) |
| OMDB | Open movie database | No | Yes | [Go!](https://omdbapi.com/) |
| Ron Swanson Quotes | Television | No | Yes | [Go!](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api) |
| TVMaze | TV Show Data | No | No | [Go!](http://www.tvmaze.com/api) |
| Vimeo | Vimeo Developer API | `OAuth` | Yes | [Go!](https://developer.vimeo.com/) |
| YouTube | Add YouTube functionality to your sites and apps. | `OAuth` required for some parts | Yes | [Go!](https://developers.google.com/youtube/) |

### Weather

| API | Description | Auth | HTTPS | Link |
|---|---|---|---|---|
| Dark Sky | Weather | `apiKey` query string | Yes | [Go!](https://darksky.net/dev/) |
| MetaWeather | Weather | No | Yes | [Go!](https://www.metaweather.com/api/) |
| OpenWeatherMap | Weather | `apiKey` query string | No | [Go!](http://openweathermap.org/api) |
| Weatherbit | Weather | `apiKey` query string | Yes | [Go!](https://www.weatherbit.io/api) |
| Wunderground | Weather | No | Yes | [Go!](https://www.wunderground.com/weather/api/) |
| Yahoo! Weather | Weather | No | Yes | [Go!](https://developer.yahoo.com/weather/) |
