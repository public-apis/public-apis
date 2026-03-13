---
name: Free Public APIs
description: Instructions and guidelines for using free, no-auth public APIs to retrieve data for users or agents.
---

# Free Public APIs Skill (it excludes the APIs that needs auth in the public API list)

This skill provides you (the AI agent) with a massive directory of free, open (No Auth), and secure (HTTPS) public APIs. Because the list is huge, we have organized it into a Table of Contents. 

## How to Use This Skill
1. **Locate the Category**: Scan the Table of Contents below to find the category that matches the user's request.
2. **Read the Reference File**: Use the `view_file` tool to read the specific reference file for that category, which contains the API list. E.g., `view_file({'AbsolutePath': '/Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/animals.md'})`
3. **Pick an API & Get Docs URL**: Pick the best API from the reference table. The reference file provides the Documentation URL.
4. **Read the Docs & Find Endpoint**: If the exact endpoint isn't obvious, use the `read_url_content` tool (or web browser) to quickly read the Documentation URL to find the exact endpoint, required parameters, and response schema.
5. **Execute Request**: Use the `run_command` tool (with `curl -s '<endpoint>'`) to fetch the data from the API and present it to the user.
6. **Do NOT summarize JSON schemas to the user** unless explicitly asked. Deliver the final useful result text naturally.

## Table of Contents

- **Animals** (21 APIs): See [`references/animals.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/animals.md)
- **Anime** (10 APIs): See [`references/anime.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/anime.md)
- **Anti-Malware** (1 APIs): See [`references/anti_malware.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/anti_malware.md)
- **Art & Design** (9 APIs): See [`references/art_design.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/art_design.md)
- **Blockchain** (4 APIs): See [`references/blockchain.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/blockchain.md)
- **Books** (16 APIs): See [`references/books.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/books.md)
- **Business** (6 APIs): See [`references/business.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/business.md)
- **Calendar** (6 APIs): See [`references/calendar.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/calendar.md)
- **Cloud Storage & File Sharing** (5 APIs): See [`references/cloud_storage_file_sharing.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/cloud_storage_file_sharing.md)
- **Cryptocurrency** (21 APIs): See [`references/cryptocurrency.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/cryptocurrency.md)
- **Currency Exchange** (9 APIs): See [`references/currency_exchange.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/currency_exchange.md)
- **Data Validation** (1 APIs): See [`references/data_validation.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/data_validation.md)
- **Development** (51 APIs): See [`references/development.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/development.md)
- **Dictionaries** (4 APIs): See [`references/dictionaries.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/dictionaries.md)
- **Documents & Productivity** (2 APIs): See [`references/documents_productivity.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/documents_productivity.md)
- **Email** (8 APIs): See [`references/email.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/email.md)
- **Entertainment** (10 APIs): See [`references/entertainment.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/entertainment.md)
- **Environment** (7 APIs): See [`references/environment.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/environment.md)
- **Finance** (8 APIs): See [`references/finance.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/finance.md)
- **Food & Drink** (10 APIs): See [`references/food_drink.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/food_drink.md)
- **Games & Comics** (58 APIs): See [`references/games_comics.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/games_comics.md)
- **Geocoding** (37 APIs): See [`references/geocoding.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/geocoding.md)
- **Government** (59 APIs): See [`references/government.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/government.md)
- **Health** (23 APIs): See [`references/health.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/health.md)
- **Jobs** (3 APIs): See [`references/jobs.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/jobs.md)
- **Machine Learning** (3 APIs): See [`references/machine_learning.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/machine_learning.md)
- **Music** (10 APIs): See [`references/music.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/music.md)
- **News** (3 APIs): See [`references/news.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/news.md)
- **Open Data** (17 APIs): See [`references/open_data.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/open_data.md)
- **Open Source Projects** (7 APIs): See [`references/open_source_projects.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/open_source_projects.md)
- **Patent** (2 APIs): See [`references/patent.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/patent.md)
- **Personality** (17 APIs): See [`references/personality.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/personality.md)
- **Phone** (1 APIs): See [`references/phone.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/phone.md)
- **Photography** (5 APIs): See [`references/photography.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/photography.md)
- **Programming** (1 APIs): See [`references/programming.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/programming.md)
- **Science & Math** (26 APIs): See [`references/science_math.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/science_math.md)
- **Security** (14 APIs): See [`references/security.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/security.md)
- **Social** (8 APIs): See [`references/social.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/social.md)
- **Sports & Fitness** (12 APIs): See [`references/sports_fitness.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/sports_fitness.md)
- **Test Data** (16 APIs): See [`references/test_data.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/test_data.md)
- **Text Analysis** (1 APIs): See [`references/text_analysis.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/text_analysis.md)
- **Tracking** (2 APIs): See [`references/tracking.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/tracking.md)
- **Transportation** (24 APIs): See [`references/transportation.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/transportation.md)
- **URL Shorteners** (10 APIs): See [`references/url_shorteners.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/url_shorteners.md)
- **Vehicle** (2 APIs): See [`references/vehicle.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/vehicle.md)
- **Video** (25 APIs): See [`references/video.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/video.md)
- **Weather** (8 APIs): See [`references/weather.md`](file:///Users/xyd945/Github/public-apis/.agents/skills/free_public_apis/references/weather.md)