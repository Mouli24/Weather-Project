import urllib.request
import json

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        return data

if __name__ == "__main__":
    print(fetch_weather())
