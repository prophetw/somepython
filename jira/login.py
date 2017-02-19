#coding:UTF-8
import requests as rs
from bs4 import BeautifulSoup
import re
import os
import json
import sys

# print('Number of arguments:')
# print(len(sys.argv))
# print('Argument list:')
# print(str(sys.argv))
#
# if len(sys.argv)==2 and sys.argv[1]:
#     keyword = sys.argv[1]
# else:
#     keyword = ''
# if keyword=='':
#     print('you need to pass params')
#     keyword = '最帅的男人'
#     # sys.exit(0)

# 网站有反爬虫 所以需要带上header

headers ={
"accept":"text/html",
"cache-control":"max-age=0",
"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
}
# 遇到一个 问题 最终原因是 mac 系统 openssl这个有问题 python 刚好借用了这个 服务 替换了下版本才终于搞定
session = rs.session()
result = session.get('https://jira.foxitsoftware.cn/secure/Dashboard.jspa',headers=headers)
# print(result.url)
# print(result.text)
print(result.cookies)

payload={
    'os_username':'prophet_wang',
    'os_password':'wangwei123'
}
loginResult = session.post('https://jira.foxitsoftware.cn/rest/gadget/1.0/login',cookies=result.cookies,headers=headers,data=payload)
# print(loginResult.url)
# print(loginResult.text)
# print(loginResult.headers)

result2 = session.get('https://jira.foxitsoftware.cn/secure/Dashboard.jspa',headers=headers)
# print(result2.url)
# print(result2.headers)
# print(result2.text)

issueUrl = 'https://jira.foxitsoftware.cn/browse/'
issueNum = 'CVAS-493'

issueHtml = session.get(issueUrl+issueNum,headers=headers)
# print(issueHtml.request.headers)
# print(issueHtml.text)
htmlElem = BeautifulSoup(issueHtml.text,'lxml')
htmlElem.prettify()

aTag = htmlElem.find('a',class_="issue-link")
issueId = aTag.get('rel')
print(issueId)

formData ={
'id':'51665',
'atl_token':'B915-4EQS-7O0Z-WBWY|8c226742c3c29402de7d3cc1d9e5adada68cb865|lin',
'formToken':'1ded8f724ac91cbd653658ec65a82db55c10864c',
'customfield_10830':'-1',
'summary':'Share File-秘密分享',
'customfield_10004':'',
'issuetype':'2',
'priority':'2',
'duedate':'',
'components':'14743',
'customfield_10631':'118',
'fixVersions':'17568',
'assignee':'prophet_wang',
'description':'Use Case多数的用户文档还是属于保密性的，比如工作文档，比如翻译初稿，不可以公开分享，只能是有密码的人才可以拿到文档。需求：在设置公开分享时，可以设置密码（密码要包含8位以上，包含字母与数字）被分享人打开link时，提示要输入密码，只有密码正确才可以打开、下载文档。',
'environment':'',
'dnd-dropzone':'',
'labels':'2017Q1',
'customfield_11934':'-1',
'customfield_10331':'',
'customfield_12233':'-1',
'customfield_10137':'-1',
'customfield_10009':'',
'customfield_10138':'',
'customfield_10932':'-1',
'customfield_10933':'',
'customfield_10934':'',
'customfield_10139':'',
'customfield_10013':'',
'customfield_10030':'-1',
'customfield_10012':'',
'customfield_10011':'',
'customfield_10015':'',
'customfield_12032':'11249',
'customfield_12031':'11228',
'customfield_10016':'',
'customfield_10017':'',
'customfield_10018':'',
'customfield_10019':'',
'customfield_10730':'maggie',
'customfield_10731':'10425',
'customfield_12231':'-1',
'customfield_10005':'prophet_wang',
'customfield_11732':'',
'customfield_11730':'',
'customfield_10143':'',
'customfield_10003':'',
'customfield_10142':'',
'customfield_11130':'-1',
'customfield_11630':'',
'customfield_11930':'',
'customfield_10006':'junyu_hu',
'customfield_10144':'',
'customfield_10008':'',
'customfield_11935':'-1',
'customfield_12130':'',
'timetracking_remainingestimate':'',
'worklog_timeLogged':'',
'worklog_startDate':'15/Feb/17 9:11 PM',
'worklog_adjustEstimate':'auto',
'isCreateIssue':'false',
'isEditIssue':'true',
'timetracking_originalestimate':'',
'isCreateIssue':'',
'hasWorkStarted':'',
'customfield_10021':'-1',
'customfield_10022':'-1',
'customfield_10023':'-1',
'comment':'',
'commentLevel':''
}


# curl 'https://jira.foxitsoftware.cn/secure/QuickEditIssue.jspa?issueId=51665&decorator=none' -H 'Cookie: Hm_lvt_c398b0a7a1a2ab94daf61f08a9898c7d=1483162600; foxit_sid=6056tUrcXXUL6oKHhXOogrYB%2FckwCwo4lGzrMhLxYgZY82DzpkXkCgs6RvNr8%2B1STNoj2ZzjMgPG0FxC3qXhMPb2qpCda9apZbXApaiXk3PZqdbFqpSv4UZqbz7qccS6gGYk; JSESSIONID=057D3FCB4884D4A7DDD2AD2DAC194B5E; atlassian.xsrf.token=B915-4EQS-7O0Z-WBWY|8c226742c3c29402de7d3cc1d9e5adada68cb865|lin; AJS.conglomerate.cookie="|hipchat.inapp.links.first.clicked.prophet_wang=false"' -H 'Origin: https://jira.foxitsoftware.cn' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: https://jira.foxitsoftware.cn/browse/CVAS-493' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'X-AUSERNAME: prophet_wang' --data 'id=51665&atl_token=B915-4EQS-7O0Z-WBWY%7C8c226742c3c29402de7d3cc1d9e5adada68cb865%7Clin&formToken=1ded8f724ac91cbd653658ec65a82db55c10864c&customfield_10830=-1&summary=Share+File-%E7%A7%98%E5%AF%86%E5%88%86%E4%BA%AB&issuetype=2&priority=2&components=14743&customfield_10631=118&fixVersions=17568&assignee=prophet_wang&description=Use+Case%0D%0A%E5%A4%9A%E6%95%B0%E7%9A%84%E7%94%A8%E6%88%B7%E6%96%87%E6%A1%A3%E8%BF%98%E6%98%AF%E5%B1%9E%E4%BA%8E%E4%BF%9D%E5%AF%86%E6%80%A7%E7%9A%84%EF%BC%8C%E6%AF%94%E5%A6%82%E5%B7%A5%E4%BD%9C%E6%96%87%E6%A1%A3%EF%BC%8C%E6%AF%94%E5%A6%82%E7%BF%BB%E8%AF%91%E5%88%9D%E7%A8%BF%EF%BC%8C%E4%B8%8D%E5%8F%AF%E4%BB%A5%E5%85%AC%E5%BC%80%E5%88%86%E4%BA%AB%EF%BC%8C%E5%8F%AA%E8%83%BD%E6%98%AF%E6%9C%89%E5%AF%86%E7%A0%81%E7%9A%84%E4%BA%BA%E6%89%8D%E5%8F%AF%E4%BB%A5%E6%8B%BF%E5%88%B0%E6%96%87%E6%A1%A3%E3%80%82%0D%0A%0D%0A%E9%9C%80%E6%B1%82%EF%BC%9A%0D%0A%E5%9C%A8%E8%AE%BE%E7%BD%AE%E5%85%AC%E5%BC%80%E5%88%86%E4%BA%AB%E6%97%B6%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%AE%BE%E7%BD%AE%E5%AF%86%E7%A0%81%EF%BC%88%E5%AF%86%E7%A0%81%E8%A6%81%E5%8C%85%E5%90%AB8%E4%BD%8D%E4%BB%A5%E4%B8%8A%EF%BC%8C%E5%8C%85%E5%90%AB%E5%AD%97%E6%AF%8D%E4%B8%8E%E6%95%B0%E5%AD%97%EF%BC%89%0D%0A%E8%A2%AB%E5%88%86%E4%BA%AB%E4%BA%BA%E6%89%93%E5%BC%80link%E6%97%B6%EF%BC%8C%E6%8F%90%E7%A4%BA%E8%A6%81%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81%EF%BC%8C%E5%8F%AA%E6%9C%89%E5%AF%86%E7%A0%81%E6%AD%A3%E7%A1%AE%E6%89%8D%E5%8F%AF%E4%BB%A5%E6%89%93%E5%BC%80%E3%80%81%E4%B8%8B%E8%BD%BD%E6%96%87%E6%A1%A3%E3%80%82%0D%0A&labels=2017Q1&customfield_11934=-1&customfield_12233=-1&customfield_10137=-1&customfield_10009=&customfield_10138=&customfield_10932=-1&customfield_10934=&customfield_10139=&customfield_10013=&customfield_10030=-1&customfield_10012=&customfield_10011=&customfield_10015=&customfield_12032=11249&customfield_12031=11228&customfield_10016=&customfield_10017=&customfield_10018=&customfield_10019=&customfield_10730=maggie&customfield_10731=10425&customfield_12231=-1&customfield_10005=prophet_wang&customfield_11732=&customfield_11730=&customfield_10143=&customfield_10003=&customfield_10142=&customfield_11130=-1&customfield_11630=&customfield_11930=&customfield_10006=junyu_hu&customfield_10144=&customfield_10008=&customfield_11935=-1&customfield_12130=&timetracking_remainingestimate=&worklog_timeLogged=&worklog_startDate=15%2FFeb%2F17+9%3A11+PM&worklog_adjustEstimate=auto&isCreateIssue=false&isEditIssue=true&timetracking_originalestimate=&isCreateIssue=&hasWorkStarted=&customfield_10021=-1&customfield_10022=-1&customfield_10023=-1&comment=&commentLevel=' --compressed


