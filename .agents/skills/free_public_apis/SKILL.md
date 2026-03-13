---
name: Free Public APIs
description: Instructions and guidelines for using free, no-auth public APIs to retrieve data for users or agents.
---

# Free Public APIs Skill

This skill provides you (the AI agent) with a massive directory of free, open (No Auth), and secure (HTTPS) public APIs. Because the list is huge, we have organized it into a Table of Contents. 

## How to Use This Skill
1. **Locate the Category**: Scan the Table of Contents below to find the category that matches the user's request.
2. **Read the Reference File**: Use the `view_file` tool to read the specific reference file for that category, which contains the API list. The files are located in the `references/` folder relative to this SKILL.md file.
3. **Pick an API & Get Docs URL**: Pick the best API from the reference table. The reference file provides the Documentation URL.
4. **Read the Docs & Find Endpoint**: If the exact endpoint isn't obvious, use the `read_url_content` tool (or web browser) to quickly read the Documentation URL to find the exact endpoint, required parameters, and response schema.
5. **Execute Request**: Use the `run_command` tool (with `curl -s '<endpoint>'`) to fetch the data from the API and present it to the user.
6. **Do NOT summarize JSON schemas to the user** unless explicitly asked. Deliver the final useful result text naturally.

## Table of Contents

- **Animals** (21 APIs): See [`references/animals.md`](references/animals.md)
- **Anime** (10 APIs): See [`references/anime.md`](references/anime.md)
- **Anti-Malware** (1 APIs): See [`references/anti_malware.md`](references/anti_malware.md)
- **Art & Design** (9 APIs): See [`references/art_design.md`](references/art_design.md)
- **Blockchain** (4 APIs): See [`references/blockchain.md`](references/blockchain.md)
- **Books** (16 APIs): See [`references/books.md`](references/books.md)
- **Business** (6 APIs): See [`references/business.md`](references/business.md)
- **Calendar** (6 APIs): See [`references/calendar.md`](references/calendar.md)
- **Cloud Storage & File Sharing** (5 APIs): See [`references/cloud_storage_file_sharing.md`](references/cloud_storage_file_sharing.md)
- **Cryptocurrency** (21 APIs): See [`references/cryptocurrency.md`](references/cryptocurrency.md)
- **Currency Exchange** (9 APIs): See [`references/currency_exchange.md`](references/currency_exchange.md)
- **Data Validation** (1 APIs): See [`references/data_validation.md`](references/data_validation.md)
- **Development** (51 APIs): See [`references/development.md`](references/development.md)
- **Dictionaries** (4 APIs): See [`references/dictionaries.md`](references/dictionaries.md)
- **Documents & Productivity** (2 APIs): See [`references/documents_productivity.md`](references/documents_productivity.md)
- **Email** (8 APIs): See [`references/email.md`](references/email.md)
- **Entertainment** (10 APIs): See [`references/entertainment.md`](references/entertainment.md)
- **Environment** (7 APIs): See [`references/environment.md`](references/environment.md)
- **Finance** (8 APIs): See [`references/finance.md`](references/finance.md)
- **Food & Drink** (10 APIs): See [`references/food_drink.md`](references/food_drink.md)
- **Games & Comics** (58 APIs): See [`references/games_comics.md`](references/games_comics.md)
- **Geocoding** (37 APIs): See [`references/geocoding.md`](references/geocoding.md)
- **Government** (59 APIs): See [`references/government.md`](references/government.md)
- **Health** (23 APIs): See [`references/health.md`](references/health.md)
- **Jobs** (3 APIs): See [`references/jobs.md`](references/jobs.md)
- **Machine Learning** (3 APIs): See [`references/machine_learning.md`](references/machine_learning.md)
- **Music** (10 APIs): See [`references/music.md`](references/music.md)
- **News** (3 APIs): See [`references/news.md`](references/news.md)
- **Open Data** (17 APIs): See [`references/open_data.md`](references/open_data.md)
- **Open Source Projects** (7 APIs): See [`references/open_source_projects.md`](references/open_source_projects.md)
- **Patent** (2 APIs): See [`references/patent.md`](references/patent.md)
- **Personality** (17 APIs): See [`references/personality.md`](references/personality.md)
- **Phone** (1 APIs): See [`references/phone.md`](references/phone.md)
- **Photography** (5 APIs): See [`references/photography.md`](references/photography.md)
- **Programming** (1 APIs): See [`references/programming.md`](references/programming.md)
- **Science & Math** (26 APIs): See [`references/science_math.md`](references/science_math.md)
- **Security** (14 APIs): See [`references/security.md`](references/security.md)
- **Social** (8 APIs): See [`references/social.md`](references/social.md)
- **Sports & Fitness** (12 APIs): See [`references/sports_fitness.md`](references/sports_fitness.md)
- **Test Data** (16 APIs): See [`references/test_data.md`](references/test_data.md)
- **Text Analysis** (1 APIs): See [`references/text_analysis.md`](references/text_analysis.md)
- **Tracking** (2 APIs): See [`references/tracking.md`](references/tracking.md)
- **Transportation** (24 APIs): See [`references/transportation.md`](references/transportation.md)
- **URL Shorteners** (10 APIs): See [`references/url_shorteners.md`](references/url_shorteners.md)
- **Vehicle** (2 APIs): See [`references/vehicle.md`](references/vehicle.md)
- **Video** (25 APIs): See [`references/video.md`](references/video.md)
- **Weather** (8 APIs): See [`references/weather.md`](references/weather.md)