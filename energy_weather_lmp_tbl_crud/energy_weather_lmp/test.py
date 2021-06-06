import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import gzip
import awswrangler.secretsmanager as sm
import uuid
import requests
import boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table('energy_weather_lmp')

def json_response(data, response_code=200):
    return json.dumps(data), response_code, {'Content-Type': 'application/json'}

def insert_ddb_table(payload):
    table.put_item(Item=payload)
    return json_response({"message": "record created"})

def gitrdun(payload):
 # parse out event parameters
    action_type = payload.pop('action_type')
    print(payload)
    
    if action_type == 'PUT':
        result = insert_ddb_table(payload)
        print(result)
        

api_key = sm.get_secret_json("pjmApiKey").get('api_key')

headers = {'Ocp-Apim-Subscription-Key': api_key,}
get_path="/api/v1/hrl_load_metered?%s"
fields = 'datetime_beginning_ept, load_area, mw, is_verified'
from_to_dates = '2021-04-01 00:00 to 2021-04-01 23:00'
load_area_cds = 'DAY'

params = urllib.parse.urlencode({
    # Request parameters
    'download': 'TRUE',
    'rowCount': '100',
    'sort': 'datetime_beginning_ept',
    'order': 'asc',
    'startRow': '1',
    'fields': fields,
    'datetime_beginning_ept': from_to_dates,
    'load_area': load_area_cds,
})
#print(params)
conn = http.client.HTTPSConnection('api.pjm.com')
conn.request("GET", get_path % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
#print(data)
conn.close()
response_data = gzip.decompress(data)
response_data = response_data.decode('utf-8')

json_obj = json.loads(response_data)
print(json_obj)

# for elt in json_obj:
#     dict_data = elt
#     #payload_type = 'hrl_load_metered'
#     dict_data = {'hrl_load_metered':elt}
#     dict_data['action_type'] = 'PUT'
#     dict_data['load_area_Id'] = dict_data['hrl_load_metered']['load_area']
#     dict_data['occurance_date'] = dict_data['hrl_load_metered']['datetime_beginning_ept']
#     dict_data['hrl_load_metered']['mw'] = str(dict_data['hrl_load_metered']['mw'])
#     dict_data['hrl_load_metered']['is_verified'] = str(dict_data['hrl_load_metered']['is_verified'])
#     # action_type = dict_data.pop('action_type')
#     gitrdun(dict_data)

    # action_type = dict_data.pop('action_type')
    # payload_type = dict_data.pop('payload_type')
    # payload = dict_data[payload_type]
    # dict_data = dict_data.pop()

# print(action_type)
# print(payload_type)
# print(payload)
# print(dict_data)


    
