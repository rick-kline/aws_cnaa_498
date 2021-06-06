import json
import requests
import math
import awswrangler.secretsmanager as sm

####################################################
## Function takes input variable city and returns
## Temperature
## Feels Like
## Humidity
## Ohioville Lat Long 40.68019752889984, -80.49203387776737
## Harshville Lat Long 40.543628195571614, -80.41924945329497
## Beaver Lat Long 40.69685862211706, -80.30114642490575
#####################################################

def get_weather(lat, lon):
    ##Request OpenWeather API key from Secrets manager
    api_key = sm.get_secret_json("OpenWeatherApiKey").get('api_key')
    ## URL for API Requests, includes city and api_key variables
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
     ## sets response variable equal to simple get request of url in json form
    response = requests.get(url).json()
    
    loc_name = response['name']
    
    ## Parse temp from response json
    temp = response['main']['temp']
    ## Temp is returned in Kelvin by default, converts to Fahrenheit
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

    ## Parse feels_like from response json
    feels_like = response['main']['feels_like']
    ## Feels Like is returned in Kelvin by default, converts to Fahrenheit
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    ## Parse humidity from response json
    humidity = response['main']['humidity']
    
    ## Returns dictionary of temp, feels like and humidity values
    return {
        'location': loc_name,
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }
## Ohioville Lat Long 40.68019752889984, -80.49203387776737
## Harshville Lat Long 40.54252512866973, -80.41634184578841
## Beaver Lat Long 40.69685862211706, -80.30114642490575
## Pittsburgh Lat Long 40.44110304746155, -80.0033777788991
## Pittsburgh Intl Airport Lat long 40.48743323452993, -80.23899332292899


lat = 40.49197381438313
lon = -80.23521525495532
# lat = 40.48743323452993
# lon = -80.23899332292899
weather = get_weather(lat, lon)
message = f"Location {weather['location']}: Temperature {weather['temp']} F -- Feels Like {weather['feels_like']} F -- Humidity {weather['humidity']} %"
    
print(message)