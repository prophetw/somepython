#coding:UTF-8

import requests as rs
from bs4 import BeautifulSoup
import re
import os
import datetime

requestNpmUrl = 'https://www.npmjs.com/package/cordova-plugin-foxitpdf'
requestGitUrl = 'https://github.com/foxitsoftware/cordova-plugin-foxitpdf/issues'

# selector .monthly-downloads .weekly-downloads .daily-downloads(last day)
# selector  js-selected-navigation-item.selected.reponav-item > octicon-issue-opened nextSibling counter

timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %a')
print('start at: '+timer)

result = rs.get(requestNpmUrl)
# print(result.status_code)
# print(result.url)
soup = BeautifulSoup(result.text, 'lxml')
soup.prettify()
monthlyDownloads = soup.find('strong', class_='monthly-downloads').get_text()
weeklyDownloads = soup.find('strong', class_='weekly-downloads').get_text()
dailyDownloads = soup.find('strong', class_='daily-downloads').get_text()
print('monthlyDownloads')
print(monthlyDownloads)
print('weeklyDownloads')
print(weeklyDownloads)
print('dailyDownloads')
print(dailyDownloads)

resultForGit = rs.get(requestGitUrl)
soup = BeautifulSoup(resultForGit.text, 'lxml')
soup.prettify()
issueCounter = soup.find('a', class_='js-selected-navigation-item selected reponav-item').find('span',class_="counter").get_text()
print('issue Counter: ')
print(issueCounter)


requestForumUrl = 'http://forums.foxitsoftware.com/forum/portable-document-format-pdf-tools/foxit-cloud/cordova-plugin-foxitpdf'
# forum http://forums.foxitsoftware.com/forum/portable-document-format-pdf-tools/foxit-cloud/cordova-plugin-foxitpdf
# tbody topic-list h-clear > tr class topic-item js-topic-item  length
resultForum = rs.get(requestForumUrl)
soup = BeautifulSoup(resultForum.text, 'lxml')
soup.prettify()
tbody = soup.find('tbody', class_='topic-list')
tr = tbody.find_all('tr', class_="topic-item")
print('#########')
topicCounter = len(tr)
print('topic Counter: ')
print(topicCounter)





# forum http://forums.foxitsoftware.com/forum/portable-document-format-pdf-tools/foxit-cloud/cordova-plugin-foxitpdf


timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %a')
print('end at: '+timer)




