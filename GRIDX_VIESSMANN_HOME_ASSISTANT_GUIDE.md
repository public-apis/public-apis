# gridX + Viessmann Integration in Home Assistant

Kompletter Guide für die Integration von **Viessmann Vitocal Wärmepumpe** und **Vitocharge Wechselrichter** über **E.ON gridX** in **Home Assistant**.

## 🎯 Dein Setup

- **Gridbox**: E.ON gridX (https://eon.gridx.de)
- **Wechselrichter**: Viessmann Vitocharge VX3
- **Wärmepumpe**: Viessmann Vitocal
- **Ziel**: Daten in Home Assistant abrufen

---

## ⚠️ Das Problem

Die **public-apis** Sammlung enthält **KEINE** spezifischen Einträge für:
- ❌ gridX / E.ON gridX
- ❌ Viessmann ViCare API
- ❌ Viessmann Vitocharge
- ❌ Viessmann Vitocal

**ABER:** Diese APIs existieren dennoch! Sie sind nur nicht in der Sammlung gelistet.

---

## ✅ Verfügbare Lösungen

### Option 1: gridX API (🥇 BESTE LÖSUNG)

Die gridX API ist deine beste Option, da:
- ✅ Alle Daten von Vitocal **UND** Vitocharge verfügbar sind
- ✅ Echtzeit-Daten und historische Zeitreihen
- ✅ Vollständige Energieflüsse (PV, Wärmepumpe, Netz, Verbrauch)
- ✅ Keine Rate-Limits wie bei ViCare

#### API Endpoints

```bash
# Live-Daten
GET https://api.gridx.de/systems/{system-id}/live

# Zeitreihen (historisch)
GET https://api.gridx.de/systems/{system-id}/timeseries

# System-Info
GET https://api.gridx.de/systems/{system-id}
```

#### Authentifizierung

**Bearer Token aus Browser holen:**

1. Öffne https://eon.gridx.de und logge dich ein
2. Öffne Browser Developer Tools (F12)
3. Gehe zum **Network** Tab
4. Aktualisiere die Seite (F5)
5. Suche nach Requests an `api.gridx.de`
6. Klicke auf einen Request
7. Gehe zu **Headers**
8. Kopiere den `Authorization` Header
   - Format: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ...`
9. Kopiere auch deine **System ID** aus der URL
   - Format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

**WICHTIG:** Der Bearer Token läuft nach einiger Zeit ab und muss erneuert werden!

#### Home Assistant Integration

**Methode 1: RESTful Sensor (Einfach)**

Füge zu deiner `configuration.yaml` hinzu:

```yaml
# configuration.yaml

sensor:
  # PV-Anlage (Vitocharge)
  - platform: rest
    name: "PV Aktuelle Leistung"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.pv.power | float / 1000 }}"
    unit_of_measurement: "kW"
    device_class: power

  - platform: rest
    name: "PV Heutige Erzeugung"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.pv.energy_today | float }}"
    unit_of_measurement: "kWh"
    device_class: energy

  # Wärmepumpe (Vitocal)
  - platform: rest
    name: "Wärmepumpe Leistung"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.heatpump.power | float / 1000 }}"
    unit_of_measurement: "kW"
    device_class: power

  - platform: rest
    name: "Wärmepumpe Status"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.heatpump.status }}"

  - platform: rest
    name: "Außentemperatur"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.heatpump.outdoor_temperature | float }}"
    unit_of_measurement: "°C"
    device_class: temperature

  - platform: rest
    name: "Wärmepumpe COP"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.heatpump.cop | float }}"

  # Netz
  - platform: rest
    name: "Netz Leistung"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.grid.power | float / 1000 }}"
    unit_of_measurement: "kW"
    device_class: power

  # Hausverbrauch
  - platform: rest
    name: "Hausverbrauch"
    resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    value_template: "{{ value_json.consumption.power | float / 1000 }}"
    unit_of_measurement: "kW"
    device_class: power
```

**Methode 2: Template Sensor mit einem API Call**

Effizienter - nur ein API Call für alle Sensoren:

```yaml
# configuration.yaml

rest:
  - resource: "https://api.gridx.de/systems/DEINE-SYSTEM-ID/live"
    headers:
      Authorization: "Bearer DEIN-BEARER-TOKEN"
    scan_interval: 60  # Alle 60 Sekunden aktualisieren
    sensor:
      - name: "gridX Live Data"
        value_template: "{{ value_json.timestamp }}"
        json_attributes:
          - pv
          - heatpump
          - grid
          - consumption
          - battery

template:
  - sensor:
      # PV Sensoren
      - name: "PV Leistung"
        unit_of_measurement: "kW"
        device_class: power
        state: >
          {{ state_attr('sensor.gridx_live_data', 'pv').power | float / 1000 }}

      - name: "PV Heute"
        unit_of_measurement: "kWh"
        device_class: energy
        state: >
          {{ state_attr('sensor.gridx_live_data', 'pv').energy_today | float }}

      # Wärmepumpen Sensoren
      - name: "Wärmepumpe Leistung"
        unit_of_measurement: "kW"
        device_class: power
        state: >
          {{ state_attr('sensor.gridx_live_data', 'heatpump').power | float / 1000 }}

      - name: "Wärmepumpe Außentemperatur"
        unit_of_measurement: "°C"
        device_class: temperature
        state: >
          {{ state_attr('sensor.gridx_live_data', 'heatpump').outdoor_temperature | float }}

      - name: "Wärmepumpe COP"
        state: >
          {{ state_attr('sensor.gridx_live_data', 'heatpump').cop | float }}
```

**Vorteile:**
- Nur 1 API-Call alle 60 Sekunden
- Alle Sensoren werden gleichzeitig aktualisiert
- Weniger Last auf die API

---

### Option 2: HACS Community Integration

Es gibt eine **HACS-Integration** speziell für gridX (1komma5grad Heartbeat):

**Repository:** https://github.com/BirknerAlex/hacs_1komma5grad

#### Installation

1. **HACS installieren** (falls noch nicht vorhanden)
   - https://hacs.xyz/docs/setup/download

2. **Integration hinzufügen:**
   ```
   HACS → Integrationen → ⋮ (Menü) → Custom repositories
   URL: https://github.com/BirknerAlex/hacs_1komma5grad
   Kategorie: Integration
   ```

3. **Integration installieren:**
   - Suche nach "1komma5grad"
   - Klicke auf Download

4. **Home Assistant neu starten**

5. **Integration konfigurieren:**
   - Einstellungen → Geräte & Dienste → Integration hinzufügen
   - Suche "1komma5grad"
   - Gib deine E.ON gridX Zugangsdaten ein

#### Vorteile
- ✅ Automatische Token-Erneuerung
- ✅ Einfache Einrichtung
- ✅ Alle Entitäten automatisch erstellt

#### Nachteile
- ⚠️ Neue API nicht in allen Regionen verfügbar
- ⚠️ Abhängig von Community-Maintenance

---

### Option 3: Viessmann ViCare API (❌ NICHT EMPFOHLEN FÜR DICH)

Home Assistant hat eine **offizielle ViCare Integration**, aber:

#### Probleme mit ViCare:

1. **Vitocharge fehlt oft**
   - Vitocharge VX3 wird häufig nicht angezeigt
   - Siehe: https://github.com/home-assistant/core/issues/122299

2. **Rate Limiting**
   - Kostenloser "Basic" Tier blockt dich für 24h bei Überschreitung
   - Siehe: https://community.home-assistant.io/t/vicare-no-data-from-vitocal-and-vitocharge/945835

3. **Unvollständige Daten**
   - Nicht alle Vitocharge-Entitäten verfügbar
   - PV-Produktionsdaten fehlen oft

4. **Probleme seit Januar 2025**
   - Viele Nutzer berichten, dass seit 01.01.2025 keine Daten mehr kommen

#### Wenn du es trotzdem versuchen willst:

**Installation:**
1. Einstellungen → Geräte & Dienste
2. Integration hinzufügen
3. Suche "Viessmann ViCare"
4. Folge dem OAuth2-Flow

**Dokumentation:**
- Home Assistant: https://www.home-assistant.io/integrations/vicare/
- API Docs: https://developer.viessmann.com/

---

## 📊 Vergleich der Optionen

| Feature | gridX API | HACS gridX | ViCare API |
|---------|-----------|------------|------------|
| **Vitocharge Daten** | ✅ Vollständig | ✅ Vollständig | ❌ Oft nicht verfügbar |
| **Vitocal Daten** | ✅ Vollständig | ✅ Vollständig | ✅ Teilweise |
| **PV-Produktion** | ✅ Ja | ✅ Ja | ❌ Oft nicht |
| **Echtzeit-Daten** | ✅ Ja | ✅ Ja | ⚠️ Verzögert |
| **Rate Limits** | ✅ Keine | ✅ Keine | ❌ Streng (24h Block) |
| **Token-Management** | ❌ Manuell | ✅ Automatisch | ✅ Automatisch |
| **Einrichtung** | ⚠️ Mittel | ✅ Einfach | ✅ Einfach |
| **Zuverlässigkeit** | ✅ Hoch | ✅ Hoch | ❌ Problematisch |
| **Energieflüsse** | ✅ Komplett | ✅ Komplett | ⚠️ Begrenzt |

---

## 🔧 Troubleshooting

### Problem: Bearer Token läuft ab

**Symptom:** API liefert 401 Unauthorized

**Lösung:**
1. Neuen Token aus Browser holen (siehe oben)
2. In `secrets.yaml` oder direkt in Config aktualisieren
3. Home Assistant neu laden (Entwicklerwerkzeuge → YAML → Alle YAML-Konfiguration neu laden)

**Langfristige Lösung:**
- HACS Integration nutzen (automatische Token-Erneuerung)
- Oder: OAuth2 Flow selbst implementieren

### Problem: Keine Daten von Vitocharge in ViCare

**Symptom:** Wärmepumpe wird angezeigt, aber kein Wechselrichter

**Grund:** ViCare API gibt Vitocharge-Daten nicht immer frei

**Lösung:** Nutze gridX API stattdessen

### Problem: Rate Limit bei ViCare

**Symptom:** 24h Sperre nach zu vielen Requests

**Grund:** ViCare "Basic" Tier ist sehr restriktiv

**Lösung:**
1. Scan Interval erhöhen (z.B. 300 Sekunden statt 60)
2. Oder: gridX API nutzen (keine Limits)

### Problem: System ID nicht bekannt

**Lösung:**
1. Login auf https://eon.gridx.de
2. URL ansehen - System ID ist im Pfad: `/systems/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`
3. Oder: Browser DevTools → Network → Suche nach `api.gridx.de` → System ID in URL

---

## 🎨 Dashboard-Beispiel

Beispiel für eine Energy Dashboard Karte:

```yaml
type: vertical-stack
cards:
  - type: entities
    title: PV-Anlage (Vitocharge)
    entities:
      - entity: sensor.pv_leistung
        name: Aktuelle Leistung
      - entity: sensor.pv_heute
        name: Heute erzeugt
      - type: divider
      - entity: sensor.hausverbrauch
        name: Hausverbrauch
      - entity: sensor.netz_leistung
        name: Netz (+ Bezug / - Einspeisung)

  - type: entities
    title: Wärmepumpe (Vitocal)
    entities:
      - entity: sensor.warmepumpe_status
        name: Status
      - entity: sensor.warmepumpe_leistung
        name: Leistung
      - entity: sensor.warmepumpe_cop
        name: COP (Effizienz)
      - entity: sensor.aussentemperatur
        name: Außentemperatur

  - type: gauge
    entity: sensor.warmepumpe_cop
    name: COP
    min: 0
    max: 5
    needle: true
    severity:
      green: 3
      yellow: 2
      red: 0
```

---

## 📚 Ressourcen & Links

### gridX API
- **Developer Community:** https://community.developer.gridx.de/
- **API Documentation:** https://community.developer.gridx.de/c/api-docs/15
- **Developer Portal:** https://developer.gridx.ai/
- **E.ON gridX Success Story:** https://www.gridx.ai/success-stories/e-on-energie-deutschland

### HACS Integration
- **GitHub Repository:** https://github.com/BirknerAlex/hacs_1komma5grad
- **Alternative (Legacy):** https://github.com/derlangemarkus/1komma5grad_ha

### Viessmann ViCare
- **Home Assistant Integration:** https://www.home-assistant.io/integrations/vicare/
- **Developer Portal:** https://developer.viessmann.com/
- **Community Forum:** https://community.viessmann.de/t5/The-Viessmann-API/bd-p/dev-viessmann-api

### Home Assistant Community
- **ViCare + Vitocharge Issues:** https://community.home-assistant.io/t/viessmann-vicare-integration-vitocharge-vx3-not-visible/848635
- **No Data Issues:** https://community.home-assistant.io/t/vicare-no-data-from-vitocal-and-vitocharge/945835

### GitHub Issues
- **Missing Vitocharge Entities:** https://github.com/home-assistant/core/issues/122299
- **Hybrid System Issues:** https://github.com/home-assistant/core/issues/103009

---

## 💡 Zusammenfassung & Empfehlung

**Für dein Setup (E.ON gridX + Vitocal + Vitocharge) empfehle ich:**

### 🥇 Beste Lösung: HACS Integration + gridX API

1. **Installiere die HACS Integration** (BirknerAlex/hacs_1komma5grad)
   - Automatische Token-Verwaltung
   - Alle Sensoren werden automatisch erstellt

2. **Falls HACS nicht funktioniert:** RESTful Sensor mit Bearer Token
   - Mehr manuelle Arbeit
   - Token muss regelmäßig erneuert werden
   - Aber vollständige Kontrolle über Sensoren

### ❌ Vermeide: ViCare API allein

- Vitocharge-Daten fehlen oft
- Rate Limiting ist problematisch
- Weniger zuverlässig als gridX

### ✅ Optimale Kombination (Optional)

Nutze **beide** APIs gleichzeitig:
- **gridX API** für Vitocharge (PV) + Energieflüsse
- **ViCare API** für erweiterte Wärmepumpen-Einstellungen (Solltemperaturen, Modi, etc.)

So bekommst du das Beste aus beiden Welten!

---

## ❓ Fragen?

Falls du Probleme bei der Einrichtung hast:

1. **Home Assistant Community:** https://community.home-assistant.io/
2. **gridX Developer Community:** https://community.developer.gridx.de/
3. **Viessmann Community:** https://community.viessmann.de/

---

**Viel Erfolg bei der Integration! 🚀**
