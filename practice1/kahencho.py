'''
def func(*args):
  print(args)
'''

def func(*args,x):
  result=', '.join(args)  
  print(f'{x}:{result}')
'''
func(1)
func(1,3,10)
'''
func('あ',x=1)
func('あ','A','a',x=2)

'''
print文は可変長関数でできている
'''
#辞書version
def func1(**kwargs):
  print(kwargs)
  
func1(name='斎藤')
func1(name='鈴木',id=1,type='02')