'''
dataの中からcsvファイルのファイル名を出力する
'''
from pathlib import Path
data_path='./data'
csv_file=Path(data_path).glob('*.csv')#globと正規表現を使ってcsvファイルを取得
for file in csv_file:
  print(file.name)#.nameとすることでファイル名のみを出力することができる