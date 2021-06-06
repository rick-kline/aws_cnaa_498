import requests
import math
import awswrangler.secretsmanager as sm

city_name = "Jupiter,US"
api_key = sm.get_secret_json("OpenWeatherApiKey").get('api_key')

def get_weather(api_key, city):
   
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    humidity = response['main']['humidity']
    
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }

weather = get_weather(api_key, city_name)
print(f"{city_name}: Temperature {weather['temp']} F -- Feels Like {weather['feels_like']} F -- Humidity {weather['humidity']} %")
