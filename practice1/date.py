from datetime import date, timedelta
from datetime import time
from datetime import datetime
from datetime import timezone,timedelta,datetime
import jpholiday
date_today=['月','火','水','木','金','土']
t=date.today()
print(t)
print(t.year)#年
print(t.month)#月
print(t.day)#日
print(t.weekday())
'''
曜日は0~6で示され順に
月火水木金土日となる
'''
print(date_today[t.weekday()])
d=date(2020,12,24)
print(d)


t=time(12,15,30,0)
print(t)
print(t.hour)#時
print(t.minute)#分
print(t.second)#秒
print(t.microsecond)#マイクロ秒

n=datetime.now()
print(n)

d1=datetime(2021,5,2)
d2=datetime(2021,5,1)
result=d1-d2
print(result)
print(result.days)

result=d1+timedelta(days=10)
print(result)


JST=timezone(timedelta(hours=+9))

t=datetime(2020,1,1,12,15,30,tzinfo=JST)
print(t)

print(jpholiday.year_holidays(2021))