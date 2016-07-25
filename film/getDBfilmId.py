import requests as rs
import re
from bs4 import BeautifulSoup

searchApi = 'https://movie.douban.com/subject_search'
s = rs.Session()
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

def getId(str):
    # print(str)
    regForId = '\d+'
    result = re.findall(regForId, str)
    # print result
    return result[0]
def getFilmId(query):
    query = query
    payloads = {'search_text':query}
    getFilmInfo = searchApi
    q = s.get(getFilmInfo,params=payloads,headers=headers)
    str = q.text
    soup = BeautifulSoup(str, 'lxml')
    soup.prettify()
    btlinks = soup.find_all('tr', 'item')
    target = None
    for index in btlinks:
        title = index.find_all('img')[0].attrs['alt']
        print(title)
        if title.find(query)>-1:
            target = index
            break
    href = target.find('a').get('href')
    regExp = r'https://movie.douban.com/subject/\d*/'
    re3 = re.findall(regExp,href)
    print(re3[0])
    searchFilmId = getId(re3[0])
    # print searchFilmId
    return searchFilmId
getFilmId('速度与激情4')