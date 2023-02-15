import datetime


def is_valid_date(*, date_string):
    try:
        datetime.datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False
