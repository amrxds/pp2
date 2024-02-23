import datetime

currenttime = datetime.datetime.now()
minus_for_year, minus_for_month, minus_for_day = 0, 0, 5

if currenttime.day < 5:
    minus_for_month = 1
    minus_for_day = -26 
if currenttime.month == 1 and minus_for_month == 1:
    minus_for_year = 1
    minus_for_month = 11 - currenttime.month
 
print(datetime.datetime(currenttime.year - minus_for_year, currenttime.month - minus_for_month, currenttime.day - minus_for_day, currenttime.hour, currenttime.minute, currenttime.second))


