# ViCare API - Fehlende Stromverbrauchs-Sensoren in Home Assistant

Kompletter Guide zum Hinzufügen der **fehlenden Stromverbrauchs-Datenpunkte** zur Home Assistant ViCare Integration.

## 🎯 Das Problem

Du hast die **offizielle Home Assistant ViCare Integration** bereits laufen, aber der **Stromverbrauch der Wärmepumpe** wird **NICHT angezeigt**.

### Warum fehlt dieser Sensor?

Die Datenpunkte existieren in der ViCare API, sind aber **nicht in der Home Assistant Integration implementiert**:

- ❌ `heating.power.consumption.dhw` (Warmwasser)
- ❌ `heating.power.consumption.heating` (Heizung)
- ❌ `heating.power.consumption.total` (Gesamt)

**Status:** GitHub Issue #155695 ist **OFFEN** (reopened im November 2025)
- **Link:** https://github.com/home-assistant/core/issues/155695
- **Code Owner (Christopher Fenner)** hat Interesse an Implementierung signalisiert
- **Noch nicht gemerged** - warte auf Update

---

## ✅ Die Lösung: Custom RESTful Sensor

Da die Standard-Integration diese Sensoren nicht hat, musst du sie **manuell hinzufügen**.

### Option 1: RESTful Command Sensor (Einfach, aber begrenzt)

**Problem:** Die ViCare API benötigt OAuth2 Token, der aus der bestehenden Integration kommt.

### Option 2: Python Script + MQTT (Fortgeschritten)

Das Python-Script `test_vicare_power_consumption.py` kannst du nutzen, um:
1. Daten aus ViCare API zu holen
2. An Home Assistant MQTT zu senden
3. Als Cronjob oder Automation laufen zu lassen

### Option 3: Custom Component Fork (Am besten)

Füge die Sensoren zur ViCare Integration hinzu, bis das offizielle Update kommt.

---

## 🔧 Praktische Lösung: Custom Sensor Template

Da du bereits die **ViCare Integration laufen hast**, kannst du versuchen, die fehlenden Datenpunkte über eine **Custom Component** zu ergänzen.

### Schritt 1: Prüfe welche Sensoren du hast

```bash
# In Home Assistant: Entwicklerwerkzeuge → Zustände
# Suche nach "vicare"
```

Typische Sensoren:
- ✅ `sensor.vicare_outside_temperature` (Außentemperatur)
- ✅ `sensor.vicare_supply_temperature` (Vorlauftemperatur)
- ✅ `sensor.vicare_heating_burner_hours` (Betriebsstunden)
- ❌ `sensor.vicare_power_consumption` (FEHLT!)

### Schritt 2: Access Token extrahieren

Der Access Token ist in der bestehenden Integration gespeichert:

```bash
# Methode 1: Via SSH
cat /config/.storage/core.config_entries | grep -A 20 "vicare"

# Methode 2: Via UI
# Entwicklerwerkzeuge → Zustände → Beliebige ViCare Entität
# → Attribute → access_token (wenn sichtbar)
```

### Schritt 3: RESTful Sensor hinzufügen

**WICHTIG:** Dies ist ein Workaround, bis die offizielle Integration aktualisiert wird!

Füge zu deiner `configuration.yaml` hinzu:

```yaml
# configuration.yaml

# OPTION A: Einfache Methode (funktioniert nur wenn Token als secret gespeichert)
# Nachteil: Token läuft ab und muss manuell erneuert werden

rest:
  - resource: "https://api.viessmann.com/iot/v1/equipment/installations/YOUR_INSTALLATION_ID/gateways/YOUR_GATEWAY_SERIAL/devices/YOUR_DEVICE_ID/features"
    headers:
      Authorization: "Bearer YOUR_ACCESS_TOKEN"
    scan_interval: 3600  # Nur alle 60 Minuten! (Rate Limit!)
    sensor:
      - name: "ViCare Power Consumption Raw"
        value_template: "OK"
        json_attributes_path: "$.data[?(@.feature == 'heating.power.consumption.total')]"
        json_attributes:
          - properties

# Template Sensoren für die Werte
template:
  - sensor:
      - name: "Wärmepumpe Stromverbrauch Heute"
        unique_id: vicare_power_consumption_today
        unit_of_measurement: "kWh"
        device_class: energy
        state_class: total_increasing
        state: >
          {% set data = state_attr('sensor.vicare_power_consumption_raw', 'properties') %}
          {% if data and data.day and data.day.value %}
            {{ data.day.value[0] | float }}
          {% else %}
            unavailable
          {% endif %}

      - name: "Wärmepumpe Stromverbrauch Woche"
        unique_id: vicare_power_consumption_week
        unit_of_measurement: "kWh"
        device_class: energy
        state: >
          {% set data = state_attr('sensor.vicare_power_consumption_raw', 'properties') %}
          {% if data and data.week and data.week.value %}
            {{ data.week.value[0] | float }}
          {% else %}
            unavailable
          {% endif %}

      - name: "Wärmepumpe Stromverbrauch Monat"
        unique_id: vicare_power_consumption_month
        unit_of_measurement: "kWh"
        device_class: energy
        state: >
          {% set data = state_attr('sensor.vicare_power_consumption_raw', 'properties') %}
          {% if data and data.month and data.month.value %}
            {{ data.month.value[0] | float }}
          {% else %}
            unavailable
          {% endif %}

      - name: "Wärmepumpe Stromverbrauch Jahr"
        unique_id: vicare_power_consumption_year
        unit_of_measurement: "kWh"
        device_class: energy
        state_class: total_increasing
        state: >
          {% set data = state_attr('sensor.vicare_power_consumption_raw', 'properties') %}
          {% if data and data.year and data.year.value %}
            {{ data.year.value[0] | float }}
          {% else %}
            unavailable
          {% endif %}
```

### Schritt 4: IDs herausfinden

Du brauchst:
- `YOUR_INSTALLATION_ID` (Zahl, z.B. 12345678)
- `YOUR_GATEWAY_SERIAL` (Seriennummer, z.B. 7571234567890123)
- `YOUR_DEVICE_ID` (Device ID, z.B. 0)

**So findest du sie:**

```python
# Nutze das test_vicare_power_consumption.py Script:
export VICARE_ACCESS_TOKEN="dein_token_hier"
python3 test_vicare_power_consumption.py

# Ausgabe zeigt:
# Installation ID: 12345678
# Gateway Serial: 7571234567890123
# Device ID: 0
```

**Oder manuell via API:**

```bash
# 1. Installations abrufen
curl -X GET "https://api.viessmann.com/iot/v1/equipment/installations" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Antwort enthält: installations[0].id

# 2. Gateways abrufen
curl -X GET "https://api.viessmann.com/iot/v1/equipment/installations/INSTALLATION_ID/gateways" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Antwort enthält: gateways[0].serial

# 3. Devices abrufen
curl -X GET "https://api.viessmann.com/iot/v1/equipment/installations/INSTALLATION_ID/gateways/GATEWAY_SERIAL/devices" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Antwort enthält: devices[0].id (meist "0")
```

---

## ⚠️ Bekannte Probleme & Einschränkungen

### 1. Rate Limiting

Die ViCare API ist **extrem rate-limited**:

| Tier | Requests | Kosten |
|------|----------|--------|
| **Basic** | Sehr begrenzt | Kostenlos |
| **Advanced** | Mehr Requests | **19,99€/Monat** |

**Symptom:** HTTP 429 Error → 24h gesperrt

**Lösung:**
- `scan_interval: 3600` (nur alle 60 Minuten)
- Oder gridX API nutzen (keine Limits)

### 2. Daten "frieren ein"

**Problem:** Die Werte von `heating.power.consumption.*` aktualisieren sich manchmal nicht täglich.

**Häufigkeit:** War bis November 2024 ein großes Problem, seitdem besser

**Workaround:**
- Reboot des Communication Modules in ViCare App
- Warten auf automatische Aktualisierung
- gridX API nutzt Echtzeit-Daten (kein Problem)

### 3. Access Token läuft ab

Der OAuth2 Token ist nicht permanent.

**Lösung:** Die Home Assistant ViCare Integration **erneuert den Token automatisch**. Wenn du den Token manuell nutzt (RESTful Sensor), musst du:
1. Regelmäßig neuen Token aus Integration holen
2. Oder Custom Component erstellen die Token-Refresh macht

### 4. Nicht alle Geräte unterstützen diese Datenpunkte

**Betroffen:** z.B. Viessmann 300G mit VitoconnectOPTO2

**Symptom:** API gibt diese Features nicht zurück

**Lösung:** Prüfe mit `test_vicare_power_consumption.py` ob deine Anlage die Datenpunkte hat

### 5. Paywall in ViCare App

Die **ViCare App** zeigt diese Daten nur mit **Plus Abo** (3,99€/Monat).

**ABER:** Die API sollte sie auch im **Basic Tier** zeigen!

---

## 🆚 Vergleich: ViCare API vs. gridX API

| Feature | ViCare API | gridX API |
|---------|-----------|-----------|
| **Stromverbrauch WP** | ✅ kumuliert (Tag/Woche/Monat/Jahr) | ✅ Echtzeit (W) |
| **In HA Integration** | ❌ Fehlt (Issue #155695) | ❌ Keine offizielle Integration |
| **Rate Limits** | ❌ Streng (24h Block möglich) | ✅ Keine bekannt |
| **Datenaktualität** | ⚠️ Friert manchmal ein | ✅ Echtzeit |
| **PV-Produktion (Vitocharge)** | ❌ Oft nicht verfügbar | ✅ Vollständig |
| **Setup-Aufwand** | ✅ Integration vorhanden | ⚠️ Manuell (Bearer Token) |
| **Token-Management** | ✅ Automatisch | ❌ Manuell (läuft ab) |
| **Kosten** | ✅ Kostenlos (Basic) / 19,99€ (Advanced) | ✅ Kostenlos |
| **Energy Dashboard** | ✅ Ja (wenn implementiert) | ⚠️ Manuell konfigurieren |

### Empfehlung:

**Für Stromverbrauch (kumuliert):**
- Versuche ViCare API Custom Sensor
- Falls Rate Limits / Freezing Probleme → gridX

**Für Echtzeit-Leistung (W):**
- gridX API ist besser
- Zeigt auch PV-Produktion von Vitocharge

**Ideal: Beide kombinieren!**
- ViCare: Für Temperaturen, Modi, Sollwerte
- gridX: Für Energieflüsse, Leistung, PV

---

## 📊 Energy Dashboard Konfiguration

Sobald du den Sensor hast, füge ihn zum Energy Dashboard hinzu:

```yaml
# Einstellungen → Dashboards → Energy

# Stromverbrauch (Individual Device)
- sensor.warmepumpe_stromverbrauch_heute
  oder
- sensor.warmepumpe_stromverbrauch_jahr
```

**WICHTIG:** Für das Energy Dashboard brauchst du:
- `state_class: total_increasing` (kumulierter Wert)
- `device_class: energy`
- `unit_of_measurement: kWh`

Das **Jahres-Sensor** eignet sich am besten, da es kontinuierlich steigt.

---

## 🔄 Alternative: Python Script + MQTT

Falls die RESTful Sensor Methode nicht funktioniert, kannst du ein **Python-Script als Cronjob** laufen lassen:

### Schritt 1: Script anpassen

```python
# vicare_mqtt_bridge.py

import os
from test_vicare_power_consumption import ViCareAPI, extract_consumption_values
import paho.mqtt.client as mqtt

# ViCare API Setup
api = ViCareAPI(access_token=os.getenv('VICARE_ACCESS_TOKEN'))

# MQTT Setup
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("homeassistant", "your_password")
mqtt_client.connect("localhost", 1883)

# Daten abrufen
installation_id = 12345678  # Deine ID
gateway_serial = "7571234567890123"  # Deine Serial
device_id = "0"

consumption = api.get_power_consumption(installation_id, gateway_serial, device_id)
total_values = extract_consumption_values(consumption['total'])

# An MQTT publishen
if total_values:
    mqtt_client.publish("homeassistant/sensor/vicare_power_today/state", total_values['day'])
    mqtt_client.publish("homeassistant/sensor/vicare_power_week/state", total_values['week'])
    mqtt_client.publish("homeassistant/sensor/vicare_power_month/state", total_values['month'])
    mqtt_client.publish("homeassistant/sensor/vicare_power_year/state", total_values['year'])

mqtt_client.disconnect()
```

### Schritt 2: Cronjob einrichten

```bash
# Alle 60 Minuten ausführen
0 * * * * cd /home/user/scripts && python3 vicare_mqtt_bridge.py
```

### Schritt 3: MQTT Sensoren in HA

```yaml
# configuration.yaml

mqtt:
  sensor:
    - name: "Wärmepumpe Stromverbrauch Heute"
      state_topic: "homeassistant/sensor/vicare_power_today/state"
      unit_of_measurement: "kWh"
      device_class: energy

    - name: "Wärmepumpe Stromverbrauch Jahr"
      state_topic: "homeassistant/sensor/vicare_power_year/state"
      unit_of_measurement: "kWh"
      device_class: energy
      state_class: total_increasing
```

---

## 🚀 Nächste Schritte

### Kurzfristig (Sofort nutzbar):

1. ✅ **gridX API nutzen** für Echtzeit-Leistung (W)
   - Siehe `GRIDX_VIESSMANN_HOME_ASSISTANT_GUIDE.md`
   - Zeigt auch Vitocharge PV-Daten!

2. ⚠️ **ViCare Custom Sensor** versuchen (falls kumulierte Werte wichtig)
   - Befolge Anleitung oben
   - Achtung: Rate Limits!

### Mittelfristig (Warten):

3. 👀 **GitHub Issue #155695 beobachten**
   - https://github.com/home-assistant/core/issues/155695
   - Wenn gemerged → automatisch in HA verfügbar

### Langfristig (Optimal):

4. ✅ **Beide APIs kombinieren:**
   - ViCare: Temperaturen, Modi, Betriebsdaten
   - gridX: Energieflüsse, Leistung, PV-Produktion

---

## 📚 Ressourcen & Links

### ViCare API
- **Developer Portal:** https://app.developer.viessmann-climatesolutions.com/
- **API Documentation:** https://api.viessmann-climatesolutions.com/documentation/data-points
- **Community Forum:** https://community.viessmann.de/t5/The-Viessmann-API/bd-p/dev-viessmann-api

### Home Assistant
- **ViCare Integration:** https://www.home-assistant.io/integrations/vicare/
- **GitHub Issue #155695:** https://github.com/home-assistant/core/issues/155695
- **Issue #99468 (Heatpump Power):** https://github.com/home-assistant/core/issues/99468

### Community Discussions
- **Power Consumption Request:** https://community.home-assistant.io/t/viessmann-vicare-power-consumption-heat-pump/525184
- **Energy Consumption 300G:** https://community.viessmann.de/t5/The-Viessmann-API/Energy-consumption-for-Viessmann-heat-pump-300G/td-p/289425

### gridX Alternative
- **gridX Guide:** `GRIDX_VIESSMANN_HOME_ASSISTANT_GUIDE.md`
- **gridX Test Script:** `test_gridx_viessmann_api.py`

---

## ❓ FAQ

**Q: Warum zeigt die Standard-Integration den Stromverbrauch nicht?**
A: Die Datenpunkte sind nicht implementiert. GitHub Issue #155695 ist offen, aber noch nicht gemerged.

**Q: Sind diese Daten kostenpflichtig?**
A: In der ViCare App ja (Plus: 3,99€/Monat). Die API sollte sie aber auch im Basic Tier zeigen.

**Q: Funktioniert das mit allen Viessmann Wärmepumpen?**
A: Nein, manche Geräte (z.B. 300G mit VitoconnectOPTO2) zeigen diese Datenpunkte nicht.

**Q: Warum frieren die Werte manchmal ein?**
A: Bekanntes Problem der API. Seit November 2024 besser, aber nicht perfekt. gridX API hat dieses Problem nicht.

**Q: Kann ich Echtzeit-Leistung (W) statt kumulierte Werte (kWh) sehen?**
A: Nicht mit ViCare API. Nutze **gridX API** für Echtzeit-Daten!

**Q: Soll ich auf das HA Integration Update warten?**
A: Issue ist offen, aber kein ETA. Nutze Workaround oder gridX API.

---

**Viel Erfolg beim Einrichten! 🎉**
