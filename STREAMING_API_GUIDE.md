# Streaming Availability APIs Guide

Dieser Guide zeigt, wie du herausfinden kannst, auf welchen Streaming-Plattformen ein Film oder eine Serie in einem bestimmten Land (z.B. Deutschland) verfügbar ist - inklusive kostenloser Optionen.

## 🎯 Use Case: Jason Bourne (2016) in Deutschland

**Frage:** Welcher Streaming-Anbieter bietet "Jason Bourne" (2016) kostenlos in Deutschland auf Deutsch an?

## 📊 Verfügbare APIs

### 1. TMDb API (The Movie Database) ⭐ EMPFOHLEN

**Warum TMDb?**
- ✅ Komplett kostenlos (nur API-Key erforderlich)
- ✅ Nutzt Daten von JustWatch
- ✅ Unterstützt Deutschland und 50+ weitere Länder
- ✅ Unterscheidet zwischen: Flatrate (Abo), Free (kostenlos mit Werbung), Rent (Ausleihe), Buy (Kauf)
- ✅ Sehr zuverlässig und gut dokumentiert

**Getting Started:**
1. Registriere dich kostenlos: https://www.themoviedb.org/signup
2. Hole dir deinen API-Key: https://www.themoviedb.org/settings/api
3. Dokumentation: https://developers.themoviedb.org/3

**Wichtige Endpoints:**

```bash
# 1. Film suchen
GET https://api.themoviedb.org/3/search/movie?api_key=YOUR_KEY&query=Jason%20Bourne&year=2016

# 2. Streaming-Anbieter abrufen
GET https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key=YOUR_KEY
```

**Beispiel Antwort für Deutschland (DE):**

```json
{
  "results": {
    "DE": {
      "link": "https://www.themoviedb.org/movie/324668-jason-bourne/watch?locale=DE",
      "flatrate": [
        {
          "provider_id": 119,
          "provider_name": "Amazon Prime Video"
        }
      ],
      "free": [
        {
          "provider_id": 123,
          "provider_name": "Rakuten TV"
        }
      ],
      "rent": [
        {
          "provider_id": 2,
          "provider_name": "Apple TV"
        }
      ],
      "buy": [
        {
          "provider_id": 2,
          "provider_name": "Apple TV"
        }
      ]
    }
  }
}
```

**Kategorien erklärt:**
- `flatrate`: Im Abo enthalten (z.B. Netflix, Prime Video)
- `free`: Kostenlos mit Werbung
- `rent`: Zum Ausleihen verfügbar
- `buy`: Zum Kaufen verfügbar

---

### 2. Watchmode API

**Features:**
- ✅ 1000 kostenlose API-Calls
- ✅ Keine Kreditkarte erforderlich
- ✅ 50+ Länder inklusive Deutschland
- ✅ 200+ Streaming-Dienste

**Getting Started:**
1. API-Key anfordern: https://api.watchmode.com/requestApiKey
2. Dokumentation: https://api.watchmode.com/docs

**Beispiel:**

```bash
# Film suchen
GET https://api.watchmode.com/v1/autocomplete-search/?apiKey=YOUR_KEY&search_value=Jason%20Bourne&search_type=1

# Details mit Deutschland-Filter
GET https://api.watchmode.com/v1/title/{watchmode_id}/details/?apiKey=YOUR_KEY&regions=DE
```

---

### 3. Streaming Availability API (Movie of the Night)

**Features:**
- ✅ 100 kostenlose Calls pro Tag
- ✅ 60 Länder inklusive Deutschland
- ✅ Netflix, Disney+, Apple TV, Max, Hulu und mehr
- ⚠️ Läuft über RapidAPI

**Getting Started:**
1. Registriere dich auf RapidAPI
2. Abonniere die API: https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability
3. Dokumentation: https://docs.movieofthenight.com/

**Beispiel:**

```bash
curl -G https://streaming-availability.p.rapidapi.com/shows/search/title \
  -H "X-RapidAPI-Key: YOUR_KEY" \
  --data-urlencode "title=Jason Bourne" \
  --data-urlencode "country=de"
```

---

## 🎬 Test-Script ausführen

Das Repository enthält ein vollständiges Python-Test-Script:

```bash
# API-Keys als Umgebungsvariablen setzen (optional)
export TMDB_API_KEY="your_tmdb_key_here"
export WATCHMODE_API_KEY="your_watchmode_key_here"

# Script ausführen
python3 test_streaming_availability.py
```

Das Script zeigt dir:
- ✅ Wo "Jason Bourne" (2016) in Deutschland verfügbar ist
- ✅ Welche Dienste kostenlos sind (mit Werbung)
- ✅ Welche Dienste ihn im Abo haben
- ✅ Wo du ihn ausleihen/kaufen kannst

---

## 💡 Wichtige Hinweise

### Was bedeutet "kostenlos"?

Es gibt zwei Arten von "kostenlos":

1. **Free (mit Werbung)** 🆓
   - Wirklich kostenlos, aber mit Werbeunterbrechungen
   - Beispiele: Rakuten TV (mit Werbung), Pluto TV, Tubi
   - In der API unter `free` zu finden

2. **Flatrate (im Abo enthalten)** 📺
   - Technisch nicht kostenlos, da Abo-Gebühr erforderlich
   - Aber "kostenlos" wenn du das Abo bereits hast
   - Beispiele: Netflix, Prime Video, Disney+
   - In der API unter `flatrate` zu finden

### Sprachverfügbarkeit

Die APIs zeigen nur, **ob** ein Film verfügbar ist, nicht in welcher Sprache. Um herauszufinden, ob ein Film auf Deutsch verfügbar ist, musst du:

1. Die Website des Streaming-Anbieters besuchen
2. Oder zusätzlich die TMDb API nutzen für Audio/Untertitel-Infos
3. Oder JustWatch.com direkt nutzen (bietet Sprachfilter)

### Datenaktualität

- TMDb: Daten von JustWatch, Update ~1x täglich
- Watchmode: Update mehrmals täglich
- Streaming Availability: Update täglich

---

## 🔍 Ergebnis für Jason Bourne (2016) in Deutschland

Stand: Januar 2026

**Im Abo enthalten:**
- Amazon Prime Video 📺

**Zum Ausleihen/Kaufen:**
- Apple TV
- Google Play Movies
- Amazon Video
- Weitere Anbieter möglich

**Kostenlos mit Werbung:**
- Je nach Verfügbarkeit (ändert sich häufig)

⚠️ **Hinweis:** Die Verfügbarkeit ändert sich ständig. Nutze die APIs für aktuelle Daten!

---

## 📚 Weitere Ressourcen

- **JustWatch.com**: Manuelle Suche ohne API - https://www.justwatch.com/de
- **Werstreamt.es**: Alternative für Deutschland - https://www.werstreamt.es/
- **TMDb Community**: https://www.themoviedb.org/talk
- **Public APIs Repository**: https://github.com/public-apis/public-apis

---

## 🤝 Attribution

Wenn du TMDb API verwendest, musst du JustWatch als Datenquelle nennen:
> "Streaming data provided by JustWatch"

---

## ⚖️ Rechtliches

- Diese APIs sind für nicht-kommerzielle und kommerzielle Nutzung verfügbar
- Beachte die jeweiligen Terms of Service
- Rate Limits beachten (TMDb: 40 requests/10 seconds)
- Attribution erforderlich (siehe oben)
