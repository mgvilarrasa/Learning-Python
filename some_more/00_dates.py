from datetime import datetime, time, date, timedelta

now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(f"{now.hour}:{now.minute}:{now.second}")
print(now.timestamp())

date_time = datetime(1989,1,7)
print(date_time)
print(date_time.timestamp())

print(now - date_time)

current_time = time()
print(current_time)
print(time(12,57,30))

current_date = date.today()
print(current_date)
print(date(2007,12,25))

current_delta = timedelta(12,hours=12, weeks=5)
print(current_delta)
print(current_delta.days)