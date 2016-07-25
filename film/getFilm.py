#coding:UTF-8
import requests as rs
import re
import json
url = 'http://www.bttiantang.com'
query = '/s.php'

# print(url+query)
filmListHtml = url+query
year = 2016  #这个地方填入 年份 比如 2015
pgNum = 4    #这个地方改变数字 可以改变页数
payload = {'q':year,'PageNo':pgNum}

#print(payload)
s = rs.Session()
r = rs.get(filmListHtml,params=payload)
q = s.get('http://movie.douban.com')
# print(r.text)
str = r.text
# print str

#电影的链接正则
urlList = []
pattLink = r'(?<=litpic"><a href=").*?(?=" target)'
re1 = re.findall(pattLink,str)
for i in re1:
    urlList.append(url+i.encode('utf-8'))
# print urlList
# print len(urlList)

#电影名称正则
nameList = []
pattFilmName = r'(?<=_blank"><b>).*?(?=<i>)'
re2 = re.findall(pattFilmName,str)
for i in re2:
    nameList.append(i.encode('utf-8'))
# print nameList
# print len(nameList)
# print(re2)

#豆瓣评分正则
pattJudge = r'<strong>\d</strong><em class="dian">\.</em><em class="fm">\d</em>'
re3 = re.findall(pattJudge,str)
# print re3
#对re3的数据进行处理  把数字弄出来
pattNum = r'\d'
re4 = re.findall(pattNum,re3[0])
# print re4[0]+re4[1]
# print(re3[0])
NumList = []
for i in re3:
    q = re.findall(pattNum,i)
    m = q[0] + q[1]
    NumList.append(int(m.encode('utf-8')))
    #print NumList
# print NumList
# print len(NumList)

#豆瓣评分人数 正则
#获得豆瓣的链接 然后把豆瓣的评分人数弄出来
#  <a href="/jumpto.php?aid=27290" rel="nofollow" target="_blank"
doubanVote = [] #用来装豆瓣评价的人数
pattDouban = r'(?<=jumpto\.php\?aid=)\d*'
re5 = re.findall(pattDouban,str)   #找到所有的 转豆瓣的aid一串数字 组合下面的jumpToDouban
# print re5  #aid数字的集合
jumpToDouban = 'http://www.bttiantang.com/jumpto.php?aid='
# headers为豆瓣反爬虫准备的  值得注意的这个里面的cookies隔一段时间可能会失效 所以隔一段就应该更新一次
headers = {
                'Host': 'movie.douban.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Cookie': 'bid="4V7GZI/4nkU"; viewed="24246865_3288908"; __utma=30149280.832776225.1444719193.1449642367.1449748605.5; __utmz=30149280.1449642367.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; gr_user_id=590e0e3b-2410-4e36-9acd-b73fcacca7f0; ll="118183"; _pk_id.100001.4cf6=2aca42cc8381cdc8.1449748605.1.1449749251.1449748605.; __utmc=30149280; __utma=223695111.996460411.1449748605.1449748605.1449748605.1; __utmc=223695111; __utmz=223695111.1449748605.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
                'Connection': 'keep-alive'
          }

#douban.text
#【BT天堂】提示：正在为您跳转到豆瓣......<script type="text/javascript">setTimeout('location.href="http://movie.douban.com/subject/25766527/";',2000)</script>
#接着把豆瓣的地址给拔出来
doubanUrlPat = r'(?<=location\.href=").*?(?=")'
#找到评价的人数
findVotePattern = r'(?<=votes">)\d*(?=</span>)'

def checkVoteNum(i):
    douban = rs.get(jumpToDouban+re5[i])
    re6 = re.findall(doubanUrlPat,douban.text)
    if re6:
        doubanTotal = rs.get(re6[0],headers=headers)
        doubanTotalHtml = doubanTotal.text
        re7 = re.findall(findVotePattern,doubanTotalHtml)
        if re7:
            return re7[0]
        else:
            return 0
    else:
        return 0
        pass




# for i in range(len(re5)):
#     douban = rs.get(jumpToDouban+re5[i])
#     re6 = re.findall(doubanUrlPat,douban.text)
#     if re6:
#         doubanTotal = rs.get(re6[0],headers=headers)
#         doubanTotalHtml = doubanTotal.text
#         re7 = re.findall(findVotePattern,doubanTotalHtml)
#         if re7:
#             doubanVote.append(re7[0])
#         else:
#             doubanVote.append(0)
#     else:
#         pass

    # doubanVote.append(re7[0])



# print doubanVote
# for i in re5:
#     douban = rs.get()

# for i in re55:
#     print i



#接下来的任务是 把三个合并到一起

dict = {}
for i in range(len(nameList)):
    if NumList[i]>70 or NumList[i]==70:
        dict[nameList[i]]={'url':urlList[i],'num':NumList[i],'vote':checkVoteNum(i)}
    else:
        pass
print(dict)
# print json.dumps(dict)
# print dict
# print len(json.dumps(dict))
# f = open('1.txt','a')
for i in dict:
    print(i)
    for q in dict[i]:
        print(dict[i][q])


#  下面出错  unicode not callable
# for i in dict:
#     for q in dict[i]:
#         if q == 'num':
#             print('score=:  ' + str(dict[i][q]))
#         if q == 'vote':
#             print('豆瓣评分人数为：'+dict[i][q])