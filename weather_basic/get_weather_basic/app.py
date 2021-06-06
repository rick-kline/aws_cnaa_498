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
## Pittsburgh Lat Long 40.44110304746155, -80.0033777788991
## Pittsburgh Intl Airport Lat long 40.48743323452993, -80.23899332292899
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

## Lambda handler is entry point to lambda City must be passed in as event
def lambda_handler(event, context):
    lat = event['latitude']
    lon = event['longitude']
    ## Sets weather = return from call to weather function providing city_name 
    weather = get_weather(lat, lon)
    message = f"Location {weather['location']}: Temperature {weather['temp']} F -- Feels Like {weather['feels_like']} F -- Humidity {weather['humidity']} %"
    
    ## Returns weather result 
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "location": ip.text.replace("\n", "")
        }),
    }
