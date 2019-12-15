# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

def scraping():
    #url
    url = "http://www.yomiuri.co.jp/"

    #get html
    html = request.urlopen(url)

    #set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")

    #get headlines
    mainNewsIndex = soup.find("ul", attrs={"class", "p-category-latest-sec-list p-list p-list-col2"})
    headlines = mainNewsIndex.find_all("a")
    
    text = []
    url = []
    for link in headlines:
        if(link.get_text(strip=True) != ''):
            text.append(link.get_text(strip=True))
            url.append(link.get("href"))
        
    # test
    # print(headlines)
    # for headline in headlines:
    #     print(headline)
        
    return text, url

if __name__ == "__main__":
    text, url = scraping()
    
    for t, u in zip(text, url):
        print(t)
        print(u)
    
