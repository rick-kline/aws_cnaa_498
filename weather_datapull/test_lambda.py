import json
import requests
import math
import awswrangler.secretsmanager as sm
from datetime import datetime, timedelta
import boto3
from dateutil.parser import parse
import time
import datetime as dt


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
    value = dt.datetime.fromtimestamp(epochdt)
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

def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//30))
               
def convert_to_unix(iso_date):
    unix_date = int(time.mktime(iso_date.timetuple()))
    return unix_date
    
def get_return(ret_message):
     # Returns weather result 
    return str(ret_message)
   

## Lambda handler is entry point to lambda City must be passed in as event
# def lambda_handler(event, context):
#     lat = event['latitude']
#     lon = event['longitude']

lat = 40.48743323452993
lon = -80.23899332292899 

now = datetime.now()
rnd_current_datetime = (hour_rounder(now))

start_pull_at = rnd_current_datetime-timedelta(days=5)
pull_date = start_pull_at
weather_hrl_list=[]

while pull_date <= rnd_current_datetime:
    unix_pull_date = convert_to_unix(pull_date)
    weather = get_weather(lat, lon, unix_pull_date)
    
    for item in weather['hourly']:
        new_item = prep_item(item)
        weather_hrl_list.append(new_item)
        
    pull_date = pull_date + timedelta(days=1)
            
    ddb_response = insert_ddb_table(weather_hrl_list)
    
    final_output = get_return(ddb_response)
    
    print(final_output)