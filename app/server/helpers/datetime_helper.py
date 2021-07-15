from datetime import timedelta, date, datetime
from datetime import timezone
# import datetime
import time


def generate_start_end_day_unix_string(date_str=None):
    dt = date.today()
    if date_str == 'yesterday':
        yest = dt - timedelta(days=1)
        st = datetime.combine(yest, datetime.min.time())
        et = datetime.combine(yest, datetime.max.time())
    else:
        st = datetime.combine(dt, datetime.min.time())
        et = datetime.combine(dt, datetime.max.time())

    stunix = time.mktime(st.timetuple())
    etunix = time.mktime(et.timetuple())
    return {"stunix": stunix, "etunix": etunix}


def generate_start_end_day_unix_string_rush_hour(date_str=None):
    dt = date.today()
    if date_str == 'yesterday':
        yest = dt - timedelta(days=1)
        data_from_date = yest - timedelta(days=7)
        st = datetime.combine(data_from_date, datetime.min.time())
        et = datetime.combine(yest, datetime.max.time())
    else:
        data_from_date = dt - timedelta(days=7)
        st = datetime.combine(data_from_date, datetime.min.time())
        et = datetime.combine(dt, datetime.max.time())

    stunix = time.mktime(st.timetuple())
    etunix = time.mktime(et.timetuple())
    return {"stunix": stunix, "etunix": etunix}
