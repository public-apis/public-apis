# API publiques [![Build Status](https://api.travis-ci.org/public-apis/public-apis.svg)](https://travis-ci.org/public-apis/public-apis)

Une liste collective d'API gratuites à utiliser dans le développement de logiciels et de sites Web.

Une API publique pour ce projet peut être trouvée [ici](https://github.com/davemachado/public-api)!

Pour plus d'informations sur la contribution à ce projet, veuillez consulter le [guide contributeur](.github/CONTRIBUTING.md).

Veuillez noter qu'un état de génération réussi indique que toutes les API répertoriées sont disponibles depuis la dernière mise à jour. Un état de génération défaillant indique qu'un ou plusieurs services peuvent ne pas être disponibles pour le moment.

## Indice

- [Animaux](#animals)
- [Manga](#anime)
- [Anti-Malware](#anti-malware)
- [Conception d'art](#art--design)
- [Livres](#books)
- [Affaires](#business)
- [Calendrier](#calendar)
- [Stockage dans le cloud et partage de fichiers](#cloud-storage--file-sharing)
- [Intégration continue](#continuous-integration)
- [Crypto-monnaie](#cryptocurrency)
- [Échange de devises](#currency-exchange)
- [La validation des données](#data-validation)
- [Développement](#development)
- [Dictionnaires](#dictionaries)
- [Documents et productivité](#documents--productivity)
- [Environnement](#environment)
- [Événements](#events)
- [La finance](#finance)
- [Nourriture boisson](#food--drink)
- [Jeux et bandes dessinées](#games--comics)
- [Géocodage](#geocoding)
- [Gouvernement](#government)
- [Santé](#health)
- [Emplois](#jobs)
- [Apprentissage automatique](#machine-learning)
- [La musique](#music)
- [Nouvelles](#news)
- [Données ouvertes](#open-data)
- [Projets Open Source](#open-source-projects)
- [Brevet](#patent)
- [Personnalité](#personality)
- [La photographie](#photography)
- [Science mathématique](#science--math)
- [Sécurité](#security)
- [Achats](#shopping)
- [Social](#social)
- [Sports et fitness](#sports--fitness)
- [Données de test](#test-data)
- [Analyse de texte](#text-analysis)
- [suivi](#tracking)
- [Transport](#transportation)
- [Raccourcisseurs d'URL](#url-shorteners)
- [Véhicule](#vehicle)
- [Vidéo](#video)
- [Temps](#weather)

### Animaux

| FEU                                                                                        | La description                                         | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------ | -------- | ----- | -------- |
| [Faits sur les chats](https://alexwohlbruck.github.io/cat-facts/)                          | Faits quotidiens sur les chats                         | Non      | Oui   | Non      |
| [Chats](https://docs.thecatapi.com/)                                                       | Photos de chats de Tumblr                              | `apiKey` | Oui   | Inconnue |
| [Chiens](https://dog.ceo/dog-api/)                                                         | Basé sur le jeu de données Stanford Dogs               | Non      | Oui   | Oui      |
| [HTTPCat](https://http.cat/)                                                               | Cat pour chaque statut HTTP                            | Non      | Oui   | Inconnue |
| [UICN](http://apiv3.iucnredlist.org/api/v3/docs)                                           | Liste rouge de l'UICN des espèces menacées             | `apiKey` | Non   | Inconnue |
| [Movebank](https://github.com/movebank/movebank-api-doc)                                   | Données sur les mouvements et la migration des animaux | Non      | Oui   | Inconnue |
| [Petfinder](https://www.petfinder.com/developers/v2/docs/)                                 | Adoption                                               | `OAuth`  | Oui   | Oui      |
| [PlaceGOAT](https://placegoat.com/)                                                        | Images de chèvre fictives                              | Non      | Oui   | Inconnue |
| [RandomCat](https://aws.random.cat/meow)                                                   | Photos aléatoires de chats                             | Non      | Oui   | Oui      |
| [RandomDog](https://random.dog/woof.json)                                                  | Photos aléatoires de chiens                            | Non      | Oui   | Oui      |
| [RandomFox](https://randomfox.ca/floof/)                                                   | Photos aléatoires de renards                           | Non      | Oui   | Non      |
| [RescueGroups](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) | Adoption                                               | Non      | Oui   | Inconnue |
| [Shibe.Online](http://shibe.online/)                                                       | Photos aléatoires de Shibu Inu, de chats ou d'oiseaux  | Non      | Oui   | Oui      |

**[⬆ Retour à l'index](#index)**

### Manga

| FEU                                                                       | La description                        | Auth    | HTTPS | CORS     |
| ------------------------------------------------------------------------- | ------------------------------------- | ------- | ----- | -------- |
| [AniList](https://github.com/AniList/ApiV2-GraphQL-Docs)                  | Découverte et suivi d'anime           | `OAuth` | Oui   | Inconnue |
| [AnimeNewsNetwork](https://www.animenewsnetwork.com/encyclopedia/api.php) | Nouvelles de l'industrie de l'anime   | Non     | Oui   | Oui      |
| [Jikan](https://jikan.moe)                                                | API MyAnimeList non officielle        | Non     | Oui   | Oui      |
| [Kitsu](http://docs.kitsu.apiary.io/)                                     | Plateforme de découverte d'anime      | `OAuth` | Oui   | Inconnue |
| [Studio Ghibli](https://ghibliapi.herokuapp.com)                          | Ressources des films du Studio Ghibli | Non     | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Anti-Malware

| FEU                                                                         | La description                      | Auth     | HTTPS | CORS     |
| --------------------------------------------------------------------------- | ----------------------------------- | -------- | ----- | -------- |
| [AbusIPDB](https://docs.abuseipdb.com/)                                     | Réputation IP / domaine / URL       | `apiKey` | Oui   | Inconnue |
| [AlienVault Open Threat Exchange (OTX)](https://otx.alienvault.com/api/)    | Réputation IP / domaine / URL       | `apiKey` | Oui   | Inconnue |
| [Navigation sécurisée Google](https://developers.google.com/safe-browsing/) | Marquage de lien / domaine Google   | `apiKey` | Oui   | Inconnue |
| [Metacert](https://metacert.com/)                                           | Signalisation de lien Metacert      | `apiKey` | Oui   | Inconnue |
| [VirusTotal](https://www.virustotal.com/en/documentation/public-api/)       | Analyse de fichier / URL VirusTotal | `apiKey` | Oui   | Inconnue |
| [Web Of Trust (WOT)](https://www.mywot.com/en/API)                          | Réputation du site Web              | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Conception d'art

| FEU                                                                      | La description            | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------ | ------------------------- | -------- | ----- | -------- |
| [Behance](https://www.behance.net/dev)                                   | Conception                | `apiKey` | Oui   | Inconnue |
| [Cooper Hewitt](https://collection.cooperhewitt.org/api)                 | Smithsonian Design Museum | `apiKey` | Oui   | Inconnue |
| [Dribble](http://developer.dribbble.com/v2/)                             | Conception                | `OAuth`  | Non   | Inconnue |
| [Musées d'art de Harvard](https://github.com/harvardartmuseums/api-docs) | Art                       | `apiKey` | Non   | Inconnue |
| [Iconfinder](https://developer.iconfinder.com)                           | Icônes                    | `apiKey` | Oui   | Inconnue |
| [Icônes8](http://docs.icons8.apiary.io/#reference/0/meta)                | Icônes                    | `OAuth`  | Oui   | Inconnue |
| [Projet de nom](http://api.thenounproject.com/index.html)                | Icônes                    | `OAuth`  | Non   | Inconnue |
| [Rijksmuseum](https://www.rijksmuseum.nl/en/api)                         | Art                       | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Livres

| FEU                                                                       | La description                                    | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------- | ------------------------------------------------- | -------- | ----- | -------- |
| [Bhagavad Gita](https://bhagavadgita.io/api)                              | Texte de la Bhagavad Gita                         | `OAuth`  | Oui   | Oui      |
| [Bibliographie nationale britannique](http://bnb.data.bl.uk/)             | Livres                                            | Non      | Non   | Inconnue |
| [Goodreads](https://www.goodreads.com/api)                                | Livres                                            | `apiKey` | Oui   | Inconnue |
| [livres Google](https://developers.google.com/books/)                     | Livres                                            | `OAuth`  | Oui   | Inconnue |
| [LibGen](http://garbage.world/posts/libgen/)                              | Moteur de recherche Library Genesis               | Non      | Non   | Inconnue |
| [Bibliothèque ouverte](https://openlibrary.org/developers/api)            | Livres, couvertures de livres et données connexes | Non      | Oui   | Inconnue |
| [Penguin Publishing](http://www.penguinrandomhouse.biz/webservices/rest/) | Livres, couvertures de livres et données connexes | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Affaires

| FEU                                                                        | La description                                                                  | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Recherche de charité](http://charityapi.orghunter.com/)                   | Données caritatives à but non lucratif                                          | `apiKey` | Non   | Inconnue |
| [Logo Clearbit](https://clearbit.com/docs#logo-api)                        | Recherchez des logos d'entreprise et intégrez-les dans vos projets              | `apiKey` | Oui   | Inconnue |
| [Domainsdb.info](https://domainsdb.info/)                                  | Recherche de noms de domaine enregistrés                                        | Non      | Oui   | Inconnue |
| [Pigiste](https://developers.freelancer.com)                               | Embaucher des pigistes pour faire le travail                                    | `OAuth`  | Oui   | Inconnue |
| [Gmail](https://developers.google.com/gmail/api/)                          | Accès flexible et RESTful à la boîte de réception de l'utilisateur              | `OAuth`  | Oui   | Inconnue |
| [Google Analytics](https://developers.google.com/analytics/)               | Collectez, configurez et analysez vos données pour atteindre le bon public      | `OAuth`  | Oui   | Inconnue |
| [MailboxValidator](https://www.mailboxvalidator.com/api-single-validation) | Valider l'adresse e-mail pour améliorer la délivrabilité                        | `apiKey` | Oui   | Inconnue |
| [mailgun](https://www.mailgun.com/)                                        | Service de messagerie                                                           | `apiKey` | Oui   | Inconnue |
| [markerapi](http://www.markerapi.com/)                                     | Recherche de marque                                                             | Non      | Non   | Inconnue |
| [Ticksel](https://ticksel.com)                                             | Des analyses de site Web conviviales conçues pour les humains                   | Non      | Oui   | Inconnue |
| [Trello](https://developers.trello.com/)                                   | Tableaux, listes et fiches pour vous aider à organiser et prioriser vos projets | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Calendrier

| FEU                                                                  | La description                                                                               | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Index du calendrier](https://www.calendarindex.com/)                | Vacances et jours ouvrables dans le monde                                                    | `apiKey` | Oui   | Oui      |
| [Calendrier de l'église](http://calapi.inadiutorium.cz/)             | Calendrier liturgique catholique                                                             | Non      | Non   | Inconnue |
| [Czech Namedays Calendar](http://svatky.adresa.info/)                | Rechercher un nom et retourne la date du jour                                                | Non      | Non   | Inconnue |
| [Google Agenda](https://developers.google.com/google-apps/calendar/) | Afficher, créer et modifier des événements d'agenda Google                                   | `OAuth`  | Oui   | Inconnue |
| [Calendrier hébreu](https://www.hebcal.com/home/developer-apis)      | Convertissez entre grégorien et hébreu, récupérez les heures de Shabbat et de vacances, etc. | Non      | Non   | Inconnue |
| [Vacances](https://holidayapi.com/)                                  | Données historiques concernant les vacances                                                  | `apiKey` | Oui   | Inconnue |
| [LectServe](http://www.lectserve.com)                                | Calendrier liturgique protestant                                                             | Non      | Non   | Inconnue |
| [Nager.Date](https://date.nager.at)                                  | Jours fériés dans plus de 90 pays                                                            | Non      | Oui   | Non      |
| [Calendrier des Namedays](https://api.abalin.net/)                   | Fournit des noms pour plusieurs pays                                                         | Non      | Oui   | Oui      |
| [Jours chômés](https://github.com/gadael/icsdb)                      | Base de données des fichiers ICS pour les jours non ouvrés                                   | Non      | Oui   | Inconnue |
| [Calendrier russe](https://github.com/egno/work-calendar)            | Vérifiez si une date est un jour férié russe ou non                                          | Non      | Oui   | Non      |

**[⬆ Retour à l'index](#index)**

### Stockage dans le cloud et partage de fichiers

| FEU                                                                     | La description                                                                  | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Boîte](https://developer.box.com/)                                     | Partage et stockage de fichiers                                                 | `OAuth`  | Oui   | Inconnue |
| [Dropbox](https://www.dropbox.com/developers)                           | Partage et stockage de fichiers                                                 | `OAuth`  | Oui   | Inconnue |
| [Google Drive](https://developers.google.com/drive/)                    | Partage et stockage de fichiers                                                 | `OAuth`  | Oui   | Inconnue |
| [OneDrive](https://dev.onedrive.com/)                                   | Partage et stockage de fichiers                                                 | `OAuth`  | Oui   | Inconnue |
| [Pastebin](https://pastebin.com/api/)                                   | Stockage de texte brut                                                          | `apiKey` | Oui   | Inconnue |
| [Temporel](https://gateway.temporal.cloud/ipns/docs.api.temporal.cloud) | Stockage et partage de fichiers basés sur IPFS avec dénomination IPNS en option | `apiKey` | Oui   | Non      |
| [WeTransfer](https://developers.wetransfer.com)                         | Partage de fichiers                                                             | `apiKey` | Oui   | Oui      |

**[⬆ Retour à l'index](#index)**

### Intégration continue

| FEU                                                     | La description                                                                                             | Auth     | HTTPS | CORS     |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [CircleCI](https://circleci.com/docs/api/v1-reference/) | Automatisez le processus de développement logiciel en utilisant une intégration et une livraison continues | `apiKey` | Oui   | Inconnue |
| [Codehiphip](https://apidocs.codeship.com/)             | Codeship est une plate-forme d'intégration continue dans le cloud                                          | `apiKey` | Oui   | Inconnue |
| [Travis CI](https://docs.travis-ci.com/api/)            | Synchronisez vos projets GitHub avec Travis CI pour tester votre code en quelques minutes                  | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Crypto-monnaie

| FEU                                                                      | La description                                                                     | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Binance](https://github.com/binance-exchange/binance-official-api-docs) | Échange contre des crypto-monnaies basées en Chine                                 | `apiKey` | Oui   | Inconnue |
| [BitcoinAverage](https://apiv2.bitcoinaverage.com/)                      | Données sur les prix des actifs numériques pour l'industrie de la blockchain       | `apiKey` | Oui   | Inconnue |
| [BitcoinCharts](https://bitcoincharts.com/about/exchanges/)              | Données financières et techniques liées au réseau Bitcoin                          | Non      | Oui   | Inconnue |
| [Bitfinex](https://docs.bitfinex.com/docs)                               | Plateforme de trading de crypto-monnaie                                            | `apiKey` | Oui   | Inconnue |
| [Bitmex](https://www.bitmex.com/app/apiOverview)                         | Plateforme de trading de dérivés de crypto-monnaie en temps réel basée à Hong Kong | `apiKey` | Oui   | Inconnue |
| [Bittrex](https://bittrex.com/Home/Api)                                  | Plateforme de trading cryptographique nouvelle génération                          | `apiKey` | Oui   | Inconnue |
| [Bloquer](https://www.block.io/docs/basic)                               | Paiement Bitcoin, portefeuille et données de transaction                           | `apiKey` | Oui   | Inconnue |
| [Blockchain](https://www.blockchain.info/api)                            | Paiement Bitcoin, portefeuille et données de transaction                           | Non      | Oui   | Inconnue |
| [CoinAPI](https://docs.coinapi.io/)                                      | Tous les échanges de devises s'intègrent sous une seule API                        | `apiKey` | Oui   | Non      |
| [Coinbase](https://developers.coinbase.com)                              | Prix Bitcoin, Bitcoin Cash, Litecoin et Ethereum                                   | `apiKey` | Oui   | Inconnue |
| [Coinbase Pro](https://docs.pro.coinbase.com/#api)                       | Plateforme de trading de crypto-monnaie                                            | `apiKey` | Oui   | Inconnue |
| [CoinDesk](http://www.coindesk.com/api/)                                 | Indice de prix Bitcoin                                                             | Non      | Non   | Inconnue |
| [CoinGecko](http://www.coingecko.com/api)                                | Prix de la crypto-monnaie, marché et données de développeur / sociales             | Non      | Oui   | Oui      |
| [Coinigy](https://coinigy.docs.apiary.io)                                | Interagir avec les comptes Coinigy et échanger directement                         | `apiKey` | Oui   | Inconnue |
| [CoinLayer](https://coinlayer.com)                                       | Taux de change des devises crypto en temps réel                                    | `apiKey` | Oui   | Inconnue |
| [Coinlib](https://coinlib.io/apidocs)                                    | Prix des devises crypto                                                            | `apiKey` | Oui   | Inconnue |
| [Coinlore](https://www.coinlore.com/cryptocurrency-data-api)             | Prix, volume et plus des crypto-monnaies                                           | Non      | Oui   | Inconnue |
| [CoinMarketCap](https://coinmarketcap.com/api/)                          | Prix des crypto-monnaies                                                           | `apiKey` | Oui   | Inconnue |
| [Coinpaprika](https://api.coinpaprika.com)                               | Prix, volume et plus des crypto-monnaies                                           | Non      | Oui   | Oui      |
| [CoinRanking](https://docs.coinranking.com/)                             | Données de crypto-monnaie en direct                                                | Non      | Oui   | Inconnue |
| [CryptoCompare](https://www.cryptocompare.com/api#)                      | Comparaison des crypto-monnaies                                                    | Non      | Oui   | Inconnue |
| [Cryptonator](https://www.cryptonator.com/api/)                          | Taux de change des crypto-monnaies                                                 | Non      | Oui   | Inconnue |
| [Gémeaux](https://docs.gemini.com/rest-api/)                             | Échange de crypto-monnaies                                                         | Non      | Oui   | Inconnue |
| [ICObench](https://icobench.com/developers)                              | Diverses informations sur la liste, les notes, les statistiques, etc.              | `apiKey` | Oui   | Inconnue |
| [Livecoin](https://www.livecoin.net/api)                                 | Échange de crypto-monnaie                                                          | Non      | Oui   | Inconnue |
| [MarketBitcoin](https://www.mercadobitcoin.net/api-doc/)                 | Informations sur la crypto-monnaie brésilienne                                     | Non      | Oui   | Inconnue |
| [Nexchange](https://nexchange2.docs.apiary.io/)                          | Service d'échange de crypto-monnaie automatisé                                     | Non      | Non   | Oui      |
| [NiceHash](https://docs.nicehash.com/)                                   | Le plus grand marché minier de cryptographie                                       | `apiKey` | Oui   | Inconnue |
| [Poloniex](https://poloniex.com/support/api/)                            | Échange d'actifs numériques basé aux États-Unis                                    | `apiKey` | Oui   | Inconnue |
| [worldcoinındex](https://www.worldcoinindex.com/apiservice)              | Prix des crypto-monnaies                                                           | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Échange de devises

| FEU                                                                                                               | La description                                                 | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------- | ----- | -------- |
| [1Forge](https://1forge.com/forex-data-api/api-documentation)                                                     | Données du marché des devises Forex                            | `apiKey` | Oui   | Inconnue |
| [Currencylayer](https://currencylayer.com/documentation)                                                          | Taux de change et conversion de devises                        | `apiKey` | Oui   | Inconnue |
| [Banque nationale tchèque](https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml) | Une collection de taux de change                               | Non      | Oui   | Inconnue |
| [ExchangeRate-API](https://www.exchangerate-api.com)                                                              | Conversion de devises gratuite                                 | Non      | Oui   | Oui      |
| [Exchangeratesapi.io](https://exchangeratesapi.io)                                                                | Taux de change avec conversion de devises                      | Non      | Oui   | Oui      |
| [Fixer.io](http://fixer.io)                                                                                       | Taux de change et conversion de devises                        | `apiKey` | Oui   | Inconnue |
| [Saucisse](https://www.frankfurter.app/docs)                                                                      | Taux de change, conversion de devises et séries chronologiques | Non      | Oui   | Oui      |
| [ratesapi](https://ratesapi.io)                                                                                   | Taux de change gratuits et taux historiques                    | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### La validation des données

| FEU                                                                         | La description                                                                        | Auth     | HTTPS | CORS     |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Cloudmersive Validate](https://cloudmersive.com/validate-api)              | Valider les adresses e-mail, numéros de téléphone, numéros de TVA et noms de domaine  | `apiKey` | Oui   | Oui      |
| [languagelayer](https://languagelayer.com)                                  | Détection de langue                                                                   | Non      | Oui   | Inconnue |
| [Lob.com](https://lob.com/)                                                 | Vérification d'adresse aux États-Unis                                                 | `apiKey` | Oui   | Inconnue |
| [boîte aux lettres](https://mailboxlayer.com)                               | Validation de l'adresse e-mail                                                        | Non      | Oui   | Inconnue |
| [NumValidate](https://numvalidate.com)                                      | Validation du numéro de téléphone Open Source                                         | Non      | Oui   | Inconnue |
| [numverify](https://numverify.com)                                          | Validation du numéro de téléphone                                                     | Non      | Oui   | Inconnue |
| [PurgoMalum](http://www.purgomalum.com)                                     | Validateur de contenu contre le blasphème et l'obscénité                              | Non      | Non   | Inconnue |
| [US Autocomplete](https://smartystreets.com/docs/cloud/us-autocomplete-api) | Entrez rapidement les données d'adresse avec des suggestions d'adresses en temps réel | `apiKey` | Oui   | Oui      |
| [Extrait américain](https://smartystreets.com/products/apis/us-extract-api) | Extraire les adresses postales de n'importe quel texte, y compris les e-mails         | `apiKey` | Oui   | Oui      |
| [Adresse US](https://smartystreets.com/docs/cloud/us-street-api)            | Valider et ajouter des données pour toute adresse postale américaine                  | `apiKey` | Oui   | Oui      |
| [vatlay est](https://vatlayer.com)                                          | Validation du numéro de TVA                                                           | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Développement

| FEU                                                                                                  | La description                                                                                                              | Auth            | HTTPS | CORS     |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------- | ----- | -------- |
| [24 demandes de tirage](https://24pullrequests.com/api)                                              | Projet de promotion de la collaboration open source en décembre                                                             | Non             | Oui   | Oui      |
| [Agify.io](https://agify.io)                                                                         | Estime l'âge à partir d'un prénom                                                                                           | Non             | Oui   | Oui      |
| [ApiFlash](https://apiflash.com/)                                                                    | API de capture d'écran basée sur Chrome pour les développeurs                                                               | `apiKey`        | Oui   | Inconnue |
| [Apility.io](https://apility.io/apidocs/)                                                            | Liste de blocage d'API anti-abus IP, Domaines et Emails                                                                     | Non             | Oui   | Oui      |
| [APIs.guru](https://apis.guru/api-doc/)                                                              | Wikipedia pour les API Web, spécifications OpenAPI / Swagger pour les API publiques                                         | Non             | Oui   | Inconnue |
| [BetterMeta](http://bettermeta.io)                                                                   | Renvoyer les balises META d'un site au format JSON                                                                          | `X-Mashape-Key` | Oui   | Inconnue |
| [Bitbucket](https://developer.atlassian.com/bitbucket/api/2/reference/)                              | API Bitbucket                                                                                                               | `OAuth`         | Oui   | Inconnue |
| [Ennuyé](https://www.boredapi.com/)                                                                  | Trouvez des activités aléatoires pour combattre l'ennui                                                                     | Non             | Oui   | Inconnue |
| [Browshot](https://browshot.com/api/documentation)                                                   | Faites facilement des captures d'écran de pages Web dans n'importe quelle taille d'écran, comme n'importe quel appareil     | `apiKey`        | Oui   | Inconnue |
| [CDNJS](https://api.cdnjs.com/libraries/jquery)                                                      | Info bibliothèque sur CDNJS                                                                                                 | Non             | Oui   | Inconnue |
| [Changelogs.md](https://changelogs.md)                                                               | Métadonnées du journal des modifications structurées à partir de projets open source                                        | Non             | Oui   | Inconnue |
| [CountAPI](https://countapi.xyz)                                                                     | Service de comptage simple et gratuit. Vous pouvez l'utiliser pour suivre les visites de page et des événements spécifiques | Non             | Oui   | Oui      |
| [Statut DigitalOcean](https://status.digitalocean.com/api/v1)                                        | Statut de tous les services DigitalOcean                                                                                    | Non             | Oui   | Inconnue |
| [Infos sur DomainDb](https://domainsdb.info)                                                         | Recherche de nom de domaine pour trouver tous les domaines contenant des mots / phrases / etc                               | Non             | Oui   | Inconnue |
| [Faceplusplus](https://www.faceplusplus.com/)                                                        | Un outil pour détecter le visage                                                                                            | `OAuth`         | Oui   | Inconnue |
| [Genderize.io](https://genderize.io)                                                                 | Estime un sexe à partir d'un prénom                                                                                         | Non             | Oui   | Oui      |
| [GitHub](https://developer.github.com/v3/)                                                           | Utilisez les référentiels GitHub, le code et les informations utilisateur par programmation                                 | `OAuth`         | Oui   | Oui      |
| [Gitlab](https://docs.gitlab.com/ee/api/)                                                            | Automatisez l'interaction GitLab par programmation                                                                          | `OAuth`         | Oui   | Inconnue |
| [la grille](https://developer.gitter.im/docs/welcome)                                                | Chat pour les développeurs                                                                                                  | `OAuth`         | Oui   | Inconnue |
| [HTTP2.Pro](https://http2.pro/doc/api)                                                               | Tester les points de terminaison pour la prise en charge du protocole HTTP / 2 client et serveur                            | Non             | Oui   | Inconnue |
| [Synthèse vocale IBM](https://console.bluemix.net/docs/services/text-to-speech/getting-started.html) | Convertir du texte en discours                                                                                              | `apiKey`        | Oui   | Oui      |
| [Graphiques d'images](https://documentation.image-charts.com/)                                       | Générez des graphiques, des codes QR et des images graphiques                                                               | Non             | Oui   | Oui      |
| [import.io](http://api.docs.import.io/)                                                              | Récupérer des données structurées à partir d'un site Web ou d'un flux RSS                                                   | `apiKey`        | Oui   | Inconnue |
| [IPify](https://www.ipify.org/)                                                                      | Une API d'adresse IP simple                                                                                                 | Non             | Oui   | Inconnue |
| [IPinfo](https://ipinfo.io/developers)                                                               | Une autre API d'adresse IP simple                                                                                           | Non             | Oui   | Inconnue |
| [JSON 2 JSONP](https://json2jsonp.com/)                                                              | Convertir JSON en JSONP (à la volée) pour des demandes de données interdomaines faciles à l'aide de JavaScript côté client  | Non             | Oui   | Inconnue |
| [JSONbin.io](https://jsonbin.io)                                                                     | Service de stockage JSON gratuit. Idéal pour les applications Web, sites Web et applications mobiles à petite échelle       | `apiKey`        | Oui   | Oui      |
| [Juge0](https://api.judge0.com/)                                                                     | Compiler et exécuter le code source                                                                                         | Non             | Oui   | Inconnue |
| [Validons](https://github.com/letsvalidate/api)                                                      | Découvre les technologies utilisées sur les sites Web et URL vers la miniature                                              | Non             | Oui   | Inconnue |
| [License-API](https://github.com/cmccandless/license-api/blob/master/README.md)                      | API REST non officielle pour choosealicense.com                                                                             | Non             | Oui   | Non      |
| [Recherche de fournisseur d'adresse MAC](https://macaddress.io)                                      | Récupérer les détails du fournisseur et d'autres informations concernant une adresse MAC donnée ou une OUI                  | `apiKey`        | Oui   | Oui      |
| [Nationalize.io](https://nationalize.io)                                                             | Estimer la nationalité d'un prénom                                                                                          | Non             | Oui   | Oui      |
| [OOPSpam](https://oopspam.com/)                                                                      | Service de filtrage de spam multiples                                                                                       | Non             | Oui   | Oui      |
| [Plino](https://plino.herokuapp.com/)                                                                | Système de filtrage anti-spam                                                                                               | Non             | Oui   | Inconnue |
| [Facteur](https://docs.api.getpostman.com/)                                                          | Outil pour tester les API                                                                                                   | `apiKey`        | Oui   | Inconnue |
| [ProxyCrawl](https://proxycrawl.com)                                                                 | Service anticaptcha de grattage et de ramper                                                                                | `apiKey`        | Oui   | Inconnue |
| [API publiques](https://github.com/davemachado/public-api)                                           | Une liste collective d'API JSON gratuites à utiliser dans le développement Web                                              | Non             | Oui   | Inconnue |
| [Poutres Pusher](https://pusher.com/beams)                                                           | Notifications push pour Android et iOS                                                                                      | `apiKey`        | Oui   | Inconnue |
| [QR Code](http://qrtag.net/api/)                                                                     | Créez un code QR et un raccourcisseur d'URL faciles à lire                                                                  | Non             | Oui   | Oui      |
| [QR Code](http://goqr.me/api/)                                                                       | Générer et décoder / lire des graphiques de code QR                                                                         | Non             | Oui   | Inconnue |
| [QuickChart](https://quickchart.io/)                                                                 | Générer des images de graphiques et de graphiques                                                                           | Non             | Oui   | Oui      |
| [ReqRes](https://reqres.in/)                                                                         | Une API REST hébergée prête à répondre à vos demandes AJAX                                                                  | Non             | Oui   | Inconnue |
| [ScraperApi](https://www.scraperapi.com)                                                             | Créez facilement des grattoirs Web évolutifs                                                                                | `apiKey`        | Oui   | Inconnue |
| [ScreenshotAPI.net](https://screenshotapi.net/)                                                      | Créez des captures d'écran de site Web au pixel près                                                                        | `apiKey`        | Oui   | Oui      |
| [SHOUTCLOUD](http://shoutcloud.io/)                                                                  | TOUT-CAPS COMME SERVICE                                                                                                     | Non             | Non   | Inconnue |
| [StackExchange](https://api.stackexchange.com/)                                                      | Forum de questions et réponses pour les développeurs                                                                        | `OAuth`         | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Dictionnaires

| FEU                                                 | La description                                                      | Auth     | HTTPS | CORS     |
| --------------------------------------------------- | ------------------------------------------------------------------- | -------- | ----- | -------- |
| [Langage du robot](https://www.linguarobot.io)      | Définitions de mots, prononciations, synonymes, antonymes et autres | `apiKey` | Oui   | Oui      |
| [Merriam Webster](https://dictionaryapi.com/)       | Dictionnaire et données du thésaurus                                | `apiKey` | Oui   | Inconnue |
| [OwlBot](https://owlbot.info/)                      | Définitions avec exemple de phrase et photo si disponibles          | `apiKey` | Oui   | Oui      |
| [Oxford](https://developer.oxforddictionaries.com/) | Données du dictionnaire                                             | `apiKey` | Oui   | Non      |
| [Wordnik](http://developer.wordnik.com)             | Données du dictionnaire                                             | `apiKey` | Non   | Inconnue |
| [Mots](https://www.wordsapi.com/)                   | Définitions et synonymes de plus de 150 000 mots                    | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Documents et productivité

| FEU                                                                                        | La description                                                                     | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Conversion de documents et de données Cloudmersive](https://cloudmersive.com/convert-api) | HTML / URL au format PDF / PNG, documents Office au format PDF, conversion d'image | `apiKey` | Oui   | Oui      |
| [File.io](https://www.file.io)                                                             | Partage de fichiers                                                                | Non      | Oui   | Inconnue |
| [Mercure](https://mercury.postlight.com/web-parser/)                                       | Analyseur Web                                                                      | `apiKey` | Oui   | Inconnue |
| [pdflayer](https://pdflayer.com)                                                           | HTML / URL vers PDF                                                                | `apiKey` | Oui   | Inconnue |
| [Poche](https://getpocket.com/developer/)                                                  | Service de bookmarking                                                             | `OAuth`  | Oui   | Inconnue |
| [PrexView](https://prexview.com)                                                           | Données de XML ou JSON vers PDF, HTML ou Image                                     | `apiKey` | Oui   | Inconnue |
| [Pack de repos](https://restpack.io/)                                                      | Fournit capture d'écran, HTML au format PDF et API d'extraction de contenu         | `apiKey` | Oui   | Inconnue |
| [Todoist](https://developer.todoist.com)                                                   | Todo Lists                                                                         | `OAuth`  | Oui   | Inconnue |
| [Vector Express](http://vector.express)                                                    | API de conversion de fichiers vectoriels gratuits                                  | Non      | Non   | Oui      |
| [WakaTime](https://wakatime.com/developers)                                                | Classements automatisés de suivi du temps pour les programmeurs                    | Non      | Oui   | Inconnue |
| [Wunderlist](https://developer.wunderlist.com/documentation)                               | Todo Lists                                                                         | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Environnement

| FEU                                                                                                    | La description                                                                                  | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [AirVisual](https://airvisual.com/api)                                                                 | Qualité de l'air et données météorologiques                                                     | `apiKey` | Oui   | Inconnue |
| [GrünstromIndex](https://www.corrently.de/hintergrund/gruenstromindex/index.html)                      | Indice de l'énergie verte pour l'Allemagne (Grünstromindex / GSI)                               | Non      | Non   | Oui      |
| [OpenAQ](https://docs.openaq.org/)                                                                     | Données de qualité en plein air                                                                 | `apiKey` | Oui   | Inconnue |
| [PM25.in](http://www.pm25.in/api_doc)                                                                  | Qualité de l'air en Chine                                                                       | `apiKey` | Non   | Inconnue |
| [PVWatts](https://developer.nrel.gov/docs/solar/pvwatts/v6/)                                           | Systèmes énergétiques de production d'énergie photovoltaïque (PV)                               | `apiKey` | Oui   | Inconnue |
| [UK Carbon Intensity](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v1-0-0) | L'API officielle de l'intensité du carbone pour la Grande-Bretagne développée par National Grid | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Événements

| FEU                                                                                                                             | La description                                          | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------- | ----- | -------- |
| [Eventbrite](https://www.eventbrite.com/developer/v3/)                                                                          | Trouver des événements                                  | `OAuth`  | Oui   | Inconnue |
| [Picatic](http://developer.picatic.com/?utm_medium=web&utm_source=github&utm_campaign=public-apis%20repo&utm_content=toddmotto) | Vendez vos billets n'importe où                         | `apiKey` | Oui   | Inconnue |
| [Ticketmaster](http://developer.ticketmaster.com/products-and-docs/apis/getting-started/)                                       | Rechercher des événements, des attractions ou des lieux | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### La finance

| FEU                                                        | La description                                                                                   | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------- | ----- | -------- |
| [Alpha Vantage](https://www.alphavantage.co/)              | Données boursières en temps réel et historiques                                                  | `apiKey` | Oui   | Inconnue |
| [Barchart OnDemand](https://www.barchartondemand.com/free) | Stock, Futures et données du marché Forex                                                        | `apiKey` | Oui   | Inconnue |
| [Nuage IEX](https://iexcloud.io/)                          | Données boursières et boursières historiques et en temps réel                                    | `apiKey` | Oui   | Oui      |
| [IG](https://labs.ig.com/gettingstarted)                   | Spreadbetting et CFD Market Data                                                                 | `apiKey` | Oui   | Inconnue |
| [Plaid](https://plaid.com/)                                | Connectez-vous avec les comptes bancaires des utilisateurs et accédez aux données de transaction | `apiKey` | Oui   | Inconnue |
| [Razorpay IFSC](https://ifsc.razorpay.com/)                | Code indien des systèmes financiers (codes des succursales bancaires)                            | Non      | Oui   | Inconnue |
| [Tradier](https://developer.tradier.com)                   | Données sur le marché américain des actions / options (différé, intrajournalier, historique)     | `OAuth`  | Oui   | Oui      |
| [YNAB](https://api.youneedabudget.com/)                    | Budgétisation et planification                                                                   | `OAuth`  | Oui   | Oui      |

**[⬆ Retour à l'index](#index)**

### Nourriture boisson

| FEU                                                                                | La description                                                      | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------- | ----- | -------- |
| [Edamam](https://developer.edamam.com/)                                            | Recherche de recettes                                               | `apiKey` | Oui   | Inconnue |
| [LCBO](https://lcboapi.com/)                                                       | De l'alcool                                                         | `apiKey` | Oui   | Inconnue |
| [Open Brewery DB](https://www.openbrewerydb.org)                                   | Brasseries, cidreries et magasins de bouteilles de bière artisanale | Non      | Oui   | Oui      |
| [Open Food Facts](https://world.openfoodfacts.org/data)                            | Base de données sur les produits alimentaires                       | Non      | Oui   | Inconnue |
| [PunkAPI](https://punkapi.com/)                                                    | Brewdog Beer Recipes                                                | Non      | Oui   | Inconnue |
| [Recette Puppy](http://www.recipepuppy.com/about/api/)                             | Aliments                                                            | Non      | Non   | Inconnue |
| [TacoFancy](https://github.com/evz/tacofancy-api)                                  | Base de données sur les tacos dirigée par la communauté             | Non      | Non   | Inconnue |
| [Le rapport de la semaine](https://github.com/andyklimczak/TheReportOfTheWeek-API) | Avis sur les aliments et les boissons                               | Non      | Oui   | Inconnue |
| [TheCocktailDB](https://www.thecocktaildb.com/api.php)                             | Recettes de cocktails                                               | `apiKey` | Oui   | Oui      |
| [TheMealDB](https://www.themealdb.com/api.php)                                     | Recettes de repas                                                   | `apiKey` | Oui   | Oui      |
| [Qu'est-ce qu'il y'a au menu?](http://nypl.github.io/menus-api/)                   | Collection de menus historiques transcrits par l'homme NYPL         | `apiKey` | Non   | Inconnue |
| [Zomato](https://developers.zomato.com/api)                                        | Découvrir les restaurants                                           | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Jeux et bandes dessinées

| FEU                                                                          | La description                                                                                                        | Auth            | HTTPS | CORS     |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------- | ----- | -------- |
| [Age of Empires II](https://age-of-empires-2-api.herokuapp.com)              | Obtenez des informations sur les ressources d'Age of Empires II                                                       | Non             | Oui   | Inconnue |
| [AmiiboAPI](http://www.amiiboapi.com/)                                       | Informations Amiibo                                                                                                   | Non             | Non   | Oui      |
| [Battle.net](https://dev.battle.net/)                                        | Blizzard Entertainment                                                                                                | `apiKey`        | Oui   | Inconnue |
| [Base de données Chuck Norris](http://www.icndb.com/api/)                    | Blagues                                                                                                               | Non             | Non   | Inconnue |
| [Clash of Clans](https://developer.clashofclans.com)                         | Informations sur le jeu Clash of Clans                                                                                | `apiKey`        | Oui   | Inconnue |
| [Clash Royale](https://developer.clashroyale.com)                            | Informations sur le jeu Clash Royale                                                                                  | `apiKey`        | Oui   | Inconnue |
| [La bande dessinée arrive](https://comicvine.gamespot.com/api/documentation) | Des bandes dessinées                                                                                                  | Non             | Oui   | Inconnue |
| [Paquet de cartes](http://deckofcardsapi.com/)                               | Paquet de cartes                                                                                                      | Non             | Non   | Inconnue |
| [Destiny The Game](https://github.com/Bungie-net/api)                        | API de la plateforme Bungie                                                                                           | `apiKey`        | Oui   | Inconnue |
| [Dota 2](https://docs.opendota.com/)                                         | Fournit des informations sur les statistiques des joueurs, les statistiques des matchs et les classements pour Dota 2 | Non             | Oui   | Inconnue |
| [Donjons et Dragons](http://www.dnd5eapi.co/)                                | Référence pour les sorts, classes, monstres et plus de la 5e édition                                                  | Non             | Non   | Non      |
| [Eve en ligne](https://esi.evetech.net/ui)                                   | Documentation du développeur tiers                                                                                    | `OAuth`         | Oui   | Inconnue |
| [Final Fantasy XIV](https://xivapi.com/)                                     | API de données de jeu Final Fantasy XIV                                                                               | Non             | Oui   | Oui      |
| [Fortnite](https://fortnitetracker.com/site-api)                             | Statistiques Fortnite                                                                                                 | `apiKey`        | Oui   | Inconnue |
| [Bombe géante](https://www.giantbomb.com/api/documentation)                  | Jeux vidéos                                                                                                           | Non             | Oui   | Inconnue |
| [Guild Wars 2](https://wiki.guildwars2.com/wiki/API:Main)                    | Informations sur le jeu Guild Wars 2                                                                                  | `apiKey`        | Oui   | Inconnue |
| [Halo](https://developer.haloapi.com/)                                       | Informations sur Halo 5 et Halo Wars 2                                                                                | `apiKey`        | Oui   | Inconnue |
| [Foyer](http://hearthstoneapi.com/)                                          | Informations sur les cartes Hearthstone                                                                               | `X-Mashape-Key` | Oui   | Inconnue |
| [Hypixel](https://api.hypixel.net/)                                          | Statistiques du joueur Hypixel                                                                                        | `apiKey`        | Oui   | Inconnue |
| [IGDB.com](https://api.igdb.com/)                                            | Base de données de jeux vidéo                                                                                         | `apiKey`        | Oui   | Inconnue |
| [JokeAPI](https://sv443.net/jokeapi)                                         | Programmation, divers et blagues sombres                                                                              | Non             | Oui   | Oui      |
| [Blagues](https://github.com/15Dkatz/official_joke_api)                      | Programmation et blagues générales                                                                                    | Non             | Oui   | Inconnue |
| [Jservice](http://jservice.io)                                               | Base de données des questions Jeopardy                                                                                | Non             | Non   | Inconnue |
| [Magic The Gathering](http://magicthegathering.io/)                          | Informations sur le jeu Magic The Gathering                                                                           | Non             | Non   | Inconnue |
| [merveille](http://developer.marvel.com)                                     | Marvel Comics                                                                                                         | `apiKey`        | Non   | Inconnue |
| [mod.io](https://docs.mod.io)                                                | API Cross Platform Mod                                                                                                | `apiKey`        | Oui   | Inconnue |
| [Open Trivia](https://opentdb.com/api_config.php)                            | Questions triviales                                                                                                   | Non             | Oui   | Inconnue |
| [PandaScore](https://pandascore.co)                                          | Jeux et résultats e-sports                                                                                            | `apiKey`        | Oui   | Inconnue |
| [Champs de bataille de PlayerUnknown](https://pubgtracker.com/site-api)      | Statistiques PUBG                                                                                                     | `apiKey`        | Oui   | Inconnue |
| [Pokéapi](https://pokeapi.co)                                                | Informations sur les Pokémon                                                                                          | Non             | Oui   | Inconnue |
| [Pokémon TCG](https://pokemontcg.io)                                         | Informations sur le JCC Pokémon                                                                                       | Non             | Oui   | Inconnue |
| [Rick et Morty](https://rickandmortyapi.com)                                 | Toutes les informations Rick et Morty, y compris les images                                                           | Non             | Oui   | Oui      |
| [Riot Games](https://developer.riotgames.com/)                               | Informations sur le jeu League of Legends                                                                             | `apiKey`        | Oui   | Inconnue |
| [Scryfall](https://scryfall.com/docs/api)                                    | Magic: la base de données Gathering                                                                                   | Non             | Oui   | Oui      |
| [Vapeur](https://developer.valvesoftware.com/wiki/Steam_Web_API)             | Interaction avec le client Steam                                                                                      | `OAuth`         | Oui   | Inconnue |
| [Super-héros](https://superheroapi.com)                                      | Toutes les données SuperHeroes et Villains de tous les univers sous une seule API                                     | `apiKey`        | Oui   | Inconnue |
| [Tronald Dump](https://www.tronalddump.io/)                                  | Les choses les plus stupides que Donald Trump ait jamais dites                                                        | Non             | Oui   | Inconnue |
| [Wargaming.net](https://developers.wargaming.net/)                           | Informations et statistiques sur Wargaming.net                                                                        | `apiKey`        | Oui   | Non      |
| [xkcd](https://xkcd.com/json.html)                                           | Récupérer des bandes dessinées xkcd au format JSON                                                                    | Non             | Oui   | Non      |

**[⬆ Retour à l'index](#index)**

### Géocodage

| FEU                                                                                                                    | La description                                                                                                                   | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [adresse.data.gouv.fr](https://adresse.data.gouv.fr)                                                                   | Base de données d'adresses de la France, géocodage et revers                                                                     | Non      | Oui   | Inconnue |
| [Battuta](http://battuta.medunes.net)                                                                                  | API de localisation en cascade (pays / région / ville)                                                                           | `apiKey` | Non   | Inconnue |
| [Cartes Bing](https://www.microsoft.com/maps/)                                                                         | Créez / personnalisez des cartes numériques basées sur les données Bing Maps                                                     | `apiKey` | Oui   | Inconnue |
| [bng2latlong](https://www.getthedata.com/bng2latlong)                                                                  | Convertir l'OSGB36 britannique à l'est et au nord (British National Grid) en latitude et longitude WGS84                         | Non      | Oui   | Oui      |
| [CitySDK](http://www.citysdk.eu/citysdk-toolkit/)                                                                      | API ouvertes pour certaines villes européennes                                                                                   | Non      | Oui   | Inconnue |
| [Cartes Daum](http://apis.map.daum.net/)                                                                               | Daum Maps fournit plusieurs API pour les cartes coréennes                                                                        | `apiKey` | Non   | Inconnue |
| [FreeGeoIP](https://freegeoip.app/)                                                                                    | Informations geo ip gratuites, aucune inscription requise. 15k / heure limite de taux                                            | Non      | Oui   | Oui      |
| [GeoApi](https://api.gouv.fr/api/geoapi.html)                                                                          | Données géographiques françaises                                                                                                 | Non      | Oui   | Inconnue |
| [Geocod.io](https://www.geocod.io/)                                                                                    | Géocodage d'adresses / géocodage inversé en vrac                                                                                 | `apiKey` | Oui   | Inconnue |
| [Geocode.xyz](https://geocode.xyz/)                                                                                    | Fournit un géocodage avant / arrière mondial, un géocodage par lots et un géoparçage                                             | Non      | Oui   | Inconnue |
| [GeoDataSource](https://www.geodatasource.com/web-service)                                                             | Géocodage du nom de la ville en utilisant les coordonnées de latitude et de longitude                                            | `apiKey` | Oui   | Inconnue |
| [GeoJS](https://geojs.io/)                                                                                             | Géolocalisation IP avec intégration ChatOps                                                                                      | Non      | Oui   | Oui      |
| [GeoNames](http://www.geonames.org/export/web-services.html)                                                           | Noms de lieux et autres données géographiques                                                                                    | Non      | Non   | Inconnue |
| [geoPlugin](https://www.geoplugin.com)                                                                                 | Géolocalisation IP et conversion de devises                                                                                      | Non      | Oui   | Oui      |
| [Google Earth Engine](https://developers.google.com/earth-engine/)                                                     | Une plateforme cloud pour l'analyse des données environnementales à l'échelle planétaire                                         | `apiKey` | Oui   | Inconnue |
| [Google Maps](https://developers.google.com/maps/)                                                                     | Créez / personnalisez des cartes numériques basées sur les données de Google Maps                                                | `apiKey` | Oui   | Inconnue |
| [HelloSalut](https://www.fourtonfish.com/hellosalut/hello/)                                                            | Obtenez la traduction de bonjour suivant la langue de l'utilisateur                                                              | Non      | Oui   | Inconnue |
| [ICI Cartes](https://developer.here.com)                                                                               | Créez / personnalisez des cartes numériques basées sur les données HERE Maps                                                     | `apiKey` | Oui   | Inconnue |
| [Villes indiennes](https://indian-cities-api-nocbegfhqg.now.sh/)                                                       | Obtenez toutes les villes indiennes dans un format JSON propre                                                                   | Non      | Oui   | Oui      |
| [Pays IP 2](https://ip2country.info)                                                                                   | Mapper une IP à un pays                                                                                                          | Non      | Oui   | Inconnue |
| [Détails de l'adresse IP](https://ipinfo.io/)                                                                          | Trouver la géolocalisation avec une adresse IP                                                                                   | Non      | Oui   | Inconnue |
| [Emplacement IP](http://ip-api.com/)                                                                                   | Trouver un emplacement avec une adresse IP                                                                                       | Non      | Non   | Inconnue |
| [Emplacement IP](https://ipapi.co/)                                                                                    | Rechercher des informations sur l'emplacement de l'adresse IP                                                                    | Non      | Oui   | Inconnue |
| [IP Sidekick](https://ipsidekick.com)                                                                                  | API de géolocalisation qui renvoie des informations supplémentaires sur une adresse IP                                           | `apiKey` | Oui   | Inconnue |
| [IP Vigilante](https://www.ipvigilante.com/)                                                                           | API de géolocalisation IP gratuite                                                                                               | Non      | Oui   | Inconnue |
| [IP2Location](https://www.ip2location.com/web-service/ip2location)                                                     | Service Web de géolocalisation IP pour obtenir plus de 55 paramètres                                                             | `apiKey` | Oui   | Inconnue |
| [IP2Proxy](https://www.ip2location.com/web-service/ip2proxy)                                                           | Détecter le proxy et le VPN à l'aide de l'adresse IP                                                                             | `apiKey` | Oui   | Inconnue |
| [IPGeolocationAPI.com](https://ipgeolocationapi.com/)                                                                  | Localisez vos visiteurs par IP avec les détails du pays                                                                          | Non      | Oui   | Oui      |
| [IPInfoDB](https://ipinfodb.com/api)                                                                                   | Outils et API de géolocalisation gratuits pour la recherche de pays, de régions, de villes et de fuseaux horaires par adresse IP | `apiKey` | Oui   | Inconnue |
| [ipstack](https://ipstack.com/)                                                                                        | Localiser et identifier les visiteurs du site Web par adresse IP                                                                 | `apiKey` | Oui   | Inconnue |
| [Réseau Kwelo](https://www.kwelo.com/network/ip-address)                                                               | Localisez et obtenez des informations détaillées sur l'adresse IP                                                                | Non      | Oui   | Oui      |
| [LocationIQ](https://locationiq.org/docs/)                                                                             | Fournit un géocodage avant / arrière et un géocodage par lots                                                                    | `apiKey` | Oui   | Oui      |
| [Mapbox](https://www.mapbox.com/developers/)                                                                           | Créez / personnalisez de superbes cartes numériques                                                                              | `apiKey` | Oui   | Inconnue |
| [Mexique](https://github.com/IcaliaLabs/sepomex)                                                                       | API de codes postaux RESTful au Mexique                                                                                          | Non      | Oui   | Inconnue |
| [One Map, Singapour](https://docs.onemap.sg/)                                                                          | Services API REST de Singapore Land Authority pour les adresses de Singapour                                                     | `apiKey` | Oui   | Inconnue |
| [Sur l'eau](https://onwater.io/)                                                                                       | Déterminer si un lat / lon est sur l'eau ou sur terre                                                                            | Non      | Oui   | Inconnue |
| [OpenCage](https://opencagedata.com)                                                                                   | Géocodage avant et arrière à l'aide de données ouvertes                                                                          | `apiKey` | Oui   | Oui      |
| [OpenStreetMap](http://wiki.openstreetmap.org/wiki/API)                                                                | Navigation, géolocalisation et données géographiques                                                                             | `OAuth`  | Non   | Inconnue |
| [PostcodeData.nl](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) | Fournir des données de géolocalisation basées sur le code postal pour les adresses néerlandaises                                 | Non      | Non   | Inconnue |
| [Postcodes.io](https://postcodes.io)                                                                                   | Recherche de code postal et géolocalisation pour le Royaume-Uni                                                                  | Non      | Oui   | Oui      |
| [Pays REST](https://restcountries.eu)                                                                                  | Obtenez des informations sur les pays via une API RESTful                                                                        | Non      | Oui   | Inconnue |
| [Uebermaps](https://uebermaps.com/api/v2)                                                                              | Découvrez et partagez des cartes avec vos amis                                                                                   | `apiKey` | Oui   | Inconnue |
| [US ZipCode](https://smartystreets.com/docs/cloud/us-zipcode-api)                                                      | Valider et ajouter des données pour tout ZipCode américain                                                                       | `apiKey` | Oui   | Oui      |
| [Utah AGRC](https://api.mapserv.utah.gov)                                                                              | API Web Utah pour géocoder les adresses Utah                                                                                     | `apiKey` | Oui   | Inconnue |
| [ViaCep](https://viacep.com.br)                                                                                        | API de codes postaux RESTful au Brésil                                                                                           | Non      | Oui   | Inconnue |
| [ZipCodeAPI](https://www.zipcodeapi.com)                                                                               | API de distance, de rayon et de localisation du code postal américain                                                            | `apiKey` | Oui   | Inconnue |
| [Zippopotam](http://www.zippopotam.us)                                                                                 | Obtenez des informations sur un lieu tel que le pays, la ville, l'état, etc.                                                     | Non      | Non   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Gouvernement

| FEU                                                                                 | La description                                                                                                                                                        | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [BCLaws](http://www.bclaws.ca/civix/template/complete/api/index.html)               | Accès aux lois de la Colombie-Britannique                                                                                                                             | Non      | Non   | Inconnue |
| [BusinessUSA](https://business.usa.gov/developer)                                   | Informations faisant autorité sur les programmes, événements, services et plus aux États-Unis                                                                         | `apiKey` | Oui   | Inconnue |
| [Census.gov](https://www.census.gov/data/developers/data-sets.html)                 | Le US Census Bureau fournit divers API et ensembles de données sur la démographie et les entreprises                                                                  | Non      | Oui   | Inconnue |
| [Ville, Lyon Opendata](https://data.beta.grandlyon.com/fr/accueil)                  | Lyon (FR) City Open Data                                                                                                                                              | `apiKey` | Oui   | Inconnue |
| [Ville, Nantes Opendata](https://data.nantesmetropole.fr/pages/home/)               | Nantes (FR) City Open Data                                                                                                                                            | `apiKey` | Oui   | Inconnue |
| [Ville, Prague Opendata](http://opendata.praha.eu/en)                               | Données ouvertes de la ville de Prague (CZ)                                                                                                                           | Non      | Non   | Inconnue |
| [Code.gov](https://code.gov)                                                        | La plate-forme principale pour l'Open Source et le partage de code pour le gouvernement fédéral américain                                                             | `apiKey` | Oui   | Inconnue |
| [Colorado Data Engine](http://codataengine.org/)                                    | Données publiques du Colorado formatées et géolocalisées                                                                                                              | Non      | Oui   | Inconnue |
| [Marché de l'information du Colorado](https://data.colorado.gov/)                   | Données ouvertes du gouvernement de l'État du Colorado                                                                                                                | Non      | Oui   | Inconnue |
| [USA date](https://datausa.io/about/api/)                                           | US Public Data                                                                                                                                                        | Non      | Oui   | Inconnue |
| [Data.gov](https://api.data.gov/)                                                   | Données du gouvernement américain                                                                                                                                     | `apiKey` | Oui   | Inconnue |
| [Data.parliament.uk](http://www.data.parliament.uk/developers/)                     | Contient des ensembles de données en direct, y compris des informations sur les pétitions, les projets de loi, les votes des députés, la participation et plus encore | Non      | Non   | Inconnue |
| [District de Columbia Open Data](http://opendata.dc.gov/pages/using-apis)           | Contient des ensembles de données publiques du gouvernement de D.C., y compris la criminalité, le SIG, les données financières, etc.                                  | Non      | Oui   | Inconnue |
| [EPA](https://developer.epa.gov/category/apis/)                                     | Services Web et ensembles de données de la US Environmental Protection Agency                                                                                         | Non      | Oui   | Inconnue |
| [FEC](https://api.open.fec.gov/developers/)                                         | Information sur les dons de campagne aux élections fédérales                                                                                                          | `apiKey` | Oui   | Inconnue |
| [Registre fédéral](https://www.federalregister.gov/reader-aids/developer-resources) | Le Daily Journal du gouvernement des États-Unis                                                                                                                       | Non      | Oui   | Inconnue |
| [Agence des normes alimentaires](http://ratings.food.gov.uk/open-data/en-GB)        | API des données d'évaluation de l'hygiène alimentaire au Royaume-Uni                                                                                                  | Non      | Non   | Inconnue |
| [Gouvernement ouvert, Australie](https://www.data.gov.au/)                          | Données ouvertes du gouvernement australien                                                                                                                           | Non      | Oui   | Inconnue |
| [Gouvernement ouvert, Belgique](https://data.gov.be/)                               | Données ouvertes du gouvernement belge                                                                                                                                | Non      | Oui   | Inconnue |
| [Gouvernement ouvert, Canada](http://open.canada.ca/en)                             | Données ouvertes du gouvernement canadien                                                                                                                             | Non      | Non   | Inconnue |
| [Gouvernement ouvert, France](https://www.data.gouv.fr/)                            | Données ouvertes du gouvernement français                                                                                                                             | `apiKey` | Oui   | Inconnue |
| [Gouvernement ouvert, Inde](https://data.gov.in/)                                   | Données ouvertes du gouvernement indien                                                                                                                               | `apiKey` | Oui   | Inconnue |
| [Gouvernement ouvert, Italie](https://www.dati.gov.it/)                             | Données ouvertes du gouvernement italien                                                                                                                              | Non      | Oui   | Inconnue |
| [Gouvernement ouvert, Nouvelle-Zélande](https://www.data.govt.nz/)                  | Données ouvertes du gouvernement de la Nouvelle-Zélande                                                                                                               | Non      | Oui   | Inconnue |
| [Gouvernement ouvert, Roumanie](http://data.gov.ro/)                                | Données ouvertes du gouvernement roumain                                                                                                                              | Non      | Non   | Inconnue |
| [Gouvernement ouvert, Taiwan](https://data.gov.tw/)                                 | Données ouvertes du gouvernement de Taiwan                                                                                                                            | Non      | Oui   | Inconnue |
| [Gouvernement ouvert, États-Unis](https://www.data.gov/)                            | Données ouvertes du gouvernement des États-Unis                                                                                                                       | Non      | Oui   | Inconnue |
| [Regulations.gov](https://regulationsgov.github.io/developers/)                     | Documents réglementaires fédéraux pour améliorer la compréhension du processus d'élaboration des règles fédérales                                                     | `apiKey` | Oui   | Inconnue |
| [Représenter par Open North](https://represent.opennorth.ca/)                       | Trouver des représentants du gouvernement canadien                                                                                                                    | Non      | Oui   | Inconnue |
| [USAspending.gov](https://api.usaspending.gov/)                                     | Données sur les dépenses fédérales américaines                                                                                                                        | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Santé

| FEU                                                        | La description                                                                                                              | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [BetterDoctor](https://developer.betterdoctor.com/)        | Informations détaillées sur les médecins de votre région                                                                    | `apiKey` | Oui   | Inconnue |
| [Covid-19](https://covid19api.com/)                        | Propagation, infection et rétablissement de Covid 19                                                                        | Non      | Oui   | Oui      |
| [Diabète](http://predictbgl.com/api/)                      | Enregistrement et récupération des informations sur le diabète                                                              | Non      | Non   | Inconnue |
| [Flutrack](http://www.flutrack.org/)                       | Symptômes pseudo-grippaux avec géolocalisation                                                                              | Non      | Non   | Inconnue |
| [Healthcare.gov](https://www.healthcare.gov/developers/)   | Contenu éducatif sur le marché américain de l'assurance maladie                                                             | Non      | Oui   | Inconnue |
| [Lexigram](https://docs.lexigram.io/v1/welcome)            | La PNL qui extrait les mentions des concepts cliniques du texte, donne accès à l'ontologie clinique                         | `apiKey` | Oui   | Inconnue |
| [Maquillage](http://makeup-api.herokuapp.com/)             | Informations sur le maquillage                                                                                              | Non      | Non   | Inconnue |
| [Medicare](https://data.medicare.gov/developers)           | Accès aux données du CMS - medicare.gov                                                                                     | Non      | Oui   | Inconnue |
| [NPPES](https://npiregistry.cms.hhs.gov/registry/help-api) | National Plan & Provider Enumeration System, informations sur les prestataires de soins de santé enregistrés aux États-Unis | Non      | Oui   | Inconnue |
| [Nutritionix](https://developer.nutritionix.com/)          | La plus grande base de données nutritionnelle vérifiée au monde                                                             | `apiKey` | Oui   | Inconnue |
| [openFDA](https://open.fda.gov)                            | Données publiques de la FDA sur les médicaments, les appareils et les aliments                                              | Non      | Oui   | Inconnue |
| [Nutriments USDA](https://fdc.nal.usda.gov/)               | Base de données nationale sur les éléments nutritifs pour référence standard                                                | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Emplois

| FEU                                                                                               | La description                                                   | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------- | ----- | -------- |
| [Adzuna](https://developer.adzuna.com/overview)                                                   | Agrégateur de job board                                          | `apiKey` | Oui   | Inconnue |
| [Careerjet](https://www.careerjet.com/partners/api/)                                              | Moteur de recherche d'emploi                                     | `apiKey` | Non   | Inconnue |
| [Emplois Github](https://jobs.github.com/api)                                                     | Emplois pour les développeurs de logiciels                       | Non      | Oui   | Oui      |
| [Emplois GraphQL](https://api.graphql.jobs)                                                       | Emplois avec GraphQL                                             | Non      | Oui   | Oui      |
| [En effet](https://www.indeed.com/publisher)                                                      | Agrégateur de job board                                          | `apiKey` | Oui   | Inconnue |
| [Jobs2Careers](http://api.jobs2careers.com/api/spec.pdf)                                          | Agrégateur de travaux                                            | `apiKey` | Oui   | Inconnue |
| [jooble](https://us.jooble.org/api/about)                                                         | Moteur de recherche d'emploi                                     | `apiKey` | Oui   | Inconnue |
| [Juju](http://www.juju.com/publisher/spec/)                                                       | Moteur de recherche d'emploi                                     | `apiKey` | Non   | Inconnue |
| [Compétences ouvertes](https://github.com/workforce-data-initiative/skills-api/wiki/API-Overview) | Titres d'emploi, compétences et données sur les emplois connexes | Non      | Non   | Inconnue |
| [Roseau](https://www.reed.co.uk/developers)                                                       | Agrégateur de job board                                          | `apiKey` | Oui   | Inconnue |
| [La muse](https://www.themuse.com/developers/api/v2)                                              | Tableau d'offres d'emploi et profils d'entreprise                | `apiKey` | Oui   | Inconnue |
| [Upwork](https://developers.upwork.com/)                                                          | Site d'emploi indépendant et système de gestion                  | `OAuth`  | Oui   | Inconnue |
| [USAJOBS](https://developer.usajobs.gov/)                                                         | Tableau d'offres d'emploi du gouvernement américain              | `apiKey` | Oui   | Inconnue |
| [ZipRecruiter](https://www.ziprecruiter.com/publishers)                                           | Application de recherche d'emploi et site Web                    | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Apprentissage automatique

| FEU                                                                               | La description                                                    | Auth     | HTTPS | CORS     |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------- | ----- | -------- |
| [Clarifai](https://developer.clarifai.com/)                                       | Vision par ordinateur                                             | `OAuth`  | Oui   | Inconnue |
| [Cloudmersive](https://www.cloudmersive.com/image-recognition-and-processing-api) | Sous-titrage d'image, reconnaissance faciale, classification NSFW | `apiKey` | Oui   | Oui      |
| [Deepcode](https://www.deepcode.ai/docs/Overview%252FOverview)                    | AI pour la révision du code                                       | Non      | Oui   | Inconnue |
| [Dialogflow](https://dialogflow.com)                                              | Traitement du langage naturel                                     | `apiKey` | Oui   | Inconnue |
| [Keen IO](https://keen.io/)                                                       | Analyse des données                                               | `apiKey` | Oui   | Inconnue |
| [Sentim-API](https://sentim-api.herokuapp.com)                                    | Analyse de sentiment de texte                                     | Non      | Oui   | Oui      |
| [Porte de temps](https://timedoor.io)                                             | Une API d'analyse de séries chronologiques                        | `apiKey` | Oui   | Oui      |
| [Débrancher](https://unplu.gg/test_api.html)                                      | API de prévision pour les données de série temporelle             | `apiKey` | Oui   | Inconnue |
| [Wit.ai](https://wit.ai/)                                                         | Traitement du langage naturel                                     | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### La musique

| FEU                                                                                                                 | La description                                                                                                                 | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------- | ----- | -------- |
| [Maîtrise de l'IA](https://aimastering.com/api_docs/)                                                               | Masterisation musicale automatisée                                                                                             | `apiKey` | Oui   | Oui      |
| [Bandsintown](https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0)                                          | Événements musicaux                                                                                                            | Non      | Oui   | Inconnue |
| [Deezer](https://developers.deezer.com/api)                                                                         | La musique                                                                                                                     | `OAuth`  | Oui   | Inconnue |
| [Discogs](https://www.discogs.com/developers/)                                                                      | La musique                                                                                                                     | `OAuth`  | Oui   | Inconnue |
| [Génie](https://docs.genius.com/)                                                                                   | Crowdsourced paroles et connaissances musicales                                                                                | `OAuth`  | Oui   | Inconnue |
| [Générateur](https://binaryjazz.us/genrenator-api/)                                                                 | Générateur de genre musical                                                                                                    | Non      | Oui   | Inconnue |
| [Recherche iTunes](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) | Produits logiciels                                                                                                             | Non      | Oui   | Inconnue |
| [Jamendo](https://developer.jamendo.com/v3.0/docs)                                                                  | La musique                                                                                                                     | `OAuth`  | Oui   | Inconnue |
| [KKBOX](https://developer.kkbox.com)                                                                                | Obtenez des bibliothèques musicales, des listes de lecture, des graphiques et jouez à partir de la plateforme de KKBOX         | `OAuth`  | Oui   | Inconnue |
| [LastFm](https://www.last.fm/api)                                                                                   | La musique                                                                                                                     | `apiKey` | Oui   | Inconnue |
| [Lyrics.ovh](http://docs.lyricsovh.apiary.io/)                                                                      | API simple pour récupérer les paroles d'une chanson                                                                            | Non      | Oui   | Inconnue |
| [Mixcloud](https://www.mixcloud.com/developers/)                                                                    | La musique                                                                                                                     | `OAuth`  | Oui   | Oui      |
| [MusicBrainz](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2)                                    | La musique                                                                                                                     | Non      | Oui   | Inconnue |
| [Musixmatch](https://developer.musixmatch.com/)                                                                     | La musique                                                                                                                     | `apiKey` | Oui   | Inconnue |
| [Openwhyd](https://openwhyd.github.io/openwhyd/API)                                                                 | Téléchargez des listes de lecture organisées de pistes en streaming (YouTube, SoundCloud, etc ...)                             | `No`     | Oui   | Non      |
| [SearchLy](https://searchly.asuarez.dev/docs/v1)                                                                    | Recherche de similitudes basée sur les paroles des chansons                                                                    | Non      | Oui   | Inconnue |
| [Songkick](https://www.songkick.com/developer/)                                                                     | Événements musicaux                                                                                                            | `OAuth`  | Oui   | Inconnue |
| [Songsterr](https://www.songsterr.com/a/wa/api/)                                                                    | Fournit des tablatures et des accords de guitare, basse et batterie                                                            | Non      | Oui   | Inconnue |
| [SoundCloud](https://developers.soundcloud.com/)                                                                    | Autoriser les utilisateurs à télécharger et partager des sons                                                                  | `OAuth`  | Oui   | Inconnue |
| [Spotify](https://beta.developer.spotify.com/documentation/web-api/)                                                | Affichez le catalogue de musique Spotify, gérez les bibliothèques des utilisateurs, obtenez des recommandations et plus encore | `OAuth`  | Oui   | Inconnue |
| [TasteDive](https://tastedive.com/read/api)                                                                         | API d'artiste similaire (fonctionne également pour les films et les émissions de télévision)                                   | `apiKey` | Oui   | Inconnue |
| [TheAudioDB](https://www.theaudiodb.com/api_guide.php)                                                              | La musique                                                                                                                     | `apiKey` | Oui   | Inconnue |
| [Luciole](https://api.vagalume.com.br/docs/)                                                                        | Crowdsourced paroles et connaissances musicales                                                                                | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Nouvelles

| FEU                                                                 | La description                                                                                   | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------- | ----- | -------- |
| [Presse associée](https://developer.ap.org/)                        | Rechercher des actualités et des métadonnées sur Associated Press                                | `apiKey` | Oui   | Inconnue |
| [Chronicling America](http://chroniclingamerica.loc.gov/about/api/) | Donne accès à des millions de pages de journaux historiques américains de la Library of Congress | Non      | Non   | Inconnue |
| [Les courants](https://currentsapi.services/)                       | Dernières nouvelles publiées dans diverses sources d'actualités, blogs et forums                 | `apiKey` | Oui   | Oui      |
| [Bac d'alimentation](https://github.com/feedbin/feedbin-api)        | Lecteur RSS                                                                                      | `OAuth`  | Oui   | Inconnue |
| [New York Times](https://developer.nytimes.com/)                    | Fournit des nouvelles                                                                            | `apiKey` | Oui   | Inconnue |
| [Nouvelles](https://newsapi.org/)                                   | Titres actuellement publiés sur une gamme de sources d'informations et de blogs                  | `apiKey` | Oui   | Inconnue |
| [NPR One](http://dev.npr.org/api/)                                  | Expérience d'écoute de nouvelles personnalisée de NPR                                            | `OAuth`  | Oui   | Inconnue |
| [Le gardien](http://open-platform.theguardian.com/)                 | Accédez à tout le contenu créé par le Guardian, classé par balises et section                    | `apiKey` | Oui   | Inconnue |
| [The Old Reader](https://github.com/theoldreader/api)               | Lecteur RSS                                                                                      | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Données ouvertes

| FEU                                                                            | La description                                                                                                | Auth     | HTTPS | CORS     |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [18F](http://18f.github.io/API-All-the-X/)                                     | Développement non officiel de l'API du gouvernement fédéral américain                                         | Non      | Non   | Inconnue |
| [Archive.org](https://archive.readme.io/docs)                                  | Les archives Internet                                                                                         | Non      | Oui   | Inconnue |
| [ARSAT](https://datos.arsat.com.ar/developers/)                                | Données publiques ARSAT                                                                                       | `apiKey` | Oui   | Inconnue |
| [Callook.info](https://callook.info)                                           | Indicatifs d'appel radioamateur des États-Unis                                                                | Non      | Oui   | Inconnue |
| [CARTO](https://carto.com/)                                                    | Prévision des informations de localisation                                                                    | `apiKey` | Oui   | Inconnue |
| [CivicFeed](https://developers.civicfeed.com/)                                 | Articles de presse et jeux de données publics                                                                 | `apiKey` | Oui   | Inconnue |
| [Enigma Public](http://docs.enigma.com/public/public_v20_api_about)            | La plus large collection de données publiques                                                                 | `apiKey` | Oui   | Oui      |
| [fonoApi](https://fonoapi.freshpixl.com/)                                      | Description de l'appareil mobile                                                                              | Non      | Oui   | Inconnue |
| [Recherche d'adresse en français](https://geo.api.gouv.fr/adresse)             | Recherche d'adresse via le gouvernement français                                                              | Non      | Oui   | Inconnue |
| [LinkPreview](https://www.linkpreview.net)                                     | Obtenez un résumé au format JSON avec le titre, la description et l'image d'aperçu pour toute URL demandée    | `apiKey` | Oui   | Oui      |
| [Souches de marijuana](http://strains.evanbusse.com/)                          | Variétés, races, saveurs et effets de la marijuana                                                            | `apiKey` | Non   | Inconnue |
| [Microlink.io](https://microlink.io)                                           | Extraire des données structurées de n'importe quel site Web                                                   | Non      | Oui   | Oui      |
| [OpenCorporates](http://api.opencorporates.com/documentation/API-Reference)    | Données sur les personnes morales et les administrateurs dans de nombreux pays                                | `apiKey` | Oui   | Inconnue |
| [quandl](https://www.quandl.com/)                                              | Données boursières                                                                                            | Non      | Oui   | Inconnue |
| [Base de données d'informations sur les loisirs](https://ridb.recreation.gov/) | Zones de loisirs, terres fédérales, sites historiques, musées et autres attractions / ressources (États-Unis) | `apiKey` | Oui   | Inconnue |
| [Scoop.it](http://www.scoop.it/dev)                                            | Service de conservation de contenu                                                                            | `apiKey` | Non   | Inconnue |
| [Téléportation](https://developers.teleport.org/)                              | Données sur la qualité de vie                                                                                 | Non      | Oui   | Inconnue |
| [Liste des universités](https://github.com/Hipo/university-domains-list)       | Noms, pays et domaines universitaires                                                                         | Non      | Oui   | Inconnue |
| [Université d'Oslo](https://data.uio.no/)                                      | Cours, vidéos-conférences, informations détaillées sur les cours, etc. pour l'Université d'Oslo (Norvège)     | Non      | Oui   | Inconnue |
| [Base de données UPC](https://upcdatabase.org/api)                             | Plus de 1,5 million de numéros de codes-barres du monde entier                                                | `apiKey` | Oui   | Inconnue |
| [Wikidata](https://www.wikidata.org/w/api.php?action=help)                     | Base de connaissances éditée en collaboration gérée par la Wikimedia Foundation                               | `OAuth`  | Oui   | Inconnue |
| [Wikipédia](https://www.mediawiki.org/wiki/API:Main_page)                      | Encyclopédie Mediawiki                                                                                        | Non      | Oui   | Inconnue |
| [Japper](https://www.yelp.com/developers/documentation/v3)                     | Trouver une entreprise locale                                                                                 | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Projets Open Source

| FEU                                                            | La description                         | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------- | -------------------------------------- | -------- | ----- | -------- |
| [Countly](https://api.count.ly/reference)                      | De nombreuses analyses Web             | Non      | Non   | Inconnue |
| [Drupal.org](https://www.drupal.org/drupalorg/docs/api)        | Drupal.org                             | Non      | Oui   | Inconnue |
| [Générateur d'insultes maléfiques](https://evilinsult.com/api) | Insultes maléfiques                    | Non      | Oui   | Oui      |
| [Libraries.io](https://libraries.io/api)                       | Bibliothèques de logiciels open source | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Brevet

| FEU                                                                           | La description                                   | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------------------- | ------------------------------------------------ | -------- | ----- | -------- |
| [OEB](https://developers.epo.org/)                                            | API du système européen de recherche de brevets  | `OAuth`  | Oui   | Inconnue |
| [TYPE](https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00) | API du système de recherche de brevets de Taiwan | `apiKey` | Oui   | Inconnue |
| [USPTO](https://www.uspto.gov/learning-and-resources/open-data-and-mobility)  | Services d'API de brevets aux États-Unis         | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Personnalité

| FEU                                                                           | La description                                                                       | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -------- | ----- | -------- |
| [Fiche de conseils](http://api.adviceslip.com/)                               | Générez des feuillets de conseils aléatoires                                         | Non      | Oui   | Inconnue |
| [chucknorris.io](https://api.chucknorris.io)                                  | API JSON pour les blagues Chuck Norris organisées à la main                          | Non      | Oui   | Inconnue |
| [FavQs.com](https://favqs.com/api)                                            | FavQs vous permet de collecter, découvrir et partager vos citations préférées        | `apiKey` | Oui   | Inconnue |
| [FOAAS](http://www.foaas.com/)                                                | Baiser comme un service                                                              | Non      | Non   | Inconnue |
| [Forismatique](http://forismatic.com/en/api/)                                 | Citations inspirantes                                                                | Non      | Non   | Inconnue |
| [icanhazdadjoke](https://icanhazdadjoke.com/api)                              | La plus grande sélection de blagues de papa sur Internet                             | Non      | Oui   | Inconnue |
| [kanye.rest](https://kanye.rest)                                              | API REST pour les cotations aléatoires de Kanye West                                 | Non      | Oui   | Oui      |
| [Moyen](https://github.com/Medium/medium-api-docs)                            | Communauté de lecteurs et d'écrivains offrant des perspectives uniques sur les idées | `OAuth`  | Oui   | Inconnue |
| [NaMoMemes](https://github.com/theIYD/NaMoMemes)                              | Mèmes sur Narendra Modi                                                              | Non      | Oui   | Inconnue |
| [Devis de programmation](https://github.com/skolakoda/programming-quotes-api) | API de programmation de devis pour les projets open source                           | Non      | Oui   | Inconnue |
| [Jardin de citation](https://pprathameshmore.github.io/QuoteGarden/)          | API REST pour plus de 5000 citations célèbres                                        | Non      | Oui   | Inconnue |
| [Citations sur le design](https://quotesondesign.com/api/)                    | Citations inspirantes                                                                | Non      | Oui   | Inconnue |
| [Traitify](https://app.traitify.com/developer)                                | Évaluer, collecter et analyser la personnalité                                       | Non      | Oui   | Inconnue |
| [tronalddump.io](https://www.tronalddump.io)                                  | API et archives Web pour les propos de Donald Trump                                  | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### La photographie

| FEU                                                   | La description                                                          | Auth     | HTTPS | CORS     |
| ----------------------------------------------------- | ----------------------------------------------------------------------- | -------- | ----- | -------- |
| [Flickr](https://www.flickr.com/services/api/)        | Services Flickr                                                         | `OAuth`  | Oui   | Inconnue |
| [Getty Images](http://developers.gettyimages.com/en/) | Créez des applications à l'aide des images les plus puissantes au monde | `OAuth`  | Oui   | Inconnue |
| [Gfycat](https://developers.gfycat.com/api/)          | Gifs Jiffier                                                            | `OAuth`  | Oui   | Inconnue |
| [Giphy](https://developers.giphy.com/docs/)           | Obtenez tous vos gifs                                                   | `apiKey` | Oui   | Inconnue |
| [Gyazo](https://gyazo.com/api/docs)                   | Importer des images                                                     | `apiKey` | Oui   | Inconnue |
| [Imgur](https://apidocs.imgur.com/)                   | Images                                                                  | `OAuth`  | Oui   | Inconnue |
| [photos de Lorem](https://picsum.photos/)             | Images de Unsplash                                                      | Non      | Oui   | Inconnue |
| [Pexels](https://www.pexels.com/api/)                 | Photos et vidéos gratuites                                              | `apiKey` | Oui   | Oui      |
| [Pixabay](https://pixabay.com/sk/service/about/api/)  | La photographie                                                         | `apiKey` | Oui   | Inconnue |
| [PlaceKitten](https://placekitten.com/)               | Images d'espace réservé de chaton redimensionnables                     | Non      | Oui   | Inconnue |
| [ScreenShotLayer](https://screenshotlayer.com)        | Image URL 2                                                             | Non      | Oui   | Inconnue |
| [Unsplash](https://unsplash.com/developers)           | La photographie                                                         | `OAuth`  | Oui   | Inconnue |
| [le Wallhav](https://wallhaven.cc/help/api)           | Papiers peints                                                          | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Science mathématique

| FEU                                                                                      | La description                                                                                              | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [arcsecond.io](https://api.arcsecond.io/)                                                | Plusieurs sources de données astronomiques                                                                  | Non      | Oui   | Inconnue |
| [COEUR](https://core.ac.uk/services#api)                                                 | Accédez aux documents de recherche sur le libre accès dans le monde                                         | `apiKey` | Oui   | Inconnue |
| [GBIF](http://api.gbif.org/v1/)                                                          | Centre mondial d'information sur la biodiversité                                                            | Non      | Oui   | Oui      |
| [iDigBio](https://github.com/idigbio/idigbio-search-api/wiki)                            | Accédez à des millions de spécimens de musée d'organisations du monde entier                                | Non      | Oui   | Inconnue |
| [inspirehep.net](https://inspirehep.net/info/hep/api?ln=en)                              | Informations sur la physique des hautes énergies. système                                                   | Non      | Oui   | Inconnue |
| [C'EST](https://www.itis.gov/ws_description.html)                                        | Système d'information taxonomique intégré                                                                   | Non      | Oui   | Inconnue |
| [Lancer la bibliothèque](https://launchlibrary.net/docs/1.3/api.html)                    | Prochains lancements spatiaux                                                                               | Non      | Oui   | Inconnue |
| [Minor Planet Center](http://www.asterank.com/mpc)                                       | Informations Asterank.com                                                                                   | Non      | Non   | Inconnue |
| [NASA](https://api.nasa.gov)                                                             | Données de la NASA, y compris l'imagerie                                                                    | Non      | Oui   | Inconnue |
| [NASA APOD (API non officielle)](https://apodapi.herokuapp.com/)                         | API pour obtenir des images APOD (Image d'astronomie du jour) ainsi que des métadonnées                     | Non      | Oui   | Oui      |
| [Newton](https://newton.now.sh/)                                                         | Calculatrice mathématique symbolique et arithmétique                                                        | Non      | Oui   | Inconnue |
| [Nombres](http://numbersapi.com)                                                         | Faits sur les chiffres                                                                                      | Non      | Non   | Inconnue |
| [Ouvrir Notifier](http://open-notify.org/Open-Notify-API/)                               | Astronautes de l'ISS, emplacement actuel, etc.                                                              | Non      | Non   | Inconnue |
| [Cadre scientifique ouvert](https://developer.osf.io)                                    | Référentiel et archives pour les plans d'étude, le matériel de recherche, les données, les manuscrits, etc. | Non      | Oui   | Inconnue |
| [PARTAGER](https://share.osf.io/api/v2/)                                                 | Un ensemble de données gratuit et ouvert sur la recherche et les activités savantes                         | Non      | Oui   | Inconnue |
| [SpaceX](https://github.com/r-spacex/SpaceX-API)                                         | Entreprise, véhicule, tableau de bord et données de lancement                                               | Non      | Oui   | Inconnue |
| [Lever et coucher de soleil](https://sunrise-sunset.org/api)                             | Heures de coucher et de lever du soleil pour une latitude et une longitude données                          | Non      | Oui   | Inconnue |
| [Trefle](https://trefle.io/)                                                             | Données botaniques pour les espèces végétales                                                               | `apiKey` | Oui   | Inconnue |
| [Programme des risques sismiques de l'USGS](https://earthquake.usgs.gov/fdsnws/event/1/) | Données sismiques en temps réel                                                                             | Non      | Oui   | Inconnue |
| [USGS Water Services](https://waterservices.usgs.gov/)                                   | Informations sur la qualité et le niveau de l'eau des rivières et des lacs                                  | Non      | Oui   | Inconnue |
| [Banque mondiale](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589)        | Données mondiales                                                                                           | Non      | Non   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Sécurité

| FEU                                                                                                        | La description                                                                                              | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Censys.io](https://censys.io/api)                                                                         | Moteur de recherche d'hôte et d'appareils connectés à Internet                                              | `apiKey` | Oui   | Non      |
| [CRXcavator](https://crxcavator.io/apidocs)                                                                | Score de risque de l'extension Chrome                                                                       | `apiKey` | Oui   | Inconnue |
| [FilterLists](https://filterlists.com)                                                                     | Listes de filtres pour adblockers et pare-feu                                                               | Non      | Oui   | Inconnue |
| [FraudLabs Pro](https://www.fraudlabspro.com/developer/api/screen-order)                                   | Filtrer les informations de commande à l'aide de l'IA pour détecter les fraudes                             | `apiKey` | Oui   | Inconnue |
| [HaveIBeenPwned](https://haveibeenpwned.com/API/v3)                                                        | Mots de passe qui ont déjà été exposés lors de violations de données                                        | `apiKey` | Oui   | Inconnue |
| [Base de données nationale sur la vulnérabilité](https://nvd.nist.gov/vuln/Data-Feeds/JSON-feed-changelog) | Base de données nationale américaine sur la vulnérabilité                                                   | Non      | Oui   | Inconnue |
| [SecurityTrails](https://securitytrails.com/corp/apidocs)                                                  | Informations liées au domaine et à l'IP, telles que les enregistrements WHOIS et DNS actuels et historiques | `apiKey` | Oui   | Inconnue |
| [Shodan](https://developer.shodan.io/)                                                                     | Moteur de recherche pour les appareils connectés à Internet                                                 | `apiKey` | Oui   | Inconnue |
| [Police britannique](https://data.police.uk/docs/)                                                         | Données de la police britannique                                                                            | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Achats

| FEU                                                                         | La description                                                               | Auth     | HTTPS | CORS     |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Meilleur achat](https://bestbuyapis.github.io/api-documentation/#overview) | Produits, options d'achat, catégories, recommandations, magasins et commerce | `apiKey` | Oui   | Inconnue |
| [Bratabase](https://developers.bratabase.com/)                              | Base de données de différents types de tailles de soutien-gorge              | `OAuth`  | Oui   | Inconnue |
| [eBay](https://go.developer.ebay.com/)                                      | Vendre et acheter sur eBay                                                   | `OAuth`  | Oui   | Inconnue |
| [Wal-Mart](https://developer.walmartlabs.com/docs)                          | Prix et disponibilité des articles                                           | `apiKey` | Oui   | Inconnue |
| [Wegmans](https://dev.wegmans.io)                                           | Marchés alimentaires de Wegmans                                              | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Social

| FEU                                                                    | La description                                                                                                                                   | Auth     | HTTPS | CORS     |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | ----- | -------- |
| [Tampon](https://buffer.com/developers/api)                            | Accès aux mises à jour en attente et envoyées dans Buffer                                                                                        | `OAuth`  | Oui   | Inconnue |
| [Cisco Spark](https://developer.ciscospark.com)                        | Logiciel de collaboration d'équipe                                                                                                               | `OAuth`  | Oui   | Inconnue |
| [Discorde](https://discordapp.com/developers/docs/intro)               | Créez des robots pour Discord, intégrez Discord sur une plateforme externe                                                                       | `OAuth`  | Oui   | Inconnue |
| [Disqus](https://disqus.com/api/docs/auth/)                            | Communiquez avec les données Disqus                                                                                                              | `OAuth`  | Oui   | Inconnue |
| [Facebook](https://developers.facebook.com/)                           | Connexion Facebook, Partager sur FB, Social Plugins, Analytics et plus                                                                           | `OAuth`  | Oui   | Inconnue |
| [Foursquare](https://developer.foursquare.com/)                        | Interagissez avec les utilisateurs et les lieux de Foursquare (enregistrements basés sur la géolocalisation, photos, conseils, événements, etc.) | `OAuth`  | Oui   | Inconnue |
| [Fuck Off en tant que service](https://www.foaas.com)                  | Demande à quelqu'un de baiser                                                                                                                    | Non      | Oui   | Inconnue |
| [Contact complet](https://www.fullcontact.com/developer/docs/)         | Obtenez les profils des médias sociaux et les coordonnées                                                                                        | `OAuth`  | Oui   | Inconnue |
| [HackerNews](https://github.com/HackerNews/API)                        | Actualités sociales pour CS et entrepreneuriat                                                                                                   | Non      | Oui   | Inconnue |
| [Instagram](https://www.instagram.com/developer/)                      | Connexion Instagram, Partager sur Instagram, Plugins sociaux et plus                                                                             | `OAuth`  | Oui   | Inconnue |
| [LinkedIn](https://developer.linkedin.com/docs/rest-api)               | La base de toutes les intégrations numériques avec LinkedIn                                                                                      | `OAuth`  | Oui   | Inconnue |
| [Meetup.com](https://www.meetup.com/meetup_api/)                       | Données sur les Meetups sur Meetup.com                                                                                                           | `apiKey` | Oui   | Inconnue |
| [Mixer](https://dev.mixer.com/)                                        | API de streaming de jeu                                                                                                                          | `OAuth`  | Oui   | Inconnue |
| [MySocialApp](https://mysocialapp.io)                                  | Fonctionnalités de réseautage social, API, SDK intégrés à n'importe quelle application                                                           | `apiKey` | Oui   | Inconnue |
| [Open Collective](https://docs.opencollective.com/help/developers/api) | Obtenez des données Open Collective                                                                                                              | Non      | Oui   | Inconnue |
| [Pinterest](https://developers.pinterest.com/)                         | Le catalogue d'idées du monde                                                                                                                    | `OAuth`  | Oui   | Inconnue |
| [PWR Telegram bot](https://pwrtelegram.xyz)                            | Version boostée de l'API Telegram bot                                                                                                            | `apiKey` | Oui   | Inconnue |
| [Reddit](https://www.reddit.com/dev/api)                               | Page d'accueil d'Internet                                                                                                                        | `OAuth`  | Oui   | Inconnue |
| [Mou](https://api.slack.com/)                                          | Messagerie instantanée d'équipe                                                                                                                  | `OAuth`  | Oui   | Inconnue |
| [Telegram Bot](https://core.telegram.org/bots/api)                     | Version HTTP simplifiée de l'API MTProto pour les bots                                                                                           | `apiKey` | Oui   | Inconnue |
| [Telegram MTProto](https://core.telegram.org/api#getting-started)      | Lire et écrire des données de télégramme                                                                                                         | `OAuth`  | Oui   | Inconnue |
| [Trash Nothing](https://trashnothing.com/developer)                    | Une communauté de freecycling avec des milliers d'articles gratuits publiés chaque jour                                                          | `OAuth`  | Oui   | Oui      |
| [Tumblr](https://www.tumblr.com/docs/en/api/v2)                        | Lire et écrire des données Tumblr                                                                                                                | `OAuth`  | Oui   | Inconnue |
| [Tic](https://dev.twitch.tv/docs)                                      | API de streaming de jeu                                                                                                                          | `OAuth`  | Oui   | Inconnue |
| [Twitter](https://developer.twitter.com/en/docs)                       | Lire et écrire des données Twitter                                                                                                               | `OAuth`  | Oui   | Non      |
| [vk](https://vk.com/dev/sites)                                         | Lire et écrire des données vk                                                                                                                    | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Sports et fitness

| FEU                                                                          | La description                                                                                                             | Auth            | HTTPS | CORS     |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------- | ----- | -------- |
| [balldontlie](https://balldontlie.io)                                        | Ballldontlie donne accès aux données statistiques de la NBA                                                                | Non             | Oui   | Oui      |
| [BikeWise](https://www.bikewise.org/documentation/api_v2)                    | Bikewise est un endroit pour en savoir plus sur les accidents de vélo, les dangers et les vols et les signaler             | Non             | Oui   | Inconnue |
| [Ligue canadienne de football (LCF)](http://api.cfl.ca/)                     | API JSON officielle fournissant des statistiques en temps réel sur les ligues, les équipes et les joueurs sur la LCF       | `apiKey`        | Oui   | Non      |
| [Vélos de ville](http://api.citybik.es/v2/)                                  | Vélos de ville dans le monde                                                                                               | Non             | Non   | Inconnue |
| [Ergast F1](http://ergast.com/mrd/)                                          | Données F1 du début des championnats du monde en 1950                                                                      | Non             | Oui   | Inconnue |
| [Fitbit](https://dev.fitbit.com/)                                            | Informations sur Fitbit                                                                                                    | `OAuth`         | Oui   | Inconnue |
| [Football (Soccer) Vidéos](https://www.scorebat.com/video-api/)              | Intégrer des codes pour les buts et les temps forts de la Premier League, de la Bundesliga, de la Serie A et bien d'autres | Non             | Oui   | Oui      |
| [Prédiction de football](https://boggio-analytics.com/fp-api/)               | Prédictions pour les prochains matchs de football, les cotes, les résultats et les statistiques                            | `X-Mashape-Key` | Oui   | Inconnue |
| [Football-Data.org](http://api.football-data.org/index)                      | Données de football                                                                                                        | Non             | Non   | Inconnue |
| [JCDecaux Bike](https://developer.jcdecaux.com/)                             | Les vélos en libre-service de JCDecaux                                                                                     | `apiKey`        | Oui   | Inconnue |
| [Statistiques NBA](https://any-api.com/nba_com/nba_com/docs/API_Description) | Statistiques NBA actuelles et historiques                                                                                  | Non             | Oui   | Inconnue |
| [Arrestations de la NFL](http://nflarrest.com/api/)                          | NFL Arrest Data                                                                                                            | Non             | Non   | Inconnue |
| [Records et statistiques de la LNH](https://gitlab.com/dword4/nhlapi)        | Données et statistiques historiques de la LNH                                                                              | Non             | Oui   | Inconnue |
| [Régime](https://strava.github.io/api/)                                      | Connectez-vous avec les athlètes, les activités et plus encore                                                             | `OAuth`         | Oui   | Inconnue |
| [SuredBits](https://suredbits.com/api/)                                      | Interroger les données sportives, y compris les équipes, les joueurs, les jeux, les scores et les statistiques             | Non             | Non   | Non      |
| [TheSportsDB](https://www.thesportsdb.com/api.php)                           | Données et illustrations sportives issues de la foule                                                                      | `apiKey`        | Oui   | Oui      |
| [Wger](https://wger.de/en/software/api)                                      | Données du gestionnaire d'entraînement sous forme d'exercices, de muscles ou d'équipement                                  | `apiKey`        | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Données de test

| FEU                                                               | La description                                                                               | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Adorables avatars](http://avatars.adorable.io)                   | Générez des avatars de dessins animés aléatoires                                             | Non      | Oui   | Inconnue |
| [très bacon](https://baconipsum.com/json-api/)                    | Un générateur de lorem ipsum plus charnu                                                     | Non      | Oui   | Inconnue |
| [Avatars de dés](https://avatars.dicebear.com/)                   | Générez des avatars pixel-art aléatoires                                                     | Non      | Oui   | Non      |
| [FakeJSON](https://fakejson.com)                                  | Service de génération de tests et de fausses données                                         | `apiKey` | Oui   | Oui      |
| [Identicon](https://www.kwelo.com/media/identicon/)               | Génère une image d'avatar abstraite                                                          | Non      | Oui   | Oui      |
| [JSONPlaceholder](http://jsonplaceholder.typicode.com/)           | Fake data for testing and prototyping                                                        | Non      | Non   | Inconnue |
| [Loripsum](http://loripsum.net/)                                  | Le générateur "lorem ipsum" qui ne craint pas                                                | Non      | Non   | Inconnue |
| [PIPL](https://pipl.ir/)                                          | API gratuite et publique qui génère des données de personnes aléatoires et fausses dans JSON | Non      | Oui   | Non      |
| [RandomUser](https://randomuser.me)                               | Génère des données utilisateur aléatoires                                                    | Non      | Oui   | Inconnue |
| [RoboHash](https://robohash.org/)                                 | Générez des avatars de robots / extraterrestres aléatoires                                   | Non      | Oui   | Inconnue |
| [Cette personne n'existe pas](https://thispersondoesnotexist.com) | Génère des visages réels de personnes qui n'existent pas                                     | Non      | Oui   | Inconnue |
| [Noms d'interface utilisateur](https://github.com/thm/uinames)    | Générer des faux noms aléatoires                                                             | Non      | Oui   | Inconnue |
| [Oui Non](https://yesno.wtf/api)                                  | Générer au hasard oui ou non                                                                 | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Analyse de texte

| FEU                                                                                                                                    | La description                                                                                                    | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Analyse de texte Aylien](http://docs.aylien.com/)                                                                                     | Une collection de récupération d'informations et d'API en langage naturel                                         | `apiKey` | Oui   | Inconnue |
| [Traitement du langage naturel Cloudmersive](https://www.cloudmersive.com/nlp-api)                                                     | Traitement du langage naturel et analyse de texte                                                                 | `apiKey` | Oui   | Oui      |
| [Détecter la langue](https://detectlanguage.com/)                                                                                      | Détecte la langue du texte                                                                                        | `apiKey` | Oui   | Inconnue |
| [Google Cloud Natural](https://cloud.google.com/natural-language/docs/)                                                                | Technologie de compréhension du langage naturel, y compris l'analyse des sentiments, des entités et de la syntaxe | `apiKey` | Oui   | Inconnue |
| [Semantira](https://semantria.readme.io/docs)                                                                                          | Analyse de texte avec analyse des sentiments, catégorisation et extraction d'entités nommées                      | `OAuth`  | Oui   | Inconnue |
| [Compréhension du langage naturel Watson](https://cloud.ibm.com/apidocs/natural-language-understanding/natural-language-understanding) | Traitement du langage naturel pour une analyse de texte avancée                                                   | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### suivi

| FEU                                              | La description                                                                                               | Auth     | HTTPS | CORS     |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | -------- | ----- | -------- |
| [Facteur](http://postmon.com.br)                 | Une API pour interroger les codes postaux brésiliens et les commandes facilement, rapidement et gratuitement | Non      | Non   | Inconnue |
| [Suède](https://developer.postnord.com/docs2)    | Fournit des informations sur les colis en transport                                                          | `apiKey` | Non   | Inconnue |
| [UPS](https://www.ups.com/upsdeveloperkit)       | Informations d'expédition et d'adresse                                                                       | `apiKey` | Oui   | Inconnue |
| [WhatPulse](https://whatpulse.org/pages/webapi/) | Petite application qui mesure l'utilisation de votre clavier / souris                                        | Non      | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Transport

| FEU                                                                                                                                 | La description                                                                                                            | Auth     | HTTPS | CORS     |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Échange ADS-B](https://www.adsbexchange.com/data/)                                                                                 | Accédez aux données historiques et en temps réel de tous les avions embarqués                                             | Non      | Oui   | Inconnue |
| [Hub AIS](http://www.aishub.net/api)                                                                                                | Données en temps réel de tout navire maritime et intérieur équipé d'un système de suivi AIS                               | `apiKey` | Non   | Inconnue |
| [AIS Web](http://www.aisweb.aer.mil.br/api/doc/index.cfm)                                                                           | Informations aéronautiques dans les médias numériques produites par le Département du contrôle de l'espace aérien (DECEA) | `apiKey` | Non   | Inconnue |
| [Amadeus Travel Innovation Sandbox](https://sandbox.amadeus.com/)                                                                   | Recherche de voyage - Utilisation limitée                                                                                 | `apiKey` | Oui   | Inconnue |
| [Transit rapide dans la région de la baie](http://api.bart.gov)                                                                     | Stations et arrivées prévues pour BART                                                                                    | `apiKey` | Non   | Inconnue |
| [BlaBlaCar](https://dev.blablacar.com)                                                                                              | Rechercher des voyages en covoiturage                                                                                     | `apiKey` | Oui   | Inconnue |
| [Transit communautaire](https://github.com/transitland/transitland-datastore/blob/master/README.md#api-endpoints)                   | API Transitland                                                                                                           | Non      | Oui   | Inconnue |
| [Goibibo](https://developer.goibibo.com/docs)                                                                                       | API pour la recherche de voyages                                                                                          | `apiKey` | Oui   | Inconnue |
| [GraphHopper](https://graphhopper.com/api/1/docs/)                                                                                  | Acheminement A vers B avec des instructions détaillées                                                                    | `apiKey` | Oui   | Inconnue |
| [API islandaises](http://docs.apis.is/)                                                                                             | API ouvertes qui fournissent des services en Islande ou concernant l'Islande                                              | Non      | Oui   | Inconnue |
| [les chemins de fer indiens](http://api.erail.in/)                                                                                  | Informations sur les chemins de fer indiens                                                                               | `apiKey` | Non   | Inconnue |
| [Izu](http://api-docs.izi.travel/)                                                                                                  | Audioguide pour les voyageurs                                                                                             | `apiKey` | Oui   | Inconnue |
| [Métro de Lisbonne](http://app.metrolisboa.pt/status/getLinhas.php)                                                                 | Retards dans les lignes de métro                                                                                          | Non      | Non   | Non      |
| [Naviti](https://api.navitia.io/)                                                                                                   | L'API ouverte pour créer des trucs sympas avec des données de transport                                                   | `apiKey` | Oui   | Inconnue |
| [REFUGE Toilettes](https://www.refugerestrooms.org/api/docs/#!/restrooms)                                                           | Fournit un accès sécurisé aux toilettes pour les personnes transgenres, intersexuées et non conformes au genre            | Non      | Oui   | Inconnue |
| [Aéroport de Schiphol](https://developer.schiphol.nl/)                                                                              | Schiphol                                                                                                                  | `apiKey` | Oui   | Inconnue |
| [TransitLand](https://transit.land/documentation/datastore/api-endpoints.html)                                                      | Agrégation de transit                                                                                                     | Non      | Oui   | Inconnue |
| [Transport pour Atlanta, États-Unis](http://www.itsmarta.com/app-developer-resources.aspx)                                          | Martha                                                                                                                    | Non      | Non   | Inconnue |
| [Transport pour Auckland, Nouvelle-Zélande](https://api.at.govt.nz/)                                                                | Auckland Transport                                                                                                        | Non      | Oui   | Inconnue |
| [Transport pour la Belgique](https://hello.irail.be/api/)                                                                           | API de transport belge                                                                                                    | Non      | Oui   | Inconnue |
| [Transport pour Berlin, Allemagne](https://github.com/derhuerst/vbb-rest/blob/3/docs/index.md)                                      | API VBB tierce                                                                                                            | Non      | Oui   | Inconnue |
| [Transport pour Bordeaux, France](https://opendata.bordeaux-metropole.fr/explore/)                                                  | Bordeaux Métropole public transport and more (France)                                                                     | `apiKey` | Oui   | Inconnue |
| [Transport pour Boston, États-Unis](https://mbta.com/developers/v3-api)                                                             | API MBTA                                                                                                                  | Non      | Non   | Inconnue |
| [Transport pour Budapest, Hongrie](https://bkkfutar.docs.apiary.io)                                                                 | API des transports publics de Budapest                                                                                    | Non      | Oui   | Inconnue |
| [Transport pour Chicago, États-Unis](http://www.transitchicago.com/developers/)                                                     | CTA                                                                                                                       | Non      | Non   | Inconnue |
| [Transport pour la République tchèque](https://www.chaps.cz/eng/products/idos-internet)                                             | API de transport tchèque                                                                                                  | Non      | Oui   | Inconnue |
| [Transport pour Denver, États-Unis](http://www.rtd-denver.com/gtfs-developer-guide.shtml)                                           | RTD                                                                                                                       | Non      | Non   | Inconnue |
| [Transport pour la Finlande](https://digitransit.fi/en/developers/)                                                                 | API de transport finlandaise                                                                                              | Non      | Oui   | Inconnue |
| [Transport pour l'Allemagne](http://data.deutschebahn.com/dataset/api-fahrplan)                                                     | API Deutsche Bahn (DB)                                                                                                    | `apiKey` | Non   | Inconnue |
| [Transport pour Grenoble, France](https://www.metromobilite.fr/pages/opendata/OpenDataApi.html)                                     | Transports publics de Grenoble                                                                                            | Non      | Non   | Non      |
| [Transport pour Honolulu, États-Unis](http://hea.thebus.org/api_info.asp)                                                           | Honolulu Transport Information                                                                                            | `apiKey` | Non   | Inconnue |
| [Transport pour l'Inde](https://data.gov.in/sector/transport)                                                                       | API de transport public en Inde                                                                                           | `apiKey` | Oui   | Inconnue |
| [Transport pour Lisbonne, Portugal](https://emel.city-platform.com/opendata/)                                                       | Données sur les itinéraires des bus, le stationnement et la circulation                                                   | `apiKey` | Oui   | Inconnue |
| [Transport pour Londres, Angleterre](https://api.tfl.gov.uk)                                                                        | API TfL                                                                                                                   | Non      | Oui   | Inconnue |
| [Transport pour Manchester, Angleterre](https://developer.tfgm.com/)                                                                | Données du réseau de transport TfGM                                                                                       | `apiKey` | Oui   | Non      |
| [Transport pour New York, États-Unis](http://datamine.mta.info/)                                                                    | MTA                                                                                                                       | `apiKey` | Non   | Inconnue |
| [Transport pour la Norvège](http://reisapi.ruter.no/help)                                                                           | API de transport norvégienne                                                                                              | Non      | Non   | Inconnue |
| [Transport pour Paris, France](http://restratpws.azurewebsites.net/swagger/)                                                        | Horaires en direct simplifiés                                                                                             | Non      | Non   | Inconnue |
| [Transport pour Paris, France](http://data.ratp.fr/api/v1/console/datasets/1.0/search/)                                             | API RATP Open Data                                                                                                        | Non      | Non   | Inconnue |
| [Transport pour Philadelphie, États-Unis](http://www3.septa.org/hackathon/)                                                         | API SEPTA                                                                                                                 | Non      | Non   | Inconnue |
| [Transport pour Sao Paulo, Brésil](http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/documentacao-api/) | SPTrans                                                                                                                   | `OAuth`  | Non   | Inconnue |
| [Transport pour la Suède](https://www.trafiklab.se/api)                                                                             | Consommateur des transports publics                                                                                       | `OAuth`  | Oui   | Inconnue |
| [Transport pour la Suisse](https://opentransportdata.swiss/en/)                                                                     | Open Data officiel des transports publics suisses                                                                         | `apiKey` | Oui   | Inconnue |
| [Transport pour la Suisse](https://transport.opendata.ch/)                                                                          | API des transports publics suisses                                                                                        | Non      | Oui   | Inconnue |
| [Transport pour les Pays-Bas](http://www.ns.nl/reisinformatie/ns-api)                                                               | NS, trains seulement                                                                                                      | `apiKey` | Non   | Inconnue |
| [Transport pour les Pays-Bas](https://github.com/skywave/KV78Turbo-OVAPI/wiki)                                                      | OVAPI, transport public à l'échelle nationale                                                                             | Non      | Oui   | Inconnue |
| [Transport pour Toronto, Canada](https://myttc.ca/developers)                                                                       | TTC                                                                                                                       | Non      | Oui   | Inconnue |
| [Transport pour les États-Unis](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf)                                              | API NextBus                                                                                                               | Non      | Non   | Inconnue |
| [Transport pour Vancouver, Canada](https://developer.translink.ca/)                                                                 | TransLink                                                                                                                 | `OAuth`  | Oui   | Inconnue |
| [Transport pour Washington, États-Unis](https://developer.wmata.com/)                                                               | API de transport du métro de Washington                                                                                   | `OAuth`  | Oui   | Inconnue |
| [Uber](https://developer.uber.com/products)                                                                                         | Demande de trajet Uber et estimation de prix                                                                              | `OAuth`  | Oui   | Oui      |
| [WhereIsMyTransport](https://developer.whereismytransport.com/)                                                                     | Plateforme de données de transports publics dans les villes émergentes                                                    | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Raccourcisseurs d'URL

| FEU                                                                        | La description                                                      | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------- | ----- | -------- |
| [Bitly](http://dev.bitly.com/get_started.html)                             | Raccourcisseur d'URL et gestion des liens                           | `OAuth`  | Oui   | Inconnue |
| [CleanURI](https://cleanuri.com/docs)                                      | Service de raccourcissement d'URL                                   | `No`     | Oui   | Oui      |
| [ClickMeter](https://support.clickmeter.com/hc/en-us/categories/201474986) | Surveillez, comparez et optimisez vos liens marketing               | `apiKey` | Oui   | Inconnue |
| [Rebrandly](https://developers.rebrandly.com/v1/docs)                      | Raccourcisseur d'URL personnalisé pour partager des liens de marque | `apiKey` | Oui   | Inconnue |
| [Relier](https://rel.ink)                                                  | Raccourcisseur d'URL gratuit et sécurisé                            | Non      | Oui   | Oui      |

**[⬆ Retour à l'index](#index)**

### Véhicule

| FEU                                                                   | La description                                                                                                                                                                   | Auth     | HTTPS | CORS     |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- | -------- |
| [Véhicules et prix brésiliens](https://deividfortuna.github.io/fipe/) | Informations sur les véhicules de la Fondation de l'Institut de recherche économique - Fipe                                                                                      | Non      | Oui   | Inconnue |
| [Kelley Blue Book](http://developer.kbb.com/#!/data/1-Default)        | Informations sur le véhicule, prix, configuration, et bien plus encore                                                                                                           | `apiKey` | Oui   | Non      |
| [Mercedes Benz](https://developer.mercedes-benz.com/apis)             | Données télématiques, accès à distance aux fonctions du véhicule, configurateur de voiture, localisation des concessionnaires de services                                        | `apiKey` | Oui   | Non      |
| [NHTSA](https://vpic.nhtsa.dot.gov/api/)                              | Catalogue d'informations sur les produits NHTSA et liste des véhicules                                                                                                           | Non      | Oui   | Inconnue |
| [Voiture intelligente](https://smartcar.com/docs/)                    | Verrouillez et déverrouillez les véhicules et obtenez des données telles que la lecture du compteur kilométrique et l'emplacement. Fonctionne sur la plupart des voitures neuves | `OAuth`  | Oui   | Oui      |

**[⬆ Retour à l'index](#index)**

### Vidéo

| FEU                                                                                                      | La description                                                  | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------- | ----- | -------- |
| [Une API de glace et de feu](https://anapioficeandfire.com/)                                             | API Game Of Thrones                                             | Non      | Oui   | Inconnue |
| [Breaking Bad](https://breakingbadapi.com/documentation)                                                 | Breaking Bad API                                                | Non      | Oui   | Inconnue |
| [Breaking Bad Quotes](https://github.com/shevabam/breaking-bad-quotes)                                   | Quelques citations de rupture                                   | Non      | Oui   | Inconnue |
| [Télévision tchèque](http://www.ceskatelevize.cz/xml/tv-program/)                                        | Programme télévisé de la télévision tchèque                     | Non      | Non   | Inconnue |
| [Dailymotion](https://developer.dailymotion.com/)                                                        | API développeur Dailymotion                                     | `OAuth`  | Oui   | Inconnue |
| [Harry Potter](https://www.potterapi.com/)                                                               | API Harry Potter                                                | `apiKey` | Oui   | Oui      |
| [Ouvrir la base de données des films](http://www.omdbapi.com/)                                           | Informations sur le film                                        | `apiKey` | Oui   | Inconnue |
| [Citations de Ron Swanson](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api) | Télévision                                                      | Non      | Oui   | Inconnue |
| [STAPI](http://stapi.co)                                                                                 | Informations sur tout ce qui concerne Star Trek                 | Non      | Non   | Non      |
| [Le Seigneur des Anneaux](https://the-one-api.herokuapp.com/)                                            | API Le Seigneur des Anneaux                                     | `apiKey` | Oui   | Inconnue |
| [TMDb](https://www.themoviedb.org/documentation/api)                                                     | Données de films communautaires                                 | `apiKey` | Oui   | Inconnue |
| [Tract](https://trakt.tv/b/api-docs)                                                                     | Film et données TV                                              | `apiKey` | Oui   | Oui      |
| [TVDB](https://api.thetvdb.com/swagger)                                                                  | Données de télévision                                           | `apiKey` | Oui   | Inconnue |
| [TVMaze](http://www.tvmaze.com/api)                                                                      | Données sur les émissions de télévision                         | Non      | Non   | Inconnue |
| [Vimeo](https://developer.vimeo.com/)                                                                    | API développeur Vimeo                                           | `OAuth`  | Oui   | Inconnue |
| [Youtube](https://developers.google.com/youtube/)                                                        | Ajoutez des fonctionnalités YouTube à vos sites et applications | `OAuth`  | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**

### Temps

| FEU                                                                        | La description                                       | Auth     | HTTPS | CORS     |
| -------------------------------------------------------------------------- | ---------------------------------------------------- | -------- | ----- | -------- |
| [7Timer!](http://www.7timer.info/doc.php?lang=en)                          | Météo, en particulier pour Astroweather              | Non      | Non   | Inconnue |
| [APIXU](https://www.apixu.com/doc/request.aspx)                            | Temps                                                | `apiKey` | Oui   | Inconnue |
| [MetaWeather](https://www.metaweather.com/api/)                            | Temps                                                | Non      | Oui   | Non      |
| [Département de météorologie](https://api.met.no/weatherapi/documentation) | Données météorologiques et climatiques               | Non      | Oui   | Inconnue |
| [Données climatiques de la NOAA](https://www.ncdc.noaa.gov/cdo-web/)       | Données météorologiques et climatiques               | `apiKey` | Oui   | Inconnue |
| [ODWeather](http://api.oceandrivers.com/static/docs.html)                  | Météo et webcams météo                               | Non      | Non   | Inconnue |
| [OpenUV](https://www.openuv.io)                                            | Prévisions de l'indice UV en temps réel              | `apiKey` | Oui   | Inconnue |
| [OpenWeatherMap](http://openweathermap.org/api)                            | Temps                                                | `apiKey` | Non   | Inconnue |
| [Verre tempête](https://stormglass.io/)                                    | Météo marine mondiale provenant de plusieurs sources | `apiKey` | Oui   | Oui      |
| [Weatherbit](https://www.weatherbit.io/api)                                | Temps                                                | `apiKey` | Oui   | Inconnue |
| [Yahoo! Temps](https://developer.yahoo.com/weather/)                       | Temps                                                | `apiKey` | Oui   | Inconnue |

**[⬆ Retour à l'index](#index)**
