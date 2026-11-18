import requests
from urllib.parse import urlparse

def check_link(url):
    try:
        # Setting a timeout for the request (10 seconds)
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Broken link found: {url} (Status Code: {response.status_code})")
        else:
            print(f"Link is working: {url}")
    except requests.exceptions.Timeout:
        print(f"Error with link: {url} -> Timeout")
    except requests.exceptions.RequestException as e:
        print(f"Error with link: {url} -> {e}")

def main():
    urls = [
        "https://github.com/davemachado/public-api",
        "https://github.com/public-apis/public-apis/issues",
        # Add the rest of the URLs you need to check
    ]
    
    for url in urls:
        check_link(url)

if __name__ == "__main__":
    main()

