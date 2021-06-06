import json
import boto3
from boto3.dynamodb.conditions import Key

# def lambda_handler(event, context):
client = boto3.resource('dynamodb')
table = client.Table('energy_weather_lmp')


response = table.get_item(
	Key={
		'load_area_id': 'DUQ',
		'occurance_date': 1559779200
	}
)

new_item = 
print(str(response['Item']))