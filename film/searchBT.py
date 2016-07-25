#coding:UTF-8
from bs4 import BeautifulSoup
import requests as rs
import re
import json
import os
def getFilmBT(query):
    params = {
        'q': query,
        'sitesearch': 'www.bttiantang.com',
        'domains': 'bttiantang.com',
        'hl': 'zh-CN',
        'ie': 'UTF-8',
        'oe': 'UTF-8'
    }
    baseURL = 'http://www.bttiantang.com'
    searchBTURL = baseURL + '/s.php'
    s = rs.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    q = s.get(searchBTURL, params=params, headers=headers)
    # print(q.url)
    html = q.text
    soup = BeautifulSoup(html, 'lxml')
    soup.prettify()
    q = soup.find_all('div', class_='litpic')
    print(len(q))
    target = None
    year = 2016
    for index in q:
        title = index.find_all('img')[0].attrs['alt']
        titleWithoutSpace = title.replace(' ', '')
        if titleWithoutSpace.find(query)>-1 and titleWithoutSpace.find(str(year))>-1:
            target = index

    # print(q[0].find('a'))
    result = q[0].find('a')
    filmbtpage = result.get('href')
    BTurl = baseURL + filmbtpage
    bthtmls = s.get(BTurl, headers=headers)
    bthtmls.encoding = 'utf-8'
    bthtml = bthtmls.text
    btsoup = BeautifulSoup(bthtml, 'lxml')
    btsoup.prettify()
    btlinks = btsoup.find_all('div', 'tinfo')
    totalbtlinks = []
    totalbttitles = []
    for links in btlinks:
        totalbtlinks.append(links.find('a').get('href'))
        totalbttitles.append(links.find('a')['title'])
    print(totalbtlinks)
    print(totalbttitles)
    whatineed = s.get(baseURL + totalbtlinks[0])
    print(whatineed.url)
    urlParams = whatineed.url
getFilmBT('绝地逃亡')


# query = '葫芦娃'
#
#
#
# params = {
#     'q':query,
#     'sitesearch':'www.bttiantang.com',
#     'domains':'bttiantang.com',
#     'hl':'zh-CN',
#     'ie':'UTF-8',
#     'oe':'UTF-8'
# }
# baseURL = 'http://www.bttiantang.com'
# searchBTURL = baseURL+'/s.php'
# s = rs.Session()
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
# }
# q = s.get(searchBTURL,params=params,headers=headers)
# print(q.url)
# html = q.text
# soup = BeautifulSoup(html,'lxml')
# soup.prettify()
# q = soup.find_all('div',class_='litpic')
# print(q[0].find('a'))
# result = q[0].find('a')
# filmbtpage = result.get('href')
# BTurl = baseURL+filmbtpage
# bthtmls = s.get(BTurl,headers=headers)
# bthtmls.encoding='utf-8'
# bthtml=bthtmls.text
# btsoup = BeautifulSoup(bthtml,'lxml')
# btsoup.prettify()
# btlinks = btsoup.find_all('div','tinfo')
# totalbtlinks = []
# totalbttitles = []
# for links in btlinks:
#     totalbtlinks.append(links.find('a').get('href'))
#     totalbttitles.append(links.find('a')['title'])
# print(totalbtlinks)
# print(totalbttitles)
# whatineed = s.get(baseURL+totalbtlinks[0])
# print(whatineed.url)
#
# urlParams = whatineed.url
# def getId(urlParams):
#     idRegular = r'id=(\d+)'
#     result = re.search(idRegular,urlParams)
#     id = result.group(1)
#     return id
# def getHash(urlParams):
#     idRegular = r'uhash=(.+)'
#     result = re.search(idRegular, urlParams)
#     hash = result.group(1)
#     return hash
#
# id= getId(urlParams)
# # print(id)
# hash= getHash(urlParams)
# # print(hash)
# # 最后一个 post 请求
# # 链接 http://www.bttiantang.com/download1.php
# downloadURL = 'http://www.bttiantang.com/download1.php'
# payload = {
#     'action':'download',
#     'id':id,
#     'uhash':hash,
#     'imageField.x':'40',
#     'imageField.y':'32'
# }
# def download():
#     bt = s.post(downloadURL,data=payload,stream=True)
#     # print(bt.text)
#     print(bt.raw)
#     file = open(query+'.torrent', 'w')
#     with open(query+'.torrent', 'wb') as fd:
#         for chunk in bt.iter_content(10):
#             fd.write(chunk)
#     fd.close()
