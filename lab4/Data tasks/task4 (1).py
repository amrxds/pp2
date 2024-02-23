import datetime

secondtdatetime = datetime.datetime(2005, 2 , 22 , 16, 35, 1, 23454)
currenttime = datetime.datetime.now()

time_difference = currenttime - secondtdatetime
dif_seconds = time_difference.total_seconds()

print(dif_seconds)
