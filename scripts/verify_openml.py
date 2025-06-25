import requests

def verify_openml():
    url = "https://www.openml.org/api/v1/json/data/list"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("OpenML API is accessible.")
        else:
            print(f" OpenML API responded with status: {response.status_code}")
    except Expception as e:
        print(f"Error accessing OpenML: {e}")

if __name__ == "__main__":
    verify_openml()