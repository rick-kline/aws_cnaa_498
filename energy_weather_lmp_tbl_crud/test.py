import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

ddb = boto3.resource('dynamodb')
table = ddb.Table('energy_weather_lmp')

def update_ddb_table(payload, payload_type, load_area, occ_date):
    
    response = table.update_item(
        Key={
            'load_area_Id': load_area,
            'occurance_date': occ_date
        },
        UpdateExpression="set "+payload_type+"=:info",
        ExpressionAttributeValues={
            ':info': payload
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


load_area_Id = 'DUQ'
occurance_date = '2021-02-01T00:00:00'
payload_type = 'rt_hrl_lmps'
map_to_update = {'datetime_beginning_ept': '2021-04-01T00:00:00', 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69}
    
payload = json.loads(json.dumps(map_to_update), parse_float=Decimal)
get_response = update_ddb_table(payload, payload_type, load_area_Id, occurance_date)

print(get_response)

