# def get_date_list_to_pull(start_date_str, end_date_str):
#     end_date   = parse(end_date_str)
#     start_date = parse(start_date_str)
#     from_to_date_list = []

#     strt_pull_at = start_date
#     end_pull_at = monthdelta(start_date, 1)

#     while end_pull_at <= end_date:
#         from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M:%S') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M:%S')
#         from2date_dict = {'from_to_dates' : from_to_dates}
#         from_to_date_list.append(from2date_dict)
#         ## Next date range
#         strt_pull_at = end_pull_at+dt.timedelta(seconds=1)
#         end_pull_at = monthdelta(strt_pull_at, 1)
        
#     return from_to_date_list

# txt = "ZAK, JJK, RRK"

# x = txt.split(", ")

# for i in x:
#     print(i)

#  "/api/v1/hrl_load_metered?%s"

# json_data = [{'datetime_beginning_ept': '2021-04-01T00:00:00', 'load_area': 'DUQ', 'mw': 1203.486, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T01:00:00', 'load_area': 'DUQ', 'mw': 1181.749, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T02:00:00', 'load_area': 'DUQ', 'mw': 1169.382, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T03:00:00', 'load_area': 'DUQ', 'mw': 1176.572, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T04:00:00', 'load_area': 'DUQ', 'mw': 1191.784, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T05:00:00', 'load_area': 'DUQ', 'mw': 1270.231, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T06:00:00', 'load_area': 'DUQ', 'mw': 1361.627, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T07:00:00', 'load_area': 'DUQ', 'mw': 1423.37, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T08:00:00', 'load_area': 'DUQ', 'mw': 1471.421, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T09:00:00', 'load_area': 'DUQ', 'mw': 1524.708, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T10:00:00', 'load_area': 'DUQ', 'mw': 1542.755, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T11:00:00', 'load_area': 'DUQ', 'mw': 1547.2, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T12:00:00', 'load_area': 'DUQ', 'mw': 1550.807, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T13:00:00', 'load_area': 'DUQ', 'mw': 1551.094, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T14:00:00', 'load_area': 'DUQ', 'mw': 1539.852, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T15:00:00', 'load_area': 'DUQ', 'mw': 1522.178, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T16:00:00', 'load_area': 'DUQ', 'mw': 1510.593, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T17:00:00', 'load_area': 'DUQ', 'mw': 1499.112, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T18:00:00', 'load_area': 'DUQ', 'mw': 1515.148, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T19:00:00', 'load_area': 'DUQ', 'mw': 1538.258, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T20:00:00', 'load_area': 'DUQ', 'mw': 1556.398, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T21:00:00', 'load_area': 'DUQ', 'mw': 1537.382, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T22:00:00', 'load_area': 'DUQ', 'mw': 1472.698, 'is_verified': False}, {'datetime_beginning_ept': '2021-04-01T23:00:00', 'load_area': 'DUQ', 'mw': 1398.897, 'is_verified': False}]

# for item in json_data:
#     item['action_type'] = "PUT"
#     item['data_product'] = "hrly_metered_load"

# print (json_data)
# import pandas as pd
# import datetime as dt
# from dateutil.parser import parse

# def monthdelta(date, delta):
#     m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
#     if not m: m = 12
#     d = min(date.day, [31,
#         29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
#     new_date = (date.replace(day=d,month=m, year=y))
#     # return new_date.strftime('%Y-%m-%d')
#     return new_date-dt.timedelta(seconds=1)

# start_date_str = "2021-01-01 00:00"
# end_date_str = "2021-04-01 23:59"

# end_date = parse(end_date_str)
# start_date = parse(start_date_str)

# strt_pull_at = start_date
# end_pull_at = monthdelta(start_date, 1)

# # print(strt_pull_at) 
# # print(end_pull_at)
# from_to_date_list = []

# while end_pull_at <= end_date:
#     # print("start: "+ strt_pull_at.strftime('%Y-%m-%d %H:%M:%S'))
#     # print("end: "+ end_pull_at.strftime('%Y-%m-%d %H:%M:%S'))
#     # print('')
#     from_to_dates = strt_pull_at.strftime('%Y-%m-%d %H:%M:%S') + ' to ' + end_pull_at.strftime('%Y-%m-%d %H:%M:%S')
#     from2date_dict = {'from_to_dates' : from_to_dates}
#     from_to_date_list.append(from2date_dict)
    
#     strt_pull_at = end_pull_at+dt.timedelta(seconds=1)
#     end_pull_at = monthdelta(strt_pull_at, 1)

# print(from_to_date_list)


# path           = "/api/v1/da_hrl_lmps?%s"
# data_product   = "da_hrl_lmps"

# path           = "/api/v1/"+data_product+"?%s"

# print(path)

# data = [{'datetime_beginning_ept': '2021-04-01T00:00:00', 'pnode_id': 21601665, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T1', 'type': 'LOAD', 'system_energy_price_da': 17.71, 'total_lmp_da': 17.83, 'congestion_price_da': 0.01, 'marginal_loss_price_da': 0.11, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-04-01T00:00:00', 'pnode_id': 21601666, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T2', 'type': 'LOAD', 'system_energy_price_da': 17.71, 'total_lmp_da': 17.83, 'congestion_price_da': 0.01, 'marginal_loss_price_da': 0.11, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-04-01T00:00:00', 'pnode_id': 21601667, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2A SS', 'type': 'LOAD', 'system_energy_price_da': 17.71, 'total_lmp_da': 17.55, 'congestion_price_da': 0.01, 'marginal_loss_price_da': -0.17, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-04-01T00:00:00', 'pnode_id': 21601668, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2B SS', 'type': 'LOAD', 'system_energy_price_da': 17.71, 'total_lmp_da': 17.55, 'congestion_price_da': 0.01, 'marginal_loss_price_da': -0.17, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-04-01T00:00:00', 'pnode_id': 21601669, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '1B SS', 'type': 'LOAD', 'system_energy_price_da': 17.71, 'total_lmp_da': 17.55, 'congestion_price_da': 0.01, 'marginal_loss_price_da': -0.17, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601665, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T1', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.25, 'congestion_price_da': 0.69, 'marginal_loss_price_da': -0.44, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601666, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T2', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.25, 'congestion_price_da': 0.69, 'marginal_loss_price_da': -0.44, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601667, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2A SS', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601668, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2B SS', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601669, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '1B SS', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}
# ]

# test_list = [{'datetime_beginning_ept': '2021-01-01T00:00:00',  'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}]

# test_list = [{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601665, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T1', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601666, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T2', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601667, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2A SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601668, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2B SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601669, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '1B SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}]

# res_list = [i for n, i in enumerate(test_list) if i not in test_list[n + 1:]]

# print(res_list)

# [{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}]


# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601665, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.25, 'congestion_price_da': 0.69, 'marginal_loss_price_da': -0.44, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601666, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.25, 'congestion_price_da': 0.69, 'marginal_loss_price_da': -0.44, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601667, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601668, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_id': 21601669, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}


# int_dict = [{'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_name': 'BETTIS', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.3, 'congestion_price_da': 0.67, 'marginal_loss_price_da': -0.37, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_name': 'BOCGASES', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.3, 'congestion_price_da': 0.67, 'marginal_loss_price_da': -0.37, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_name': 'BRENTWOO', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.29, 'congestion_price_da': 0.68, 'marginal_loss_price_da': -0.39, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'},
# {'datetime_beginning_ept': '2021-05-01T00:00:00', 'pnode_name': 'BRUNOTIS', 'voltage': '138 KV', 'type': 'LOAD', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.25, 'congestion_price_da': 0.72, 'marginal_loss_price_da': -0.47, 'load_area': 'DUQ', 'action_type': 'PUT', 'data_product': 'da_hrl_lmps'}]

# for item in int_dict:
#     item.pop('pnode_name')
# print(int_dict)
# import collections, functools, operator

# result = dict(functools.reduce(operator.add,
#          map(collections.Counter, int_dict)))
  
# print("resultant dictionary : ", str(result))

# payload = {payload_type: event_record}
#     # extracts the load_area and date into top level of dictionary
#     payload['load_area_Id'] = payload[payload_type]['load_area']
#     payload['occurance_date'] = payload[payload_type]['datetime_beginning_ept']
# import collections, functools, operator

int_dict =[{'datetime_beginning_ept': '2021-05-01T00:00:00', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.06, 'congestion_price_da': 0.75, 'marginal_loss_price_da': -0.69},
{'datetime_beginning_ept': '2021-05-01T00:00:00', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.3, 'congestion_price_da': 0.67, 'marginal_loss_price_da': -0.37},
{'datetime_beginning_ept': '2021-05-01T00:00:00', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.3, 'congestion_price_da': 0.67, 'marginal_loss_price_da': -0.37}, 
{'datetime_beginning_ept': '2021-05-01T00:00:00', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.29, 'congestion_price_da': 0.68, 'marginal_loss_price_da': -0.39},
{'datetime_beginning_ept': '2021-05-01T00:00:00', 'system_energy_price_da': 23.0, 'total_lmp_da': 23.25, 'congestion_price_da': 0.72, 'marginal_loss_price_da': -0.47},
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35},
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35},
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66},
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66},
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66}]

def dedupe_list(data):
    res_list = [i for n, i in enumerate(data) if i not in data[n + 1:]]
    return res_list

date_begin_ept = '1900-01-01T00:00:00'
new_payload = []
payload = []
data_product = "da_hrl_lmps"

if data_product == "da_hrl_lmps":
        suffix = "_da"
else:
    suffix = "_rt"

for item in int_dict:
    if item['datetime_beginning_ept'] == date_begin_ept:
        continue
    else:
        date_begin_ept = item['datetime_beginning_ept']
        for item2 in int_dict:
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
        
print(new_payload)

[{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601665, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T1', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601666, 'pnode_name': 'ARSENAL', 'voltage': '138 KV', 'equipment': 'T2', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.94, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.35, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601667, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2A SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601668, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '2B SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601669, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '1B SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601670, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': '1A SS', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'},
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601671, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': 'ERF3B', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601672, 'pnode_name': 'BEAV DUQ', 'voltage': '138 KV', 'equipment': 'ERF3A', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.63, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.66, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601674, 'pnode_name': 'BETTIS', 'voltage': '138 KV', 'equipment': 'LOADB', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.99, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.3, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}, 
{'datetime_beginning_ept': '2021-01-01T00:00:00', 'pnode_id': 21601675, 'pnode_name': 'BETTIS', 'voltage': '138 KV', 'equipment': 'LOADA', 'type': 'LOAD', 'system_energy_price_da': 19.29, 'total_lmp_da': 18.99, 'congestion_price_da': 0.0, 'marginal_loss_price_da': -0.3, 'row_is_current': True, 'version_nbr': 1, 'load_area': 'DUQ'}]