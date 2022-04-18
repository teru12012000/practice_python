'''
[a9あ]「a」か「9」か「あ」
[a-z]こもぃの英字1文字
[0-9]半角1文字
[a-zA-Z]
[^]ある集合以外の1文字
. 改行以外の1文字
^ 文字列の先頭
$ 文字列の末尾
＊ 直前の文字を0回以上繰り返し
+ 直前の文字を1回以上繰り返し
？ 直前の文字を0/1回繰り返し
'''
import re
s='090333'
m=re.match(r'[0-9]{3}',s)
print(m)

if m:
  print(m.group())
  print(m.span())
  
s='bananaは￥300です'
m=re.search(r'￥[1-9][0-9]*',s)

if m:
  print(m.group())
  print(m.span())
























