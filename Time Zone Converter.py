import datetime as dt
import pytz

timezone_nw = pytz.timezone('America/New_York')
nw_datetime_obj = dt.datetime.now(timezone_nw)

timezone_london = pytz.timezone('Europe/London')
london_datetime_obj = nw_datetime_obj.astimezone(timezone_london)


print('America/New_York:', nw_datetime_obj)
print('Europe/London:', london_datetime_obj)