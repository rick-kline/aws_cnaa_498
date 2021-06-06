import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import gzip
import awswrangler.secretsmanager as sm
import uuid
import requests
import boto3
import datetime as dt
from dateutil.parser import parse
import time

client = boto3.client('lambda')

def get_data(data_product, from_to_dates, load_area_to_get, start_row):
    api_key = sm.get_secret_json("pjmApiKey").get('api_key')
    get_path = "/api/v1/"+data_product+"?%s"
    headers = {'Ocp-Apim-Subscription-Key': api_key,}
    
    if data_product == 'hrl_load_metered':
        params = urllib.parse.urlencode({
            # Request parameters
            'download': 'TRUE',
            'rowCount': '1000',
            'sort': 'datetime_beginning_ept',
            'order': 'asc',
            'startRow': start_row,
            'fields': 'datetime_beginning_ept, nerc_region, mkt_region, zone, load_area, mw, is_verified',
            'datetime_beginning_ept': from_to_dates,
            'load_area': load_area_to_get,
        })
    elif data_product == 'load_frcstd_7_day': #not gzipped
        params = urllib.parse.urlencode({
            # Request parameters
            'download': 'TRUE',
            'rowCount': '1000',
            'sort': 'forecast_datetime_beginning_ept',
            'order': 'asc',
            'startRow': start_row,
            'fields': 'evaluated_at_datetime_utc, evaluated_at_datetime_ept, forecast_datetime_beginning_ept, forecast_datetime_ending_ept, forecast_area, forecast_load_mw',
            'forecast_datetime_beginning_ept': from_to_dates,
            'forecast_area': load_area_to_get,
        })
    elif data_product == 'load_frcstd_hist': #not gzipped
        params = urllib.parse.urlencode({
            # Request parameters
            'download': 'TRUE',
            'rowCount': '1000',
            'sort': 'forecast_hour_beginning_ept',
            'order': 'asc',
            'startRow': start_row,
            'fields': 'evaluated_at_ept, forecast_hour_beginning_ept, forecast_area, forecast_load_mw',
            'forecast_hour_beginning_ept': from_to_dates,
            'forecast_area': load_area_to_get,
        })
    elif data_product == 'da_hrl_lmps':
        params = urllib.parse.urlencode({
            # Request parameters
            'download': 'TRUE',
            'rowCount': '50000',
            'sort': 'datetime_beginning_ept',
            'order': 'asc',
            'startRow': start_row,
            'fields': 'datetime_beginning_utc, zone, system_energy_price_da, total_lmp_da, congestion_price_da, marginal_loss_price_da',
            'datetime_beginning_utc': from_to_dates,
            'type': 'LOAD',
            'zone': load_area_to_get,
            'row_is_current': 'TRUE',
        })
    # elif data_product == 'da_hrl_lmps':
    #     params = urllib.parse.urlencode({
    #         # Request parameters
    #         'download': 'TRUE',
    #         'rowCount': '50000',
    #         'sort': 'datetime_beginning_ept',
    #         'order': 'asc',
    #         'startRow': start_row,
    #         'fields': 'datetime_beginning_ept, zone, system_energy_price_da, total_lmp_da, congestion_price_da, marginal_loss_price_da',
    #         'datetime_beginning_ept': from_to_dates,
    #         'type': 'LOAD',
    #         'zone': load_area_to_get,
    #         'row_is_current': 'TRUE',
    #     })
    else: # rt_hrl_lmps
        params = urllib.parse.urlencode({
            # Request parameters
            'download': 'TRUE',
            'rowCount': '50000',
            'sort': 'datetime_beginning_ept',
            'order': 'asc',
            'startRow': start_row,
            'fields': "datetime_beginning_ept, zone, system_energy_price_rt, total_lmp_rt, congestion_price_rt, marginal_loss_price_rt",
            'datetime_beginning_ept': from_to_dates,
            'type': 'LOAD',
            'zone': load_area_to_get,
            'row_is_current': 'TRUE', 
         })
    
    conn = http.client.HTTPSConnection('api.pjm.com')
    conn.request("GET", get_path % params, "{body}", headers)
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read()
        if data:
            print("Got response.read")
            conn.close()
            response_data = gzip.decompress(data)
            response_data = response_data.decode('utf-8')
            response_json = json.loads(response_data)
            for item in response_json:
                has_key = checkKey(item, 'zone')
                if has_key == 1:
                   item['load_area'] = item.pop('zone') 
            return response_json
        else:
            response_json = {}
            return response_json
    else:
        conn.close()
        print("response status: ", str(response.status))
        

def insert_ddb_table(json_data, data_product):
    i=1
    for item in json_data:
        if i <=5:
            item['action_type'] = "PUT"
            item['data_product'] = data_product
            response = client.invoke(
            FunctionName = 'arn:aws:lambda:us-east-2:133803608902:function:energy-weather-lmp-tbl-cr-EnergyWeatherLmpCrudFunc-1LJ4PSNBUD3UJ',
            InvocationType = 'RequestResponse',
            Payload = json.dumps(json_data)
            )
            print(response)
        i = i+1
  
    return i
    
def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    new_date = (date.replace(day=d,month=m, year=y))
    # return new_date.strftime('%Y-%m-%d')
    return new_date-dt.timedelta(minutes=1)

def get_date_list_to_pull_month(start_date_str, end_date_str):
    end_date   = parse(end_date_str)
    start_date = parse(start_date_str)
    from_to_date_list = []

    strt_pull_at = start_date
    end_pull_at = monthdelta(start_date, 1)

    while end_pull_at <= end_date:
        from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M')
        from2date_dict = {'from_to_dates' : from_to_dates}
        from_to_date_list.append(from2date_dict)
        ## Next date range
        strt_pull_at = end_pull_at+dt.timedelta(minutes=1)
        end_pull_at = monthdelta(strt_pull_at, 1)
        
    return from_to_date_list    

def get_date_list_to_pull_day(start_date_str, end_date_str):
    end_date   = parse(end_date_str)
    start_date = parse(start_date_str)
    from_to_date_list = []

    strt_pull_at = start_date
    end_pull_at =start_date+dt.timedelta(hours=24)-dt.timedelta(minutes=1)

    while end_pull_at <= end_date:
        from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M')
        from2date_dict = {'from_to_dates' : from_to_dates}
        from_to_date_list.append(from2date_dict)
        ## Next date range
        strt_pull_at = end_pull_at+dt.timedelta(minutes=1)
        end_pull_at = strt_pull_at+dt.timedelta(hours=24)-dt.timedelta(minutes=1)
        # print(end_pull_at)
        
    return from_to_date_list
    
def checkKey(dict, key):
    if key in dict.keys():
        return 1
    else:
        return 0

def dedupe_list(data):
    res_list = [i for n, i in enumerate(data) if i not in data[n + 1:]]
    return res_list

def reduce_lmp(data, data_product):
    date_begin_ept = '1900-01-01T00:00:00'
    new_payload = []
    payload = []
    if data_product == "da_hrl_lmps":
        suffix = "_da"
    else:
        suffix = "_rt"
    
    for item in data:
        if item['datetime_beginning_ept'] == date_begin_ept:
            continue
        else:
            date_begin_ept = item['datetime_beginning_ept']
            for item2 in data:
                if item2['datetime_beginning_ept'] == date_begin_ept:
                    payload.append(item2)
            system_energy_price_da = round(sum(d['system_energy_price'+suffix] for d in payload) / len(payload),2)
            total_lmp_da = round(sum(d['total_lmp'+suffix] for d in payload) / len(payload),2)
            congestion_price_da = round(sum(d['congestion_price'+suffix] for d in payload) / len(payload),2)
            marginal_loss_price_da = round(sum(d['marginal_loss_price'+suffix] for d in payload) / len(payload),2)
            for item3 in payload:
                item3['system_energy_price'+suffix] = system_energy_price_da
                item3['total_lmp'+suffix] = total_lmp_da
                item3['congestion_price'+suffix] = congestion_price_da
                item3['marginal_loss_price'+suffix] = marginal_loss_price_da
            dup_list = dedupe_list(payload)
            new_payload.append(dup_list[0])
            payload = []
        
    return new_payload


# def lambda_handler(event, context):
#     path           = event['DataProductPath']
#     data_product   = event['DataProduct']
#     dates_str      = event['DataDateRange']
#     load_area_list = event['LoadAreas']

#  "/api/v1/load_frcstd_7_day/metadata?%s"
#  "/api/v1/load_frcstd_7_day?%s"
#  "/api/v1/load_frcstd_7_day?%s"

# data_product   = "da_hrl_lmps"
# data_product   = "rt_hrl_lmps"
data_product   = 'hrl_load_metered'
start_date_str = "2021-01-01 00:00"
end_date_str   = "2021-06-30 23:59"
load_area_list = ["DUQ"]
start_row = 1

if data_product == "da_hrl_lmps" or data_product == "rt_hrl_lmps":
    from_to_date_list = get_date_list_to_pull_day(start_date_str, end_date_str)
else:
    from_to_date_list = get_date_list_to_pull_month(start_date_str, end_date_str)
    
for load_area in load_area_list:
    for date_item in from_to_date_list:
        # time.sleep(30)
        print(date_item)
        data = get_data(data_product, date_item['from_to_dates'], load_area, start_row)
        if bool(data) == 0:
            print("no data found")
            continue
        else:
            if data_product == "da_hrl_lmps" or data_product == "rt_hrl_lmps":
                print("len before: ", str(len(data)))
                data = reduce_lmp(data, data_product)
                print(date_item['from_to_dates'])
            result = insert_ddb_table(data, data_product)
            print(result)
        



    
    