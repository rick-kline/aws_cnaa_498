import json
import requests
import math
import awswrangler.secretsmanager as sm
import datetime
import boto3

client = boto3.client('lambda')

####################################################
## Function takes input variable city and returns
## Temperature
## Feels Like
## Humidity
## Ohioville Lat Long 40.68019752889984, -80.49203387776737
## Harshville Lat Long 40.543628195571614, -80.41924945329497
## Beaver Lat Long 40.69685862211706, -80.30114642490575
#####################################################

def get_weather(lat, lon, utcdttm):
    ##Request OpenWeather API key from Secrets manager
    api_key = sm.get_secret_json("OpenWeatherApiKey").get('api_key')
    ## URL for API Requests, includes city and api_key variables
    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&units=imperial&dt={utcdttm}&appid={api_key}"
    
     ## sets response variable equal to simple get request of url in json form
    response = requests.get(url).json()
    return response

def get_iso_datetime(epochdt):
    value = datetime.datetime.fromtimestamp(epochdt)
    return f"{value:%Y-%m-%d %H:%M:%S}"
    
def prep_item(item_dict):
    item_dict.pop('weather')
    item_dict.pop('rain', None)
    item_dict.pop('dew_point')
    item_dict.pop('visibility', None)
    item_dict.pop('wind_gust', None)
    item_dict['datetime_beginning_utc'] = item_dict.pop('dt')
    item_dict['load_area'] = 'DUQ'
    item_dict['action_type'] = "UPDATE"
    item_dict['data_product'] = "hrl_weather"
    item_dict['hrl_weather_data'] = {}
    item_dict['hrl_weather_data']['temp'] = item_dict.pop('temp')
    item_dict['hrl_weather_data']['feels_like'] = item_dict.pop('feels_like')
    item_dict['hrl_weather_data']['pressure'] = item_dict.pop('pressure')
    item_dict['hrl_weather_data']['humidity'] = item_dict.pop('humidity')
    item_dict['hrl_weather_data']['iso_datetime_beginning_utc'] = get_iso_datetime(item_dict['datetime_beginning_utc'])
    item_dict['hrl_weather_data']['wind_speed'] = item_dict.pop('wind_speed')
    item_dict['hrl_weather_data']['wind_direction'] = item_dict.pop('wind_deg')
    item_dict['hrl_weather_data']['cloud_coverage'] = item_dict.pop('clouds')/100

    return item_dict

def insert_ddb_table(json_data):
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-2:133803608902:function:energy-weather-lmp-tbl-cr-EnergyWeatherLmpCrudFunc-1LJ4PSNBUD3UJ',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(json_data)
        )
        
    return response
   

lat = 40.48743323452993
lon = -80.23899332292899
utcdttm = 1622419200
weather = get_weather(lat, lon, utcdttm)
# print(str(weather))
weather_hrl_list=[]

for item in weather['hourly']:
    new_item = prep_item(item)
    weather_hrl_list.append(new_item)

# print(str(weather_hrl_list[1]))

ddb_response = insert_ddb_table(weather_hrl_list)
print(str(ddb_response))

   



 # loc_name = response['name']
    
    # ## Parse temp from response json
    # temp = response['main']['temp']
    # ## Temp is returned in Kelvin by default, converts to Fahrenheit
    # temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

    # ## Parse feels_like from response json
    # feels_like = response['main']['feels_like']
    # ## Feels Like is returned in Kelvin by default, converts to Fahrenheit
    # feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    # ## Parse humidity from response json
    # humidity = response['main']['humidity']
    
    # ## Returns dictionary of temp, feels like and humidity values
    # return {
    #     'location': loc_name,
    #     'temp': temp,
    #     'feels_like': feels_like,
    #     'humidity': humidity
    # }
## Ohioville Lat Long 40.68019752889984, -80.49203387776737
## Harshville Lat Long 40.54252512866973, -80.41634184578841
## Beaver Lat Long 40.69685862211706, -80.30114642490575
## Pittsburgh Lat Long 40.44110304746155, -80.0033777788991
## Pittsburgh Intl Airport Lat long 40.48743323452993, -80.23899332292899


# message = f"Location {weather['location']}: Temperature {weather['temp']} F -- Feels Like {weather['feels_like']} F -- Humidity {weather['humidity']} %"
 