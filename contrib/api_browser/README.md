# API Browser

A small Python CLI tool for browsing and filtering the public APIs list from the repository.

## Features

- **Parse APIs**: Read and parse APIs from the repository's README.md file
- **Filter APIs**: Filter APIs by keyword in name or description
- **Category Filter**: Filter APIs by category
- **Output Formats**: Support JSON and table output formats
- **Local Cache**: Cache parsed APIs locally for faster access (default 24 hours)
- **Cache Refresh**: Force refresh the local cache

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make the CLI script executable (optional):
```bash
chmod +x cli.py
```

## Usage

### Basic Usage

```bash
python cli.py
```

This will display all APIs in a table format.

### Filter by Keyword

```bash
python cli.py -q "weather"
```

This will display all APIs related to weather.

### Filter by Category

```bash
python cli.py -c "development"
```

This will display all APIs in the Development category.

### Combine Filters

```bash
python cli.py -q "oauth" -c "social"
```

This will display all APIs in the Social category that use OAuth authentication.

### JSON Output

```bash
python cli.py -q "weather" -o json
```

This will display the filtered APIs in JSON format.

### Force Cache Refresh

```bash
python cli.py --cache-refresh
```

This will force refresh the local cache by re-parsing the README.md file.

## Testing

Run the unit tests using pytest:

```bash
pytest test_api_browser.py
```

## Project Structure

```
api_browser/
├── cli.py              # Main CLI entry point
├── parser.py           # API parsing logic
├── filter.py           # API filtering logic
├── cache.py            # Cache management
├── test_api_browser.py # Unit tests
├── requirements.txt    # Dependencies
└── README.md           # This file
```

## License

MIT
