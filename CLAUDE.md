# CLAUDE.md - Project Guide

## Project Overview

**UI for Public APIs** is a curated library of free public APIs, designed to be transformed into a beautiful, user-friendly web interface. The repository currently serves as a comprehensive data source documenting hundreds of accessible APIs with their key characteristics, organized by category.

### Vision

Create a stunning, modern web UI that allows developers to:
- Browse and discover public APIs effortlessly
- Filter and search by category, authentication type, HTTPS support, and CORS compatibility
- View clean, well-organized documentation for each API
- Access a visually appealing, responsive interface that works on all devices

## Repository Structure

```
UI-for-public-apis/
├── README.md                    # Main API catalogue (~1,891 APIs in 49 categories)
├── CLAUDE.md                    # This file - project guide for Claude
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── .gitignore                   # Python-specific ignore patterns
│
├── .github/
│   ├── workflows/               # CI/CD pipelines
│   │   ├── test_of_validate_package.yml
│   │   ├── validate_links.yml
│   │   └── test_of_push_and_pull.yml
│   ├── ISSUE_TEMPLATE.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── assets/                  # Sponsor logos and images
│
└── scripts/
    ├── README.md                # Scripts documentation
    ├── requirements.txt         # Python dependencies
    ├── github_pull_request.sh   # PR validation script
    ├── validate/                # Validation modules
    │   ├── format.py            # Markdown format validation
    │   └── links.py             # URL link validation
    └── tests/                   # Unit tests
        ├── test_validate_format.py
        └── test_validate_links.py
```

## Data Source

### API Catalogue (README.md)

The main data lives in `README.md` as markdown tables organized by category.

**Categories (49 total):** Animals, Anime, Anti-Malware, Art & Design, Authentication, Blockchain, Books, Business, Calendar, Cloud Storage, Continuous Integration, Cryptocurrency, Currency Exchange, Data Validation, Development, Dictionaries, Documents & Productivity, Email, Entertainment, Environment, Events, Finance, Food & Drink, Games & Comics, Geocoding, Government, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Phone, Photography, Programming, Science & Math, Security, Shopping, Social, Sports & Fitness, Test Data, Text Analysis, Tracking, Transportation, URL Shorteners, Vehicle, Video, Weather

**Entry Format:**
```markdown
| [API Name](URL) | Description | Auth | HTTPS | CORS |
```

**Field Specifications:**
| Field | Valid Values | Notes |
|-------|-------------|-------|
| API | `[Name](URL)` | Cannot end with "API" |
| Description | Free text | Max 100 chars, capitalized, no ending punctuation |
| Auth | `No`, `` `apiKey` ``, `` `OAuth` ``, `` `X-Mashape-Key` ``, `` `User-Agent` `` | Backtick-enclosed except "No" |
| HTTPS | `Yes`, `No` | |
| CORS | `Yes`, `No`, `Unknown` | |

## Development Commands

### Validation Scripts

```bash
# Install Python dependencies
pip install -r scripts/requirements.txt

# Validate README format
python scripts/validate/format.py README.md

# Check for duplicate links only (fast)
python scripts/validate/links.py README.md -odlc

# Full link validation (slow - checks all URLs)
python scripts/validate/links.py README.md

# Run unit tests
cd scripts && python -m unittest discover tests/ --verbose
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature

# After making changes
git add .
git commit -m "Add: descriptive message"
git push -u origin feature/your-feature
```

## UI Development Goals

### Target Features

1. **Modern Design**
   - Clean, minimal interface with excellent typography
   - Dark/light mode support
   - Responsive design for mobile, tablet, and desktop

2. **Search & Discovery**
   - Full-text search across API names and descriptions
   - Category-based browsing
   - Filter by Auth type, HTTPS support, CORS compatibility

3. **API Cards/Listings**
   - Visual cards showing API info at a glance
   - Quick-view authentication requirements
   - Direct links to documentation

4. **Organization**
   - Category navigation (sidebar or top nav)
   - Alphabetical sorting within categories
   - Favorites/bookmarking capability

### Suggested Tech Stack

For a beautiful, modern web UI consider:
- **Framework:** Next.js, Astro, or SvelteKit for static site generation
- **Styling:** Tailwind CSS for rapid, consistent styling
- **Search:** Fuse.js for client-side fuzzy search
- **Hosting:** Vercel, Netlify, or GitHub Pages
- **Data:** Parse README.md into JSON at build time

### Data Transformation

The README.md needs to be parsed into structured JSON for the UI:
```json
{
  "categories": [
    {
      "name": "Animals",
      "slug": "animals",
      "apis": [
        {
          "name": "Cat Facts",
          "url": "https://catfact.ninja/",
          "description": "Daily cat facts",
          "auth": "No",
          "https": true,
          "cors": "Yes"
        }
      ]
    }
  ]
}
```

## Quality Standards

### API Entry Requirements
- Alphabetical ordering within categories
- Minimum 3 entries per category
- Descriptions under 100 characters
- Valid Auth/HTTPS/CORS values only
- All links must be working

### Code Quality
- Run format validation before committing
- Ensure all tests pass
- Follow existing patterns and conventions

## CI/CD Pipelines

Three GitHub Actions workflows handle quality assurance:

1. **test_of_push_and_pull.yml** - Format validation on push/PR
2. **validate_links.yml** - Daily link checking (scheduled)
3. **test_of_validate_package.yml** - Unit tests on push/PR

## Contributing

See `CONTRIBUTING.md` for detailed guidelines. Key points:
- One API per PR
- Follow alphabetical ordering
- PR title format: `Add [API-Name] API`
- Squash commits before merging
- Target master branch

## Key Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Main API catalogue - the data source |
| `CONTRIBUTING.md` | Contribution guidelines |
| `scripts/validate/format.py` | Format validation logic |
| `scripts/validate/links.py` | Link validation logic |
| `scripts/requirements.txt` | Python dependencies |

## License

MIT License - see `LICENSE` file for details.
