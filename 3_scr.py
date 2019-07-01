import requests
import re
import sys
from bs4 import BeautifulSoup


box = []
url = 'http://ja.pokemongopokedex.site'
headers = {}
soup = BeautifulSoup(requests.get(url,headers=headers,'lxml')
 # 画像リストの空配列

for img in soup.find_all('img')
    # コンソールへスクレイピング対象の画像URLを表示。特段必須ではない
    # imagesの空配列へsrcを登録
    box.append('img')

# imagesからtargetに入れる
for target in box:
    re = requests.get(target)
    with open('/Users/arimachishun/desktop/img' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
      # .contentで画像データとして書き込む
      f.write(re.content)

# スクレイピング終了確認
print("画像保存が完了しました。")
