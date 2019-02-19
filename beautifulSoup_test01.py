# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:27:16 2019

@author: izumiy
"""
# 

import requests
from bs4 import BeautifulSoup


# url = "http://www.nogizaka46.com/member/"
url = "https://www.akb48.co.jp/about/members/"

# アクセス拒否対策
headers = {"User-Agent":"Mozilla/5.0"}

soup = BeautifulSoup(requests.get(url,headers=headers).content,"html.parser")

members = []

# 乃木坂46のメンバーの名前を取得
"""
for div in soup.find_all("div", class_="unit"):
    for span in div.find_all("span", class_="main"):
        member.append(span.string)
"""

# AKB48のメンバーの名前を取得
for name in soup.find_all("h4", class_="memberListNamej"):
    members.append(name.string)
    
for i, name in enumerate(members):
    print(str(i) + ":" + name)
