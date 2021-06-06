
import json
import boto3
import time
###################################################################
# insert 
s3_client = boto3.client("s3")
S3_BUCKET = 'energy-temperature-data'
# SOURCE_FILE_PATH = 'open_weathermap_json/weather_history_duq.json'
# SOURCE_FILE_PATH = 'weather_2011.json'
LOCAL_FILE_SYS = "/tmp"
BUCKET_FOLDER = 'weather-data'

client = boto3.client('lambda')

def insert_ddb_table(json_data):
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-2:133803608902:function:energy-weather-lmp-tbl-cr-EnergyWeatherLmpCrudFunc-1LJ4PSNBUD3UJ',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(json_data)
        )
        
    return response

def get_file(SOURCE_FILE_PATH):
    obj = s3_client.get_object(Bucket=S3_BUCKET,Key=SOURCE_FILE_PATH)
    data = obj['Body'].read().decode('utf-8')
    weather_data = json.loads(data)
    return weather_data

    
# 'weather_2011.json',
#                         'weather_2012.json',
#                         'weather_2013.json',
#                         'weather_2014.json',
#                         'weather_2015.json',
#                         'weather_2016.json',
#                         'weather_2017.json',
#                         'weather_2018.json',
#                         'weather_2019.json',
#                         'weather_2020.json',

#  i= 1
#     for item in data_to_insert:
#         if i <=5:
#             print(str(item))
#         else:
#             break
#         i+=1
list_of_filenames = []
for i in range(2016,2017):
    for j in range(1,5):
        filename = 'weather_' +str(i)+'_Q'+str(j)
        list_of_filenames.append(filename)
        # print(filename)
insert_list = []
for item in list_of_filenames:
    file_path = BUCKET_FOLDER+'/'+item
    data_to_insert = get_file(file_path)
    item_counter = 0
    print('starting: '+file_path)
    for item in data_to_insert:
        insert_list.append(item)
        item_counter +=1
        if item_counter%300 == 0:
            ddb_response = insert_ddb_table(insert_list)
            print(str(ddb_response))
            insert_list = []
    if len(insert_list)>=1:
        ddb_response = insert_ddb_table(insert_list)
        print(str(ddb_response))
        print('completed: '+file_path)
        insert_list = []
