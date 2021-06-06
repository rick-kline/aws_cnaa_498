import datetime as dt
from dateutil.parser import parse

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    new_date = (date.replace(day=d,month=m, year=y))
    # return new_date.strftime('%Y-%m-%d')
    return new_date-dt.timedelta(seconds=1)
    
def get_date_list_to_pull(start_date_str, end_date_str):
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
    

start_date_str = "2021-01-01 00:00"
end_date_str   = "2021-06-30 23:59"

from_to_date_list = get_date_list_to_pull(start_date_str, end_date_str)

for i in from_to_date_list:
    print(i)
    
# end_date   = parse(end_date_str)
# start_date = parse(start_date_str)
#     # from_to_date_list = []

# strt_pull_at = start_date
# end_pull_at =start_date+dt.timedelta(days=1)-dt.timedelta(seconds=1)

# print(strt_pull_at)
# print(end_pull_at)