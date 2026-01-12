# API Vergleich: gridX vs. ViCare für Viessmann Vitocal + Vitocharge

Detaillierter Vergleich der beiden APIs für dein Setup (E.ON gridX + Viessmann Vitocal WP + Vitocharge WR) in Home Assistant.

---

## 🎯 Dein Setup

- **Energy Management:** E.ON gridX (https://eon.gridx.de) mit Gridbox
- **Wärmepumpe:** Viessmann Vitocal
- **Wechselrichter:** Viessmann Vitocharge VX3
- **Ziel:** Alle Daten in Home Assistant für Energy Dashboard

---

## 📊 API Vergleich im Detail

### 1. **Datenverfügbarkeit**

| Datenpunkt | gridX API | ViCare API | Wer gewinnt? |
|-----------|-----------|-----------|--------------|
| **PV-Leistung (aktuell)** | ✅ Ja (W) | ❌ Nein | 🥇 gridX |
| **PV-Produktion (kumuliert)** | ✅ Ja (kWh) | ❌ Nein | 🥇 gridX |
| **WP-Leistung (aktuell)** | ✅ Ja (W) | ❌ Nein | 🥇 gridX |
| **WP-Verbrauch (kumuliert)** | ❌ Nein | ✅ Ja (kWh)* | 🥇 ViCare |
| **WP-Temperaturen** | ⚠️ Begrenzt | ✅ Vollständig | 🥇 ViCare |
| **WP-Betriebsmodus** | ⚠️ Status | ✅ Modi + Steuerung | 🥇 ViCare |
| **WP-COP (Effizienz)** | ✅ Ja | ❌ Nein | 🥇 gridX |
| **Netz (Bezug/Einspeisung)** | ✅ Ja | ❌ Nein | 🥇 gridX |
| **Hausverbrauch** | ✅ Ja | ❌ Nein | 🥇 gridX |
| **Batterie (falls vorhanden)** | ✅ Ja | ❌ Nein | 🥇 gridX |

**Legende:**
- ✅ Vollständig verfügbar
- ⚠️ Teilweise verfügbar
- ❌ Nicht verfügbar
- \* = Nicht in Standard HA Integration (siehe Issue #155695)

---

### 2. **Datentyp & Nutzung**

#### gridX API:

**Stärken:**
- ✅ **Echtzeit-Leistung** (W) - perfekt für Live-Monitoring
- ✅ **Energieflüsse** - zeigt woher Strom kommt/geht
- ✅ **Vollständiges PV-Monitoring** (Vitocharge)
- ✅ **Hausverbrauch & Netz** - komplettes Energie-Ökosystem

**Schwächen:**
- ❌ Keine kumulierten Verbrauchswerte (kWh über Zeit)
- ❌ Keine WP-Steuerung (nur Monitoring)
- ❌ Keine detaillierten WP-Temperaturen/Modi

**Best Use Case:**
- Live-Dashboard mit Energieflüssen
- Automatisierungen basierend auf Leistung
- Optimierung des Eigenverbrauchs

#### ViCare API:

**Stärken:**
- ✅ **Kumulierte Verbrauchswerte** (Tag/Woche/Monat/Jahr)
- ✅ **Vollständige WP-Steuerung** (Modi, Solltemperaturen)
- ✅ **Alle Temperaturen** (Vorlauf, Rücklauf, Raum, Außen)
- ✅ **Betriebsdaten** (Betriebsstunden, Zyklen, etc.)

**Schwächen:**
- ❌ **Vitocharge fehlt oft** (PV-Daten nicht verfügbar)
- ❌ **Keine Echtzeit-Leistung** (nur kumulierte Werte)
- ❌ **Rate Limits** (kann 24h sperren)
- ❌ **Daten frieren ein** (Update-Probleme)

**Best Use Case:**
- Energy Dashboard (kumulierte Verbräuche)
- WP-Steuerung & Automatisierungen
- Langzeit-Statistiken

---

### 3. **Home Assistant Integration**

#### gridX API:

| Aspekt | Status | Details |
|--------|--------|---------|
| **Offizielle Integration** | ❌ Nein | Keine HA Integration |
| **Setup-Methode** | RESTful Sensor | Bearer Token aus Browser |
| **Konfiguration** | ⚠️ Mittel | Manuell, aber gut dokumentiert |
| **Token-Management** | ❌ Manuell | Token läuft nach Wochen ab |
| **Update-Häufigkeit** | ✅ Flexibel | 60 Sekunden empfohlen |
| **Zuverlässigkeit** | ✅ Sehr gut | Keine bekannten Ausfälle |

**Code-Beispiel:**
```yaml
rest:
  - resource: "https://api.gridx.de/systems/YOUR-ID/live"
    headers:
      Authorization: "Bearer YOUR-TOKEN"
    scan_interval: 60
```

#### ViCare API:

| Aspekt | Status | Details |
|--------|--------|---------|
| **Offizielle Integration** | ✅ Ja | Eingebaut in HA |
| **Setup-Methode** | UI-Flow | OAuth2, sehr einfach |
| **Konfiguration** | ✅ Einfach | Automatisch |
| **Token-Management** | ✅ Automatisch | Integration kümmert sich darum |
| **Update-Häufigkeit** | ⚠️ Begrenzt | Rate Limits! |
| **Zuverlässigkeit** | ⚠️ Problematisch | Freezing, Vitocharge fehlt |

**Problem:**
```
❌ Stromverbrauch-Sensoren fehlen in Standard-Integration
   GitHub Issue #155695 - noch nicht implementiert
```

---

### 4. **API-Limits & Kosten**

#### gridX API:

| Tier | Requests | Rate Limit | Kosten | Details |
|------|----------|------------|--------|---------|
| **Standard** | Unlimitiert* | Unbekannt | Kostenlos | Via E.ON gridX Zugang |

*Keine bekannten Limits für normale Nutzung (alle 60 Sekunden)

#### ViCare API:

| Tier | Requests | Rate Limit | Kosten | Details |
|------|----------|------------|--------|---------|
| **Basic** | Sehr begrenzt | ??? | Kostenlos | Blockiert bei Überschreitung 24h |
| **Advanced** | 1,450,000/Monat | 120/min | **19,99€/Monat** | Mehr Datenpunkte |

**Realität:**
- ⚠️ Basic Tier kann dich schnell für 24h sperren
- ⚠️ Genaue Limits sind nicht dokumentiert
- ⚠️ HA Integration macht viele Requests → Risiko

---

### 5. **Verfügbare Datenpunkte im Detail**

#### gridX API - Live Data (`/systems/{id}/live`)

**PV-Anlage (Vitocharge):**
```json
{
  "pv": {
    "power": 3500,           // Aktuelle Leistung (W)
    "energy_today": 12.5,    // Heutige Produktion (kWh)
    "energy_total": 8450.2   // Gesamt-Produktion (kWh)
  }
}
```

**Wärmepumpe (Vitocal):**
```json
{
  "heatpump": {
    "status": "heating",                // Status
    "power": 850,                       // Leistungsaufnahme (W)
    "flow_temperature": 35.2,           // Vorlauftemperatur (°C)
    "return_temperature": 30.1,         // Rücklauftemperatur (°C)
    "outdoor_temperature": -2.5,        // Außentemperatur (°C)
    "cop": 3.8                          // COP (Effizienz)
  }
}
```

**Energieflüsse:**
```json
{
  "grid": {
    "power": -2100,          // Netz (W, + = Bezug, - = Einspeisung)
    "import_today": 5.2,     // Heutiger Bezug (kWh)
    "export_today": 8.3      // Heutige Einspeisung (kWh)
  },
  "consumption": {
    "power": 1400,           // Hausverbrauch (W)
    "energy_today": 18.5     // Heutiger Verbrauch (kWh)
  }
}
```

#### ViCare API - Power Consumption

**Stromverbrauch Wärmepumpe:**
```json
{
  "heating.power.consumption.dhw": {      // Warmwasser
    "properties": {
      "day": {"value": [2.3], "unit": "kilowattHour"},
      "week": {"value": [18.5], "unit": "kilowattHour"},
      "month": {"value": [75.2], "unit": "kilowattHour"},
      "year": {"value": [850.6], "unit": "kilowattHour"}
    }
  },
  "heating.power.consumption.heating": {  // Heizung
    "properties": {
      "day": {"value": [12.8], "unit": "kilowattHour"},
      "week": {"value": [95.3], "unit": "kilowattHour"},
      "month": {"value": [385.7], "unit": "kilowattHour"},
      "year": {"value": [3250.4], "unit": "kilowattHour"}
    }
  },
  "heating.power.consumption.total": {    // Gesamt
    "properties": {
      "day": {"value": [15.1], "unit": "kilowattHour"},
      "year": {"value": [4101.0], "unit": "kilowattHour"}
    }
  }
}
```

**WICHTIG:**
- ❌ Diese Datenpunkte sind **NICHT in der HA Integration**
- ⚠️ Werte **frieren manchmal ein** (nicht täglich aktualisiert)
- ⚠️ Manche Geräte zeigen sie **gar nicht**

---

## 🏆 Direkte Gegenüberstellung

### Szenario 1: "Ich will Live-Energieflüsse sehen"

**Gewinner: 🥇 gridX API**

✅ **Warum:**
- Echtzeit-Daten alle 60 Sekunden
- Zeigt woher Strom kommt (PV/Netz) und wohin er geht (WP/Haus/Batterie/Netz)
- Perfekt für Energy Flow Karte in HA

❌ **ViCare kann das nicht:** Keine Echtzeit-Leistung, keine PV-Daten

---

### Szenario 2: "Ich will Statistiken im Energy Dashboard"

**Gewinner: 🥇 ViCare API (mit Workaround)**

✅ **Warum:**
- Kumulierte Werte (kWh) über Tag/Woche/Monat/Jahr
- Perfekt für `state_class: total_increasing`
- Energy Dashboard braucht genau diese Werte

⚠️ **ABER:**
- Nicht in Standard-Integration → Custom Sensor nötig
- Daten frieren manchmal ein
- Rate Limits

🔄 **gridX Alternative:**
- Kann kumulierte Tageswerte liefern
- Aber keine historischen Wochen/Monate/Jahre
- Nur für PV, nicht für WP-Verbrauch

---

### Szenario 3: "Ich will PV-Produktion (Vitocharge) sehen"

**Gewinner: 🥇 gridX API**

✅ **Warum:**
- Vitocharge wird vollständig unterstützt
- Echtzeit + kumulierte Tageswerte
- Keine Probleme

❌ **ViCare:** Vitocharge fehlt oft komplett in der API/Integration

---

### Szenario 4: "Ich will Wärmepumpe steuern (Modi, Temperaturen)"

**Gewinner: 🥇 ViCare API**

✅ **Warum:**
- Vollständige Steuerung über API
- Setzen von Solltemperaturen
- Ändern von Betriebsmodi
- HA Integration unterstützt das

❌ **gridX:** Nur Monitoring, keine Steuerung

---

### Szenario 5: "Ich will COP (Effizienz) der Wärmepumpe tracken"

**Gewinner: 🥇 gridX API**

✅ **Warum:**
- COP wird direkt geliefert
- Echtzeit-Wert

❌ **ViCare:** COP nicht als Datenpunkt (muss man selbst berechnen aus Leistung und Wärmeleistung)

---

## 💡 Konkrete Empfehlungen

### ✅ **Beste Lösung: BEIDE APIs kombinieren!**

Jede API hat ihre Stärken - nutze beide parallel:

| Datenpunkt | API | Grund |
|-----------|-----|-------|
| PV-Leistung (aktuell) | gridX | ViCare zeigt Vitocharge nicht |
| PV-Produktion (gesamt) | gridX | ViCare zeigt Vitocharge nicht |
| WP-Leistung (aktuell) | gridX | ViCare hat keine Echtzeit-Leistung |
| **WP-Verbrauch (kumuliert)** | **ViCare** | gridX hat keine kumulierten Werte |
| WP-Temperaturen | ViCare | gridX hat nur begrenzte Daten |
| WP-Modi & Steuerung | ViCare | gridX nur Monitoring |
| COP (Effizienz) | gridX | ViCare berechnet das nicht |
| Netz & Hausverbrauch | gridX | ViCare hat das nicht |

### 📋 Setup-Plan:

**1. ViCare Integration (bereits vorhanden):**
```
✅ Einstellungen → Geräte & Dienste → ViCare
→ Liefert: Temperaturen, Modi, Betriebsdaten
```

**2. ViCare Custom Sensor hinzufügen:**
```
⚠️ Für Stromverbrauch (kumuliert)
→ Siehe: VICARE_POWER_CONSUMPTION_GUIDE.md
→ Nur wenn Energy Dashboard wichtig ist
```

**3. gridX RESTful Sensor:**
```
✅ Für: PV, Echtzeit-Leistung, Energieflüsse
→ Siehe: GRIDX_VIESSMANN_HOME_ASSISTANT_GUIDE.md
→ Bearer Token aus Browser holen
```

---

## 🎨 Dashboard-Beispiel: Beide APIs kombiniert

```yaml
# Energy Flow Card (gridX)
type: energy-flow-card
entities:
  grid:
    consumption: sensor.netz_leistung  # gridX
  solar:
    production: sensor.pv_leistung     # gridX
  home:
    consumption: sensor.hausverbrauch  # gridX
  individual:
    - entity_id: sensor.warmepumpe_leistung  # gridX
      name: Wärmepumpe
      icon: mdi:heat-pump

# Energy Dashboard (ViCare + gridX)
energy:
  devices:
    - sensor.warmepumpe_stromverbrauch_jahr  # ViCare (kumuliert)
  solar_production:
    - sensor.pv_heute  # gridX (kumuliert Tageswert)

# Wärmepumpen-Details (ViCare)
type: entities
title: Wärmepumpe Details
entities:
  - sensor.vicare_outside_temperature      # ViCare
  - sensor.vicare_supply_temperature       # ViCare
  - sensor.vicare_heating_burner_hours     # ViCare
  - sensor.warmepumpe_cop                  # gridX
  - sensor.warmepumpe_leistung             # gridX (Echtzeit)
  - sensor.warmepumpe_stromverbrauch_heute # ViCare (kumuliert)
```

---

## ⚠️ Wichtige Hinweise

### gridX API:

**Pro:**
- ✅ Keine Rate Limits (normale Nutzung)
- ✅ Vollständige PV-Daten (Vitocharge)
- ✅ Echtzeit-Energieflüsse

**Contra:**
- ❌ Bearer Token läuft ab (manuell erneuern)
- ❌ Keine offizielle HA Integration
- ❌ Keine WP-Steuerung

**Setup-Aufwand:** ⚠️ Mittel (Bearer Token Management)

---

### ViCare API:

**Pro:**
- ✅ Offizielle HA Integration
- ✅ Automatisches Token-Management
- ✅ WP-Steuerung möglich
- ✅ Kumulierte Verbrauchswerte

**Contra:**
- ❌ Vitocharge fehlt oft
- ❌ Stromverbrauch nicht in Standard-Integration
- ❌ Rate Limits (24h Sperre möglich)
- ❌ Daten frieren manchmal ein

**Setup-Aufwand:** ✅ Einfach (aber Stromverbrauch = Custom Sensor)

---

## 🔧 Troubleshooting

### Problem: "gridX Token läuft ab"

**Lösung:**
1. Neuen Token aus Browser holen (siehe gridX Guide)
2. In `secrets.yaml` aktualisieren
3. HA YAML neu laden

**Langfristig:**
- Prüfe ob es eine Community HACS Integration gibt
- Oder: Schreibe eigene Integration mit OAuth2

---

### Problem: "ViCare Rate Limit (429 Error)"

**Symptom:** 24h Sperre

**Ursache:** Zu viele API Requests

**Lösung:**
1. Scan Interval erhöhen (360+ Sekunden)
2. Anzahl der Sensoren reduzieren
3. Upgrade auf Advanced Tier (19,99€/Monat)
4. **Oder: gridX API nutzen (keine Limits)**

---

### Problem: "Vitocharge erscheint nicht in ViCare"

**Häufig!** ViCare API gibt Vitocharge-Daten nicht immer frei.

**Lösung:** **gridX API nutzen** - Vitocharge wird dort vollständig unterstützt

---

### Problem: "ViCare Stromverbrauch friert ein"

**Symptom:** Werte aktualisieren sich nicht täglich

**Workaround:**
1. Communication Module in ViCare App rebooten
2. Warten (manchmal aktualisiert es sich später)
3. **gridX API nutzen** (keine Freezing-Probleme)

---

## 📊 Zusammenfassung

### Für dein Setup (E.ON gridX + Vitocal + Vitocharge):

| Ziel | Beste Lösung | Aufwand |
|------|-------------|---------|
| **Live-Energieflüsse** | 🥇 gridX | ⚠️ Mittel |
| **PV-Monitoring (Vitocharge)** | 🥇 gridX | ⚠️ Mittel |
| **WP-Stromverbrauch (kumuliert)** | ⚠️ ViCare Custom Sensor | ⚠️ Mittel |
| **WP-Temperaturen & Modi** | 🥇 ViCare (Standard) | ✅ Einfach |
| **WP-Steuerung** | 🥇 ViCare (Standard) | ✅ Einfach |
| **Energy Dashboard** | 🔄 Beide kombinieren | ⚠️ Mittel |

### Empfohlenes Setup:

```
1. ✅ ViCare Integration (bereits aktiv)
   → Temperaturen, Modi, Betriebsdaten

2. ✅ gridX RESTful Sensor (neu einrichten)
   → PV, Energieflüsse, Echtzeit-Leistung

3. ⚠️ ViCare Custom Sensor (optional)
   → Nur wenn kumulierter WP-Verbrauch kritisch
   → Achtung: Rate Limits!

4. 📊 Energy Dashboard
   → PV: gridX (Tageswerte)
   → WP: ViCare Custom Sensor (Jahreswerte)
```

---

## 📚 Nächste Schritte

1. **Lies die Guides:**
   - `GRIDX_VIESSMANN_HOME_ASSISTANT_GUIDE.md` (gridX Setup)
   - `VICARE_POWER_CONSUMPTION_GUIDE.md` (ViCare Stromverbrauch)

2. **Teste die Scripts:**
   - `test_gridx_viessmann_api.py` (zeigt gridX Daten)
   - `test_vicare_power_consumption.py` (zeigt ViCare Stromverbrauch)

3. **Entscheide dich:**
   - **Nur Live-Monitoring?** → gridX reicht
   - **Nur WP-Steuerung?** → ViCare Standard reicht
   - **Alles?** → Beide kombinieren!

4. **Richte ein:**
   - Befolge die Guides Schritt für Schritt
   - Teste jeden Sensor einzeln
   - Baue Dashboard nach deinen Wünschen

---

**Viel Erfolg mit deinem Energy Management Setup! ⚡🏠**
