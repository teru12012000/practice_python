x=['a','b','c']
print(x)
print(len(x))
print(x[1])

#要素追加
x.append('e')
print(x)

#要素を削除
x.remove('b')
print(x)

#リストの結合(2通り)
x=['a','b','c']
y=['e','f']
#1通り目
x.extend(y)
print(x)
#2通り目
x=['a','b','c']
y=['e','f']
z=x+y
print(z)

#リストの分割
x=['a','b','c','d','e']
print(x[1:])
print(x[:3])
print(x[1:4])