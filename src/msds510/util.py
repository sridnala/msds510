import datetime
from datetime import date


def get_month(introValue):
    try:
        date_time_obj = datetime.datetime.strptime(introValue, '%b-%y')
    except:
        date_time_obj = datetime.datetime.strptime(introValue, '%d-%b')
    return date_time_obj.month


def get_date_joined(yearValue, introValue):
    try:
        date_time_str = yearValue + str(get_month(introValue)) + '01'
        date_time_obj = datetime.datetime.strptime(date_time_str, "%Y%m%d").date()
    except:
        print("Unable to join the date")
        return None
    return date_time_obj


def days_since_joined(yearValue, introValue):
    try:
        recordDate = get_date_joined(yearValue, introValue)
        currentDate = date.today()
        totalDays = (currentDate - recordDate).days
    except:
        print("Unable to count total number of days")
        return None
    return totalDays
