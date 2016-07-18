#coding:utf-8


import requests as rs

s=rs.Session()



postUrl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_35403523/?csrf_token='
postData = {
	'params':'mtUz8PGd7lIHasG/ED9UHfha9Pa0Z1+uoL3oYd8WmzMnoeZncMjDV2V5QnNB4oWRAPXZjyJaH0Dw7B84aT4IZLfqjprhpPGY91P2UZn5bPxsipTNet7MUUVOSBrS7MLXM+JGdqcy3LcTHUl9S07PKvdyjiZs/mP6Y7BRWrb0howALmG0pB4o4hUGFLS0QAb9',
	'encSecKey':'43155db5f1e8e26facd62802ea3d4fa207bf109645921903419c50a2bd9762f764ad05edacffe5ca4dd406383144387c01e5ead2c3ebe055d9c14d5a85ece6c76b64a741e9393057a5aa01437ac7428ecb1c48dc0fe04e8437474d24466df3857a14a0c0a22992b636dbce534fc55de3932350ebf8dbaa6a19de4f8ec9b08c27'
	}
headers = {
	'Host':'music.163.com',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
	'Referer':'http://music.163.com/song?id=35403523',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate',
	'Connection':'keep-alive'
}

s = requests.post(postUrl,postData,headers)
print s.text



