import json
import requests
import math
import awswrangler.secretsmanager as sm
import datetime
import boto3

client = boto3.client('lambda')


def get_iso_datetime(epochdt):
    value = datetime.datetime.fromtimestamp(epochdt)
    return f"{value:%Y-%m-%d %H:%M:%S}"
    
def insert_ddb_table(json_data):
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-2:133803608902:function:energy-weather-lmp-tbl-cr-EnergyWeatherLmpCrudFunc-1LJ4PSNBUD3UJ',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(json_data)
        )
        
    return response



twenty_sixth_weather_hrl_list=[
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
                    {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}}]
# twenty_fourth_weather_hrl_list=[
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}}]
# twenty_fifth_weather_hrl_list=[
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}},
#                     {'datetime_beginning_utc': 1621990800, 'load_area': 'DUQ', 'action_type': 'UPDATE', 'data_product': 'hrl_weather', 'hrl_weather_data': {'temp': 66.56, 'feels_like': 68.49, 'pressure': 1017, 'humidity': 92, 'iso_datetime_beginning_utc': '2021-05-26 01:00:00', 'wind_speed': 5.35, 'wind_direction': 207, 'cloud_coverage': 0.04}}]
x = 1621987200
twenty_sixth_dt_list = []
for i in range(24):
    twenty_sixth_dt_list.append(x)
    x=x+3600

# x = 1621814400
# twenty_fourth_dt_list = []
# for i in range(24):
#     twenty_fourth_dt_list.append(x)
#     x=x+3600
    
# x = 1621900800
# twenty_fifth_dt_list = []
# for i in range(24):
#     twenty_fifth_dt_list.append(x)
#     x=x+3600

twenty_sixth_temp_list = [82,	80,	76,	74,	73,	74,	74,	74,	73,	70,	72,	72,	73,	72,	77,	77,	78,	83,	84,	85,	83,	74,	68,	68]
twenty_sixth_hum_list = [44,	47,	56,	59,	61,	57,	57,	57,	59,	65,	64,	66,	66,	73,	62,	62,	60,	47,	46,	43,	42,	73,	93,	93]
twenty_sixth_wind_list = [5,	7,	5,	5,	3,	5,	7,	6,	3,	3,	7,	8,	12,	6,	10,	10,	10,	15,	21,	17,	14,	25,	7,	9]
twenty_sixth_pre_list = [975,	975,	975,	975,	975,	975,	975,	974,	974,	974,	974,	974,	974,	974,	974,	974,	974,	973,	972,	971,	970,	972,	972,	973]
twenty_sixth_feel_list = [84,	82,	78,	76,	75,	76,	76,	76,	75,	72,	74,	74,	75,	74,	79,	79,	80,	85,	87,	88,	85,	76,	70,	70]


# twenty_fourth_temp_list  = [82,	79,	77,	77,	73,	72,	70,	69,	68,	68,	68,	67,	68,	72,	71,	70,	69,	72,	75,	75,	75,	73,	75,	73]
# twenty_fourth_hum_list  = [45,	50,	52,	54,	64,	71,	78,	81,	87,	87,	87,	93,	90,	84,	84,	87,	90,	84,	69,	69,	69,	79,	76,	81]
# twenty_fourth_wind_list  = [10,	6,	3,	0,	12,	0,	3,	3,	5,	3,	0,	3,	5,	0,	6,	6,	6,	8,	7,	7,	0,	5,	6,	7]
# twenty_fourth_pre_list  = [975,976,976,977,977,977,977,976,976,976,976,977,977,978,978,978,978,978,978,978,978,977,977,977]
# twenty_fourth_feel_list  = [84,	81,	79,	79,	75,	74,	72,	71,	70,	70,	70,	69,	70,	74,	73,	72,	71,	74,	77,	77,	77,	75,	77,	75]

# twenty_fifth_temp_list   = [73,	71,	70,	68,	68,	67,	66,	65,	64,	64,	63,	64,	65,	70,	76,	80,	84,	84,	84,	86,	85,	85,	85,	83]
# twenty_fifth_hum_list  = [79,81,84,	87,	87,	90,	90,	90,	96,	100,100,100,100,84,	69,	58,	46,	44,	46,	38,	40,	41,	38,	41]
# twenty_fifth_pre_list  = [7,6,5,3,3,0,	3,	0,	0,	3,	3,	3,	5,	6,	5,	8,	14,	13,	10,	15,	10,	12,	10,	9]
# twenty_fifth_wind_list  = [978,978,978,978,979,978,978,978,977,977,977,978,978,978,978,978,977,977,976,976,976,975,975,975]
# twenty_fifth_feel_list  = [75,	73,	72,	70,	70,	69,	68,	67,	66,	66,	65,	66,	67,	72,	78,	82,	87,	87,	87,	89,	88,	88,	88,	85]

insert_list = []
for i in range(24):
    item = twenty_sixth_weather_hrl_list[i]
    item['datetime_beginning_utc'] = twenty_sixth_dt_list[i]
    item['hrl_weather_data']['temp'] = twenty_sixth_temp_list[i]
    item['hrl_weather_data']['humidity'] = twenty_sixth_hum_list[i] 
    item['hrl_weather_data']['wind_speed'] = twenty_sixth_wind_list[i]
    item['hrl_weather_data']['pressure'] = twenty_sixth_pre_list[i]
    item['hrl_weather_data']['feels_like'] = twenty_sixth_feel_list[i]
    item['hrl_weather_data']['iso_datetime_beginning_utc'] = get_iso_datetime(item['datetime_beginning_utc'])
    
    insert_list.append(item)

# for i in range(24):
#     item = twenty_fourth_weather_hrl_list[i]
#     item['datetime_beginning_utc'] = twenty_fourth_dt_list[i]
#     item['hrl_weather_data']['temp'] = twenty_fourth_temp_list[i]
#     item['hrl_weather_data']['humidity'] = twenty_fourth_hum_list[i] 
#     item['hrl_weather_data']['wind_speed'] = twenty_fourth_wind_list[i]
#     item['hrl_weather_data']['pressure'] = twenty_fourth_pre_list[i]
#     item['hrl_weather_data']['feels_like'] = twenty_fourth_feel_list[i]
#     item['hrl_weather_data']['iso_datetime_beginning_utc'] = get_iso_datetime(item['datetime_beginning_utc'])
#     insert_list.append(item)

# for i in range(24):
#     item = twenty_fifth_weather_hrl_list[i]
#     item['datetime_beginning_utc'] = twenty_fifth_dt_list[i]
#     item['hrl_weather_data']['temp'] = twenty_fifth_temp_list[i]
#     item['hrl_weather_data']['humidity'] = twenty_fifth_hum_list[i] 
#     item['hrl_weather_data']['wind_speed'] = twenty_fifth_wind_list[i]
#     item['hrl_weather_data']['pressure'] = twenty_fifth_pre_list[i]
#     item['hrl_weather_data']['feels_like'] = twenty_fifth_feel_list[i]
#     item['hrl_weather_data']['iso_datetime_beginning_utc'] = get_iso_datetime(item['datetime_beginning_utc'])
#     insert_list.append(item)


ddb_response = insert_ddb_table(insert_list)
print(str(ddb_response))





