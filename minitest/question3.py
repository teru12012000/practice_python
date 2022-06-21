'''
5科目中、国語英語数学の三科目を引数に引き取って平均点を返す関数を作成する

'''
scores = {
  '国語': 87, '数学': 86, '英語': 70, '理科': 73, '社会': 80
}
def ave(scores):
  total_score=0
  for sbj ,score in scores.items():#辞書の時はこうやってfor文で要素を取り出していく
    if sbj in ['国語','数学','英語']:#もし、sbjに国語もしくは数学もしくは英語がはいっているのならば。。。
      total_score+=score
  total_score/=3
  return total_score

result=ave(scores)
print(result)