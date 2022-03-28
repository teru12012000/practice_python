sales_2020=[400239,560231,542490]
sales_2019=[489028,400123,442489]

for current,previous in zip(sales_2020,sales_2019):
  print(current,previous)
  result=(current/previous-1)*100
  print(f'{result:.1f}%')
  
names=['鈴木','斎藤','大川']
for i,n in enumerate(names,start=1):
 print(f'{i}位:{n}') 