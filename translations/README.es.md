# API públicas [![Build Status](https://api.travis-ci.org/public-apis/public-apis.svg)](https://travis-ci.org/public-apis/public-apis)

Una lista colectiva de API gratuitas para su uso en software y desarrollo web.

Se puede encontrar una API pública para este proyecto [aquí](https://github.com/davemachado/public-api)!

Para obtener información sobre cómo contribuir a este proyecto, consulte el [guía contribuyente](.github/CONTRIBUTING.md).

Tenga en cuenta que un estado de compilación aprobado indica que todas las API enumeradas están disponibles desde la última actualización. Un estado de compilación defectuoso indica que 1 o más servicios pueden no estar disponibles en este momento.

## Índice

- [Animales](#animals)
- [Anime](#anime)
- [Anti-Malware](#anti-malware)
- [Diseño artístico](#art--design)
- [Libros](#books)
- [Negocio](#business)
- [Calendario](#calendar)
- [Almacenamiento en la nube y uso compartido de archivos](#cloud-storage--file-sharing)
- [Integración continua](#continuous-integration)
- [Criptomoneda](#cryptocurrency)
- [Cambio de divisas](#currency-exchange)
- [Validación de datos](#data-validation)
- [Desarrollo](#development)
- [Diccionarios](#dictionaries)
- [Documentos y productividad](#documents--productivity)
- [Ambiente](#environment)
- [Eventos](#events)
- [Finanzas](#finance)
- [Comida y bebida](#food--drink)
- [Juegos y comics](#games--comics)
- [Geocodificación](#geocoding)
- [Gobierno](#government)
- [Salud](#health)
- [Trabajos](#jobs)
- [Aprendizaje automático](#machine-learning)
- [Música](#music)
- [Noticias](#news)
- [Información abierta](#open-data)
- [Proyectos de código abierto](#open-source-projects)
- [Patentar](#patent)
- [Personalidad](#personality)
- [Fotografía](#photography)
- [Ciencia matemática](#science--math)
- [Seguridad](#security)
- [Compras](#shopping)
- [Social](#social)
- [Deportes y fitness](#sports--fitness)
- [Datos de prueba](#test-data)
- [Análisis de texto](#text-analysis)
- [Rastreo](#tracking)
- [Transporte](#transportation)
- [Acortadores de URL](#url-shorteners)
- [Vehículo](#vehicle)
- [Vídeo](#video)
- [Clima](#weather)

### Animales

| FUEGO                                                                                           | Descripción                                       | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------- | ----- | ----------- |
| [Datos del gato](https://alexwohlbruck.github.io/cat-facts/)                                    | Datos diarios del gato                            | No            | si    | No          |
| [Gatos](https://docs.thecatapi.com/)                                                            | Fotos de gatos de Tumblr                          | `apiKey`      | si    | Desconocido |
| [Perros](https://dog.ceo/dog-api/)                                                              | Basado en el conjunto de datos de Stanford Dogs   | No            | si    | si          |
| [HTTPCat](https://http.cat/)                                                                    | Cat para cada estado HTTP                         | No            | si    | Desconocido |
| [UICN](http://apiv3.iucnredlist.org/api/v3/docs)                                                | Lista Roja de la UICN de especies amenazadas      | `apiKey`      | No    | Desconocido |
| [Movebank](https://github.com/movebank/movebank-api-doc)                                        | Datos de movimiento y migración de animales.      | No            | si    | Desconocido |
| [Petfinder](https://www.petfinder.com/developers/v2/docs/)                                      | Adopción                                          | `OAuth`       | si    | si          |
| [PlaceGOAT](https://placegoat.com/)                                                             | Imágenes de cabra de marcador de posición         | No            | si    | Desconocido |
| [RandomCat](https://aws.random.cat/meow)                                                        | Imágenes aleatorias de gatos                      | No            | si    | si          |
| [RandomDog](https://random.dog/woof.json)                                                       | Imágenes aleatorias de perros                     | No            | si    | si          |
| [RandomFox](https://randomfox.ca/floof/)                                                        | Imágenes aleatorias de zorros                     | No            | si    | No          |
| [Grupos de rescate](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) | Adopción                                          | No            | si    | Desconocido |
| [Shibe.Online](http://shibe.online/)                                                            | Imágenes aleatorias de Shibu Inu, gatos o pájaros | No            | si    | si          |

**[⬆ Volver al índice](#index)**

### Anime

| FUEGO                                                                     | Descripción                                | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------- | ------------------------------------------ | ------------- | ----- | ----------- |
| [AniList](https://github.com/AniList/ApiV2-GraphQL-Docs)                  | Descubrimiento y seguimiento de anime      | `OAuth`       | si    | Desconocido |
| [AnimeNewsNetwork](https://www.animenewsnetwork.com/encyclopedia/api.php) | Noticias de la industria del anime         | No            | si    | si          |
| [Jikan](https://jikan.moe)                                                | API MyAnimeList no oficial                 | No            | si    | si          |
| [Kitsu](http://docs.kitsu.apiary.io/)                                     | Plataforma de descubrimiento de anime      | `OAuth`       | si    | Desconocido |
| [Studio Ghibli](https://ghibliapi.herokuapp.com)                          | Recursos de las películas de Studio Ghibli | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Anti-Malware

| FUEGO                                                                       | Descripción                            | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------- | -------------------------------------- | ------------- | ----- | ----------- |
| [Abuso IPDB](https://docs.abuseipdb.com/)                                   | IP / dominio / URL de reputación       | `apiKey`      | si    | Desconocido |
| [AlienVault Open Threat Exchange (OTX)](https://otx.alienvault.com/api/)    | IP / dominio / URL de reputación       | `apiKey`      | si    | Desconocido |
| [Navegación segura de Google](https://developers.google.com/safe-browsing/) | Enlace de Google / Marcado de dominios | `apiKey`      | si    | Desconocido |
| [Metacert](https://metacert.com/)                                           | Metacert Link Flagging                 | `apiKey`      | si    | Desconocido |
| [VirusTotal](https://www.virustotal.com/en/documentation/public-api/)       | VirusTotal File / Análisis de URL      | `apiKey`      | si    | Desconocido |
| [Web de confianza (WOT)](https://www.mywot.com/en/API)                      | Reputación del sitio web               | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Diseño artístico

| FUEGO                                                                      | Descripción                 | Autenticación | HTTPS | CORAZONES   |
| -------------------------------------------------------------------------- | --------------------------- | ------------- | ----- | ----------- |
| [Behance](https://www.behance.net/dev)                                     | Diseño                      | `apiKey`      | si    | Desconocido |
| [Cooper Hewitt](https://collection.cooperhewitt.org/api)                   | Museo Smithsonian de Diseño | `apiKey`      | si    | Desconocido |
| [Regatear](http://developer.dribbble.com/v2/)                              | Diseño                      | `OAuth`       | No    | Desconocido |
| [Museos de arte de Harvard](https://github.com/harvardartmuseums/api-docs) | Arte                        | `apiKey`      | No    | Desconocido |
| [Iconfinder](https://developer.iconfinder.com)                             | Íconos                      | `apiKey`      | si    | Desconocido |
| [Iconos8](http://docs.icons8.apiary.io/#reference/0/meta)                  | Íconos                      | `OAuth`       | si    | Desconocido |
| [Proyecto sustantivo](http://api.thenounproject.com/index.html)            | Íconos                      | `OAuth`       | No    | Desconocido |
| [Rijksmuseum](https://www.rijksmuseum.nl/en/api)                           | Arte                        | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Libros

| FUEGO                                                                     | Descripción                                      | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------- | ------------------------------------------------ | ------------- | ----- | ----------- |
| [Bhagavad Gita](https://bhagavadgita.io/api)                              | Texto del Bhagavad Gita                          | `OAuth`       | si    | si          |
| [Bibliografía nacional británica](http://bnb.data.bl.uk/)                 | Libros                                           | No            | No    | Desconocido |
| [Goodreads](https://www.goodreads.com/api)                                | Libros                                           | `apiKey`      | si    | Desconocido |
| [libros de Google](https://developers.google.com/books/)                  | Libros                                           | `OAuth`       | si    | Desconocido |
| [LibGen](http://garbage.world/posts/libgen/)                              | Motor de búsqueda Library Genesis                | No            | No    | Desconocido |
| [Biblioteca abierta](https://openlibrary.org/developers/api)              | Libros, portadas de libros y datos relacionados. | No            | si    | Desconocido |
| [Penguin Publishing](http://www.penguinrandomhouse.biz/webservices/rest/) | Libros, portadas de libros y datos relacionados. | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Negocio

| FUEGO                                                                        | Descripción                                                                     | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Búsqueda de caridad](http://charityapi.orghunter.com/)                      | Datos de caridad sin fines de lucro                                             | `apiKey`      | No    | Desconocido |
| [Clearbit Logo](https://clearbit.com/docs#logo-api)                          | Busque logotipos de empresas e incrústelos en sus proyectos                     | `apiKey`      | si    | Desconocido |
| [Domainsdb.info](https://domainsdb.info/)                                    | Búsqueda de nombres de dominio registrados                                      | No            | si    | Desconocido |
| [Persona de libre dedicación](https://developers.freelancer.com)             | Contrata a trabajadores independientes para hacer el trabajo                    | `OAuth`       | si    | Desconocido |
| [Gmail](https://developers.google.com/gmail/api/)                            | Acceso RESTful flexible a la bandeja de entrada del usuario                     | `OAuth`       | si    | Desconocido |
| [Google analitico](https://developers.google.com/analytics/)                 | Recopile, configure y analice sus datos para llegar al público adecuado.        | `OAuth`       | si    | Desconocido |
| [Validador de buzón](https://www.mailboxvalidator.com/api-single-validation) | Validar la dirección de correo electrónico para mejorar la capacidad de entrega | `apiKey`      | si    | Desconocido |
| [arma de correo](https://www.mailgun.com/)                                   | Servicio de correo electronico                                                  | `apiKey`      | si    | Desconocido |
| [markerapi](http://www.markerapi.com/)                                       | Búsqueda de marcas                                                              | No            | No    | Desconocido |
| [Cosquillas](https://ticksel.com)                                            | Análisis de sitios web amigables hechos para humanos                            | No            | si    | Desconocido |
| [Trello](https://developers.trello.com/)                                     | Tableros, listas y tarjetas para ayudarlo a organizar y priorizar sus proyectos | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Calendario

| FUEGO                                                                       | Descripción                                                                         | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Índice de calendario](https://www.calendarindex.com/)                      | Días festivos mundiales y días laborables                                           | `apiKey`      | si    | si          |
| [Calendario de la iglesia](http://calapi.inadiutorium.cz/)                  | Calendario litúrgico católico                                                       | No            | No    | Desconocido |
| [Calendario de nombres checos](http://svatky.adresa.info/)                  | Busca un nombre y devuelve la fecha del día del nombre                              | No            | No    | Desconocido |
| [calendario de Google](https://developers.google.com/google-apps/calendar/) | Mostrar, crear y modificar eventos del calendario de Google                         | `OAuth`       | si    | Desconocido |
| [Calendario hebreo](https://www.hebcal.com/home/developer-apis)             | Convierte entre gregoriano y hebreo, busca los tiempos de Shabat y vacaciones, etc. | No            | No    | Desconocido |
| [Días festivos](https://holidayapi.com/)                                    | Datos históricos sobre vacaciones                                                   | `apiKey`      | si    | Desconocido |
| [LectServe](http://www.lectserve.com)                                       | Calendario litúrgico protestante                                                    | No            | No    | Desconocido |
| [Nager.Date](https://date.nager.at)                                         | Días festivos para más de 90 países.                                                | No            | si    | No          |
| [Calendario de Namedays](https://api.abalin.net/)                           | Proporciona días de nombre para múltiples países                                    | No            | si    | si          |
| [Días no laborables](https://github.com/gadael/icsdb)                       | Base de datos de archivos ICS para días no laborables                               | No            | si    | Desconocido |
| [Calendario ruso](https://github.com/egno/work-calendar)                    | Compruebe si una fecha es un feriado ruso o no                                      | No            | si    | No          |

**[⬆ Volver al índice](#index)**

### Almacenamiento en la nube y uso compartido de archivos

| FUEGO                                                                   | Descripción                                                                                | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------- | ----- | ----------- |
| [Caja](https://developer.box.com/)                                      | Intercambio de archivos y almacenamiento                                                   | `OAuth`       | si    | Desconocido |
| [Dropbox](https://www.dropbox.com/developers)                           | Intercambio de archivos y almacenamiento                                                   | `OAuth`       | si    | Desconocido |
| [Google Drive](https://developers.google.com/drive/)                    | Intercambio de archivos y almacenamiento                                                   | `OAuth`       | si    | Desconocido |
| [OneDrive](https://dev.onedrive.com/)                                   | Intercambio de archivos y almacenamiento                                                   | `OAuth`       | si    | Desconocido |
| [Pastebin](https://pastebin.com/api/)                                   | Almacenamiento de texto sin formato                                                        | `apiKey`      | si    | Desconocido |
| [Temporal](https://gateway.temporal.cloud/ipns/docs.api.temporal.cloud) | Almacenamiento y uso compartido de archivos basados en IPFS con nomenclatura IPNS opcional | `apiKey`      | si    | No          |
| [WeTransfer](https://developers.wetransfer.com)                         | Compartición de archivos                                                                   | `apiKey`      | si    | si          |

**[⬆ Volver al índice](#index)**

### Integración continua

| FUEGO                                                   | Descripción                                                                                        | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [CircleCI](https://circleci.com/docs/api/v1-reference/) | Automatice el proceso de desarrollo de software utilizando integración continua y entrega continua | `apiKey`      | si    | Desconocido |
| [Codeship](https://apidocs.codeship.com/)               | Codeship es una plataforma de integración continua en la nube                                      | `apiKey`      | si    | Desconocido |
| [Travis CI](https://docs.travis-ci.com/api/)            | Sincronice sus proyectos de GitHub con Travis CI para probar su código en minutos                  | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Criptomoneda

| FUEGO                                                                    | Descripción                                                                                  | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Binance](https://github.com/binance-exchange/binance-official-api-docs) | Intercambio para el comercio de criptomonedas con sede en China                              | `apiKey`      | si    | Desconocido |
| [BitcoinAverage](https://apiv2.bitcoinaverage.com/)                      | Datos de precios de activos digitales para la industria blockchain                           | `apiKey`      | si    | Desconocido |
| [Gráficos de Bitcoin](https://bitcoincharts.com/about/exchanges/)        | Datos financieros y técnicos relacionados con la red Bitcoin                                 | No            | si    | Desconocido |
| [Bitfinex](https://docs.bitfinex.com/docs)                               | Plataforma de comercio de criptomonedas                                                      | `apiKey`      | si    | Desconocido |
| [Bitmex](https://www.bitmex.com/app/apiOverview)                         | Plataforma de negociación de derivados de criptomonedas en tiempo real con sede en Hong Kong | `apiKey`      | si    | Desconocido |
| [Bittrex](https://bittrex.com/Home/Api)                                  | Plataforma Crypto Trading de próxima generación                                              | `apiKey`      | si    | Desconocido |
| [Bloquear](https://www.block.io/docs/basic)                              | Datos de pago, billetera y transacción de Bitcoin                                            | `apiKey`      | si    | Desconocido |
| [Blockchain](https://www.blockchain.info/api)                            | Datos de pago, billetera y transacción de Bitcoin                                            | No            | si    | Desconocido |
| [CoinAPI](https://docs.coinapi.io/)                                      | Todos los intercambios de divisas se integran bajo una sola API                              | `apiKey`      | si    | No          |
| [Coinbase](https://developers.coinbase.com)                              | Precios de Bitcoin, Bitcoin Cash, Litecoin y Ethereum                                        | `apiKey`      | si    | Desconocido |
| [Coinbase Pro](https://docs.pro.coinbase.com/#api)                       | Plataforma de comercio de criptomonedas                                                      | `apiKey`      | si    | Desconocido |
| [CoinDesk](http://www.coindesk.com/api/)                                 | Índice de precios de Bitcoin                                                                 | No            | No    | Desconocido |
| [MonedaGecko](http://www.coingecko.com/api)                              | Precio de criptomonedas, mercado y desarrollador / datos sociales                            | No            | si    | si          |
| [Moneda](https://coinigy.docs.apiary.io)                                 | Interactuando con Cuentas Coinigy e Intercambio Directamente                                 | `apiKey`      | si    | Desconocido |
| [CoinLayer](https://coinlayer.com)                                       | Tipos de cambio de moneda criptográfica en tiempo real                                       | `apiKey`      | si    | Desconocido |
| [Coinlib](https://coinlib.io/apidocs)                                    | Precios de moneda criptográfica                                                              | `apiKey`      | si    | Desconocido |
| [Moneda](https://www.coinlore.com/cryptocurrency-data-api)               | Precios de criptomonedas, volumen y más                                                      | No            | si    | Desconocido |
| [MonedaMercadoCap](https://coinmarketcap.com/api/)                       | Precios de criptomonedas                                                                     | `apiKey`      | si    | Desconocido |
| [Coinpaprika](https://api.coinpaprika.com)                               | Precios de criptomonedas, volumen y más                                                      | No            | si    | si          |
| [Clasificación de monedas](https://docs.coinranking.com/)                | Datos de criptomonedas en vivo                                                               | No            | si    | Desconocido |
| [CryptoCompare](https://www.cryptocompare.com/api#)                      | Comparación de criptomonedas                                                                 | No            | si    | Desconocido |
| [Criptonador](https://www.cryptonator.com/api/)                          | Tipos de cambio de criptomonedas                                                             | No            | si    | Desconocido |
| [Geminis](https://docs.gemini.com/rest-api/)                             | Intercambio de criptomonedas                                                                 | No            | si    | Desconocido |
| [ICObench](https://icobench.com/developers)                              | Información variada sobre listados, calificaciones, estadísticas y más                       | `apiKey`      | si    | Desconocido |
| [Livecoin](https://www.livecoin.net/api)                                 | Intercambio de criptomonedas                                                                 | No            | si    | Desconocido |
| [MercadoBitcoin](https://www.mercadobitcoin.net/api-doc/)                | Información de criptomonedas brasileña                                                       | No            | si    | Desconocido |
| [Nexchange](https://nexchange2.docs.apiary.io/)                          | Servicio automatizado de intercambio de criptomonedas                                        | No            | No    | si          |
| [NiceHash](https://docs.nicehash.com/)                                   | El mercado de criptominería más grande                                                       | `apiKey`      | si    | Desconocido |
| [Poloniex](https://poloniex.com/support/api/)                            | Intercambio de activos digitales con sede en EE. UU.                                         | `apiKey`      | si    | Desconocido |
| [worldcoinındex](https://www.worldcoinindex.com/apiservice)              | Precios de criptomonedas                                                                     | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Cambio de divisas

| FUEGO                                                                                                         | Descripción                                              | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------- | ----- | ----------- |
| [1Forge](https://1forge.com/forex-data-api/api-documentation)                                                 | Datos del mercado de divisas Forex                       | `apiKey`      | si    | Desconocido |
| [Moneda](https://currencylayer.com/documentation)                                                             | Tipos de cambio y conversión de moneda                   | `apiKey`      | si    | Desconocido |
| [Banco Nacional checo](https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml) | Una colección de tasas de cambio                         | No            | si    | Desconocido |
| [ExchangeRate-API](https://www.exchangerate-api.com)                                                          | Conversión de moneda gratis                              | No            | si    | si          |
| [Exchangeratesapi.io](https://exchangeratesapi.io)                                                            | Tipos de cambio con conversión de moneda                 | No            | si    | si          |
| [Fixer.io](http://fixer.io)                                                                                   | Tipos de cambio y conversión de moneda                   | `apiKey`      | si    | Desconocido |
| [Salchicha](https://www.frankfurter.app/docs)                                                                 | Tipos de cambio, conversión de moneda y series de tiempo | No            | si    | si          |
| [rateapi](https://ratesapi.io)                                                                                | Tipos de cambio gratuitos y tasas históricas             | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Validación de datos

| FUEGO                                                                                 | Descripción                                                                                         | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Validación de Cloudmersive](https://cloudmersive.com/validate-api)                   | Validar direcciones de correo electrónico, números de teléfono, números de IVA y nombres de dominio | `apiKey`      | si    | si          |
| [idioma](https://languagelayer.com)                                                   | Detección de idioma                                                                                 | No            | si    | Desconocido |
| [Lob.com](https://lob.com/)                                                           | Verificación de Domicilio                                                                           | `apiKey`      | si    | Desconocido |
| [buzón](https://mailboxlayer.com)                                                     | Validación de dirección de correo electrónico                                                       | No            | si    | Desconocido |
| [NumValidate](https://numvalidate.com)                                                | Validación de número de teléfono de código abierto                                                  | No            | si    | Desconocido |
| [numverify](https://numverify.com)                                                    | Validación de número de teléfono                                                                    | No            | si    | Desconocido |
| [PurgoMalum](http://www.purgomalum.com)                                               | Validador de contenido contra blasfemias y obscenidades                                             | No            | No    | Desconocido |
| [Autocompletado de EE. UU.](https://smartystreets.com/docs/cloud/us-autocomplete-api) | Ingrese datos de direcciones rápidamente con sugerencias de direcciones en tiempo real              | `apiKey`      | si    | si          |
| [Extracto de EE. UU.](https://smartystreets.com/products/apis/us-extract-api)         | Extraer direcciones postales de cualquier texto, incluidos correos electrónicos                     | `apiKey`      | si    | si          |
| [Domicilio de los Estados Unidos](https://smartystreets.com/docs/cloud/us-street-api) | Valide y agregue datos para cualquier dirección postal de EE. UU.                                   | `apiKey`      | si    | si          |
| [vatlay es](https://vatlayer.com)                                                     | Validación de número de IVA                                                                         | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Desarrollo

| FUEGO                                                                                               | Descripción                                                                                                                                | Autenticación   | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ----- | ----------- |
| [24 solicitudes de extracción](https://24pullrequests.com/api)                                      | Proyecto para promover la colaboración de código abierto durante diciembre                                                                 | No              | si    | si          |
| [Agify.io](https://agify.io)                                                                        | Estima la edad de un nombre                                                                                                                | No              | si    | si          |
| [ApiFlash](https://apiflash.com/)                                                                   | API de captura de pantalla basada en Chrome para desarrolladores                                                                           | `apiKey`        | si    | Desconocido |
| [Apility.io](https://apility.io/apidocs/)                                                           | Lista de bloqueo de API anti-abuso de IP, dominios y correos electrónicos                                                                  | No              | si    | si          |
| [APIs.guru](https://apis.guru/api-doc/)                                                             | Wikipedia para API web, especificaciones OpenAPI / Swagger para API públicas                                                               | No              | si    | Desconocido |
| [BetterMeta](http://bettermeta.io)                                                                  | Devuelve las metaetiquetas de un sitio en formato JSON                                                                                     | `X-Mashape-Key` | si    | Desconocido |
| [Bitbucket](https://developer.atlassian.com/bitbucket/api/2/reference/)                             | API de Bitbucket                                                                                                                           | `OAuth`         | si    | Desconocido |
| [aburrido](https://www.boredapi.com/)                                                               | Encuentra actividades aleatorias para combatir el aburrimiento                                                                             | No              | si    | Desconocido |
| [Browshot](https://browshot.com/api/documentation)                                                  | Realice fácilmente capturas de pantalla de páginas web en cualquier tamaño de pantalla, como cualquier dispositivo                         | `apiKey`        | si    | Desconocido |
| [CDNJS](https://api.cdnjs.com/libraries/jquery)                                                     | Información de la biblioteca en CDNJS                                                                                                      | No              | si    | Desconocido |
| [Changelogs.md](https://changelogs.md)                                                              | Metadatos de registro de cambios estructurados de proyectos de código abierto                                                              | No              | si    | Desconocido |
| [CountAPI](https://countapi.xyz)                                                                    | Servicio de conteo gratuito y sencillo. Puede usarlo para rastrear visitas a la página y eventos específicos                               | No              | si    | si          |
| [DigitalOcean Status](https://status.digitalocean.com/api/v1)                                       | Estado de todos los servicios de DigitalOcean                                                                                              | No              | si    | Desconocido |
| [Información de dominioDb](https://domainsdb.info)                                                  | Búsqueda de nombres de dominio para encontrar todos los dominios que contienen palabras / frases / etc. particulares                       | No              | si    | Desconocido |
| [Faceplusplus](https://www.faceplusplus.com/)                                                       | Una herramienta para detectar caras                                                                                                        | `OAuth`         | si    | Desconocido |
| [Genderize.io](https://genderize.io)                                                                | Estima un género a partir de un nombre                                                                                                     | No              | si    | si          |
| [GitHub](https://developer.github.com/v3/)                                                          | Utilice los repositorios de GitHub, el código y la información del usuario mediante programación                                           | `OAuth`         | si    | si          |
| [Gitlab](https://docs.gitlab.com/ee/api/)                                                           | Automatice la interacción de GitLab mediante programación.                                                                                 | `OAuth`         | si    | Desconocido |
| [Cuadrícula](https://developer.gitter.im/docs/welcome)                                              | Chat para desarrolladores                                                                                                                  | `OAuth`         | si    | Desconocido |
| [HTTP2.Pro](https://http2.pro/doc/api)                                                              | Pruebe los puntos finales para el soporte de protocolo HTTP / 2 de cliente y servidor                                                      | No              | si    | Desconocido |
| [Texto a voz de IBM](https://console.bluemix.net/docs/services/text-to-speech/getting-started.html) | Convertir texto a voz                                                                                                                      | `apiKey`        | si    | si          |
| [Gráficos de imagen](https://documentation.image-charts.com/)                                       | Genere cuadros, códigos QR e imágenes gráficas.                                                                                            | No              | si    | si          |
| [import.io](http://api.docs.import.io/)                                                             | Recupere datos estructurados de un sitio web o fuente RSS                                                                                  | `apiKey`        | si    | Desconocido |
| [IPify](https://www.ipify.org/)                                                                     | Una simple API de dirección IP                                                                                                             | No              | si    | Desconocido |
| [IPinfo](https://ipinfo.io/developers)                                                              | Otra API simple de dirección IP                                                                                                            | No              | si    | Desconocido |
| [JSON 2 JSONP](https://json2jsonp.com/)                                                             | Convierta JSON a JSONP (sobre la marcha) para facilitar las solicitudes de datos entre dominios utilizando JavaScript del lado del cliente | No              | si    | Desconocido |
| [JSONbin.io](https://jsonbin.io)                                                                    | Servicio gratuito de almacenamiento JSON. Ideal para aplicaciones web a pequeña escala, sitios web y aplicaciones móviles                  | `apiKey`        | si    | si          |
| [Juez0](https://api.judge0.com/)                                                                    | Compilar y ejecutar código fuente                                                                                                          | No              | si    | Desconocido |
| [Validemos](https://github.com/letsvalidate/api)                                                    | Descubre las tecnologías utilizadas en sitios web y URL a miniatura                                                                        | No              | si    | Desconocido |
| [Licencia-API](https://github.com/cmccandless/license-api/blob/master/README.md)                    | API REST no oficial para choosealicense.com                                                                                                | No              | si    | No          |
| [Búsqueda de proveedor de dirección MAC](https://macaddress.io)                                     | Recupere los detalles del proveedor y otra información con respecto a una dirección MAC dada o una OUI                                     | `apiKey`        | si    | si          |
| [Nationalize.io](https://nationalize.io)                                                            | Estimar la nacionalidad de un nombre                                                                                                       | No              | si    | si          |
| [OOPSpam](https://oopspam.com/)                                                                     | Servicio de filtrado de spam múltiple                                                                                                      | No              | si    | si          |
| [Plino](https://plino.herokuapp.com/)                                                               | Sistema de filtrado de spam                                                                                                                | No              | si    | Desconocido |
| [Cartero](https://docs.api.getpostman.com/)                                                         | Herramienta para probar API                                                                                                                | `apiKey`        | si    | Desconocido |
| [ProxyCrawl](https://proxycrawl.com)                                                                | Servicio anticaptcha de raspado y rastreo                                                                                                  | `apiKey`        | si    | Desconocido |
| [API públicas](https://github.com/davemachado/public-api)                                           | Una lista colectiva de API JSON gratuitas para usar en desarrollo web                                                                      | No              | si    | Desconocido |
| [Haces de empuje](https://pusher.com/beams)                                                         | Notificaciones push para Android e iOS                                                                                                     | `apiKey`        | si    | Desconocido |
| [Código QR](http://qrtag.net/api/)                                                                  | Cree un código QR y un acortador de URL fáciles de leer                                                                                    | No              | si    | si          |
| [Código QR](http://goqr.me/api/)                                                                    | Generar y decodificar / leer gráficos de código QR                                                                                         | No              | si    | Desconocido |
| [QuickChart](https://quickchart.io/)                                                                | Generar imágenes de cuadros y gráficos.                                                                                                    | No              | si    | si          |
| [ReqRes](https://reqres.in/)                                                                        | Una API REST alojada lista para responder a sus solicitudes AJAX                                                                           | No              | si    | Desconocido |
| [ScraperApi](https://www.scraperapi.com)                                                            | Cree fácilmente raspadores web escalables                                                                                                  | `apiKey`        | si    | Desconocido |
| [ScreenshotAPI.net](https://screenshotapi.net/)                                                     | Crea capturas de pantalla de sitios web perfectos para píxeles                                                                             | `apiKey`        | si    | si          |
| [NUBE DE GRITOS](http://shoutcloud.io/)                                                             | TODAS LAS TAPAS COMO SERVICIO                                                                                                              | No              | No    | Desconocido |
| [StackExchange](https://api.stackexchange.com/)                                                     | Foro de preguntas y respuestas para desarrolladores                                                                                        | `OAuth`         | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Diccionarios

| FUEGO                                               | Descripción                                                              | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------- | ------------------------------------------------------------------------ | ------------- | ----- | ----------- |
| [Lenguaje robot](https://www.linguarobot.io)        | Definiciones de palabras, pronunciaciones, sinónimos, antónimos y otros. | `apiKey`      | si    | si          |
| [Merriam Webster](https://dictionaryapi.com/)       | Datos de diccionario y tesauro                                           | `apiKey`      | si    | Desconocido |
| [OwlBot](https://owlbot.info/)                      | Definiciones con oración de ejemplo y foto si están disponibles          | `apiKey`      | si    | si          |
| [Oxford](https://developer.oxforddictionaries.com/) | Datos del diccionario                                                    | `apiKey`      | si    | No          |
| [Wordnik](http://developer.wordnik.com)             | Datos del diccionario                                                    | `apiKey`      | No    | Desconocido |
| [Palabras](https://www.wordsapi.com/)               | Definiciones y sinónimos de más de 150,000 palabras.                     | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Documentos y productividad

| FUEGO                                                                               | Descripción                                                                       | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Conversión de datos y documentos en la nube](https://cloudmersive.com/convert-api) | HTML / URL a PDF / PNG, documentos de Office a PDF, conversión de imágenes        | `apiKey`      | si    | si          |
| [File.io](https://www.file.io)                                                      | Compartición de archivos                                                          | No            | si    | Desconocido |
| [Mercurio](https://mercury.postlight.com/web-parser/)                               | Analizador web                                                                    | `apiKey`      | si    | Desconocido |
| [pdflayer](https://pdflayer.com)                                                    | HTML / URL a PDF                                                                  | `apiKey`      | si    | Desconocido |
| [Bolsillo](https://getpocket.com/developer/)                                        | Servicio de marcadores                                                            | `OAuth`       | si    | Desconocido |
| [PrexView](https://prexview.com)                                                    | Datos desde XML o JSON a PDF, HTML o Imagen                                       | `apiKey`      | si    | Desconocido |
| [Paquete de descanso](https://restpack.io/)                                         | Proporciona captura de pantalla, HTML a PDF y API de extracción de contenido      | `apiKey`      | si    | Desconocido |
| [Todoist](https://developer.todoist.com)                                            | Todo Listas                                                                       | `OAuth`       | si    | Desconocido |
| [Vector Express](http://vector.express)                                             | API de conversión de archivos vectoriales gratis                                  | No            | No    | si          |
| [WakaTime](https://wakatime.com/developers)                                         | Tablas de clasificación automatizadas de seguimiento de tiempo para programadores | No            | si    | Desconocido |
| [Wunderlist](https://developer.wunderlist.com/documentation)                        | Todo Listas                                                                       | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Ambiente

| FUEGO                                                                                                                    | Descripción                                                                              | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [AirVisual](https://airvisual.com/api)                                                                                   | Calidad del aire y datos meteorológicos.                                                 | `apiKey`      | si    | Desconocido |
| [GrünstromIndex](https://www.corrently.de/hintergrund/gruenstromindex/index.html)                                        | Índice de energía verde para Alemania (Grünstromindex / GSI)                             | No            | No    | si          |
| [OpenAQ](https://docs.openaq.org/)                                                                                       | Datos de calidad del aire abierto                                                        | `apiKey`      | si    | Desconocido |
| [PM25.in](http://www.pm25.in/api_doc)                                                                                    | Calidad del aire de China                                                                | `apiKey`      | No    | Desconocido |
| [PVWatts](https://developer.nrel.gov/docs/solar/pvwatts/v6/)                                                             | Sistemas de producción de energía fotovoltaica (FV).                                     | `apiKey`      | si    | Desconocido |
| [Intensidad de carbono del Reino Unido](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v1-0-0) | La API oficial de intensidad de carbono para Gran Bretaña desarrollada por National Grid | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Eventos

| FUEGO                                                                                                                            | Descripción                           | Autenticación | HTTPS | CORAZONES   |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------- | ----- | ----------- |
| [Eventbrite](https://www.eventbrite.com/developer/v3/)                                                                           | Encuentra eventos                     | `OAuth`       | si    | Desconocido |
| [Picatica](http://developer.picatic.com/?utm_medium=web&utm_source=github&utm_campaign=public-apis%20repo&utm_content=toddmotto) | Vende entradas en cualquier lugar     | `apiKey`      | si    | Desconocido |
| [Ticketmaster](http://developer.ticketmaster.com/products-and-docs/apis/getting-started/)                                        | Buscar eventos, atracciones o lugares | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Finanzas

| FUEGO                                                      | Descripción                                                                                    | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Alpha Vantage](https://www.alphavantage.co/)              | Datos de stock históricos y en tiempo real                                                     | `apiKey`      | si    | Desconocido |
| [Barchart OnDemand](https://www.barchartondemand.com/free) | Datos del mercado de acciones, futuros y divisas                                               | `apiKey`      | si    | Desconocido |
| [IEX Cloud](https://iexcloud.io/)                          | Datos bursátiles e históricos en tiempo real                                                   | `apiKey`      | si    | si          |
| [YO G](https://labs.ig.com/gettingstarted)                 | Spreadbetting y CFD Market Data                                                                | `apiKey`      | si    | Desconocido |
| [Tartán](https://plaid.com/)                               | Conéctese con las cuentas bancarias de los usuarios y acceda a los datos de las transacciones. | `apiKey`      | si    | Desconocido |
| [Razorpay IFSC](https://ifsc.razorpay.com/)                | Código de sistemas financieros de la India (códigos de sucursales bancarias)                   | No            | si    | Desconocido |
| [Tradier](https://developer.tradier.com)                   | Datos del mercado de acciones / opciones de EE. UU. (Retrasado, intradía, histórico)           | `OAuth`       | si    | si          |
| [YNAB](https://api.youneedabudget.com/)                    | Presupuestos y planificación                                                                   | `OAuth`       | si    | si          |

**[⬆ Volver al índice](#index)**

### Comida y bebida

| FUEGO                                                                             | Descripción                                                       | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Edamam](https://developer.edamam.com/)                                           | Búsqueda de recetas                                               | `apiKey`      | si    | Desconocido |
| [LCBO](https://lcboapi.com/)                                                      | Alcohol                                                           | `apiKey`      | si    | Desconocido |
| [Open Brewery DB](https://www.openbrewerydb.org)                                  | Cervecerías, sidrerías y tiendas de botellas de cerveza artesanal | No            | si    | si          |
| [Datos de alimentos abiertos](https://world.openfoodfacts.org/data)               | Base de datos de productos alimenticios                           | No            | si    | Desconocido |
| [PunkAPI](https://punkapi.com/)                                                   | Brewdog Beer Recipes                                              | No            | si    | Desconocido |
| [Receta Cachorro](http://www.recipepuppy.com/about/api/)                          | Comida                                                            | No            | No    | Desconocido |
| [TacoFancy](https://github.com/evz/tacofancy-api)                                 | Base de datos de tacos dirigida por la comunidad                  | No            | No    | Desconocido |
| [El informe de la semana](https://github.com/andyklimczak/TheReportOfTheWeek-API) | Comentarios de comida y bebida                                    | No            | si    | Desconocido |
| [TheCocktailDB](https://www.thecocktaildb.com/api.php)                            | Recetas De Cócteles                                               | `apiKey`      | si    | si          |
| [TheMealDB](https://www.themealdb.com/api.php)                                    | Recetas De Comida                                                 | `apiKey`      | si    | si          |
| [¿Que hay en el menu?](http://nypl.github.io/menus-api/)                          | NYPL colección de menú histórico transcrito por humanos           | `apiKey`      | No    | Desconocido |
| [Zomato](https://developers.zomato.com/api)                                       | Descubre restaurantes                                             | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Juegos y comics

| FUEGO                                                               | Descripción                                                                                                    | Autenticación   | HTTPS | CORAZONES   |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------- | ----- | ----------- |
| [Age of Empires II](https://age-of-empires-2-api.herokuapp.com)     | Obtenga información sobre los recursos de Age of Empires II                                                    | No              | si    | Desconocido |
| [AmiiboAPI](http://www.amiiboapi.com/)                              | Información de amiibo                                                                                          | No              | No    | si          |
| [Battle.net](https://dev.battle.net/)                               | Blizzard Entertainment                                                                                         | `apiKey`        | si    | Desconocido |
| [Chuck Norris Database](http://www.icndb.com/api/)                  | Chistes                                                                                                        | No              | No    | Desconocido |
| [Choque de clanes](https://developer.clashofclans.com)              | Choque de clanes Información del juego                                                                         | `apiKey`        | si    | Desconocido |
| [Choque real](https://developer.clashroyale.com)                    | Información del juego Clash Royale                                                                             | `apiKey`        | si    | Desconocido |
| [Comic se acerca](https://comicvine.gamespot.com/api/documentation) | Historietas                                                                                                    | No              | si    | Desconocido |
| [Mazo de cartas](http://deckofcardsapi.com/)                        | Mazo de cartas                                                                                                 | No              | No    | Desconocido |
| [Destiny The Game](https://github.com/Bungie-net/api)               | API de plataforma Bungie                                                                                       | `apiKey`        | si    | Desconocido |
| [dota 2](https://docs.opendota.com/)                                | Proporciona información sobre estadísticas de jugadores, estadísticas de partidos, clasificaciones para Dota 2 | No              | si    | Desconocido |
| [Calabozos y Dragones](http://www.dnd5eapi.co/)                     | Referencia para hechizos, clases, monstruos y más de la quinta edición.                                        | No              | No    | No          |
| [Eva en línea](https://esi.evetech.net/ui)                          | Documentación de desarrollador de terceros                                                                     | `OAuth`         | si    | Desconocido |
| [Final Fantasy XIV](https://xivapi.com/)                            | API de datos del juego Final Fantasy XIV                                                                       | No              | si    | si          |
| [Fortnite](https://fortnitetracker.com/site-api)                    | Estadísticas de Fortnite                                                                                       | `apiKey`        | si    | Desconocido |
| [Bomba gigante](https://www.giantbomb.com/api/documentation)        | Videojuegos                                                                                                    | No              | si    | Desconocido |
| [Guild Wars 2](https://wiki.guildwars2.com/wiki/API:Main)           | Información del juego de Guild Wars 2                                                                          | `apiKey`        | si    | Desconocido |
| [aureola](https://developer.haloapi.com/)                           | Información de Halo 5 y Halo Wars 2                                                                            | `apiKey`        | si    | Desconocido |
| [Piedra de la chimenea](http://hearthstoneapi.com/)                 | Información de tarjetas de Hearthstone                                                                         | `X-Mashape-Key` | si    | Desconocido |
| [Hipixel](https://api.hypixel.net/)                                 | Estadísticas de jugadores de Hypixel                                                                           | `apiKey`        | si    | Desconocido |
| [IGDB.com](https://api.igdb.com/)                                   | Base de datos de videojuegos                                                                                   | `apiKey`        | si    | Desconocido |
| [JokeAPI](https://sv443.net/jokeapi)                                | Programación, Varios y Chistes Oscuros                                                                         | No              | si    | si          |
| [Chistes](https://github.com/15Dkatz/official_joke_api)             | Programación y bromas generales.                                                                               | No              | si    | Desconocido |
| [Jservice](http://jservice.io)                                      | Base de datos de preguntas de peligro                                                                          | No              | No    | Desconocido |
| [Magic The Gathering](http://magicthegathering.io/)                 | Información del juego Magic The Gathering                                                                      | No              | No    | Desconocido |
| [Maravilla](http://developer.marvel.com)                            | Comics Marvel                                                                                                  | `apiKey`        | No    | Desconocido |
| [mod.io](https://docs.mod.io)                                       | API multiplataforma mod                                                                                        | `apiKey`        | si    | Desconocido |
| [Trivia abierta](https://opentdb.com/api_config.php)                | Preguntas de trivia                                                                                            | No              | si    | Desconocido |
| [PandaScore](https://pandascore.co)                                 | Juegos y resultados de deportes electrónicos                                                                   | `apiKey`        | si    | Desconocido |
| [PlayerUnknown's Battlegrounds](https://pubgtracker.com/site-api)   | Estadísticas de PUBG                                                                                           | `apiKey`        | si    | Desconocido |
| [Pokéapi](https://pokeapi.co)                                       | Información Pokémon                                                                                            | No              | si    | Desconocido |
| [Pokémon TCG](https://pokemontcg.io)                                | Información de JCC Pokémon                                                                                     | No              | si    | Desconocido |
| [Rick y Morty](https://rickandmortyapi.com)                         | Toda la información de Rick y Morty, incluidas las imágenes.                                                   | No              | si    | si          |
| [Juegos antidisturbios](https://developer.riotgames.com/)           | Información del juego de League of Legends                                                                     | `apiKey`        | si    | Desconocido |
| [Scryfall](https://scryfall.com/docs/api)                           | Base de datos Magic: The Gathering                                                                             | No              | si    | si          |
| [Vapor](https://developer.valvesoftware.com/wiki/Steam_Web_API)     | Interacción con el cliente de Steam                                                                            | `OAuth`         | si    | Desconocido |
| [Superhéroes](https://superheroapi.com)                             | Todos los datos de Superhéroes y Villanos de todos los universos bajo una sola API                             | `apiKey`        | si    | Desconocido |
| [Volcado de Tronald](https://www.tronalddump.io/)                   | Las cosas más tontas que Donald Trump ha dicho                                                                 | No              | si    | Desconocido |
| [Wargaming.net](https://developers.wargaming.net/)                  | Información y estadísticas de Wargaming.net                                                                    | `apiKey`        | si    | No          |
| [xkcd](https://xkcd.com/json.html)                                  | Recupere los cómics xkcd como JSON                                                                             | No              | si    | No          |

**[⬆ Volver al índice](#index)**

### Geocodificación

| FUEGO                                                                                                                  | Descripción                                                                                                           | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [adresse.data.gouv.fr](https://adresse.data.gouv.fr)                                                                   | Base de datos de direcciones de Francia, geocodificación y reversa                                                    | No            | si    | Desconocido |
| [Battuta](http://battuta.medunes.net)                                                                                  | Una API de ubicación en cascada (país / región / ciudad)                                                              | `apiKey`      | No    | Desconocido |
| [Mapas de Bing](https://www.microsoft.com/maps/)                                                                       | Crear / personalizar mapas digitales basados en datos de Bing Maps                                                    | `apiKey`      | si    | Desconocido |
| [bng2latlong](https://www.getthedata.com/bng2latlong)                                                                  | Convertir británico OSGB36 este y norte (British National Grid) a WGS84 latitud y longitud                            | No            | si    | si          |
| [CitySDK](http://www.citysdk.eu/citysdk-toolkit/)                                                                      | API abiertas para ciudades europeas seleccionadas                                                                     | No            | si    | Desconocido |
| [Daum Maps](http://apis.map.daum.net/)                                                                                 | Daum Maps proporciona múltiples API para mapas coreanos                                                               | `apiKey`      | No    | Desconocido |
| [FreeGeoIP](https://freegeoip.app/)                                                                                    | Información de geo ip gratuita, no es necesario registrarse. Límite de tarifa de 15 k / hora                          | No            | si    | si          |
| [GeoApi](https://api.gouv.fr/api/geoapi.html)                                                                          | Datos geográficos franceses                                                                                           | No            | si    | Desconocido |
| [Geocod.io](https://www.geocod.io/)                                                                                    | Dirección de geocodificación / geocodificación inversa en masa                                                        | `apiKey`      | si    | Desconocido |
| [Geocode.xyz](https://geocode.xyz/)                                                                                    | Proporciona geocodificación hacia adelante / atrás en todo el mundo, geocodificación por lotes y geoparsing           | No            | si    | Desconocido |
| [GeoDataSource](https://www.geodatasource.com/web-service)                                                             | Geocodificación del nombre de la ciudad utilizando coordenadas de latitud y longitud                                  | `apiKey`      | si    | Desconocido |
| [GeoJS](https://geojs.io/)                                                                                             | Geolocalización de IP con integración ChatOps                                                                         | No            | si    | si          |
| [GeoNames](http://www.geonames.org/export/web-services.html)                                                           | Nombres de lugares y otros datos geográficos                                                                          | No            | No    | Desconocido |
| [geoPlugin](https://www.geoplugin.com)                                                                                 | Geolocalización de IP y conversión de moneda                                                                          | No            | si    | si          |
| [Google Earth Engine](https://developers.google.com/earth-engine/)                                                     | Una plataforma basada en la nube para el análisis de datos ambientales a escala planetaria                            | `apiKey`      | si    | Desconocido |
| [mapas de Google](https://developers.google.com/maps/)                                                                 | Crear / personalizar mapas digitales basados en datos de Google Maps                                                  | `apiKey`      | si    | Desconocido |
| [Hola salut](https://www.fourtonfish.com/hellosalut/hello/)                                                            | Obtenga hola traducción siguiendo el idioma del usuario                                                               | No            | si    | Desconocido |
| [AQUÍ Mapas](https://developer.here.com)                                                                               | Crear / personalizar mapas digitales basados en datos de mapas AQUÍ                                                   | `apiKey`      | si    | Desconocido |
| [Ciudades indias](https://indian-cities-api-nocbegfhqg.now.sh/)                                                        | Obtenga todas las ciudades indias en un formato JSON limpio                                                           | No            | si    | si          |
| [IP 2 Country](https://ip2country.info)                                                                                | Mapear una IP a un país                                                                                               | No            | si    | Desconocido |
| [Detalles de la dirección IP](https://ipinfo.io/)                                                                      | Encuentra geolocalización con dirección IP                                                                            | No            | si    | Desconocido |
| [Ubicación IP](http://ip-api.com/)                                                                                     | Encuentra ubicación con dirección IP                                                                                  | No            | No    | Desconocido |
| [Ubicación IP](https://ipapi.co/)                                                                                      | Encuentra la información de ubicación de la dirección IP                                                              | No            | si    | Desconocido |
| [IP Sidekick](https://ipsidekick.com)                                                                                  | API de geolocalización que devuelve información adicional sobre una dirección IP                                      | `apiKey`      | si    | Desconocido |
| [Vigilante IP](https://www.ipvigilante.com/)                                                                           | API de geolocalización IP gratuita                                                                                    | No            | si    | Desconocido |
| [IP2Location](https://www.ip2location.com/web-service/ip2location)                                                     | Servicio web de geolocalización IP para obtener más de 55 parámetros                                                  | `apiKey`      | si    | Desconocido |
| [IP2Proxy](https://www.ip2location.com/web-service/ip2proxy)                                                           | Detectar proxy y VPN usando la dirección IP                                                                           | `apiKey`      | si    | Desconocido |
| [IPGeolocationAPI.com](https://ipgeolocationapi.com/)                                                                  | Localiza a tus visitantes por IP con detalles del país                                                                | No            | si    | si          |
| [IPInfoDB](https://ipinfodb.com/api)                                                                                   | Herramientas y API de geolocalización gratuitas para búsqueda de país, región, ciudad y zona horaria por dirección IP | `apiKey`      | si    | Desconocido |
| [ipstack](https://ipstack.com/)                                                                                        | Localizar e identificar visitantes del sitio web por dirección IP                                                     | `apiKey`      | si    | Desconocido |
| [Red Kwelo](https://www.kwelo.com/network/ip-address)                                                                  | Localice y obtenga información detallada sobre la dirección IP                                                        | No            | si    | si          |
| [LocationIQ](https://locationiq.org/docs/)                                                                             | Proporciona geocodificación directa / inversa y geocodificación por lotes                                             | `apiKey`      | si    | si          |
| [Mapbox](https://www.mapbox.com/developers/)                                                                           | Crea / personaliza hermosos mapas digitales                                                                           | `apiKey`      | si    | Desconocido |
| [Mexico](https://github.com/IcaliaLabs/sepomex)                                                                        | API de códigos postales RESTful de México                                                                             | No            | si    | Desconocido |
| [One Map, Singapur](https://docs.onemap.sg/)                                                                           | Servicios API REST de la Autoridad de Tierras de Singapur para direcciones de Singapur                                | `apiKey`      | si    | Desconocido |
| [En agua](https://onwater.io/)                                                                                         | Determine si un lat / lon está en agua o tierra                                                                       | No            | si    | Desconocido |
| [OpenCage](https://opencagedata.com)                                                                                   | Geocodificación directa e inversa utilizando datos abiertos                                                           | `apiKey`      | si    | si          |
| [OpenStreetMap](http://wiki.openstreetmap.org/wiki/API)                                                                | Navegación, geolocalización y datos geográficos.                                                                      | `OAuth`       | No    | Desconocido |
| [PostcodeData.nl](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) | Proporcione datos de geolocalización basados en código postal para direcciones holandesas                             | No            | No    | Desconocido |
| [Postcodes.io](https://postcodes.io)                                                                                   | Búsqueda de código postal y geolocalización para el Reino Unido                                                       | No            | si    | si          |
| [Países de descanso](https://restcountries.eu)                                                                         | Obtenga información sobre países a través de una API RESTful                                                          | No            | si    | Desconocido |
| [Uebermaps](https://uebermaps.com/api/v2)                                                                              | Descubre y comparte mapas con amigos                                                                                  | `apiKey`      | si    | Desconocido |
| [Código postal de EE. UU.](https://smartystreets.com/docs/cloud/us-zipcode-api)                                        | Valide y agregue datos para cualquier código postal de EE. UU.                                                        | `apiKey`      | si    | si          |
| [Utah AGRC](https://api.mapserv.utah.gov)                                                                              | Utah Web API para geocodificar direcciones de Utah                                                                    | `apiKey`      | si    | Desconocido |
| [ViaCep](https://viacep.com.br)                                                                                        | API de códigos postales RESTful de Brasil                                                                             | No            | si    | Desconocido |
| [ZipCodeAPI](https://www.zipcodeapi.com)                                                                               | Código postal de EE. UU. Distancia, radio y ubicación API                                                             | `apiKey`      | si    | Desconocido |
| [Zippopotam](http://www.zippopotam.us)                                                                                 | Obtenga información sobre lugares como país, ciudad, estado, etc.                                                     | No            | No    | Desconocido |

**[⬆ Volver al índice](#index)**

### Gobierno

| FUEGO                                                                               | Descripción                                                                                                                    | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----- | ----------- |
| [BCLaws](http://www.bclaws.ca/civix/template/complete/api/index.html)               | Acceso a las leyes de Columbia Británica.                                                                                      | No            | No    | Desconocido |
| [BusinessUSA](https://business.usa.gov/developer)                                   | Información autorizada sobre programas, eventos, servicios y más de EE. UU.                                                    | `apiKey`      | si    | Desconocido |
| [Census.gov](https://www.census.gov/data/developers/data-sets.html)                 | La Oficina del Censo de EE. UU. Proporciona varias API y conjuntos de datos sobre demografía y negocios                        | No            | si    | Desconocido |
| [Ciudad, Lyon Opendata](https://data.beta.grandlyon.com/fr/accueil)                 | Datos abiertos de la ciudad de Lyon (FR)                                                                                       | `apiKey`      | si    | Desconocido |
| [Ciudad, Nantes Opendata](https://data.nantesmetropole.fr/pages/home/)              | Datos abiertos de la ciudad de Nantes (FR)                                                                                     | `apiKey`      | si    | Desconocido |
| [Ciudad, Praga Opendata](http://opendata.praha.eu/en)                               | Datos abiertos de la ciudad de Praga (CZ)                                                                                      | No            | No    | Desconocido |
| [Code.gov](https://code.gov)                                                        | La plataforma principal para código abierto y código compartido para el gobierno federal de EE. UU.                            | `apiKey`      | si    | Desconocido |
| [Motor de datos de Colorado](http://codataengine.org/)                              | Datos públicos de Colorado formateados y geolocalizados                                                                        | No            | si    | Desconocido |
| [Mercado de información de Colorado](https://data.colorado.gov/)                    | Datos abiertos del gobierno del estado de Colorado                                                                             | No            | si    | Desconocido |
| [Fecha USA](https://datausa.io/about/api/)                                          | Datos públicos de EE. UU.                                                                                                      | No            | si    | Desconocido |
| [Data.gov](https://api.data.gov/)                                                   | Datos del gobierno de EE. UU.                                                                                                  | `apiKey`      | si    | Desconocido |
| [Data.parliament.uk](http://www.data.parliament.uk/developers/)                     | Contiene conjuntos de datos en vivo que incluyen información sobre peticiones, proyectos de ley, votos de MP, asistencia y más | No            | No    | Desconocido |
| [Datos abiertos del Distrito de Columbia](http://opendata.dc.gov/pages/using-apis)  | Contiene conjuntos de datos públicos del gobierno de DC, incluidos delitos, SIG, datos financieros, etc.                       | No            | si    | Desconocido |
| [EPA](https://developer.epa.gov/category/apis/)                                     | Servicios web y conjuntos de datos de la Agencia de Protección Ambiental de EE. UU.                                            | No            | si    | Desconocido |
| [FEC](https://api.open.fec.gov/developers/)                                         | Información sobre donaciones de campaña en elecciones federales                                                                | `apiKey`      | si    | Desconocido |
| [registro Federal](https://www.federalregister.gov/reader-aids/developer-resources) | The Daily Journal del gobierno de los Estados Unidos                                                                           | No            | si    | Desconocido |
| [Agencia de normas alimentarias](http://ratings.food.gov.uk/open-data/en-GB)        | API de datos de calificación de higiene alimentaria del Reino Unido                                                            | No            | No    | Desconocido |
| [Gobierno Abierto, Australia](https://www.data.gov.au/)                             | Datos abiertos del gobierno australiano                                                                                        | No            | si    | Desconocido |
| [Gobierno abierto, Bélgica](https://data.gov.be/)                                   | Datos abiertos del gobierno de Bélgica                                                                                         | No            | si    | Desconocido |
| [Gobierno abierto, Canadá](http://open.canada.ca/en)                                | Datos abiertos del gobierno canadiense                                                                                         | No            | No    | Desconocido |
| [Gobierno abierto, Francia](https://www.data.gouv.fr/)                              | Datos abiertos del gobierno francés                                                                                            | `apiKey`      | si    | Desconocido |
| [Gobierno Abierto, India](https://data.gov.in/)                                     | Datos abiertos del gobierno indio                                                                                              | `apiKey`      | si    | Desconocido |
| [Gobierno abierto, Italia](https://www.dati.gov.it/)                                | Datos abiertos del gobierno de Italia                                                                                          | No            | si    | Desconocido |
| [Gobierno Abierto, Nueva Zelanda](https://www.data.govt.nz/)                        | Datos abiertos del gobierno de Nueva Zelanda                                                                                   | No            | si    | Desconocido |
| [Gobierno Abierto, Rumania](http://data.gov.ro/)                                    | Datos abiertos del gobierno de Rumania                                                                                         | No            | No    | Desconocido |
| [Gobierno abierto, Taiwán](https://data.gov.tw/)                                    | Datos abiertos del gobierno de Taiwán                                                                                          | No            | si    | Desconocido |
| [Gobierno Abierto, Estados Unidos](https://www.data.gov/)                           | Datos abiertos del gobierno de los Estados Unidos                                                                              | No            | si    | Desconocido |
| [Regulaciones.gov](https://regulationsgov.github.io/developers/)                    | Materiales regulatorios federales para aumentar la comprensión del proceso de elaboración de normas federales                  | `apiKey`      | si    | Desconocido |
| [Representado por Open North](https://represent.opennorth.ca/)                      | Encuentre representantes del gobierno canadiense                                                                               | No            | si    | Desconocido |
| [USAspending.gov](https://api.usaspending.gov/)                                     | Datos de gastos federales de EE. UU.                                                                                           | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Salud

| FUEGO                                                            | Descripción                                                                                                                    | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----- | ----------- |
| [BetterDoctor](https://developer.betterdoctor.com/)              | Información detallada sobre médicos en su área.                                                                                | `apiKey`      | si    | Desconocido |
| [COVID-19](https://covid19api.com/)                              | Covid 19 propagación, infección y recuperación                                                                                 | No            | si    | si          |
| [Diabetes](http://predictbgl.com/api/)                           | Registrar y recuperar información sobre diabetes                                                                               | No            | No    | Desconocido |
| [Flutrack](http://www.flutrack.org/)                             | Síntomas parecidos a los de la gripe con seguimiento geológico                                                                 | No            | No    | Desconocido |
| [Healthcare.gov](https://www.healthcare.gov/developers/)         | Contenido educativo sobre el mercado de seguros de salud de EE. UU.                                                            | No            | si    | Desconocido |
| [Lexigram](https://docs.lexigram.io/v1/welcome)                  | PNL que extrae menciones de conceptos clínicos del texto, da acceso a ontología clínica                                        | `apiKey`      | si    | Desconocido |
| [Maquillaje](http://makeup-api.herokuapp.com/)                   | Información de maquillaje                                                                                                      | No            | No    | Desconocido |
| [Seguro médico del estado](https://data.medicare.gov/developers) | Acceso a los datos del CMS - medicare.gov                                                                                      | No            | si    | Desconocido |
| [NPPES](https://npiregistry.cms.hhs.gov/registry/help-api)       | Plan nacional y sistema de enumeración de proveedores, información sobre proveedores de atención médica registrados en EE. UU. | No            | si    | Desconocido |
| [Nutritionix](https://developer.nutritionix.com/)                | La base de datos de nutrición verificada más grande del mundo                                                                  | `apiKey`      | si    | Desconocido |
| [openFDA](https://open.fda.gov)                                  | Datos públicos de la FDA sobre medicamentos, dispositivos y alimentos.                                                         | No            | si    | Desconocido |
| [Nutrientes del USDA](https://fdc.nal.usda.gov/)                 | Base de datos nacional de nutrientes para referencia estándar                                                                  | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Trabajos

| FUEGO                                                                                             | Descripción                                                      | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Adzuna](https://developer.adzuna.com/overview)                                                   | Agregador de bolsa de trabajo                                    | `apiKey`      | si    | Desconocido |
| [Careerjet](https://www.careerjet.com/partners/api/)                                              | Buscador de empleo                                               | `apiKey`      | No    | Desconocido |
| [Empleos de Github](https://jobs.github.com/api)                                                  | Empleos para desarrolladores de software                         | No            | si    | si          |
| [Trabajos GraphQL](https://api.graphql.jobs)                                                      | Trabajos con GraphQL                                             | No            | si    | si          |
| [En efecto](https://www.indeed.com/publisher)                                                     | Agregador de bolsa de trabajo                                    | `apiKey`      | si    | Desconocido |
| [Jobs2Careers](http://api.jobs2careers.com/api/spec.pdf)                                          | Agregador de trabajo                                             | `apiKey`      | si    | Desconocido |
| [jooble](https://us.jooble.org/api/about)                                                         | Buscador de empleo                                               | `apiKey`      | si    | Desconocido |
| [Juju](http://www.juju.com/publisher/spec/)                                                       | Buscador de empleo                                               | `apiKey`      | No    | Desconocido |
| [Habilidades abiertas](https://github.com/workforce-data-initiative/skills-api/wiki/API-Overview) | Títulos de trabajo, habilidades y datos de trabajos relacionados | No            | No    | Desconocido |
| [Junco](https://www.reed.co.uk/developers)                                                        | Agregador de bolsa de trabajo                                    | `apiKey`      | si    | Desconocido |
| [La musa](https://www.themuse.com/developers/api/v2)                                              | Bolsa de trabajo y perfiles de empresa                           | `apiKey`      | si    | Desconocido |
| [Upwork](https://developers.upwork.com/)                                                          | Bolsa de trabajo independiente y sistema de gestión              | `OAuth`       | si    | Desconocido |
| [EMPLEOS](https://developer.usajobs.gov/)                                                         | Bolsa de trabajo del gobierno de EE. UU.                         | `apiKey`      | si    | Desconocido |
| [ZipRecruiter](https://www.ziprecruiter.com/publishers)                                           | Aplicación de búsqueda de empleo y sitio web                     | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Aprendizaje automático

| FUEGO                                                                             | Descripción                                                       | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Clarifai](https://developer.clarifai.com/)                                       | Visión por computador                                             | `OAuth`       | si    | Desconocido |
| [Cloudmersive](https://www.cloudmersive.com/image-recognition-and-processing-api) | Subtítulos de imágenes, reconocimiento facial, clasificación NSFW | `apiKey`      | si    | si          |
| [Deepcode](https://www.deepcode.ai/docs/Overview%252FOverview)                    | AI para revisión de código                                        | No            | si    | Desconocido |
| [Dialogflow](https://dialogflow.com)                                              | Procesamiento natural del lenguaje                                | `apiKey`      | si    | Desconocido |
| [Keen entusiasta](https://keen.io/)                                               | Análisis de datos                                                 | `apiKey`      | si    | Desconocido |
| [Sentimos-API](https://sentim-api.herokuapp.com)                                  | Análisis de sentimiento de texto                                  | No            | si    | si          |
| [Puerta del tiempo](https://timedoor.io)                                          | Una API de análisis de series temporales                          | `apiKey`      | si    | si          |
| [Desenchufar](https://unplu.gg/test_api.html)                                     | API de pronóstico para datos de series de tiempo                  | `apiKey`      | si    | Desconocido |
| [Wit.ai](https://wit.ai/)                                                         | Procesamiento natural del lenguaje                                | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Música

| FUEGO                                                                                                                 | Descripción                                                                                                     | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [AI Mastering](https://aimastering.com/api_docs/)                                                                     | Masterización Automatizada de Música                                                                            | `apiKey`      | si    | si          |
| [Bandsintown](https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0)                                            | Eventos musicales                                                                                               | No            | si    | Desconocido |
| [Deezer](https://developers.deezer.com/api)                                                                           | Música                                                                                                          | `OAuth`       | si    | Desconocido |
| [Discogs](https://www.discogs.com/developers/)                                                                        | Música                                                                                                          | `OAuth`       | si    | Desconocido |
| [Genio](https://docs.genius.com/)                                                                                     | Letras y conocimiento musical de crowdsourced                                                                   | `OAuth`       | si    | Desconocido |
| [Genrenator](https://binaryjazz.us/genrenator-api/)                                                                   | Generador de género musical                                                                                     | No            | si    | Desconocido |
| [Búsqueda de iTunes](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) | Productos de software                                                                                           | No            | si    | Desconocido |
| [Jamendo](https://developer.jamendo.com/v3.0/docs)                                                                    | Música                                                                                                          | `OAuth`       | si    | Desconocido |
| [KKBOX](https://developer.kkbox.com)                                                                                  | Obtenga bibliotecas de música, listas de reproducción, gráficos y actúe fuera de la plataforma de KKBOX         | `OAuth`       | si    | Desconocido |
| [Last FM](https://www.last.fm/api)                                                                                    | Música                                                                                                          | `apiKey`      | si    | Desconocido |
| [Lyrics.ovh](http://docs.lyricsovh.apiary.io/)                                                                        | API simple para recuperar la letra de una canción                                                               | No            | si    | Desconocido |
| [Mixcloud](https://www.mixcloud.com/developers/)                                                                      | Música                                                                                                          | `OAuth`       | si    | si          |
| [MusicBrainz](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2)                                      | Música                                                                                                          | No            | si    | Desconocido |
| [Musixmatch](https://developer.musixmatch.com/)                                                                       | Música                                                                                                          | `apiKey`      | si    | Desconocido |
| [Openwhyd](https://openwhyd.github.io/openwhyd/API)                                                                   | Descargue listas de reproducción seleccionadas de pistas de transmisión (YouTube, SoundCloud, etc.)             | `No`          | si    | No          |
| [SearchLy](https://searchly.asuarez.dev/docs/v1)                                                                      | Búsqueda de similitudes basada en letras de canciones                                                           | No            | si    | Desconocido |
| [Songkick](https://www.songkick.com/developer/)                                                                       | Eventos musicales                                                                                               | `OAuth`       | si    | Desconocido |
| [Songsterr](https://www.songsterr.com/a/wa/api/)                                                                      | Proporciona tablaturas para guitarra, bajo y batería y acordes.                                                 | No            | si    | Desconocido |
| [SoundCloud](https://developers.soundcloud.com/)                                                                      | Permitir a los usuarios cargar y compartir sonidos                                                              | `OAuth`       | si    | Desconocido |
| [Spotify](https://beta.developer.spotify.com/documentation/web-api/)                                                  | Vea el catálogo de música de Spotify, administre las bibliotecas de los usuarios, obtenga recomendaciones y más | `OAuth`       | si    | Desconocido |
| [TasteDive](https://tastedive.com/read/api)                                                                           | API de artista similar (también funciona para películas y programas de televisión)                              | `apiKey`      | si    | Desconocido |
| [TheAudioDB](https://www.theaudiodb.com/api_guide.php)                                                                | Música                                                                                                          | `apiKey`      | si    | Desconocido |
| [Luciérnaga](https://api.vagalume.com.br/docs/)                                                                       | Letras y conocimiento musical de crowdsourced                                                                   | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Noticias

| FUEGO                                                               | Descripción                                                                                                   | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Associated Press](https://developer.ap.org/)                       | Busque noticias y metadatos de Associated Press                                                               | `apiKey`      | si    | Desconocido |
| [Chronicling America](http://chroniclingamerica.loc.gov/about/api/) | Proporciona acceso a millones de páginas de periódicos históricos de EE. UU. Desde la Biblioteca del Congreso | No            | No    | Desconocido |
| [Las corrientes](https://currentsapi.services/)                     | Últimas noticias publicadas en varias fuentes de noticias, blogs y foros.                                     | `apiKey`      | si    | si          |
| [Feedbin](https://github.com/feedbin/feedbin-api)                   | lector de RSS                                                                                                 | `OAuth`       | si    | Desconocido |
| [New York Times](https://developer.nytimes.com/)                    | Proporciona noticias                                                                                          | `apiKey`      | si    | Desconocido |
| [Noticias](https://newsapi.org/)                                    | Titulares publicados actualmente en una variedad de fuentes de noticias y blogs                               | `apiKey`      | si    | Desconocido |
| [NPR One](http://dev.npr.org/api/)                                  | Experiencia de escucha de noticias personalizada de NPR                                                       | `OAuth`       | si    | Desconocido |
| [El guardián](http://open-platform.theguardian.com/)                | Acceda a todo el contenido que crea The Guardian, categorizado por etiquetas y sección                        | `apiKey`      | si    | Desconocido |
| [El viejo lector](https://github.com/theoldreader/api)              | lector de RSS                                                                                                 | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Información abierta

| FUEGO                                                                       | Descripción                                                                                                        | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------- | ----- | ----------- |
| [18F](http://18f.github.io/API-All-the-X/)                                  | Desarrollo no oficial de API del gobierno federal de EE. UU.                                                       | No            | No    | Desconocido |
| [Archive.org](https://archive.readme.io/docs)                               | El archivo de internet                                                                                             | No            | si    | Desconocido |
| [ARSAT](https://datos.arsat.com.ar/developers/)                             | Datos públicos de ARSAT                                                                                            | `apiKey`      | si    | Desconocido |
| [Callook.info](https://callook.info)                                        | Indicativos de radioaficionados de Estados Unidos                                                                  | No            | si    | Desconocido |
| [CARTO](https://carto.com/)                                                 | Predicción de información de ubicación                                                                             | `apiKey`      | si    | Desconocido |
| [CivicFeed](https://developers.civicfeed.com/)                              | Artículos de noticias y conjuntos de datos públicos.                                                               | `apiKey`      | si    | Desconocido |
| [Enigma Public](http://docs.enigma.com/public/public_v20_api_about)         | La más amplia recopilación de datos públicos.                                                                      | `apiKey`      | si    | si          |
| [fonoApi](https://fonoapi.freshpixl.com/)                                   | Descripción del dispositivo móvil                                                                                  | No            | si    | Desconocido |
| [Búsqueda de dirección en francés](https://geo.api.gouv.fr/adresse)         | Búsqueda de direcciones a través del gobierno francés                                                              | No            | si    | Desconocido |
| [LinkPreview](https://www.linkpreview.net)                                  | Obtenga un resumen con formato JSON con título, descripción e imagen de vista previa para cualquier URL solicitada | `apiKey`      | si    | si          |
| [Cepas de marihuana](http://strains.evanbusse.com/)                         | Cepas de marihuana, razas, sabores y efectos.                                                                      | `apiKey`      | No    | Desconocido |
| [Microlink.io](https://microlink.io)                                        | Extraer datos estructurados de cualquier sitio web                                                                 | No            | si    | si          |
| [OpenCorporates](http://api.opencorporates.com/documentation/API-Reference) | Datos sobre entidades corporativas y directores en muchos países.                                                  | `apiKey`      | si    | Desconocido |
| [quandl](https://www.quandl.com/)                                           | Datos del mercado de valores                                                                                       | No            | si    | Desconocido |
| [Base de datos de información de recreación](https://ridb.recreation.gov/)  | Áreas recreativas, tierras federales, sitios históricos, museos y otras atracciones / recursos (EE. UU.)           | `apiKey`      | si    | Desconocido |
| [Sáquelo](http://www.scoop.it/dev)                                          | Servicio de curación de contenido                                                                                  | `apiKey`      | No    | Desconocido |
| [Teletransporte](https://developers.teleport.org/)                          | Datos de calidad de vida                                                                                           | No            | si    | Desconocido |
| [Lista de universidades](https://github.com/Hipo/university-domains-list)   | Nombres de universidades, países y dominios.                                                                       | No            | si    | Desconocido |
| [Universidad de oslo](https://data.uio.no/)                                 | Cursos, videos de conferencias, información detallada de cursos, etc. para la Universidad de Oslo (Noruega)        | No            | si    | Desconocido |
| [Base de datos UPC](https://upcdatabase.org/api)                            | Más de 1.5 millones de números de códigos de barras de todo el mundo.                                              | `apiKey`      | si    | Desconocido |
| [Wikidata](https://www.wikidata.org/w/api.php?action=help)                  | Base de conocimiento editada en colaboración operada por la Fundación Wikimedia                                    | `OAuth`       | si    | Desconocido |
| [Wikipedia](https://www.mediawiki.org/wiki/API:Main_page)                   | Enciclopedia de Mediawiki                                                                                          | No            | si    | Desconocido |
| [Gañido](https://www.yelp.com/developers/documentation/v3)                  | Encuentra negocios locales                                                                                         | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Proyectos de código abierto

| FUEGO                                                      | Descripción                               | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------- | ----------------------------------------- | ------------- | ----- | ----------- |
| [Condescendiente](https://api.count.ly/reference)          | Numerosas analíticas web                  | No            | No    | Desconocido |
| [Drupal.org](https://www.drupal.org/drupalorg/docs/api)    | Drupal.org                                | No            | si    | Desconocido |
| [Generador de insulto malvado](https://evilinsult.com/api) | Malos insultos                            | No            | si    | si          |
| [Bibliotecas.io](https://libraries.io/api)                 | Bibliotecas de software de código abierto | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Patentar

| FUEGO                                                                         | Descripción                                   | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------------- | --------------------------------------------- | ------------- | ----- | ----------- |
| [EPO](https://developers.epo.org/)                                            | Sistema de búsqueda de patentes europeas api  | `OAuth`       | si    | Desconocido |
| [TIPO](https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00) | Sistema de búsqueda de patentes de Taiwán api | `apiKey`      | si    | Desconocido |
| [USPTO](https://www.uspto.gov/learning-and-resources/open-data-and-mobility)  | Servicios de API de patentes de EE. UU.       | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Personalidad

| FUEGO                                                                               | Descripción                                                                     | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Hoja de consejos](http://api.adviceslip.com/)                                      | Generar boletas de consejos al azar                                             | No            | si    | Desconocido |
| [chucknorris.io](https://api.chucknorris.io)                                        | API JSON para bromas de Chuck Norris seleccionadas a mano                       | No            | si    | Desconocido |
| [FavQs.com](https://favqs.com/api)                                                  | FavQs te permite recopilar, descubrir y compartir tus citas favoritas           | `apiKey`      | si    | Desconocido |
| [FOAAS](http://www.foaas.com/)                                                      | Joder como un servicio                                                          | No            | No    | Desconocido |
| [Forismático](http://forismatic.com/en/api/)                                        | Citas de inspiración                                                            | No            | No    | Desconocido |
| [icanhazdadjoke](https://icanhazdadjoke.com/api)                                    | La mayor selección de chistes de papá en internet                               | No            | si    | Desconocido |
| [kanye.rest](https://kanye.rest)                                                    | REST API para citas aleatorias de Kanye West                                    | No            | si    | si          |
| [Medio](https://github.com/Medium/medium-api-docs)                                  | Comunidad de lectores y escritores que ofrecen perspectivas únicas sobre ideas. | `OAuth`       | si    | Desconocido |
| [NaMoMemes](https://github.com/theIYD/NaMoMemes)                                    | Memes sobre Narendra Modi                                                       | No            | si    | Desconocido |
| [Cotizaciones de programación](https://github.com/skolakoda/programming-quotes-api) | Programación de API de Cotizaciones para proyectos de código abierto            | No            | si    | Desconocido |
| [Jardín de citas](https://pprathameshmore.github.io/QuoteGarden/)                   | REST API para más de 5000 citas famosas                                         | No            | si    | Desconocido |
| [Citas sobre diseño](https://quotesondesign.com/api/)                               | Citas de inspiración                                                            | No            | si    | Desconocido |
| [Traitificar](https://app.traitify.com/developer)                                   | Evaluar, recopilar y analizar la personalidad.                                  | No            | si    | Desconocido |
| [tronalddump.io](https://www.tronalddump.io)                                        | Api y archivo web de las cosas que Donald Trump ha dicho                        | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Fotografía

| FUEGO                                                    | Descripción                                                       | Autenticación | HTTPS | CORAZONES   |
| -------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Flickr](https://www.flickr.com/services/api/)           | Servicios de Flickr                                               | `OAuth`       | si    | Desconocido |
| [imágenes falsas](http://developers.gettyimages.com/en/) | Cree aplicaciones utilizando las imágenes más potentes del mundo. | `OAuth`       | si    | Desconocido |
| [Gfycat](https://developers.gfycat.com/api/)             | GIFs Jiffier                                                      | `OAuth`       | si    | Desconocido |
| [Giphy](https://developers.giphy.com/docs/)              | Consigue todos tus gifs                                           | `apiKey`      | si    | Desconocido |
| [Gyazo](https://gyazo.com/api/docs)                      | Sube imágenes                                                     | `apiKey`      | si    | Desconocido |
| [Imgur](https://apidocs.imgur.com/)                      | Imágenes                                                          | `OAuth`       | si    | Desconocido |
| [fotos de lorem](https://picsum.photos/)                 | Imágenes de Unsplash                                              | No            | si    | Desconocido |
| [Pexels](https://www.pexels.com/api/)                    | Fotos y videos gratis                                             | `apiKey`      | si    | si          |
| [Pixabay](https://pixabay.com/sk/service/about/api/)     | Fotografía                                                        | `apiKey`      | si    | Desconocido |
| [PlaceKitten](https://placekitten.com/)                  | Imágenes de marcador de posición de gatitos redimensionables      | No            | si    | Desconocido |
| [ScreenShotLayer](https://screenshotlayer.com)           | Imagen de URL 2                                                   | No            | si    | Desconocido |
| [Unsplash](https://unsplash.com/developers)              | Fotografía                                                        | `OAuth`       | si    | Desconocido |
| [el Wallhav](https://wallhaven.cc/help/api)              | Fondos de pantalla                                                | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Ciencia matemática

| FUEGO                                                                                      | Descripción                                                                                          | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [arcsecond.io](https://api.arcsecond.io/)                                                  | Múltiples fuentes de datos astronómicos                                                              | No            | si    | Desconocido |
| [NÚCLEO](https://core.ac.uk/services#api)                                                  | Acceda a los trabajos de investigación de acceso abierto del mundo                                   | `apiKey`      | si    | Desconocido |
| [GBIF](http://api.gbif.org/v1/)                                                            | Facilidad Global de Información sobre Biodiversidad                                                  | No            | si    | si          |
| [iDigBio](https://github.com/idigbio/idigbio-search-api/wiki)                              | Acceda a millones de muestras de museos de organizaciones de todo el mundo                           | No            | si    | Desconocido |
| [inspirehep.net](https://inspirehep.net/info/hep/api?ln=en)                                | Información de física de alta energía. sistema                                                       | No            | si    | Desconocido |
| [ES](https://www.itis.gov/ws_description.html)                                             | Sistema Integrado de Información Taxonómica                                                          | No            | si    | Desconocido |
| [Lanzar biblioteca](https://launchlibrary.net/docs/1.3/api.html)                           | Próximos lanzamientos espaciales                                                                     | No            | si    | Desconocido |
| [Minor Planet Center](http://www.asterank.com/mpc)                                         | Información de Asterank.com                                                                          | No            | No    | Desconocido |
| [NASA](https://api.nasa.gov)                                                               | Datos de la NASA, incluidas imágenes                                                                 | No            | si    | Desconocido |
| [NASA APOD (API no oficial)](https://apodapi.herokuapp.com/)                               | API para obtener imágenes APOD (Imagen Astronómica del Día) junto con metadatos                      | No            | si    | si          |
| [Newton](https://newton.now.sh/)                                                           | Calculadora matemática simbólica y aritmética                                                        | No            | si    | Desconocido |
| [Números](http://numbersapi.com)                                                           | Hechos sobre números                                                                                 | No            | No    | Desconocido |
| [Abrir notificación](http://open-notify.org/Open-Notify-API/)                              | ISS astronautas, ubicación actual, etc.                                                              | No            | No    | Desconocido |
| [Open Science Framework](https://developer.osf.io)                                         | Repositorio y archivo para diseños de estudio, materiales de investigación, datos, manuscritos, etc. | No            | si    | Desconocido |
| [COMPARTIR](https://share.osf.io/api/v2/)                                                  | Un conjunto de datos gratuito y abierto sobre investigación y actividades académicas.                | No            | si    | Desconocido |
| [SpaceX](https://github.com/r-spacex/SpaceX-API)                                           | Empresa, vehículo, plataforma de lanzamiento y datos de lanzamiento                                  | No            | si    | Desconocido |
| [Amanecer y el atardecer](https://sunrise-sunset.org/api)                                  | Horas de puesta y salida del sol para una latitud y longitud dada                                    | No            | si    | Desconocido |
| [Trébol](https://trefle.io/)                                                               | Datos botánicos para especies de plantas.                                                            | `apiKey`      | si    | Desconocido |
| [Programa de Peligros de Terremotos del USGS](https://earthquake.usgs.gov/fdsnws/event/1/) | Terremotos de datos en tiempo real                                                                   | No            | si    | Desconocido |
| [Servicios de agua de USGS](https://waterservices.usgs.gov/)                               | Calidad del agua y nivel de información para ríos y lagos.                                           | No            | si    | Desconocido |
| [Banco Mundial](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589)            | Datos mundiales                                                                                      | No            | No    | Desconocido |

**[⬆ Volver al índice](#index)**

### Seguridad

| FUEGO                                                                                                | Descripción                                                                                       | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Censys.io](https://censys.io/api)                                                                   | Motor de búsqueda para host y dispositivos conectados a Internet                                  | `apiKey`      | si    | No          |
| [CRXcavator](https://crxcavator.io/apidocs)                                                          | Puntuación de riesgo de extensión de Chrome                                                       | `apiKey`      | si    | Desconocido |
| [FilterLists](https://filterlists.com)                                                               | Listas de filtros para bloqueadores de anuncios y cortafuegos                                     | No            | si    | Desconocido |
| [FraudLabs Pro](https://www.fraudlabspro.com/developer/api/screen-order)                             | Pantalla de información de pedidos utilizando AI para detectar fraudes                            | `apiKey`      | si    | Desconocido |
| [HaveIBeenPwned](https://haveibeenpwned.com/API/v3)                                                  | Contraseñas que previamente han sido expuestas en violaciones de datos                            | `apiKey`      | si    | Desconocido |
| [Base de datos de vulnerabilidad nacional](https://nvd.nist.gov/vuln/Data-Feeds/JSON-feed-changelog) | Base de datos de vulnerabilidad nacional de EE. UU.                                               | No            | si    | Desconocido |
| [Senderos de seguridad](https://securitytrails.com/corp/apidocs)                                     | Información relacionada con el dominio y la IP, como registros de DNS y DNS actuales e históricos | `apiKey`      | si    | Desconocido |
| [Shodan](https://developer.shodan.io/)                                                               | Buscador para dispositivos conectados a Internet                                                  | `apiKey`      | si    | Desconocido |
| [Policía del reino unido](https://data.police.uk/docs/)                                              | Datos de la policía del Reino Unido                                                               | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Compras

| FUEGO                                                                        | Descripción                                                                    | Autenticación | HTTPS | CORAZONES   |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------- | ----- | ----------- |
| [La mejor compra](https://bestbuyapis.github.io/api-documentation/#overview) | Productos, opciones de compra, categorías, recomendaciones, tiendas y comercio | `apiKey`      | si    | Desconocido |
| [Bratabase](https://developers.bratabase.com/)                               | Base de datos de diferentes tipos de tallas de sujetador                       | `OAuth`       | si    | Desconocido |
| [eBay](https://go.developer.ebay.com/)                                       | Vende y compra en eBay                                                         | `OAuth`       | si    | Desconocido |
| [Wal-Mart](https://developer.walmartlabs.com/docs)                           | Precio del artículo y disponibilidad                                           | `apiKey`      | si    | Desconocido |
| [Wegmans](https://dev.wegmans.io)                                            | Wegmans Food Markets                                                           | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Social

| FUEGO                                                                    | Descripción                                                                                                            | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Buffer](https://buffer.com/developers/api)                              | Acceso a actualizaciones pendientes y enviadas en Buffer                                                               | `OAuth`       | si    | Desconocido |
| [Cisco Spark](https://developer.ciscospark.com)                          | Software de colaboración en equipo                                                                                     | `OAuth`       | si    | Desconocido |
| [Discordia](https://discordapp.com/developers/docs/intro)                | Haga bots para Discord, integre Discord en una plataforma externa                                                      | `OAuth`       | si    | Desconocido |
| [Disqus](https://disqus.com/api/docs/auth/)                              | Comunicarse con datos de Disqus                                                                                        | `OAuth`       | si    | Desconocido |
| [Facebook](https://developers.facebook.com/)                             | Inicio de sesión en Facebook, compartir en Facebook, complementos sociales, análisis y más                             | `OAuth`       | si    | Desconocido |
| [Firme](https://developer.foursquare.com/)                               | Interactúa con usuarios y lugares de Foursquare (registros basados en geolocalización, fotos, consejos, eventos, etc.) | `OAuth`       | si    | Desconocido |
| [Joder como un servicio](https://www.foaas.com)                          | Pide a alguien que se vaya a la mierda                                                                                 | No            | si    | Desconocido |
| [Contacto total](https://www.fullcontact.com/developer/docs/)            | Obtenga perfiles de redes sociales e información de contacto                                                           | `OAuth`       | si    | Desconocido |
| [HackerNews](https://github.com/HackerNews/API)                          | Noticias sociales para CS y emprendimiento                                                                             | No            | si    | Desconocido |
| [Instagram](https://www.instagram.com/developer/)                        | Inicio de sesión en Instagram, compartir en Instagram, complementos sociales y más                                     | `OAuth`       | si    | Desconocido |
| [LinkedIn](https://developer.linkedin.com/docs/rest-api)                 | La base de todas las integraciones digitales con LinkedIn                                                              | `OAuth`       | si    | Desconocido |
| [Meetup.com](https://www.meetup.com/meetup_api/)                         | Datos sobre Meetups de Meetup.com                                                                                      | `apiKey`      | si    | Desconocido |
| [Mezclador](https://dev.mixer.com/)                                      | API de transmisión de juegos                                                                                           | `OAuth`       | si    | Desconocido |
| [MySocialApp](https://mysocialapp.io)                                    | Funciones integradas de redes sociales, API, SDK para cualquier aplicación                                             | `apiKey`      | si    | Desconocido |
| [Colectivo abierto](https://docs.opencollective.com/help/developers/api) | Obtenga datos colectivos abiertos                                                                                      | No            | si    | Desconocido |
| [Pinterest](https://developers.pinterest.com/)                           | El catálogo mundial de ideas.                                                                                          | `OAuth`       | si    | Desconocido |
| [PWR Telegram bot](https://pwrtelegram.xyz)                              | Versión mejorada de la API de bot de Telegram                                                                          | `apiKey`      | si    | Desconocido |
| [Reddit](https://www.reddit.com/dev/api)                                 | Página de inicio de internet                                                                                           | `OAuth`       | si    | Desconocido |
| [Flojo](https://api.slack.com/)                                          | Team Instant Messaging                                                                                                 | `OAuth`       | si    | Desconocido |
| [Telegram Bot](https://core.telegram.org/bots/api)                       | Versión HTTP simplificada de la API MTProto para bots                                                                  | `apiKey`      | si    | Desconocido |
| [Telegram MTProto](https://core.telegram.org/api#getting-started)        | Leer y escribir datos de Telegram                                                                                      | `OAuth`       | si    | Desconocido |
| [Basura Nada](https://trashnothing.com/developer)                        | Una comunidad de freecycling con miles de artículos gratuitos publicados todos los días.                               | `OAuth`       | si    | si          |
| [Tumblr](https://www.tumblr.com/docs/en/api/v2)                          | Leer y escribir datos de Tumblr                                                                                        | `OAuth`       | si    | Desconocido |
| [Contracción nerviosa](https://dev.twitch.tv/docs)                       | API de transmisión de juegos                                                                                           | `OAuth`       | si    | Desconocido |
| [Gorjeo](https://developer.twitter.com/en/docs)                          | Leer y escribir datos de Twitter                                                                                       | `OAuth`       | si    | No          |
| [vk](https://vk.com/dev/sites)                                           | Leer y escribir datos vk                                                                                               | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Deportes y fitness

| FUEGO                                                                              | Descripción                                                                                                     | Autenticación   | HTTPS | CORAZONES   |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------- | ----- | ----------- |
| [balldontlie](https://balldontlie.io)                                              | Ballldontlie proporciona acceso a datos estadísticos de la NBA                                                  | No              | si    | si          |
| [BikeWise](https://www.bikewise.org/documentation/api_v2)                          | Bikewise es un lugar para aprender y reportar accidentes de bicicleta, riesgos y robos                          | No              | si    | Desconocido |
| [Canadian Football League (CFL)](http://api.cfl.ca/)                               | API JSON oficial que proporciona estadísticas de liga, equipo y jugadores en tiempo real sobre la CFL           | `apiKey`        | si    | No          |
| [Bicis de la ciudad](http://api.citybik.es/v2/)                                    | Bicicletas de ciudad alrededor del mundo                                                                        | No              | No    | Desconocido |
| [Ergast F1](http://ergast.com/mrd/)                                                | Datos de F1 desde el comienzo del campeonato mundial en 1950                                                    | No              | si    | Desconocido |
| [Fitbit](https://dev.fitbit.com/)                                                  | Información de Fitbit                                                                                           | `OAuth`         | si    | Desconocido |
| [Videos de fútbol (soccer)](https://www.scorebat.com/video-api/)                   | Incruste códigos para goles y momentos destacados de la Premier League, la Bundesliga, la Serie A y muchos más. | No              | si    | si          |
| [Predicción de fútbol](https://boggio-analytics.com/fp-api/)                       | Predicciones para los próximos partidos de fútbol, cuotas, resultados y estadísticas.                           | `X-Mashape-Key` | si    | Desconocido |
| [Football-Data.org](http://api.football-data.org/index)                            | Datos de fútbol                                                                                                 | No              | No    | Desconocido |
| [JCDecaux Bike](https://developer.jcdecaux.com/)                                   | Las bicicletas de autoservicio de JCDecaux                                                                      | `apiKey`        | si    | Desconocido |
| [Estadísticas de la NBA](https://any-api.com/nba_com/nba_com/docs/API_Description) | Estadísticas actuales e históricas de la NBA                                                                    | No              | si    | Desconocido |
| [Detenciones de la NFL](http://nflarrest.com/api/)                                 | Datos de arresto de la NFL                                                                                      | No              | No    | Desconocido |
| [Registros y estadísticas de NHL](https://gitlab.com/dword4/nhlapi)                | Datos históricos y estadísticas de NHL                                                                          | No              | si    | Desconocido |
| [Dieta](https://strava.github.io/api/)                                             | Conéctese con atletas, actividades y más                                                                        | `OAuth`         | si    | Desconocido |
| [SuredBits](https://suredbits.com/api/)                                            | Consultar datos deportivos, incluidos equipos, jugadores, juegos, puntajes y estadísticas                       | No              | No    | No          |
| [TheSportsDB](https://www.thesportsdb.com/api.php)                                 | Datos deportivos y obras de arte de multitudes                                                                  | `apiKey`        | si    | si          |
| [Wger](https://wger.de/en/software/api)                                            | Datos del gerente de entrenamiento como ejercicios, músculos o equipo                                           | `apiKey`        | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Datos de prueba

| FUEGO                                                        | Descripción                                                                     | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Adorables avatares](http://avatars.adorable.io)             | Generar avatares de dibujos animados al azar                                    | No            | si    | Desconocido |
| [muy tocino](https://baconipsum.com/json-api/)               | Un generador de ipsum lorem más carnoso                                         | No            | si    | Desconocido |
| [Avatares de osos](https://avatars.dicebear.com/)            | Genera avatares aleatorios de pixel art                                         | No            | si    | No          |
| [FakeJSON](https://fakejson.com)                             | Servicio para generar datos de prueba y falsos.                                 | `apiKey`      | si    | si          |
| [Identicon](https://www.kwelo.com/media/identicon/)          | Genera una imagen de avatar abstracta                                           | No            | si    | si          |
| [JSONPlaceholder](http://jsonplaceholder.typicode.com/)      | Datos falsos para pruebas y prototipos                                          | No            | No    | Desconocido |
| [Loripsum](http://loripsum.net/)                             | El generador "lorem ipsum" que no apesta                                        | No            | No    | Desconocido |
| [PIPL](https://pipl.ir/)                                     | API pública y gratuita que genera datos aleatorios y falsos de personas en JSON | No            | si    | No          |
| [RandomUser](https://randomuser.me)                          | Genera datos de usuario aleatorios.                                             | No            | si    | Desconocido |
| [RoboHash](https://robohash.org/)                            | Generar avatares de robot / alienígenas aleatorios                              | No            | si    | Desconocido |
| [Esta persona no existe](https://thispersondoesnotexist.com) | Genera rostros de la vida real de personas que no existen.                      | No            | si    | Desconocido |
| [Nombres de UI](https://github.com/thm/uinames)              | Generar nombres falsos aleatorios                                               | No            | si    | Desconocido |
| [sí No](https://yesno.wtf/api)                               | Genera sí o no al azar                                                          | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Análisis de texto

| FUEGO                                                                                                                                     | Descripción                                                                                                | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Análisis de texto de Aylien](http://docs.aylien.com/)                                                                                    | Una colección de API de recuperación de información y lenguaje natural.                                    | `apiKey`      | si    | Desconocido |
| [Procesamiento de lenguaje natural en la nube](https://www.cloudmersive.com/nlp-api)                                                      | Procesamiento del lenguaje natural y análisis de texto.                                                    | `apiKey`      | si    | si          |
| [Detectar idioma](https://detectlanguage.com/)                                                                                            | Detecta el idioma del texto.                                                                               | `apiKey`      | si    | Desconocido |
| [Google Cloud Natural](https://cloud.google.com/natural-language/docs/)                                                                   | Tecnología de comprensión del lenguaje natural, incluido el análisis de sentimientos, entidades y sintaxis | `apiKey`      | si    | Desconocido |
| [Semantira](https://semantria.readme.io/docs)                                                                                             | Análisis de texto con análisis de sentimientos, categorización y extracción de entidades con nombre        | `OAuth`       | si    | Desconocido |
| [Comprensión del lenguaje natural de Watson](https://cloud.ibm.com/apidocs/natural-language-understanding/natural-language-understanding) | Procesamiento de lenguaje natural para análisis de texto avanzado.                                         | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Rastreo

| FUEGO                                            | Descripción                                                                                     | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Cartero](http://postmon.com.br)                 | Una API para consultar códigos postales y pedidos brasileños de manera fácil, rápida y gratuita | No            | No    | Desconocido |
| [Suecia](https://developer.postnord.com/docs2)   | Proporciona información sobre paquetes en el transporte.                                        | `apiKey`      | No    | Desconocido |
| [UPS](https://www.ups.com/upsdeveloperkit)       | Información de envío y dirección                                                                | `apiKey`      | si    | Desconocido |
| [WhatPulse](https://whatpulse.org/pages/webapi/) | Pequeña aplicación que mide el uso de tu teclado / mouse                                        | No            | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Transporte

| FUEGO                                                                                                                                | Descripción                                                                                                    | Autenticación | HTTPS | CORAZONES   |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [ADS-B Exchange](https://www.adsbexchange.com/data/)                                                                                 | Acceda a datos históricos y en tiempo real de todos y cada uno de los aviones aéreos                           | No            | si    | Desconocido |
| [AIS Hub](http://www.aishub.net/api)                                                                                                 | Datos en tiempo real de cualquier embarcación marina e interior equipada con sistema de seguimiento AIS        | `apiKey`      | No    | Desconocido |
| [Web AIS](http://www.aisweb.aer.mil.br/api/doc/index.cfm)                                                                            | Información aeronáutica en medios digitales producida por el Departamento de Control del Espacio Aéreo (DECEA) | `apiKey`      | No    | Desconocido |
| [Amadeus Travel Innovation Sandbox](https://sandbox.amadeus.com/)                                                                    | Búsqueda de viajes: uso limitado                                                                               | `apiKey`      | si    | Desconocido |
| [zona de la bahía de tránsito rápido](http://api.bart.gov)                                                                           | Estaciones y llegadas previstas para BART                                                                      | `apiKey`      | No    | Desconocido |
| [BlaBlaCar](https://dev.blablacar.com)                                                                                               | Buscar viajes para compartir coche                                                                             | `apiKey`      | si    | Desconocido |
| [Tránsito comunitario](https://github.com/transitland/transitland-datastore/blob/master/README.md#api-endpoints)                     | API de Transitland                                                                                             | No            | si    | Desconocido |
| [Goibibo](https://developer.goibibo.com/docs)                                                                                        | API para búsqueda de viajes                                                                                    | `apiKey`      | si    | Desconocido |
| [GraphHopper](https://graphhopper.com/api/1/docs/)                                                                                   | Enrutamiento de A a B con instrucciones paso a paso                                                            | `apiKey`      | si    | Desconocido |
| [APIs islandesas](http://docs.apis.is/)                                                                                              | API abiertas que brindan servicios en o con respecto a Islandia                                                | No            | si    | Desconocido |
| [ferrocarriles de la India](http://api.erail.in/)                                                                                    | Información de ferrocarriles indios                                                                            | `apiKey`      | No    | Desconocido |
| [Izu](http://api-docs.izi.travel/)                                                                                                   | Audioguía para viajeros                                                                                        | `apiKey`      | si    | Desconocido |
| [Metro de lisboa](http://app.metrolisboa.pt/status/getLinhas.php)                                                                    | Retrasos en líneas de metro                                                                                    | No            | No    | No          |
| [Naviti](https://api.navitia.io/)                                                                                                    | La API abierta para construir cosas geniales con datos de transporte                                           | `apiKey`      | si    | Desconocido |
| [BAÑOS DE REFUGIO](https://www.refugerestrooms.org/api/docs/#!/restrooms)                                                            | Proporciona acceso seguro a los baños para personas transgénero, intersexuales y no conformes con el género.   | No            | si    | Desconocido |
| [Aeropuerto de Schiphol](https://developer.schiphol.nl/)                                                                             | Schiphol                                                                                                       | `apiKey`      | si    | Desconocido |
| [TransitLand](https://transit.land/documentation/datastore/api-endpoints.html)                                                       | Agregación de tránsito                                                                                         | No            | si    | Desconocido |
| [Transporte para Atlanta, EE. UU.](http://www.itsmarta.com/app-developer-resources.aspx)                                             | Marta                                                                                                          | No            | No    | Desconocido |
| [Transporte para Auckland, Nueva Zelanda](https://api.at.govt.nz/)                                                                   | Transporte de Auckland                                                                                         | No            | si    | Desconocido |
| [Transporte para Bélgica](https://hello.irail.be/api/)                                                                               | API de transporte belga                                                                                        | No            | si    | Desconocido |
| [Transporte para Berlín, Alemania](https://github.com/derhuerst/vbb-rest/blob/3/docs/index.md)                                       | API de VBB de terceros                                                                                         | No            | si    | Desconocido |
| [Transporte a Burdeos, Francia](https://opendata.bordeaux-metropole.fr/explore/)                                                     | Burdeos Métropole transporte público y más (Francia)                                                           | `apiKey`      | si    | Desconocido |
| [Transporte para Boston, EE. UU.](https://mbta.com/developers/v3-api)                                                                | API de MBTA                                                                                                    | No            | No    | Desconocido |
| [Transporte para Budapest, Hungría](https://bkkfutar.docs.apiary.io)                                                                 | API de transporte público de Budapest                                                                          | No            | si    | Desconocido |
| [Transporte para Chicago, EE. UU.](http://www.transitchicago.com/developers/)                                                        | CTA                                                                                                            | No            | No    | Desconocido |
| [Transporte para la República Checa](https://www.chaps.cz/eng/products/idos-internet)                                                | API de transporte checo                                                                                        | No            | si    | Desconocido |
| [Transporte para Denver, EE. UU.](http://www.rtd-denver.com/gtfs-developer-guide.shtml)                                              | RTD                                                                                                            | No            | No    | Desconocido |
| [Transporte para Finlandia](https://digitransit.fi/en/developers/)                                                                   | API de transporte finlandés                                                                                    | No            | si    | Desconocido |
| [Transporte para Alemania](http://data.deutschebahn.com/dataset/api-fahrplan)                                                        | Deutsche Bahn (DB) API                                                                                         | `apiKey`      | No    | Desconocido |
| [Transporte a Grenoble, Francia](https://www.metromobilite.fr/pages/opendata/OpenDataApi.html)                                       | Transporte publico de Grenoble                                                                                 | No            | No    | No          |
| [Transporte para Honolulu, EE. UU.](http://hea.thebus.org/api_info.asp)                                                              | Información de transporte de Honolulu                                                                          | `apiKey`      | No    | Desconocido |
| [Transporte para la India](https://data.gov.in/sector/transport)                                                                     | API de transporte público de India                                                                             | `apiKey`      | si    | Desconocido |
| [Transporte para Lisboa, Portugal](https://emel.city-platform.com/opendata/)                                                         | Datos sobre rutas de autobuses, estacionamiento y tráfico.                                                     | `apiKey`      | si    | Desconocido |
| [Transporte para Londres, Inglaterra](https://api.tfl.gov.uk)                                                                        | API de TfL                                                                                                     | No            | si    | Desconocido |
| [Transporte para Manchester, Inglaterra](https://developer.tfgm.com/)                                                                | Datos de la red de transporte TfGM                                                                             | `apiKey`      | si    | No          |
| [Transporte para la ciudad de Nueva York, EE. UU.](http://datamine.mta.info/)                                                        | MTA                                                                                                            | `apiKey`      | No    | Desconocido |
| [Transporte para Noruega](http://reisapi.ruter.no/help)                                                                              | API de transporte noruego                                                                                      | No            | No    | Desconocido |
| [Transporte para Paris, Francia](http://restratpws.azurewebsites.net/swagger/)                                                       | Horarios en vivo simplificados                                                                                 | No            | No    | Desconocido |
| [Transporte para Paris, Francia](http://data.ratp.fr/api/v1/console/datasets/1.0/search/)                                            | API de datos abiertos RATP                                                                                     | No            | No    | Desconocido |
| [Transporte para Filadelfia, EE. UU.](http://www3.septa.org/hackathon/)                                                              | API SEPTA                                                                                                      | No            | No    | Desconocido |
| [Transporte para Sao Paulo, Brasil](http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/documentacao-api/) | SPTrans                                                                                                        | `OAuth`       | No    | Desconocido |
| [Transporte para Suecia](https://www.trafiklab.se/api)                                                                               | Consumidor de transporte público                                                                               | `OAuth`       | si    | Desconocido |
| [Transporte para Suiza](https://opentransportdata.swiss/en/)                                                                         | Datos abiertos oficiales de transporte público suizo                                                           | `apiKey`      | si    | Desconocido |
| [Transporte para Suiza](https://transport.opendata.ch/)                                                                              | API de transporte público suizo                                                                                | No            | si    | Desconocido |
| [Transporte para los Países Bajos](http://www.ns.nl/reisinformatie/ns-api)                                                           | NS, solo trenes                                                                                                | `apiKey`      | No    | Desconocido |
| [Transporte para los Países Bajos](https://github.com/skywave/KV78Turbo-OVAPI/wiki)                                                  | OVAPI, transporte público en todo el país                                                                      | No            | si    | Desconocido |
| [Transporte para Toronto, Canadá](https://myttc.ca/developers)                                                                       | Impuestos incluidos.                                                                                           | No            | si    | Desconocido |
| [Transporte para Estados Unidos](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf)                                              | API NextBus                                                                                                    | No            | No    | Desconocido |
| [Transporte para Vancouver, Canadá](https://developer.translink.ca/)                                                                 | TransLink                                                                                                      | `OAuth`       | si    | Desconocido |
| [Transporte para Washington, EE. UU.](https://developer.wmata.com/)                                                                  | API de transporte del metro de Washington                                                                      | `OAuth`       | si    | Desconocido |
| [Uber](https://developer.uber.com/products)                                                                                          | Solicitudes de viaje Uber y estimación de precios                                                              | `OAuth`       | si    | si          |
| [WhereIsMyTransport](https://developer.whereismytransport.com/)                                                                      | Plataforma de datos de transporte público en ciudades emergentes.                                              | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Acortadores de URL

| FUEGO                                                                      | Descripción                                                    | Autenticación | HTTPS | CORAZONES   |
| -------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Poco](http://dev.bitly.com/get_started.html)                              | Acortador de URL y gestión de enlaces                          | `OAuth`       | si    | Desconocido |
| [CleanURI](https://cleanuri.com/docs)                                      | Servicio de acortador de URL                                   | `No`          | si    | si          |
| [ClickMeter](https://support.clickmeter.com/hc/en-us/categories/201474986) | Monitoree, compare y optimice sus enlaces de marketing         | `apiKey`      | si    | Desconocido |
| [Rebrandly](https://developers.rebrandly.com/v1/docs)                      | Acortador de URL personalizado para compartir enlaces de marca | `apiKey`      | si    | Desconocido |
| [Reenlace](https://rel.ink)                                                | Acortador de URL gratuito y seguro                             | No            | si    | si          |

**[⬆ Volver al índice](#index)**

### Vehículo

| FUEGO                                                                   | Descripción                                                                                                                             | Autenticación | HTTPS | CORAZONES   |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Vehículos y precios brasileños](https://deividfortuna.github.io/fipe/) | Información sobre vehículos de la Economic Institute Institute Foundation - Fipe                                                        | No            | si    | Desconocido |
| [Kelley Blue Book](http://developer.kbb.com/#!/data/1-Default)          | Información del vehículo, precios, configuración y mucho más.                                                                           | `apiKey`      | si    | No          |
| [Mercedes Benz](https://developer.mercedes-benz.com/apis)               | Datos telemáticos, acceso remoto a las funciones del vehículo, configurador del automóvil, localizar concesionarios de servicio         | `apiKey`      | si    | No          |
| [NHTSA](https://vpic.nhtsa.dot.gov/api/)                                | Catálogo de información de productos NHTSA y listado de vehículos                                                                       | No            | si    | Desconocido |
| [Auto inteligente](https://smartcar.com/docs/)                          | Bloquee y desbloquee vehículos y obtenga datos como la lectura y la ubicación del odómetro. Funciona en la mayoría de los autos nuevos. | `OAuth`       | si    | si          |

**[⬆ Volver al índice](#index)**

### Vídeo

| FUEGO                                                                                              | Descripción                                                     | Autenticación | HTTPS | CORAZONES   |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------- | ----- | ----------- |
| [Una API de hielo y fuego](https://anapioficeandfire.com/)                                         | API de Juego de Tronos                                          | No            | si    | Desconocido |
| [Hacerse malo](https://breakingbadapi.com/documentation)                                           | Breaking Bad API                                                | No            | si    | Desconocido |
| [Rompiendo malas citas](https://github.com/shevabam/breaking-bad-quotes)                           | Algunas citas de Breaking Bad                                   | No            | si    | Desconocido |
| [Televisión checa](http://www.ceskatelevize.cz/xml/tv-program/)                                    | Programa de televisión de la televisión checa                   | No            | No    | Desconocido |
| [Dailymotion](https://developer.dailymotion.com/)                                                  | Dailymotion Developer API                                       | `OAuth`       | si    | Desconocido |
| [Harry Potter](https://www.potterapi.com/)                                                         | API de Harry Potter                                             | `apiKey`      | si    | si          |
| [Abrir base de datos de películas](http://www.omdbapi.com/)                                        | Información de la película                                      | `apiKey`      | si    | Desconocido |
| [Ron Swanson Quotes](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api) | Televisión                                                      | No            | si    | Desconocido |
| [STAPI](http://stapi.co)                                                                           | Información sobre todas las cosas de Star Trek                  | No            | No    | No          |
| [El Señor de los Anillos](https://the-one-api.herokuapp.com/)                                      | El señor de los anillos API                                     | `apiKey`      | si    | Desconocido |
| [TMDb](https://www.themoviedb.org/documentation/api)                                               | Datos de películas basadas en la comunidad.                     | `apiKey`      | si    | Desconocido |
| [Tracto](https://trakt.tv/b/api-docs)                                                              | Datos de películas y televisión                                 | `apiKey`      | si    | si          |
| [TVDB](https://api.thetvdb.com/swagger)                                                            | Datos de televisión                                             | `apiKey`      | si    | Desconocido |
| [TVMaze](http://www.tvmaze.com/api)                                                                | Datos del programa de televisión                                | No            | No    | Desconocido |
| [Vimeo](https://developer.vimeo.com/)                                                              | API de desarrollador de Vimeo                                   | `OAuth`       | si    | Desconocido |
| [Youtube](https://developers.google.com/youtube/)                                                  | Agregue la funcionalidad de YouTube a sus sitios y aplicaciones | `OAuth`       | si    | Desconocido |

**[⬆ Volver al índice](#index)**

### Clima

| FUEGO                                                                       | Descripción                              | Autenticación | HTTPS | CORAZONES   |
| --------------------------------------------------------------------------- | ---------------------------------------- | ------------- | ----- | ----------- |
| [7Timer!](http://www.7timer.info/doc.php?lang=en)                           | Clima, especialmente para Astroweather   | No            | No    | Desconocido |
| [APIXU](https://www.apixu.com/doc/request.aspx)                             | Clima                                    | `apiKey`      | si    | Desconocido |
| [MetaWeather](https://www.metaweather.com/api/)                             | Clima                                    | No            | si    | No          |
| [Departamento de Meteorología](https://api.met.no/weatherapi/documentation) | Datos meteorológicos y climáticos.       | No            | si    | Desconocido |
| [Datos climáticos de NOAA](https://www.ncdc.noaa.gov/cdo-web/)              | Datos meteorológicos y climáticos.       | `apiKey`      | si    | Desconocido |
| [ODWeather](http://api.oceandrivers.com/static/docs.html)                   | Tiempo y cámaras web meteorológicas      | No            | No    | Desconocido |
| [OpenUV](https://www.openuv.io)                                             | Pronóstico del índice UV en tiempo real  | `apiKey`      | si    | Desconocido |
| [OpenWeatherMap](http://openweathermap.org/api)                             | Clima                                    | `apiKey`      | No    | Desconocido |
| [Vidrio de tormenta](https://stormglass.io/)                                | Clima marino global de múltiples fuentes | `apiKey`      | si    | si          |
| [Weatherbit](https://www.weatherbit.io/api)                                 | Clima                                    | `apiKey`      | si    | Desconocido |
| [Yahoo! Clima](https://developer.yahoo.com/weather/)                        | Clima                                    | `apiKey`      | si    | Desconocido |

**[⬆ Volver al índice](#index)**
