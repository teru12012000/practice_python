from unicodedata import name


def func2():
  print('func2です')
  
def func3():
  print('func3です')


'''
if __name__ == '__main__'
がないとmodule1.pyを実行したときに
一緒にfunc3()も実行されてしまう
'''  
if __name__=='__main__':
  func3()
