import requests
import json
import time
import pandas as pd

API_KEY = "619c54b8862540ebb94175102261304"

api_url = "https://api.weatherapi.com/v1/forecast.json"  # API endpoint for forecast

zip_codes = [
    "90045",  # Los Angeles, CA
    "10001",  # New York, NY
    "60601",  # Chicago, IL
    "98101",  # Seattle, WA
    "33101",  # Miami, FL
    "85001",  # Phoenix, AZ
    "19101",  # Philadelphia, PA
    "78201",  # San Antonio, TX
    "92101",  # San Diego, CA
    "75201",  # Dallas, TX
    "95101",  # San Jose, CA
    "78701",  # Austin, TX
    "32099",  # Jacksonville, FL
    "76101",  # Fort Worth, TX
    "43215",  # Columbus, OH
    "28201",  # Charlotte, NC
    "46201",  # Indianapolis, IN
    "94102",  # San Francisco, CA
    "80201",  # Denver, CO
    "02101",  # Boston, MA
]

results = []

for zip_code in zip_codes:
    # Parameters for the API request
    params = {
        "key": API_KEY,
        "q": zip_code,
        "days": 7
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    city = data["location"]["name"]
    region = data["location"]["region"]

    print(f"Fetched 7-day forecast for {city}, {region}")

    for day in data["forecast"]["forecastday"]:
        result = {
            "zip_code": zip_code,
            "city": city,
            "region": region,
            "date": day["date"],
            "max_temp_f": day["day"]["maxtemp_f"],
            "min_temp_f": day["day"]["mintemp_f"],
            "condition": day["day"]["condition"]["text"]
        }
        results.append(result)

    time.sleep(1)

df = pd.DataFrame(results)

print(f"\nWeather Data Table:")
print(df.to_string(index=False))

print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")

df.to_csv("weather_data.csv", index=False)
print("Saved to weather_data.csv")

