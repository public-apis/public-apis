#!/usr/bin/env python3
"""
Test script for Viessmann ViCare API - Power Consumption Data Points
Repository: public-apis

This script demonstrates how to access power consumption data from
Viessmann Vitocal heat pumps that is NOT shown in the standard
Home Assistant ViCare integration.

Use Case: Get electrical power consumption of heat pump for Home Assistant Energy Dashboard

API Documentation: https://api.viessmann-climatesolutions.com/documentation/data-points
Developer Portal: https://app.developer.viessmann-climatesolutions.com/
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime


class ViCareAPI:
    """
    Viessmann ViCare API Client

    WICHTIG: Die Standard Home Assistant ViCare Integration zeigt NICHT
    alle verfügbaren Datenpunkte! Speziell fehlen:
    - heating.power.consumption.dhw (Warmwasser Stromverbrauch)
    - heating.power.consumption.heating (Heizung Stromverbrauch)
    - heating.power.consumption.total (Gesamt Stromverbrauch)

    Diese müssen manuell abgefragt werden!

    GitHub Issue: https://github.com/home-assistant/core/issues/155695
    """

    BASE_URL = "https://api.viessmann.com/iot/v1"

    def __init__(self, access_token: Optional[str] = None):
        self.access_token = access_token or os.getenv('VICARE_ACCESS_TOKEN')

        if not self.access_token:
            print("⚠️  Hinweis: Kein ViCare Access Token gefunden.")
            print("   Du kannst den Token aus der Home Assistant Integration holen:")
            print("   1. Einstellungen → Geräte & Dienste → ViCare")
            print("   2. Oder manuell OAuth2 Flow durchführen")
            print("   3. Token als VICARE_ACCESS_TOKEN Umgebungsvariable setzen\n")

        self.session = requests.Session()
        if self.access_token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json'
            })

    def get_installations(self) -> List[Dict[str, Any]]:
        """Ruft alle Installationen des Accounts ab"""
        url = f"{self.BASE_URL}/equipment/installations"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()['data']

    def get_gateways(self, installation_id: int) -> List[Dict[str, Any]]:
        """Ruft alle Gateways einer Installation ab"""
        url = f"{self.BASE_URL}/equipment/installations/{installation_id}/gateways"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()['data']

    def get_devices(self, installation_id: int, gateway_serial: str) -> List[Dict[str, Any]]:
        """Ruft alle Geräte eines Gateways ab"""
        url = f"{self.BASE_URL}/equipment/installations/{installation_id}/gateways/{gateway_serial}/devices"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()['data']

    def get_features(self, installation_id: int, gateway_serial: str, device_id: str) -> Dict[str, Any]:
        """
        Ruft alle Features/Datenpunkte eines Geräts ab

        Enthält u.a.:
        - heating.power.consumption.dhw
        - heating.power.consumption.heating
        - heating.power.consumption.total
        - heating.circuits.X.temperature
        - heating.compressors.X.statistics
        - etc.
        """
        url = f"{self.BASE_URL}/equipment/installations/{installation_id}/gateways/{gateway_serial}/devices/{device_id}/features"

        response = self.session.get(url)
        response.raise_for_status()

        return response.json()['data']

    def get_power_consumption(self, installation_id: int, gateway_serial: str, device_id: str) -> Dict[str, Any]:
        """
        Ruft spezifisch die Stromverbrauchs-Datenpunkte ab

        Returns: Dictionary mit dhw, heating, total consumption
        """
        features = self.get_features(installation_id, gateway_serial, device_id)

        power_consumption = {
            'dhw': None,      # Domestic Hot Water (Warmwasser)
            'heating': None,  # Space Heating (Heizung)
            'total': None     # Total (Gesamt)
        }

        # Extrahiere die relevanten Features
        for feature in features:
            feature_name = feature.get('feature', '')

            if feature_name == 'heating.power.consumption.dhw':
                power_consumption['dhw'] = feature
            elif feature_name == 'heating.power.consumption.heating':
                power_consumption['heating'] = feature
            elif feature_name == 'heating.power.consumption.total':
                power_consumption['total'] = feature

        return power_consumption


def extract_consumption_values(feature: Dict[str, Any]) -> Dict[str, float]:
    """
    Extrahiert die Verbrauchswerte aus einem Feature

    Format der API-Antwort:
    {
        "properties": {
            "day": {"value": [1.2, 1.5, ...], "unit": "kilowattHour"},
            "week": {"value": [8.5, 9.2, ...], "unit": "kilowattHour"},
            "month": {"value": [35.6, 42.3, ...], "unit": "kilowattHour"},
            "year": {"value": [450.2, 520.8, ...], "unit": "kilowattHour"}
        }
    }
    """
    if not feature:
        return {}

    properties = feature.get('properties', {})
    values = {}

    # Extrahiere die aktuellen Werte (erstes Element der Arrays)
    for period in ['day', 'week', 'month', 'year']:
        if period in properties:
            value_array = properties[period].get('value', [])
            if value_array and len(value_array) > 0:
                values[period] = value_array[0]  # Aktueller Wert
                values[f'{period}_unit'] = properties[period].get('unit', 'kilowattHour')

    return values


def print_power_consumption(consumption_data: Dict[str, Any]):
    """Formatierte Ausgabe der Stromverbrauchs-Daten"""

    print(f"\n{'='*80}")
    print(f"⚡ STROMVERBRAUCH WÄRMEPUMPE (ViCare API)")
    print(f"{'='*80}")

    # Warmwasser (DHW)
    if consumption_data['dhw']:
        print("\n🚿 WARMWASSER (Domestic Hot Water):")
        print("-" * 80)
        dhw_values = extract_consumption_values(consumption_data['dhw'])
        if dhw_values:
            print(f"  Heute:       {dhw_values.get('day', 0):.2f} kWh")
            print(f"  Diese Woche: {dhw_values.get('week', 0):.2f} kWh")
            print(f"  Dieser Monat:{dhw_values.get('month', 0):.2f} kWh")
            print(f"  Dieses Jahr: {dhw_values.get('year', 0):.2f} kWh")
        else:
            print("  ⚠️  Keine Daten verfügbar")
    else:
        print("\n🚿 WARMWASSER: ❌ Nicht verfügbar in API")

    # Heizung (Heating)
    if consumption_data['heating']:
        print("\n🔥 HEIZUNG (Space Heating):")
        print("-" * 80)
        heating_values = extract_consumption_values(consumption_data['heating'])
        if heating_values:
            print(f"  Heute:       {heating_values.get('day', 0):.2f} kWh")
            print(f"  Diese Woche: {heating_values.get('week', 0):.2f} kWh")
            print(f"  Dieser Monat:{heating_values.get('month', 0):.2f} kWh")
            print(f"  Dieses Jahr: {heating_values.get('year', 0):.2f} kWh")
        else:
            print("  ⚠️  Keine Daten verfügbar")
    else:
        print("\n🔥 HEIZUNG: ❌ Nicht verfügbar in API")

    # Gesamt (Total)
    if consumption_data['total']:
        print("\n📊 GESAMT (Total):")
        print("-" * 80)
        total_values = extract_consumption_values(consumption_data['total'])
        if total_values:
            print(f"  Heute:       {total_values.get('day', 0):.2f} kWh")
            print(f"  Diese Woche: {total_values.get('week', 0):.2f} kWh")
            print(f"  Dieser Monat:{total_values.get('month', 0):.2f} kWh")
            print(f"  Dieses Jahr: {total_values.get('year', 0):.2f} kWh")
        else:
            print("  ⚠️  Keine Daten verfügbar")
    else:
        print("\n📊 GESAMT: ❌ Nicht verfügbar in API")

    print("\n" + "="*80)


def main():
    """Hauptfunktion zum Testen der ViCare API"""

    print("\n" + "="*80)
    print("VICARE API TESTER - Power Consumption Data Points")
    print("="*80)
    print("Ziel: Stromverbrauch der Wärmepumpe für Home Assistant abrufen")
    print("="*80 + "\n")

    api = ViCareAPI()

    if not api.access_token:
        print("⏭️  Tests übersprungen (kein Access Token)")
        print("\n" + "="*80)
        print("📝 SO HOLST DU DEN ACCESS TOKEN AUS HOME ASSISTANT:")
        print("="*80)
        print("""
1. Öffne Home Assistant
2. Gehe zu: Entwicklerwerkzeuge → Zustände
3. Suche nach: "vicare"
4. Klicke auf eine Entität (z.B. sensor.vicare_heating_burner_active)
5. Scrolle zu "Attributes"
6. Kopiere den "access_token" Wert

ODER:

1. SSH in Home Assistant
2. cat /config/.storage/core.config_entries
3. Suche nach "vicare"
4. Kopiere den "access_token"

ODER:

Nutze den OAuth2 Flow (siehe ViCare API Dokumentation)
        """)
        print("="*80 + "\n")

        # Demo-Daten zeigen
        print("📝 DEMO: So würden die Daten aussehen:")
        print("-" * 80)
        demo_data = {
            'dhw': {
                'feature': 'heating.power.consumption.dhw',
                'properties': {
                    'day': {'value': [2.3], 'unit': 'kilowattHour'},
                    'week': {'value': [18.5], 'unit': 'kilowattHour'},
                    'month': {'value': [75.2], 'unit': 'kilowattHour'},
                    'year': {'value': [850.6], 'unit': 'kilowattHour'}
                }
            },
            'heating': {
                'feature': 'heating.power.consumption.heating',
                'properties': {
                    'day': {'value': [12.8], 'unit': 'kilowattHour'},
                    'week': {'value': [95.3], 'unit': 'kilowattHour'},
                    'month': {'value': [385.7], 'unit': 'kilowattHour'},
                    'year': {'value': [3250.4], 'unit': 'kilowattHour'}
                }
            },
            'total': {
                'feature': 'heating.power.consumption.total',
                'properties': {
                    'day': {'value': [15.1], 'unit': 'kilowattHour'},
                    'week': {'value': [113.8], 'unit': 'kilowattHour'},
                    'month': {'value': [460.9], 'unit': 'kilowattHour'},
                    'year': {'value': [4101.0], 'unit': 'kilowattHour'}
                }
            }
        }
        print_power_consumption(demo_data)
        return

    # Mit Token: Echte Daten abrufen
    try:
        print("[TEST 1] Installationen abrufen...")
        installations = api.get_installations()

        if not installations:
            print("❌ Keine Installationen gefunden")
            return

        installation = installations[0]
        installation_id = installation['id']
        print(f"✅ Installation gefunden: ID {installation_id}")

        print(f"\n[TEST 2] Gateways abrufen...")
        gateways = api.get_gateways(installation_id)

        if not gateways:
            print("❌ Keine Gateways gefunden")
            return

        gateway = gateways[0]
        gateway_serial = gateway['serial']
        print(f"✅ Gateway gefunden: {gateway_serial}")

        print(f"\n[TEST 3] Geräte abrufen...")
        devices = api.get_devices(installation_id, gateway_serial)

        if not devices:
            print("❌ Keine Geräte gefunden")
            return

        device = devices[0]
        device_id = device['id']
        print(f"✅ Gerät gefunden: {device_id}")
        print(f"   Typ: {device.get('deviceType', 'Unknown')}")

        print(f"\n[TEST 4] Stromverbrauchs-Daten abrufen...")
        consumption = api.get_power_consumption(installation_id, gateway_serial, device_id)

        print_power_consumption(consumption)

        print("\n✅ ALLE TESTS ERFOLGREICH!")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("❌ Fehler: Ungültiger Access Token oder abgelaufen")
            print("   Hole neuen Token aus Home Assistant (siehe oben)")
        elif e.response.status_code == 429:
            print("❌ Fehler: Rate Limit erreicht")
            print("   ViCare API hat strikte Limits!")
            print("   Warte 24h oder upgraden auf Advanced Tier (19,99€/Monat)")
        else:
            print(f"❌ HTTP Fehler: {e}")
            print(f"   Response: {e.response.text if e.response else 'N/A'}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

    # Zusammenfassung
    print("\n\n" + "="*80)
    print("📊 WICHTIGE ERKENNTNISSE")
    print("="*80)
    print("""
1. ❌ STANDARD HOME ASSISTANT INTEGRATION ZEIGT DIESE DATEN NICHT
   - GitHub Issue #155695 ist noch OFFEN
   - Die Datenpunkte existieren in der API, sind aber nicht implementiert

2. ⚠️  BEKANNTE PROBLEME MIT DIESEN DATENPUNKTEN:
   - Werte "frieren" manchmal ein (werden nicht täglich aktualisiert)
   - Seit November 2024 bessere Stabilität
   - Manche Geräte zeigen diese Datenpunkte nicht (z.B. 300G mit VitoconnectOPTO2)

3. 💰 PAYWALL BEI VICARE APP
   - Diese Daten sind in der ViCare App nur mit "Plus" verfügbar (3,99€/Monat)
   - API "Basic" Tier sollte sie aber zeigen (kostenlos)
   - "Advanced" API Tier (19,99€/Monat) hat mehr Datenpunkte

4. ✅ WORKAROUND FÜR HOME ASSISTANT:
   - Nutze RESTful Sensor mit diesem Script
   - Oder warte auf HA Integration Update (Issue #155695)
   - Oder nutze gridX API (zeigt Echtzeit-Leistung statt kumulierte Werte)

5. 🔄 ALTERNATIVE: gridX API
   - Zeigt Echtzeit-Leistungsaufnahme (W) statt kumulierte Werte (kWh)
   - Keine Rate-Limits
   - Vollständiger als ViCare für Energie-Monitoring
""")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
