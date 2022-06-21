'''
今年があと年日あるか今日の日付を算出して「今年はあと○○日」と出力する
'''
from datetime import date
d_today=date.today()
new_year=date(d_today.year+1,1,1)
deff=new_year-d_today
print(f'今年はあと{deff.days}日です')
