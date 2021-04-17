import json
import boto3
from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)
ddb = boto3.resource('dynamodb')
table = ddb.Table('energy_usage')

@app.route('/')
def index():
    return json_response({"message": "Energy Usage Planning"})
    
@app.route('/hello')
def hello():
    return json_response({"message": "hello world!"})
    
@app.route('/meters', methods=['GET', 'POST'])
def put_list_meters():
    if request.method == 'GET':
        meters = table.scan()['Items']
        return json_response(meters)
    else:
        table.put_item(Item=request.form.to_dict())
        return json_response({"message": "meter entry created"})


@app.route('/meters/<meterId>', methods=['GET', 'PATCH', 'DELETE'])
def get_patch_delete_meter(meterId):
    key = {'meterId': meterId}
    if request.method == 'GET':
        meter = table.get_item(Key=key).get('Item')
        if meter:
            return json_response(meter)
        else:
            return json_response({"message": "meter not found"}, 404)
    elif request.method == 'PATCH':
        attribute_updates = {key: {'Value': value, 'Action': 'PUT'}
                             for key, value in request.form.items()}
        table.update_item(Key=key, AttributeUpdates=attribute_updates)
        return json_response({"message": "meter entry updated"})
    else:
        table.delete_item(Key=key)
        return json_response({"message": "meter entry deleted"})


def json_response(data, response_code=200):
    return json.dumps(data), response_code, {'Content-Type': 'application/json'}