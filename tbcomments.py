#coding:UTF-8

import json
import re
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL' 
import requests as rs
#开启一个session会话
s = rs.Session()
#利用session去打开网页，然后可以获取cookies，下次去访问的时候就会带着cookies去访问
#不会被当作是爬虫
s.get('https://www.taobao.com')
url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=19675612870&userNumId=93487779&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&showContent=1&attribute=&folded=0&ua=069UW5TcyMNYQwiAiwTR3tCf0J/QnhEcUpkMmQ=|Um5OcktySnFKdk5ySHNGeC4=|U2xMHDJ+H2QJZwBxX39RaFR6WnQzWjEfSR8=|VGhXd1llXGVdZl1hWWVfZFFvWGVHfkpzTHRAfER5TXJKckd4TWM1|VWldfS0SMg00CCgUKwslGi8LYlp/ST1CK1B8UgRS|VmJCbEIU|V2lJGSUaIgI/HyMcJx8/ADwGOBgkGy4TMwY7BiYaJRAtDTcLMWcx|WGFcYUF8XGNDf0Z6WmRcZkZ8R2dZDw==&_ksTS=1445661519435_1225&callback=jsonp_tbcrate_reviews_list'
headers={
	"Host":"rate.taobao.com",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding":"gzip, deflate",
	"Referer":"https://item.taobao.com/item.htm?spm=a230r.1.14.66.P2lgls&id=19675612870&ns=1&abbucket=9",
	"Cookie":"t=212faf781fa68339c3abe4623883b610; cna=nKVqDtpM0BICASQhAen60jIt; thw=cn; isg=CAC889C96CAEA06FA25EE721A517D830; l=AnR0qFMm6ZczA1zrvsVmRDkmZDzmHpg3; uc3=nk2=1T0QpJYMzOc%3D&id2=VAXb2Bm9c6RW&vt3=F8dASMhx4E7Y%2BjXA76Q%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=%5Cu72EC%5Cu7231%5Cu5F26%5Cu5B50; _cc_=URm48syIZQ%3D%3D; tg=0; ali_ab=114.96.157.161.1444377900211.2; lgc=%5Cu72EC%5Cu7231%5Cu5F26%5Cu5B50; mt=ci=1_1; v=0; cookie2=12a4e3a4769d1157ff2f64181d333140; uc1=cookie14=UoWzXLYbA3bJlA%3D%3D; _tb_token_=1ew269hQfH0I",
	"Connection":"keep-alive"
}
r = rs.get(url,headers=headers)
print(r)
#print(r.text)
#返回de值不是一个json而是一个方法名可以利用正则表达式提取主要的内容
response = r.text
print(type(response))
reg_exp = r'(?<=\()(.*)(?=\))'
result = re.findall(reg_exp,response)
#result is type of list
print(type(result))
result1 = json.loads(result[0])
#result1[comments]是一个数组
#result1['comments'][0]是一个对象  result1['comments'][0]['user']也是一个对象，然后里面nick这个#属性为用户昵称
#result1['comments'][n]['content']每个评价内容
#result1['comments'][n]['user']['nick'] 每个用户昵称
res = result1['comments']
print type(res)
#print res
#print(res[1]['user']['nick'])
#print(res[0]['content'])
res = result1['comments']
for n in range(len(res)):
	print 'usrnick:'+res[n]['user']['nick']+'comment:'+res[n]['content']
	
	
#'usrnick:'+res[n]['user']['nick']

