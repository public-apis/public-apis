#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复有明确新 URL 的 API 条目
"""

import re

README_PATH = "README.md"

# 明确已知需要更新的映射
URL_UPDATES = {
    # Blockchain
    "https://www.covalenthq.com/docs/api/": "https://goldrush.mintlify.app/docs/api",
    # Cryptocurrency
    "https://docs.alchemy.com/alchemy/": "https://www.alchemy.com/docs/alchemy",
    # Email
    "https://mailtrap.docs.apiary.io/#": "https://mailtrap.docs.apiary.io/",
    "https://developers.sendinblue.com/docs": "https://developers.brevo.com/docs",
    # Games & Comics
    "https://www.giantbomb.com/api/documentation": "https://giantbomb.com/api/documentation",
    # Government
    "http://opendata.praha.eu/en": "https://opendata.praha.eu/en",
    "http://ratings.food.gov.uk/open-data/en-GB": "https://ratings.food.gov.uk/open-data/en-GB",
    "https://data.gov.sg/developer": "https://guide.data.gov.sg/developers/apis",
    # Health
    "https://www.hpb.health.gov.lk/en/api-documentation": "https://hpb.health.gov.lk/en/api-documentation",
    # Machine Learning
    "https://www.machinetutors.com/portfolio/MT_api.html": "https://machinetutors.com/portfolio/MT_api.html",
    # Social
    "https://developers.revolt.chat/api/": "https://developers.stoat.chat/api/",
    # Sports & Fitness
    "https://sportdataapi.com": "https://sportdataapi.com/",
    # Transportation
    "https://dev.blablacar.com": "https://dev.blablacar.com/",
    "https://developer.translink.ca/": "https://www.translink.ca/about-us/doing-business-with-translink/app-developer-resources",
}

def update_readme():
    """更新 README.md"""
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    updated_count = 0
    for old_url, new_url in URL_UPDATES.items():
        pattern = re.compile(re.escape(old_url))
        new_content, count = pattern.subn(new_url, content)
        if count > 0:
            print(f"✅ 更新: {old_url[:50]}")
            content = new_content
            updated_count += count

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n共更新了 {updated_count} 个链接")
    return updated_count

if __name__ == '__main__':
    print("=" * 60)
    print("🔧 修复有明确新 URL 的 API 条目")
    print("=" * 60)
    update_readme()
