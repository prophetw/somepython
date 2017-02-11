import requests


s = requests.session()
r = s.get('https://upload.115.com/cross.php')
rr = s.post()
'''
https://webapi.115.com/files/add

cname=78
pid=839290952215697485


POST /files/add HTTP/1.1
Host: webapi.115.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Referer: https://webapi.115.com/bridge_2.0.html?namespace=Core.DataAccess&api=UDataAPI&_t=v5
Content-Length: 31
Cookie: UID=85475634_A1_1470066499; CID=369b0dbc42baa6ce649d870ad0245af9; SEID=5e7f0e34ecb7979cd1fc0acc31c3ddaf597f0e75888aec5b39da3341bd24532f933193c61d13eb581bbc6844baf73406dd2eabbd7571b1d63f165b4c; OOFL=85475634; ssov_85475634=1_85475634_27969c53e3cb79dd3eae569aade3891b
Connection: keep-alive



'https://upload.115.com/cross.php' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Connection: keep-alive' -H 'Cookie: UID=85475634_A1_1470066499; CID=369b0dbc42baa6ce649d870ad0245af9; SEID=5e7f0e34ecb7979cd1fc0acc31c3ddaf597f0e75888aec5b39da3341bd24532f933193c61d13eb581bbc6844baf73406dd2eabbd7571b1d63f165b4c; OOFL=85475634; ssov_85475634=1_85475634_27969c53e3cb79dd3eae569aade3891b' -H 'Host: upload.115.com' -H 'Referer: https://115.com/' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0'

'''