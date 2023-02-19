import urllib
from webbrowser import get
import requests
from bs4 import BeautifulSoup
import os
import sys

# Webサイトダウンロードメソッド
def get_web(url):
    # DEBUG
    header = {"User-Agent" : "Mozilla/5.0"}

    res = requests.get(url,headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 取得したwebサイトのタイトルをファイル名とする
    title = soup.find("title").text
    file_name = title + '.html'
    #save_path = "./data/"
    save_path = "./dst/"
    save_file = save_path + file_name

    # 保存処理
    urllib.request.urlretrieve(url, save_file)

    print(sys._getframe().f_code.co_name + " : OK")
    return save_file

if __name__ == "__main__":
    url = input("url : ")
    get_web(url)
