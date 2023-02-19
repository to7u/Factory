import urllib
from webbrowser import get
import requests
from bs4 import BeautifulSoup
import os
import sys

"""
対象サイト
https://www.freeproxylists.net/ja/?c=&pt=&pr=HTTPS&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0
国 : すべて
ポート : 指定なし
プロトコル : HTTPS
匿名性 : None,Anonymous,High Anonymous

http://free-proxy.cz/ja/proxylist/country/all/https/ping/all
国 : すべて
プロトコル : HTTPS

"""

# Webサイトダウンロードメソッド
def get_web(url):
    # DEBUG
    header = {"User-Agent" : "Mozilla/5.0"}

    res = requests.get(url,headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')

    # DEBUG
    print(soup)

    #proxy_list = soup.select('#proxy_list tbody tr td')
    # DEBUG
    #print(proxy_list)

    # 取得したwebサイトのタイトルをファイル名とする
    title = soup.find("title").text
    file_name = title + '.html'
    #save_path = "./data/"
    save_path = "./dst/"
    save_file = save_path + file_name

    # 保存処理
    #urllib.request.urlretrieve(url, save_file)

    #print(sys._getframe().f_code.co_name + " : OK")
    #return save_file

if __name__ == "__main__":
    #url = input("url : ")
    # test
    #url = "http://free-proxy.cz/ja/proxylist/country/all/https/ping/all"
    url = "https://www.freeproxylists.net/ja/?c=&pt=&pr=HTTPS&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0"
    get_web(url)
