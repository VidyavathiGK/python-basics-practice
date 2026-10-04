import os
import requests


def get_weather_data(city_name, api_key):
  """Fetches current weather data for a given city from OpenWeatherMap API."""
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  params = {"q": city_name, "appid": api_key, "units": "metric"}

  try:
    response = requests.get(base_url, params=params)

    # Check if the city was found or if there's an API error
    if response.status_code == 200:
      return response.json()
    elif response.status_code == 401:
      print("\n[Error] Invalid API Key. Please check your OpenWeatherMap key.")
    elif response.status_code == 404:
      print(f"\n[Error] City '{city_name}' not found. Please check spelling.")
    else:
      print(f"\n[Error] Unexpected error occurred (Code: {response.status_code})")

    return None

  except requests.exceptions.RequestException as e:
    print(f"\n[Connection Error] Could not connect to the weather service: {e}")
    return None


def display_weather(data):
  """Parses and neatly displays the weather data."""
  if not data:
    return

  city = data.get("name")
  country = data.get("sys", {}).get("country")
  weather_desc = data.get("weather", [{}])[0].get("description", "").title()
  temp = data.get("main", {}).get("temp")
  feels_like = data.get("main", {}).get("feels_like")
  humidity = data.get("main", {}).get("humidity")
  wind_speed = data.get("wind", {}).get("speed")

  print("\n" + "=" * 40)
  print(f" Weather Report for: {city}, {country}")
  print("=" * 40)
  print(f" Condition   : {weather_desc}")
  print(f" Temperature : {temp}°C (Feels like {feels_like}°C)")
  print(f" Humidity    : {humidity}%")
  print(f" Wind Speed  : {wind_speed} m/s")
  print("=" * 40 + "\n")


def main():
  print("--- Command Line Weather Dashboard ---")

  # You can hardcode your API key here or load it from an environment variable
  # Sign up for a free account at https://openweathermap.org/ to get an API key
  api_key = os.getenv("OPENWEATHER_API_KEY")

  if not api_key:
    api_key = input("Enter your OpenWeatherMap API key: ").strip()

  if not api_key:
    print("API key is required to fetch weather data. Exiting.")
    return

  while True:
    city = input(
        "Enter city name (or type 'exit' to quit): "
    ).strip()

    if city.lower() == "exit":
      print("Goodbye!")
      break

    if not city:
      print("City name cannot be empty.")
      continue

    print(f"Fetching weather for {city}...")
    weather_data = get_weather_data(city, api_key)
    display_weather(weather_data)


if __name__ == "__main__":
  main()
