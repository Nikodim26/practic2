import datetime

date_obj = datetime.datetime(2022, 3, 8, 15, 45, 0)
print(date_obj)

year = date_obj.year
month = date_obj.month
day = date_obj.day
hour = date_obj.hour
minute = date_obj.minute
second = date_obj.second

print(year, month, day, hour, minute, second)

date_string = date_obj.strftime("%d-%m-%Y %H:%M:%S")
print(date_string)
date_string = date_obj.strftime("%b")
print(date_string)

time_obj = datetime.datetime(2022, 3, 8, 15, 45, 0)
new_time_obj = time_obj + datetime.timedelta(hours=1, minutes=30)
print(new_time_obj)
date_obj = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(date_obj)

