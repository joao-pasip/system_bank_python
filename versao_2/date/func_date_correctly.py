from datetime import datetime


def str_date_time():
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    date_time = datetime.fromtimestamp(ts)
    str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
    return str_date_time
