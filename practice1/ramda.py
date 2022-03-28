func=lambda x,y:print(f'{x}さんは{y}です!')

func('鈴木','学生')

'''
ラムダ式は他の関数と組み合わせて使うこと
'''
names=['鈴木','斎藤','田中']
names2=['めい','ゆずき','ひなた']
result=list(map(lambda x,y:x+y+'さん',names,names2))
print(result)


numbers=[1,4,6,10,22,30]
result=list(filter(lambda x:x>=10,numbers))

print(result)

