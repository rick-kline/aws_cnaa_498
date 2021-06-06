# from datetime import datetime
# from time import mktime
# import json
# from dateutil.parser import parse

import datetime as dt
from dateutil.parser import parse
import time
from datetime import datetime


# dict_data = {'datetime_beginning_ept': '2021-05-01T00:00:00', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.3, 'congestion_price_da': 0.67, 'marginal_loss_price_da': -0.37}

# ept_datetm = parse(dict_data['datetime_beginning_ept'])

# dict_data['datetime_beginning_ept'] = mktime(ept_datetm.timetuple())
# ts = dict_data['datetime_beginning_ept']
# print(type(dict_data['datetime_beginning_ept']))
# print(dict_data)
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


# To do:
#   Change all dates to UTC --done
#   work on not closing connection after every pull from pjm

# def get_date_list_to_pull_10_day(start_date_str, end_date_str):
#     end_date   = parse(end_date_str)
#     start_date = parse(start_date_str)
#     from_to_date_list = []

#     strt_pull_at = start_date
#     end_pull_at =start_date+dt.timedelta(days=10)-dt.timedelta(minutes=1)
#     end_date_ext = end_date+dt.timedelta(days=10)-dt.timedelta(minutes=1)

#     while end_pull_at <= end_date_ext:
#         from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M')
#         from2date_dict = {'from_to_dates' : from_to_dates}
#         from_to_date_list.append(from2date_dict)
#         ## Next date range
#         strt_pull_at = end_pull_at+dt.timedelta(minutes=1)
#         end_pull_at = strt_pull_at+dt.timedelta(days=10)-dt.timedelta(minutes=1)
#     return from_to_date_list

# start_date_str = "2021-05-01 00:00"
# end_date_str   = "2021-05-31 23:59"

# from_to_date_list = get_date_list_to_pull_10_day(start_date_str, end_date_str)

# print(from_to_date_list)

pull_count = 1
for i in range(12):
    print("count: "+str(i))
    print("pull_count: " + str(pull_count))
    countmod = pull_count%7
    if countmod ==0:
        print("countmod: " + str(countmod))
    pull_count+=1