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

def get_date_list_to_pull_10_day(start_date_str, end_date_str):
    end_date   = parse(end_date_str)
    start_date = parse(start_date_str)
    from_to_date_list = []

    strt_pull_at = start_date
    end_pull_at = end_date
    cntr = 0

    while end_pull_at <= end_date:
        if cntr == 0:
            strt_pull_at = start_date
            end_pull_at =start_date+dt.timedelta(days=10)-dt.timedelta(minutes=1)
        else:
            strt_pull_at = end_pull_at+dt.timedelta(minutes=1)
            end_pull_at = strt_pull_at+dt.timedelta(days=10)-dt.timedelta(minutes=1)
        
        if end_pull_at <= end_date:
            from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M')
            from2date_dict = {'from_to_dates' : from_to_dates}
            from_to_date_list.append(from2date_dict)
            
        if end_pull_at >= end_date:
            from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_date.strftime('%Y-%m-%d %H:%M')
            from2date_dict = {'from_to_dates' : from_to_dates}
            from_to_date_list.append(from2date_dict)
        cntr+=1
    return from_to_date_list
    
start_date_str = "2021-05-27 00:00"
end_date_str   = "2021-06-30 23:59"

from_to_date_list = get_date_list_to_pull_10_day(start_date_str, end_date_str)

for item in from_to_date_list:
    print(str(item))
    
# old version from 6/1
# def get_date_list_to_pull_10_day(start_date_str, end_date_str):
#     end_date   = parse(end_date_str)
#     start_date = parse(start_date_str)
#     from_to_date_list = []

#     strt_pull_at = start_date
#     end_pull_at =start_date+dt.timedelta(days=10)-dt.timedelta(minutes=1)
#     end_date_ext = end_date-dt.timedelta(minutes=1)

#     while end_pull_at <= end_date_ext:
#         from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M')
#         from2date_dict = {'from_to_dates' : from_to_dates}
#         from_to_date_list.append(from2date_dict)
#         ## Next date range
#         strt_pull_at = end_pull_at+dt.timedelta(minutes=1)
#         end_pull_at = strt_pull_at+dt.timedelta(days=10)-dt.timedelta(minutes=1)
#         if end_pull_at >= end_date_ext:
#             from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_date_ext.strftime('%Y-%m-%d %H:%M')
#             from2date_dict = {'from_to_dates' : from_to_dates}
#             from_to_date_list.append(from2date_dict)
#     return from_to_date_list