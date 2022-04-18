from dateutil.relativedelta import relativedelta
from datetime import datetime
import calendar

today=datetime.today()
print(today)

d1=today-relativedelta(months=7)
print(d1)

'''
文字列にするときはstrftime
'''

today_str=today.strftime('%Y年%m月%d日')
print(today_str)

c=calendar.month(2021,1)
print(c)

'''
月末の表示に便利！！！
'''

w,days=calendar.monthrange(2020, 2)
print(days)