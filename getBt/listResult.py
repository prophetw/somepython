#coding:UTF-8
import requests as rs
from bs4 import BeautifulSoup
import re
import os
import json
import sys

print('Number of arguments:')
print(len(sys.argv))
print('Argument list:')
print(str(sys.argv))

if len(sys.argv)==2 and sys.argv[1]:
    keyword = sys.argv[1]
else:
    keyword = ''
if keyword=='':
    print('you need to pass params')
    keyword = 'SMD-116'
    # sys.exit(0)

# 网站有反爬虫 所以需要带上header

headers ={
"accept":"text/html",
"cache-control":"max-age=0",
"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
}
# 遇到一个 问题 最终原因是 mac 系统 openssl这个有问题 python 刚好借用了这个 服务 替换了下版本才终于搞定
session = rs.session()
result = session.get('https://www.torrentkitty.tv/search/'+keyword,headers=headers)
print(result.url)

if result.status_code!=200:
    print('status_code != 200 没有拿到结果')
    sys.exit(0)
htmlElem = BeautifulSoup(result.text,'lxml')
htmlElem.prettify()

# print(htmlElem)
table = htmlElem.find('table',id="archiveResult")
action = table.find_all('td',class_="action")
# print(action)
hashArr = []

def getHash(str):
    if len(str)>0:
        toArr = str.split('/')
        return toArr[-1]
    else:
        return ''
for content in action:
    if content.find('a',rel="information"):
        link = getHash(content.find('a').get('href'))
        if link!= '':
            hashArr.append(link)

# print(hashArr)

baseUrl = 'http://www.torrent.org.cn'
getResultByHashUrl = baseUrl+'/home/convert/magnet2torrent.html?hash='
def getDownloadUrl(strHash):
    result = rs.get(getResultByHashUrl+strHash,headers=headers)
    if result.status_code!=200:
        print('connect not success')
        sys.exit(0)
    htmlElem = BeautifulSoup(result.text,'lxml')
    print(result.url)
    result = htmlElem.find('a',id="download")
    if result != None:
        downloadLink = result.find_next_sibling('a')
        print(downloadLink.get('href'))
        return downloadLink.get('href')
    else:
        return ''


    # print(type(result))
    # print(result)


headers2 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=lqp9n6mfcbuagombquue06qrp0; CNZZDATA5848809=cnzz_eid%3D521029807-1486790302-http%253A%252F%252Fwww.torrent.org.cn%252F%26ntime%3D1486819316; Hm_lvt_8d49907796aa9ef8039994cef084cfc0=1486791912,1486817556; Hm_lpvt_8d49907796aa9ef8039994cef084cfc0=1486824435",
    "Host": "www.torrent.org.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
def startDownload(link):
    # print('downloadlink',link)
    theLink = link.replace('Torrent','torrent')
    print('downloadlink', theLink)
    # result = rs.get(theLink,headers=headers2)
    # print(result.url)

for hash in hashArr:
    downloadLink = getDownloadUrl(hash)
    if downloadLink!='':
        downloadLink = baseUrl+downloadLink
        startDownload(downloadLink)
        print('find bt the end!')
        break
    else:
        continue
    print('not find bt!')






# cmd = ''' curl https://www.torrentkitty.tv/information/A5B5DC31FD19BB265C321237F3B72F758EF10033 '''  #此为伪命令
# result = commands.getoutput(cmd)
# print(result)