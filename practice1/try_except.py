x=1
y=1

try:
  result=x/y
except ZeroDivisionError as e:
  print('ゼロで割ることはできません.')
  print(e)
except NameError as e:
  print('変数が定義されていません.')
  print(e)
else:
  print(result)
  print('正常に終了しました')
finally:
  print('割り算を終了します')
  

  