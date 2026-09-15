import requests

def get_weather(city):
    api_key = "your_openweather_api_key"  # get free API key from https://openweathermap.org/api
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)