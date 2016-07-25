from bs4 import BeautifulSoup
import requests as rs
import re
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
    data = []
    for links in btlinks:
        totalbtlinks.append(baseURL+links.find('a').get('href'))
        totalbttitles.append(links.find('a')['title'])
        data.append({
            'title': links.find('a')['title'],
            'link': baseURL+links.find('a').get('href')
        })
    return data
data1 = getFilmBT('疯狂动物城')
print(data1)