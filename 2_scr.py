import requests
import re
import sys
from bs4 import BeautifulSoup



#ライブラリを用いてHTMLコンテンツを取得
if __name__ == '__main__':
    home_url = "http://ja.pokemongopokedex.site/"#ここに任意のURL
    img_dir = 'images'
    timeout = 10
    params  = {}
    cookies = {}
    headers = {}

    home_response = requests.get(home_url, timeout=timeout, params=params, cookies=cookies, headers=headers, stream=True)

    if home_response.raise_for_status() != None:
        sys.exit('HTTP Error When Accesing The target URL!')
        #取得したHTMLからJPEGファイルのリンク先を取得

    html = home_response.text
    img_search = re.findall(r'"(https?://[a-zA-Z0-9:/.=_\-]*png|PNG)"', html)

    if img_search == []:
        sys.exit('Not Found Image URLs!')

        #再度requestsライブラリを用いてJPEGファイルのリンク先のコンテンツを取得し、JPEGファイルとして保存
    for img_url in img_search:
        name_search = re.findall(r'\/([a-zA-Z0-9:.=_-]*png|PNG)', img_url)
        img_name = name_search[0]
        img_response = requests.get(img_url, timeout=timeout, params=params, cookies=cookies, headers=headers, stream=False)
        if img_response.raise_for_status() != None:
            sys.exit('HTTP Error When Accesing The target URL!')
        with open('/Users/arimachishun/desktop/img/'+img_name, 'wb') as f:
            f.write(img_response.content)
