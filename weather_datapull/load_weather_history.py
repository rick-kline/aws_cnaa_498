import json
import boto3
from os import listdir
from os.path import isfile, join

## Global
s3_client = boto3.client("s3")
SOURCE_S3_BUCKET = 'smart-hub-data-133803608902-us-east-2'
SOURCE_FILE_PATH = 'open_weathermap_json/weather_history_duq.json'
TARGET_S3_BUCKET = 'energy-temperature-data'
# SOURCE_FILE_PATH = 'weather_2011.json'
LOCAL_FILE_SYS = "/tmp"
BUCKET_FOLDER = 'weather-data'

def upload_file_to_s3(upload_file, file_name):
    result = s3_client.upload_file(upload_file, TARGET_S3_BUCKET, file_name)
    return result

def write_to_local(year_qtr_list, file_name, loc=LOCAL_FILE_SYS):
    file_name = loc + "/" + file_name
    with open(file_name, "w") as file:
        json.dump(year_qtr_list, file)
    return file_name

def prep_item(item_dict):
    item_dict['datetime_beginning_utc'] = item_dict.pop('dt')
    item_dict['load_area'] = 'DUQ'
    item_dict['action_type'] = "UPDATE"
    item_dict['data_product'] = "hrl_weather"
    item_dict['hrl_weather_data'] = item_dict['main']
    item_dict['hrl_weather_data']['iso_datetime_beginning_utc'] = item_dict['dt_iso']
    item_dict['hrl_weather_data']['wind_speed'] = item_dict['wind']['speed']
    item_dict['hrl_weather_data']['wind_direction'] = item_dict['wind']['deg']
    item_dict['hrl_weather_data']['cloud_coverage'] = item_dict['clouds']['all']/100
            
    item_dict.pop('weather')
    item_dict.pop('main')
    item_dict.pop('timezone')
    item_dict.pop('wind')
    item_dict.pop('clouds')
    item_dict.pop('lat')
    item_dict.pop('lon')
    item_dict.pop('city_name')
    item_dict.pop('dt_iso')
    return item_dict
    

obj = s3_client.get_object(Bucket=SOURCE_S3_BUCKET,Key=SOURCE_FILE_PATH)
data = obj['Body'].read().decode('utf-8')
weather_data = json.loads(data)

list_of_lists = []

for i in range(43):
    list_of_lists.append([])

list_of_filenames = []
for i in range(2011,2022):
    for j in range(1,5):
        filename = 'weather_' +str(i)+'_Q'+str(j)
        list_of_filenames.append(filename)


for item in weather_data:
    new_item = prep_item(item)
#### 2011
    if new_item['datetime_beginning_utc'] >= 1293840000 and new_item['datetime_beginning_utc']<=1301612400:
        list_of_lists[0].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1301616000 and new_item['datetime_beginning_utc']<=1309474800:
        list_of_lists[1].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1309478400 and new_item['datetime_beginning_utc']<=1317423600:
        list_of_lists[2].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1317427200 and new_item['datetime_beginning_utc']<=1325372400:
        list_of_lists[3].append(new_item)
################################################################################################################
#### 2012
    elif new_item['datetime_beginning_utc'] >= 1325376000 and new_item['datetime_beginning_utc']<=1333234800:
        list_of_lists[4].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1333238400 and new_item['datetime_beginning_utc']<=1341097200:
        list_of_lists[5].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1341100800 and new_item['datetime_beginning_utc']<=1349046000:
        list_of_lists[6].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1349049600 and new_item['datetime_beginning_utc']<=1356994800:
        list_of_lists[7].append(new_item)
################################################################################################################
#### 2013
    elif new_item['datetime_beginning_utc'] >= 1356998400 and new_item['datetime_beginning_utc']<=1364770800:
        list_of_lists[8].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1364774400 and new_item['datetime_beginning_utc']<=1372633200:
        list_of_lists[9].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1372636800 and new_item['datetime_beginning_utc']<=1380582000:
        list_of_lists[10].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1380585600 and new_item['datetime_beginning_utc']<=1388530800:
        list_of_lists[11].append(new_item)
################################################################################################################
#### 2014
    elif new_item['datetime_beginning_utc'] >= 1388534400 and new_item['datetime_beginning_utc']<=1396306800:
        list_of_lists[12].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1396310400 and new_item['datetime_beginning_utc']<=1404169200:
        list_of_lists[13].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1404172800 and new_item['datetime_beginning_utc']<=1412118000:
        list_of_lists[14].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1412121600 and new_item['datetime_beginning_utc']<=1420066800:
        list_of_lists[15].append(new_item)
################################################################################################################
#### 2015
    elif new_item['datetime_beginning_utc'] >= 1420070400 and new_item['datetime_beginning_utc']<=1427842800:
        list_of_lists[16].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1427846400 and new_item['datetime_beginning_utc']<=1435705200:
        list_of_lists[17].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1435708800 and new_item['datetime_beginning_utc']<=1443654000:
        list_of_lists[18].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1443657600 and new_item['datetime_beginning_utc']<=1451602800:
        list_of_lists[19].append(new_item)
################################################################################################################
#### 2016
    elif new_item['datetime_beginning_utc'] >= 1451606400 and new_item['datetime_beginning_utc']<=1459465200:
        list_of_lists[20].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1459468800 and new_item['datetime_beginning_utc']<=1467327600:
        list_of_lists[21].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1467331200 and new_item['datetime_beginning_utc']<=1475276400:
        list_of_lists[22].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1475280000 and new_item['datetime_beginning_utc']<=1483225200:
        list_of_lists[23].append(new_item)
################################################################################################################
#### 2017
    elif new_item['datetime_beginning_utc'] >= 1483228800 and new_item['datetime_beginning_utc']<=1491001200:
        list_of_lists[24].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1491004800 and new_item['datetime_beginning_utc']<=1498863600:
        list_of_lists[25].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1498867200 and new_item['datetime_beginning_utc']<=1506812400:
        list_of_lists[26].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1506816000 and new_item['datetime_beginning_utc']<=1514761200:
        list_of_lists[27].append(new_item)
################################################################################################################
#### 2018
    elif new_item['datetime_beginning_utc'] >= 1514764800 and new_item['datetime_beginning_utc']<=1522537200:
        list_of_lists[28].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1522540800 and new_item['datetime_beginning_utc']<=1530399600:
        list_of_lists[29].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1530403200 and new_item['datetime_beginning_utc']<=1538348400:
        list_of_lists[30].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1538352000 and new_item['datetime_beginning_utc']<=1546297200:
        list_of_lists[31].append(new_item)
################################################################################################################
#### 2019
    elif new_item['datetime_beginning_utc'] >= 1546300800 and new_item['datetime_beginning_utc']<=1554073200:
        list_of_lists[32].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1554076800 and new_item['datetime_beginning_utc']<=1561935600:
        list_of_lists[33].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1561939200 and new_item['datetime_beginning_utc']<=1569884400:
        list_of_lists[34].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1569888000 and new_item['datetime_beginning_utc']<=1577833200:
        list_of_lists[35].append(new_item)
################################################################################################################
#### 2020
    elif new_item['datetime_beginning_utc'] >= 1577836800 and new_item['datetime_beginning_utc']<=1585695600:
        list_of_lists[36].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1585699200 and new_item['datetime_beginning_utc']<=1593558000:
        list_of_lists[37].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1593561600 and new_item['datetime_beginning_utc']<=1601506800:
        list_of_lists[38].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1601510400 and new_item['datetime_beginning_utc']<=1609455600:
        list_of_lists[39].append(new_item)
################################################################################################################
#### 2021
    elif new_item['datetime_beginning_utc'] >= 1609459200 and new_item['datetime_beginning_utc']<=1617231600:
        list_of_lists[40].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1617235200 and new_item['datetime_beginning_utc']<=1625094000:
        list_of_lists[41].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1625097600 and new_item['datetime_beginning_utc']<=1633042800:
        list_of_lists[42].append(new_item)
    elif new_item['datetime_beginning_utc'] >= 1633046400 and new_item['datetime_beginning_utc']<=1640991600:
        list_of_lists[43].append(new_item)
    else:
        print(str(new_item))
################################################################################################################
    
    
for j in range(43):
    file_to_upload = write_to_local(list_of_lists[j], list_of_filenames[j])
    target_file_name = BUCKET_FOLDER+'/'+ list_of_filenames[j]
    result_returned = upload_file_to_s3(file_to_upload, target_file_name)
    print(result_returned)



        
        
    