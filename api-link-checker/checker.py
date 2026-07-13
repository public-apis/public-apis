import requests

print("🔍 Checking multiple API links...\n")

api_links = [
    "https://google.com",
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts",
    "https://example.com",
]

for url in api_links:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"✔ Working: {url}")
        else:
            print(f"⚠ Status {r.status_code}: {url}")
    except Exception as e:
        print(f"❌ Error for {url} -> {e}")