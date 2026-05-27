import requests

apis = [
    'https://www.alphavantage.co/',
    'https://fred.stlouisfed.org/docs/api/fred/',
    'https://www.coingecko.com/api',
    'https://api.nasa.gov',
    'https://dog.ceo/dog-api/',
    'https://pokeapi.co/',
    'https://restcountries.com/',
    'https://official-joke-api.appspot.com/',
    'https://api.chucknorris.io/',
]

results = []
for url in apis:
    try:
        r = requests.head(url, timeout=8, allow_redirects=True)
        results.append({'url': url, 'status': r.status_code, 'ok': r.ok})
    except Exception as e:
        results.append({'url': url, 'status': 'ERR', 'ok': False, 'err': str(e)[:60]})

for r in results:
    icon = 'OK' if r['ok'] else 'FAIL'
    status = r.get('status', 'ERR')
    print(f"[{icon}] {status} {r['url']}")
print(f"\n{sum(1 for r in results if r['ok'])}/{len(results)} reachable")
