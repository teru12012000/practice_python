'''
複数のファイルから共通の数字を出力しろ
'''
from pathlib import Path
data_path='./data'
txt_file=list(Path(data_path).glob('*.txt'))

def read_num(file):
  with open(file) as f:
    numbers=set([x.strip() for x in f.readlines()])
  return numbers    

dep_num=read_num(txt_file[0])

for file in txt_file[1:]:
  numbers=read_num(file)
  dep_num=dep_num & numbers

for i in dep_num:
  print(i)
  
'''
共通の数字を出せというときには
積集合を使うといい
'''