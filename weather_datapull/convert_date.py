# import datetime as dt
from dateutil.parser import parse
import time
from datetime import datetime, timedelta

def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//30))
               
def convert_to_unix(iso_date):
    unix_date = int(time.mktime(iso_date.timetuple()))
    return unix_date

now = datetime.now()
rnd_current_datetime = (hour_rounder(now))

start_pull_at = rnd_current_datetime-timedelta(days=5)

pull_date = start_pull_at

while pull_date <= rnd_current_datetime:
    print("pull_date: "+ str(pull_date))
    unix_pull_date = convert_to_unix(pull_date)
    print("unix_pull_date: "+ str(unix_pull_date))
    pull_date = pull_date + timedelta(days=1)
    

