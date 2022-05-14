from datetime import datetime,time,date,timedelta


now = datetime.utcnow()
now =[now.year, now.month, now.day, now.hour]

date2 = date(now[0], now[1], now[2])
time2 = time(now[3])

date1 = datetime.combine(date2, time2)
print(date1)

date1 += timedelta(days=1)

print(date1)