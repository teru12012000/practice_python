'''
辞書型とは
キーと値がペアになっている
'''

x={'リンゴ':120,'バナナ':300,'いちご':450}
print(x)

banana=x['バナナ']
print(banana)

#要素追加
x['トマト']=340
print(x)

#キーの値変更

x['いちご']=350
print(x)

#結合
x={'リンゴ':120,'バナナ':300,'いちご':450}
y={'トマト':280,'梨':150}
x.update(y)
print(x)

x={'リンゴ':120,'バナナ':300,'いちご':450}
y={'トマト':280,'梨':150}
x.update(y)
print(y)

'''
python3.9~
z=x|y
でも結合できる
'''

#辞書のfor

x_dict={'apple':100,'banana':350}
for key,value in x_dict.items():
  text=key+'は'+str(value)+'円です'
  print(text)