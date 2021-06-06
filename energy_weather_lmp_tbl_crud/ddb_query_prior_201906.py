import json
import boto3
from boto3.dynamodb.conditions import Key

# def lambda_handler(event, context):
client = boto3.resource('dynamodb')
table = client.Table('energy_weather_lmp')

	#1. Example - Get Item By Id
	
def insert_ddb_table(payload):
    response = table.put_item(Item=payload)
    return response

 #Make Initial Query
response = table.query(
  KeyConditionExpression=Key('load_area_id').eq('DUQ') & Key('occurance_date').between(1451606400, 1546297200)
)

#Extract the Results
items = response['Items']
for item in items:
    new_item = {}
    ## Keys
    new_item['load_area_id'] = item['load_area_id']
    new_item['occurance_date'] = item['occurance_date']
    
    ## 'hrl_load_metered'
    item['hrl_load_metered'].pop('load_area')
    item['hrl_load_metered'].pop('datetime_beginning_utc')
    item['hrl_load_metered'].pop('mkt_region')
    item['hrl_load_metered'].pop('is_verified')
    item['hrl_load_metered'].pop('nerc_region')
    new_item['hrl_load_metered'] = item['hrl_load_metered']
    
    ## 'da_hrl_lmps'
    # new_item['da_hrl_lmps'] = item['da_hrl_lmps']
    # new_item['da_hrl_lmps'].pop('load_area', None)
    # new_item['da_hrl_lmps'].pop('datetime_beginning_utc', None)
    
    ## rt_hrl_lmps
    # new_item['rt_hrl_lmps'] = item['rt_hrl_lmps']
    # new_item['rt_hrl_lmps'].pop('load_area', None)
    # new_item['rt_hrl_lmps'].pop('datetime_beginning_utc', None)

    ## 'hrl_weather'
    new_item['hrl_weather'] = item['hrl_weather']['hrl_weather_data']
    # print(str(new_item['occurance_date']))
    result = insert_ddb_table(new_item)
    # print(str(result))
    
print("-----first----------"+str(new_item['occurance_date']))
    
while 'LastEvaluatedKey' in response:
    key = response['LastEvaluatedKey']
    response = table.query(
                    KeyConditionExpression=Key('load_area_id').eq('DUQ') & Key('occurance_date').between(1451606400, 1546297200), ExclusiveStartKey=key
                    )
    items = response['Items']
    for item in items:
        new_item = {}
        ## Keys
        new_item['load_area_id'] = item['load_area_id']
        new_item['occurance_date'] = item['occurance_date']
        
        ## 'hrl_load_metered'
        item['hrl_load_metered'].pop('load_area')
        item['hrl_load_metered'].pop('datetime_beginning_utc')
        item['hrl_load_metered'].pop('mkt_region')
        item['hrl_load_metered'].pop('is_verified')
        item['hrl_load_metered'].pop('nerc_region')
        new_item['hrl_load_metered'] = item['hrl_load_metered']
        
        ## 'da_hrl_lmps'
        # new_item['da_hrl_lmps'] = item['da_hrl_lmps']
        # new_item['da_hrl_lmps'].pop('load_area', None)
        # new_item['da_hrl_lmps'].pop('datetime_beginning_utc', None)
        
        ## rt_hrl_lmps
        # new_item['rt_hrl_lmps'] = item['rt_hrl_lmps']
        # new_item['rt_hrl_lmps'].pop('load_area', None)
        # new_item['rt_hrl_lmps'].pop('datetime_beginning_utc', None)
    
        ## 'hrl_weather'
        new_item['hrl_weather'] = item['hrl_weather']['hrl_weather_data']
        
        result = insert_ddb_table(new_item)
        # print(str(result))
        # print(str(new_item['occurance_date']))
   
    print("------second---------"+str(new_item['occurance_date']))


# 	print('\n\n\n-----\n\n\n')

# 	#2. Example 2 - Query by Partition Key / Sort Key Criteria

# 	response = table.query(
# 		KeyConditionExpression=Key('TransactionType_OriginCountry').eq('PURCHASE_USA') & Key('Date').gt('2019-11-15')
# 	)

# 	items = response['Items']
# 	for item in items:
# 		print(item)

# response = table.get_item(
# 	Key={
# 		'load_area_id': 'DUQ',
# 		'occurance_date': 1559779200
# 	}
# )

# print(str(response['Item']))