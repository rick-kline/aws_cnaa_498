# import json

# payload = {'datetime_beginning_ept': '2021-04-01T00:00:00', 'load_area': 'DUQ', 'mw': 1203.486, 'is_verified': False}

# print(payload)
  
# # using naive method
# # type converstion in list of dicts.
# for dicts in payload:
#     if isinstance(payload[dicts],str) == 0:
#         payload[dicts] = str(payload[dicts])
        
# print(payload)

# load_area_cds = "DUQ, DAY"
# load_area_list = load_area_cds.split(", ")

load_area_list = ['DUQ', 'DAY']


for load_area in load_area_list:
    print(load_area)