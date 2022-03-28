'''
集合
重複はできない
グループ全体の処理に使える

タプル
戻り値やfor文のときに変数を2つ用意しなくていい
'''




x_set={11,222,333}
y_list=[11,333,444,555,11]
y_set=set(y_list)

result=x_set&y_set
print(result)

result=x_set-y_set
print(result)

result=x_set|y_set

print(result)

x_tuple=(1,3,5)
y_list=[3,4,5]
y_tuple=tuple(y_list)

result=x_tuple+y_tuple

print(result)




