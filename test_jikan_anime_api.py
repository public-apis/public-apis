#!/usr/bin/env python3
"""
Test script for Jikan API (Unofficial MyAnimeList API)
Repository: public-apis
API: https://jikan.moe
"""

import requests
import json
from typing import Dict, Any


class JikanAPITester:
    """Tester für die Jikan Anime API"""

    BASE_URL = "https://api.jikan.moe/v4"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'JikanAPI-Tester/1.0'
        })

    def get_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        """Ruft Details eines bestimmten Anime ab"""
        url = f"{self.BASE_URL}/anime/{anime_id}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def search_anime(self, query: str, limit: int = 5) -> Dict[str, Any]:
        """Sucht nach Anime anhand eines Suchbegriffs"""
        url = f"{self.BASE_URL}/anime"
        params = {'q': query, 'limit': limit}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_top_anime(self, limit: int = 10) -> Dict[str, Any]:
        """Ruft die Top-bewerteten Anime ab"""
        url = f"{self.BASE_URL}/top/anime"
        params = {'limit': limit}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_random_anime(self) -> Dict[str, Any]:
        """Ruft einen zufälligen Anime ab"""
        url = f"{self.BASE_URL}/random/anime"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_current_season(self) -> Dict[str, Any]:
        """Ruft Anime der aktuellen Season ab"""
        url = f"{self.BASE_URL}/seasons/now"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()


def print_anime_info(anime_data: Dict[str, Any], compact: bool = False):
    """Formatierte Ausgabe von Anime-Informationen"""
    if 'data' in anime_data:
        anime = anime_data['data']
    else:
        anime = anime_data

    print(f"\n{'=' * 70}")
    print(f"Titel: {anime.get('title', 'N/A')}")
    print(f"Englischer Titel: {anime.get('title_english', 'N/A')}")
    print(f"Japanischer Titel: {anime.get('title_japanese', 'N/A')}")
    print(f"Typ: {anime.get('type', 'N/A')}")
    print(f"Episoden: {anime.get('episodes', 'N/A')}")
    print(f"Status: {anime.get('status', 'N/A')}")
    print(f"Score: {anime.get('score', 'N/A')} (bewertet von {anime.get('scored_by', 'N/A')} Benutzern)")
    print(f"Rank: #{anime.get('rank', 'N/A')}")
    print(f"Popularität: #{anime.get('popularity', 'N/A')}")

    if not compact and anime.get('synopsis'):
        print(f"\nSynopsis:\n{anime['synopsis'][:300]}...")

    print(f"URL: {anime.get('url', 'N/A')}")
    print('=' * 70)


def main():
    """Hauptfunktion zum Testen der Jikan API"""

    print("\n" + "="*70)
    print("JIKAN API TESTER - Unofficial MyAnimeList API")
    print("="*70)

    tester = JikanAPITester()

    # Test 1: Spezifischen Anime abrufen (Cowboy Bebop)
    print("\n\n[TEST 1] Abrufen von Cowboy Bebop (ID: 1)")
    print("-" * 70)
    try:
        cowboy_bebop = tester.get_anime_by_id(1)
        print_anime_info(cowboy_bebop)
        print("✓ Test erfolgreich!")
    except Exception as e:
        print(f"✗ Fehler: {e}")

    # Test 2: Nach Anime suchen
    print("\n\n[TEST 2] Suche nach 'One Piece'")
    print("-" * 70)
    try:
        search_results = tester.search_anime("One Piece", limit=3)
        print(f"Gefunden: {len(search_results['data'])} Ergebnisse")
        for idx, anime in enumerate(search_results['data'], 1):
            print(f"\n--- Ergebnis {idx} ---")
            print(f"Titel: {anime['title']}")
            print(f"Typ: {anime.get('type', 'N/A')}, Episoden: {anime.get('episodes', 'N/A')}")
            print(f"Score: {anime.get('score', 'N/A')}")
        print("\n✓ Test erfolgreich!")
    except Exception as e:
        print(f"✗ Fehler: {e}")

    # Test 3: Top Anime abrufen
    print("\n\n[TEST 3] Top 5 bewertete Anime")
    print("-" * 70)
    try:
        top_anime = tester.get_top_anime(limit=5)
        for idx, anime in enumerate(top_anime['data'], 1):
            print(f"\n{idx}. {anime['title']}")
            print(f"   Score: {anime.get('score', 'N/A')} | Rank: #{anime.get('rank', 'N/A')}")
            print(f"   Typ: {anime.get('type', 'N/A')} | Episoden: {anime.get('episodes', 'N/A')}")
        print("\n✓ Test erfolgreich!")
    except Exception as e:
        print(f"✗ Fehler: {e}")

    # Test 4: Zufälliger Anime
    print("\n\n[TEST 4] Zufälliger Anime")
    print("-" * 70)
    try:
        random_anime = tester.get_random_anime()
        print_anime_info(random_anime, compact=True)
        print("✓ Test erfolgreich!")
    except Exception as e:
        print(f"✗ Fehler: {e}")

    # Test 5: Aktuelle Season
    print("\n\n[TEST 5] Anime der aktuellen Season (erste 3)")
    print("-" * 70)
    try:
        current_season = tester.get_current_season()
        print(f"Gesamt in aktueller Season: {len(current_season['data'])} Anime")
        for idx, anime in enumerate(current_season['data'][:3], 1):
            print(f"\n{idx}. {anime['title']}")
            print(f"   Typ: {anime.get('type', 'N/A')} | Status: {anime.get('status', 'N/A')}")
            print(f"   Score: {anime.get('score', 'N/A')}")
        print("\n✓ Test erfolgreich!")
    except Exception as e:
        print(f"✗ Fehler: {e}")

    print("\n\n" + "="*70)
    print("ALLE TESTS ABGESCHLOSSEN!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
