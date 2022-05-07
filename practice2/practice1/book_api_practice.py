import requests
import pprint
import pandas as pd

def main():
  word=input('検索キーワード:')
  
  res=requests.get('https://ci.nii.ac.jp/books/opensearch/search?'
               f'format=json&q={word}&sortorder=3&count=100')
  #失敗時は例外を抽出
  res.raise_for_status()
  
  books=res.json()
  graph=books['@graph'][0]
  
  #該当の書籍なしの場合
  if 'items' not in graph.keys():
    print('該当する書籍は見つかりません')
    return  
  items=graph['items']
  #pprint.pprint(graph)
  #excelに出力
  df=pd.DataFrame(items)
  (df.rename(columns={
      'title':'タイトル',
      'dc:creator':'著者名',
      'dc:date':'出版年'
      })
    .loc[:,['タイトル','著者名','出版年']]
    .to_excel(f'./{word}.xlsx'))

if __name__ =='__main__':
  main()