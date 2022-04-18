class WizardClass:
  def __init__(self):
    self.mp=100
    print('WizardClassのinit')
  def cast_spell(self):
    print('呪文を唱える')
  
class SwordFighterClass:
  def attack_with_sword(self):
    print('剣で攻撃をする')

class MagicSwordFighterClass(WizardClass,SwordFighterClass):
  pass

msf=MagicSwordFighterClass()
msf.cast_spell()
msf.attack_with_sword()