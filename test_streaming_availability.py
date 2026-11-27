#!/usr/bin/env python3
"""
Test script for Streaming Availability APIs
Repository: public-apis

This script demonstrates how to find where a movie is available for streaming
in a specific region (e.g., Germany) using various APIs.

APIs tested:
1. TMDb (The Movie Database) - Free, requires API key
2. Watchmode - 1000 free calls, requires API key
3. Streaming Availability API - 100 free calls/day

Use Case: Find where "Jason Bourne" (2016) is available for streaming in Germany
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional


class TMDbStreamingAPI:
    """
    TMDb API for movie information and streaming availability

    Get your free API key at: https://www.themoviedb.org/settings/api
    The API uses data from JustWatch for streaming providers.
    """

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('TMDB_API_KEY')
        if not self.api_key:
            print("⚠️  Hinweis: Kein TMDb API-Key gefunden.")
            print("   Registriere dich kostenlos auf: https://www.themoviedb.org/signup")
            print("   Dann hole dir deinen API-Key: https://www.themoviedb.org/settings/api\n")

        self.session = requests.Session()
        self.session.params = {'api_key': self.api_key}  # type: ignore

    def search_movie(self, title: str, year: Optional[int] = None) -> List[Dict[str, Any]]:
        """Sucht nach einem Film anhand des Titels"""
        url = f"{self.BASE_URL}/search/movie"
        params = {'query': title, 'language': 'de-DE'}

        if year:
            params['year'] = year

        response = self.session.get(url, params=params)
        response.raise_for_status()

        return response.json().get('results', [])

    def get_streaming_providers(self, movie_id: int) -> Dict[str, Any]:
        """
        Ruft Streaming-Anbieter für einen Film ab

        Returns: Dictionary mit Anbietern pro Land
        Daten stammen von JustWatch (Attribution erforderlich!)
        """
        url = f"{self.BASE_URL}/movie/{movie_id}/watch/providers"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()

    def get_movie_details(self, movie_id: int) -> Dict[str, Any]:
        """Ruft detaillierte Film-Informationen ab"""
        url = f"{self.BASE_URL}/movie/{movie_id}"
        params = {'language': 'de-DE'}

        response = self.session.get(url, params=params)
        response.raise_for_status()

        return response.json()


class WatchmodeAPI:
    """
    Watchmode API for streaming availability

    Get your free API key at: https://api.watchmode.com/requestApiKey
    1000 free API calls, no credit card required.
    """

    BASE_URL = "https://api.watchmode.com/v1"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('WATCHMODE_API_KEY')
        if not self.api_key:
            print("⚠️  Hinweis: Kein Watchmode API-Key gefunden.")
            print("   Hole dir 1000 kostenlose API-Calls: https://api.watchmode.com/requestApiKey\n")

    def search_title(self, title: str) -> List[Dict[str, Any]]:
        """Sucht nach einem Film/Serie"""
        url = f"{self.BASE_URL}/autocomplete-search/"
        params = {'apiKey': self.api_key, 'search_value': title, 'search_type': 1}  # 1 = movies only

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json().get('results', [])

    def get_title_details(self, watchmode_id: int, regions: str = "DE") -> Dict[str, Any]:
        """
        Ruft Details und Streaming-Verfügbarkeit ab

        Args:
            watchmode_id: Die Watchmode ID des Films
            regions: Komma-getrennte Liste von ISO-3166-1 Ländercodes (z.B. "DE" für Deutschland)
        """
        url = f"{self.BASE_URL}/title/{watchmode_id}/details/"
        params = {'apiKey': self.api_key, 'regions': regions}

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()


def print_streaming_info_tmdb(providers_data: Dict[str, Any], country_code: str = "DE"):
    """Formatierte Ausgabe der TMDb Streaming-Informationen"""

    results = providers_data.get('results', {})

    if country_code not in results:
        print(f"❌ Keine Streaming-Daten für {country_code} verfügbar")
        return

    country_data = results[country_code]
    link = country_data.get('link', 'N/A')

    print(f"\n{'='*80}")
    print(f"🌍 Streaming-Verfügbarkeit in Deutschland (DE)")
    print(f"{'='*80}")
    print(f"📊 Datenquelle: JustWatch (via TMDb API)")
    print(f"🔗 Mehr Infos: {link}\n")

    # Flatrate (Subscription/Kostenlos im Abo)
    if 'flatrate' in country_data:
        print("📺 FLATRATE / ABO-DIENSTE (im Abonnement enthalten):")
        print("-" * 80)
        for provider in country_data['flatrate']:
            print(f"  • {provider['provider_name']} (ID: {provider['provider_id']})")
        print()

    # Free (Kostenlos mit Werbung)
    if 'free' in country_data:
        print("🆓 KOSTENLOS (mit Werbung):")
        print("-" * 80)
        for provider in country_data['free']:
            print(f"  • {provider['provider_name']} (ID: {provider['provider_id']})")
        print()

    # Rent (Ausleihen)
    if 'rent' in country_data:
        print("💰 AUSLEIHEN:")
        print("-" * 80)
        for provider in country_data['rent']:
            print(f"  • {provider['provider_name']} (ID: {provider['provider_id']})")
        print()

    # Buy (Kaufen)
    if 'buy' in country_data:
        print("🛒 KAUFEN:")
        print("-" * 80)
        for provider in country_data['buy']:
            print(f"  • {provider['provider_name']} (ID: {provider['provider_id']})")
        print()

    # Wenn nichts verfügbar ist
    available_types = [k for k in ['flatrate', 'free', 'rent', 'buy'] if k in country_data]
    if not available_types:
        print("❌ Aktuell nicht zum Streaming verfügbar in Deutschland")

    print("="*80)


def main():
    """Hauptfunktion zum Testen der Streaming Availability APIs"""

    print("\n" + "="*80)
    print("STREAMING AVAILABILITY API TESTER")
    print("="*80)
    print("Use Case: Wo kann ich 'Jason Bourne' (2016) in Deutschland streamen?")
    print("="*80 + "\n")

    # =============================================================================
    # TEST 1: TMDb API
    # =============================================================================
    print("\n[TEST 1] TMDb API (The Movie Database)")
    print("-" * 80)

    tmdb = TMDbStreamingAPI()

    if tmdb.api_key:
        try:
            # Suche nach "Jason Bourne" (2016)
            print("🔍 Suche nach 'Jason Bourne' (2016)...\n")
            search_results = tmdb.search_movie("Jason Bourne", year=2016)

            if search_results:
                movie = search_results[0]
                movie_id = movie['id']

                print(f"✅ Film gefunden!")
                print(f"   Titel: {movie['title']}")
                print(f"   Original-Titel: {movie.get('original_title', 'N/A')}")
                print(f"   Erscheinungsdatum: {movie.get('release_date', 'N/A')}")
                print(f"   Bewertung: {movie.get('vote_average', 'N/A')}/10")
                print(f"   TMDb ID: {movie_id}")
                print(f"   Übersicht: {movie.get('overview', 'N/A')[:200]}...")

                # Hole Streaming-Anbieter
                print(f"\n🔍 Lade Streaming-Verfügbarkeit...")
                providers = tmdb.get_streaming_providers(movie_id)

                print_streaming_info_tmdb(providers, country_code="DE")

                print("\n✅ TEST 1 ERFOLGREICH!")

            else:
                print("❌ Kein Film gefunden")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("❌ Fehler: Ungültiger API-Key")
                print("   Registriere dich kostenlos auf: https://www.themoviedb.org/signup")
            else:
                print(f"❌ HTTP Fehler: {e}")
        except Exception as e:
            print(f"❌ Fehler: {e}")
    else:
        print("⏭️  Übersprungen (kein API-Key)")
        print("\n📝 DEMO: So würde die Ausgabe aussehen:")
        print("-" * 80)
        demo_response = {
            'results': {
                'DE': {
                    'link': 'https://www.themoviedb.org/movie/324668-jason-bourne/watch?locale=DE',
                    'flatrate': [
                        {'provider_id': 119, 'provider_name': 'Amazon Prime Video'}
                    ],
                    'rent': [
                        {'provider_id': 2, 'provider_name': 'Apple TV'},
                        {'provider_id': 3, 'provider_name': 'Google Play Movies'},
                        {'provider_id': 10, 'provider_name': 'Amazon Video'}
                    ],
                    'buy': [
                        {'provider_id': 2, 'provider_name': 'Apple TV'},
                        {'provider_id': 3, 'provider_name': 'Google Play Movies'},
                        {'provider_id': 10, 'provider_name': 'Amazon Video'}
                    ]
                }
            }
        }
        print_streaming_info_tmdb(demo_response, country_code="DE")


    # =============================================================================
    # TEST 2: Watchmode API
    # =============================================================================
    print("\n\n[TEST 2] Watchmode API")
    print("-" * 80)

    watchmode = WatchmodeAPI()

    if watchmode.api_key:
        try:
            print("🔍 Suche nach 'Jason Bourne'...\n")
            results = watchmode.search_title("Jason Bourne")

            if results:
                # Finde den 2016er Film
                jason_bourne_2016 = None
                for item in results:
                    if '2016' in str(item.get('year', '')):
                        jason_bourne_2016 = item
                        break

                if jason_bourne_2016:
                    print(f"✅ Film gefunden!")
                    print(f"   Titel: {jason_bourne_2016['name']}")
                    print(f"   Jahr: {jason_bourne_2016.get('year', 'N/A')}")
                    print(f"   Watchmode ID: {jason_bourne_2016['id']}")

                    # Hole Details mit DE region
                    print(f"\n🔍 Lade Streaming-Verfügbarkeit für Deutschland...")
                    details = watchmode.get_title_details(jason_bourne_2016['id'], regions="DE")

                    print(f"\n{'='*80}")
                    print(f"🌍 Streaming-Verfügbarkeit in Deutschland (Watchmode)")
                    print(f"{'='*80}")

                    sources = details.get('sources', [])
                    if sources:
                        for source in sources:
                            region = source.get('region', 'Unknown')
                            if region == 'DE':
                                print(f"\n📺 {source.get('name', 'Unknown')}")
                                print(f"   Typ: {source.get('type', 'Unknown')}")
                                print(f"   Format: {source.get('format', 'Unknown')}")
                                print(f"   Link: {source.get('web_url', 'N/A')}")
                    else:
                        print("❌ Keine Streaming-Quellen gefunden")

                    print("="*80)
                    print("\n✅ TEST 2 ERFOLGREICH!")
                else:
                    print("❌ Jason Bourne (2016) nicht in den Suchergebnissen")
            else:
                print("❌ Keine Suchergebnisse")

        except Exception as e:
            print(f"❌ Fehler: {e}")
    else:
        print("⏭️  Übersprungen (kein API-Key)")
        print("   Hole dir 1000 kostenlose API-Calls: https://api.watchmode.com/requestApiKey")


    # =============================================================================
    # ZUSAMMENFASSUNG
    # =============================================================================
    print("\n\n" + "="*80)
    print("📊 ZUSAMMENFASSUNG - APIs für Streaming-Verfügbarkeit")
    print("="*80)

    print("\n🥇 EMPFOHLENE APIs FÜR DEINEN USE-CASE:")
    print("-" * 80)

    print("\n1️⃣  TMDb API (The Movie Database)")
    print("   ✅ Kostenlos (API-Key erforderlich)")
    print("   ✅ Daten von JustWatch")
    print("   ✅ Deutschland-Support (DE)")
    print("   ✅ Zeigt: Abo-Dienste, Kostenlos, Ausleihe, Kauf")
    print("   ✅ Sehr umfangreich und zuverlässig")
    print("   🔗 Anmelden: https://www.themoviedb.org/signup")
    print("   📖 Docs: https://developers.themoviedb.org/3")

    print("\n2️⃣  Watchmode API")
    print("   ✅ 1000 kostenlose API-Calls")
    print("   ✅ Keine Kreditkarte erforderlich")
    print("   ✅ 50+ Länder inkl. Deutschland")
    print("   ✅ 200+ Streaming-Dienste")
    print("   🔗 API-Key holen: https://api.watchmode.com/requestApiKey")
    print("   📖 Docs: https://api.watchmode.com/docs")

    print("\n3️⃣  Streaming Availability API (Movie of the Night)")
    print("   ✅ 100 kostenlose Calls pro Tag")
    print("   ✅ 60 Länder inkl. Deutschland")
    print("   ✅ Netflix, Disney+, Apple TV, Max, Hulu etc.")
    print("   ⚠️  Läuft über RapidAPI")
    print("   🔗 RapidAPI: https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability")
    print("   📖 Docs: https://docs.movieofthenight.com/")

    print("\n4️⃣  JustWatch API")
    print("   ⚠️  Keine offizielle öffentliche API")
    print("   ℹ️  TMDb nutzt JustWatch-Daten (siehe Option 1)")
    print("   🔗 Website: https://www.justwatch.com/de")

    print("\n" + "="*80)
    print("💡 ANTWORT AUF DEINE FRAGE:")
    print("="*80)
    print("""
Für deinen Use-Case (Jason Bourne 2016 in Deutschland, kostenlos) empfehle ich:

🎯 BESTE LÖSUNG: TMDb API
   - Kostenlos und einfach zu nutzen
   - Zeigt explizit, welche Dienste KOSTENLOS sind (mit Werbung)
   - Unterscheidet zwischen Abo-Diensten und wirklich kostenlosen Optionen
   - Endpoint: /movie/{id}/watch/providers

⚠️ WICHTIG: "Kostenlos" bedeutet in den meisten Fällen:
   1. Mit Werbung (Free tier)
   2. Im Abo enthalten (Flatrate) - nicht direkt kostenlos, aber im Abo dabei

Für echte kostenlose Optionen schau nach Anbietern unter dem "free" key,
diese sind mit Werbung finanziert und erfordern kein Abonnement.
""")

    print("="*80 + "\n")


if __name__ == "__main__":
    main()
