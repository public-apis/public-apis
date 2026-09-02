import sys

CATEGORY_MODELS = {
    "Weather": ["weather", "forecast", "temperature", "rain", "climate", "meteorology"],
    "Finance & Currency": ["finance", "currency", "bitcoin", "crypto", "stock", "exchange", "money"],
    "Games & Comics": ["game", "comic", "pokemon", "rpg", "dice", "steam", "boardgame"],
    "Data Validation": ["validate", "phone", "email", "postal", "address", "verification"],
    "Machine Learning / AI": ["ai", "machine learning", "deep learning", "vision", "text-to-speech", "openai"]
}

def suggest_category(api_description):
    print(f"\n[Analiz Edilen API Aciklamasi]: '{api_description}'")
    desc_lower = api_description.lower()
    scores = {category: 0 for category in CATEGORY_MODELS}

    for category, keywords in CATEGORY_MODELS.items():
        for keyword in keywords:
            if keyword in desc_lower:
                scores[category] += 1

    best_category = max(scores, key=scores.get)

    if scores[best_category] > 0:
        print(f"[ONERI]: Bu API %{scores[best_category]*20 + 40} ihtimalle '{best_category}' kategorisine ait!")
        return best_category
    else:
        print("[ONERI]: Net bir esleme bulunamadi. Tavsiye edilen genel kategori: 'Development'")
        return "Development"

if __name__ == "__main__":
    print("=== API Kategori Oneri Sistemi Aktif ===")

    sample_desc = "A free API that provides real-time bitcoin prices and historical stock currency exchange rates."

    if len(sys.argv) > 1:
        sample_desc = " ".join(sys.argv[1:])

    suggest_category(sample_desc)