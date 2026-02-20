#!/usr/bin/env python3
"""
Test script for gridX API and E.ON gridX Integration
Repository: public-apis

This script demonstrates how to retrieve data from the gridX API for
Viessmann Vitocal heat pumps and Vitocharge inverters connected via
E.ON gridX platform (https://eon.gridx.de)

APIs tested:
1. gridX Live Data API - Real-time system data
2. gridX Timeseries API - Historical data
3. gridX DER (Distributed Energy Resources) API

Use Case: Get energy data for Viessmann Vitocal WP + Vitocharge WR for Home Assistant
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta


class GridXAPI:
    """
    gridX API Client for E.ON gridX platform

    API Documentation: https://community.developer.gridx.de/
    Developer Portal: https://developer.gridx.ai/

    Requirements:
    1. gridX Account (e.g., via E.ON gridX)
    2. System ID (from your gridX dashboard)
    3. Bearer Token (OAuth2 authentication)

    How to get your credentials:
    1. Login to https://eon.gridx.de (or your gridX provider)
    2. Open browser developer tools (F12)
    3. Go to Network tab
    4. Refresh the page
    5. Look for requests to api.gridx.de
    6. Copy the Authorization header (Bearer token)
    7. Copy your system ID from the URL (format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
    """

    BASE_URL = "https://api.gridx.de"

    def __init__(self, system_id: Optional[str] = None, bearer_token: Optional[str] = None):
        self.system_id = system_id or os.getenv('GRIDX_SYSTEM_ID')
        self.bearer_token = bearer_token or os.getenv('GRIDX_BEARER_TOKEN')

        if not self.system_id:
            print("⚠️  Hinweis: Keine gridX System ID gefunden.")
            print("   Setze GRIDX_SYSTEM_ID Umgebungsvariable")
            print("   Format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\n")

        if not self.bearer_token:
            print("⚠️  Hinweis: Kein gridX Bearer Token gefunden.")
            print("   Setze GRIDX_BEARER_TOKEN Umgebungsvariable")
            print("   Hole Token aus Browser DevTools (siehe Docstring)\n")

        self.session = requests.Session()
        if self.bearer_token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.bearer_token}',
                'Content-Type': 'application/json'
            })

    def get_live_data(self) -> Dict[str, Any]:
        """
        Ruft Live-Daten des Systems ab

        Enthält u.a.:
        - PV-Erzeugung (Vitocharge)
        - Wärmepumpen-Status (Vitocal)
        - Batterie-Status
        - Netz-Bezug/Einspeisung
        - Hausverbrauch
        """
        url = f"{self.BASE_URL}/systems/{self.system_id}/live"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()

    def get_timeseries(self,
                       start: datetime,
                       end: datetime,
                       resolution: str = "PT15M") -> Dict[str, Any]:
        """
        Ruft historische Zeitreihendaten ab

        Args:
            start: Start-Zeitpunkt (datetime)
            end: End-Zeitpunkt (datetime)
            resolution: Auflösung (z.B. "PT15M" = 15 Minuten, "PT1H" = 1 Stunde)

        Returns:
            Zeitreihendaten für PV, Wärmepumpe, etc.
        """
        url = f"{self.BASE_URL}/systems/{self.system_id}/timeseries"

        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'resolution': resolution
        }

        response = self.session.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def get_system_info(self) -> Dict[str, Any]:
        """
        Ruft allgemeine System-Informationen ab

        Enthält:
        - Installierte Geräte (Vitocharge, Vitocal, etc.)
        - System-Konfiguration
        - Standort
        """
        url = f"{self.BASE_URL}/systems/{self.system_id}"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()


class ViessmannViCareAPI:
    """
    Viessmann ViCare API Client

    API Documentation: https://developer.viessmann.com/

    HINWEIS: Die ViCare API ist rate-limited und bietet nicht alle
    Daten, die über die gridX Integration verfügbar sind!

    Für Home Assistant wird die offizielle ViCare Integration empfohlen:
    https://www.home-assistant.io/integrations/vicare/
    """

    BASE_URL = "https://api.viessmann.com/iot/v1"

    def __init__(self, access_token: Optional[str] = None):
        self.access_token = access_token or os.getenv('VICARE_ACCESS_TOKEN')

        if not self.access_token:
            print("⚠️  Hinweis: Kein ViCare Access Token gefunden.")
            print("   OAuth2 Flow erforderlich")
            print("   Siehe: https://developer.viessmann.com/\n")

        self.session = requests.Session()
        if self.access_token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.access_token}'
            })

    def get_installations(self) -> Dict[str, Any]:
        """Ruft alle Installationen des Accounts ab"""
        url = f"{self.BASE_URL}/equipment/installations"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()


def print_live_data(data: Dict[str, Any]):
    """Formatierte Ausgabe der Live-Daten"""

    print(f"\n{'='*80}")
    print(f"⚡ LIVE-DATEN VOM GRIDX SYSTEM")
    print(f"{'='*80}")
    print(f"Zeitstempel: {data.get('timestamp', 'N/A')}")
    print()

    # PV-Anlage (Vitocharge)
    if 'pv' in data:
        pv = data['pv']
        print("☀️  PV-ANLAGE (Vitocharge Wechselrichter):")
        print("-" * 80)
        print(f"  Aktuelle Leistung: {pv.get('power', 0)} W")
        print(f"  Heutige Erzeugung: {pv.get('energy_today', 0)} kWh")
        print(f"  Gesamt-Erzeugung: {pv.get('energy_total', 0)} kWh")
        print()

    # Wärmepumpe (Vitocal)
    if 'heatpump' in data:
        hp = data['heatpump']
        print("🔥 WÄRMEPUMPE (Vitocal):")
        print("-" * 80)
        print(f"  Status: {hp.get('status', 'N/A')}")
        print(f"  Leistungsaufnahme: {hp.get('power', 0)} W")
        print(f"  Vorlauftemperatur: {hp.get('flow_temperature', 'N/A')} °C")
        print(f"  Rücklauftemperatur: {hp.get('return_temperature', 'N/A')} °C")
        print(f"  Außentemperatur: {hp.get('outdoor_temperature', 'N/A')} °C")
        print(f"  COP (aktuell): {hp.get('cop', 'N/A')}")
        print()

    # Batterie (falls vorhanden)
    if 'battery' in data:
        bat = data['battery']
        print("🔋 BATTERIE:")
        print("-" * 80)
        print(f"  Ladestand: {bat.get('soc', 0)} %")
        print(f"  Leistung: {bat.get('power', 0)} W (+ = Laden, - = Entladen)")
        print()

    # Netz
    if 'grid' in data:
        grid = data['grid']
        print("🏘️  NETZ:")
        print("-" * 80)
        print(f"  Leistung: {grid.get('power', 0)} W (+ = Bezug, - = Einspeisung)")
        print(f"  Heutiger Bezug: {grid.get('import_today', 0)} kWh")
        print(f"  Heutige Einspeisung: {grid.get('export_today', 0)} kWh")
        print()

    # Hausverbrauch
    if 'consumption' in data:
        cons = data['consumption']
        print("🏠 HAUSVERBRAUCH:")
        print("-" * 80)
        print(f"  Aktuelle Leistung: {cons.get('power', 0)} W")
        print(f"  Heutiger Verbrauch: {cons.get('energy_today', 0)} kWh")
        print()

    print("="*80)


def main():
    """Hauptfunktion zum Testen der gridX API"""

    print("\n" + "="*80)
    print("GRIDX API TESTER - E.ON gridX Integration")
    print("="*80)
    print("Für: Viessmann Vitocal Wärmepumpe + Vitocharge Wechselrichter")
    print("Ziel: Integration in Home Assistant")
    print("="*80 + "\n")

    # =============================================================================
    # TEST 1: gridX Live Data API
    # =============================================================================
    print("\n[TEST 1] gridX Live Data API")
    print("-" * 80)

    gridx = GridXAPI()

    if gridx.system_id and gridx.bearer_token:
        try:
            print("🔍 Lade Live-Daten...\n")
            live_data = gridx.get_live_data()

            print_live_data(live_data)

            print("\n✅ TEST 1 ERFOLGREICH!")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("❌ Fehler: Ungültiger Bearer Token oder abgelaufen")
                print("   Hole neuen Token aus Browser DevTools")
            elif e.response.status_code == 404:
                print("❌ Fehler: System ID nicht gefunden")
            else:
                print(f"❌ HTTP Fehler: {e}")
        except Exception as e:
            print(f"❌ Fehler: {e}")
    else:
        print("⏭️  Übersprungen (keine Credentials)")
        print("\n📝 DEMO: So würden die Daten aussehen:")
        print("-" * 80)
        demo_data = {
            'timestamp': '2026-01-11T14:30:00Z',
            'pv': {
                'power': 3500,
                'energy_today': 12.5,
                'energy_total': 8450.2
            },
            'heatpump': {
                'status': 'heating',
                'power': 850,
                'flow_temperature': 35.2,
                'return_temperature': 30.1,
                'outdoor_temperature': -2.5,
                'cop': 3.8
            },
            'grid': {
                'power': -2100,  # Einspeisung
                'import_today': 5.2,
                'export_today': 8.3
            },
            'consumption': {
                'power': 1400,
                'energy_today': 18.5
            }
        }
        print_live_data(demo_data)


    # =============================================================================
    # TEST 2: gridX System Info
    # =============================================================================
    print("\n\n[TEST 2] gridX System Information")
    print("-" * 80)

    if gridx.system_id and gridx.bearer_token:
        try:
            print("🔍 Lade System-Informationen...\n")
            system_info = gridx.get_system_info()

            print(f"System Name: {system_info.get('name', 'N/A')}")
            print(f"System ID: {system_info.get('id', 'N/A')}")
            print(f"Standort: {system_info.get('location', {}).get('city', 'N/A')}")
            print("\nInstallierte Geräte:")

            devices = system_info.get('devices', [])
            for device in devices:
                print(f"  - {device.get('type', 'N/A')}: {device.get('name', 'N/A')}")

            print("\n✅ TEST 2 ERFOLGREICH!")

        except Exception as e:
            print(f"❌ Fehler: {e}")
    else:
        print("⏭️  Übersprungen (keine Credentials)")


    # =============================================================================
    # ZUSAMMENFASSUNG & HOME ASSISTANT INTEGRATION
    # =============================================================================
    print("\n\n" + "="*80)
    print("📊 ZUSAMMENFASSUNG - APIs für Viessmann + gridX Integration")
    print("="*80)

    print("\n🎯 BESTE LÖSUNG FÜR HOME ASSISTANT:")
    print("-" * 80)

    print("\n1️⃣  gridX API (über E.ON gridX) ⭐ EMPFOHLEN")
    print("   ✅ Echtzeit-Daten von Vitocal + Vitocharge")
    print("   ✅ Vollständige Energieflüsse")
    print("   ✅ PV-Produktion, Wärmepumpen-Status, Netz, Verbrauch")
    print("   ✅ Live-Daten und historische Zeitreihen")
    print("   ⚠️  Benötigt Bearer Token (aus Browser holen)")
    print("   🔗 API Docs: https://community.developer.gridx.de/")
    print("   🔗 Developer Portal: https://developer.gridx.ai/")

    print("\n2️⃣  Viessmann ViCare API")
    print("   ✅ Offizielle Home Assistant Integration")
    print("   ✅ Direkt einrichtbar")
    print("   ⚠️  Rate-Limited (kann 24h blocken)")
    print("   ⚠️  Nicht alle Daten verfügbar (z.B. PV-Produktion fehlt oft)")
    print("   ⚠️  Vitocharge VX3 wird oft nicht angezeigt")
    print("   🔗 HA Integration: https://www.home-assistant.io/integrations/vicare/")
    print("   🔗 API: https://developer.viessmann.com/")

    print("\n3️⃣  HACS Community Integration (1komma5grad/gridX)")
    print("   ✅ Für gridX/1komma5grad Heartbeat")
    print("   ✅ HACS Installation möglich")
    print("   ⚠️  Neue API nicht in allen Regionen verfügbar")
    print("   🔗 GitHub: https://github.com/BirknerAlex/hacs_1komma5grad")

    print("\n" + "="*80)
    print("💡 EMPFEHLUNG FÜR DEIN SETUP:")
    print("="*80)
    print("""
Da du bereits E.ON gridX (https://eon.gridx.de) nutzt, hast du 2 Optionen:

OPTION A: gridX API direkt nutzen (empfohlen) ⭐
  1. Hole Bearer Token aus Browser DevTools (siehe Script-Kommentare)
  2. Verwende RESTful Sensor in Home Assistant
  3. Konfiguriere Sensoren für PV, Wärmepumpe, etc.

  Beispiel Home Assistant configuration.yaml:
  ```yaml
  sensor:
    - platform: rest
      name: "gridX Live Data"
      resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
      headers:
        Authorization: "Bearer DEIN-TOKEN"
      json_attributes:
        - pv
        - heatpump
        - grid
        - consumption
      value_template: "{{ value_json.timestamp }}"
  ```

OPTION B: HACS Integration nutzen
  1. Installiere HACS (falls noch nicht vorhanden)
  2. Füge Repository hinzu: https://github.com/BirknerAlex/hacs_1komma5grad
  3. Installiere Integration
  4. Konfiguriere mit deinen gridX Credentials

WICHTIG:
- gridX API bietet MEHR Daten als ViCare API
- gridX zeigt Vitocharge PV-Daten (ViCare oft nicht)
- Bearer Token läuft nach einiger Zeit ab → muss erneuert werden
- Alternative: OAuth2 Flow implementieren (komplexer)
""")

    print("="*80 + "\n")


if __name__ == "__main__":
    main()
