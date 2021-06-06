import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
# import requests

ddb = boto3.resource('dynamodb')
table = ddb.Table('energy_weather_lmp')

def json_response(data, response_code=200):
    return json.dumps(data), response_code, {'Content-Type': 'application/json'}

def insert_ddb_table(payload):
    response = table.put_item(Item=payload)
    return response

def update_ddb_table(payload, payload_type, load_area, occ_date):
    
    response = table.update_item(
        Key={
            'load_area_id': load_area,
            'occurance_date': occ_date
        },
        UpdateExpression="set "+payload_type+"=:info",
        ExpressionAttributeValues={
            ':info': payload
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
    
def parse_float_to_decimal(event_record):
    parsed_event_record = json.loads(json.dumps(event_record), parse_float=Decimal)
    return parsed_event_record

def prep_payload(event_record, payload_type):
    # parse float to decimal for ddb insert-update
    parsed_event_record = parse_float_to_decimal(event_record)
    
    # payload becomes nested dictionary with payload_type as key 
    payload = {payload_type: parsed_event_record}
    # extracts the load_area and date into top level of dictionary
    payload['load_area_id'] = payload[payload_type]['load_area']
    payload['occurance_date'] = payload[payload_type]['datetime_beginning_utc']
    return payload

def lambda_handler(event, context):
 # parse out event parameters
    for record in event:
            action_type = record.pop('action_type')
    
            if action_type == 'PUT':
                payload_type = record.pop('data_product')
                # at this point both action_type an payload_type have been popped from event.
                payload = prep_payload(record, payload_type)
                result = insert_ddb_table(payload)
            elif action_type == 'UPDATE':
                 payload_type = record.pop('data_product')
                 payload = parse_float_to_decimal(record)
                 load_area = payload['load_area']
                 occ_date = payload['datetime_beginning_utc']
                 result = update_ddb_table(payload, payload_type, load_area, occ_date)
            else:
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "message": "No Action Defined",
                        # "location": ip.text.replace("\n", "")
                    }),
                }
    return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Insert-Update Completed Sucessfully",
                    # "location": ip.text.replace("\n", "")
                }),
            }