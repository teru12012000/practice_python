from dataclasses import field,dataclass
from typing import List
'''
classを書くときにちょー楽になる.
デフォルト値を設定することができるけど
設定しないものの後に書く
'''
@dataclass
class User:
  name:str
  age:int
  items:list=field(default_factory=list)
user=User('sato',10)
print(user.items)
'''
python3.8.0のときはlistでOK
'''