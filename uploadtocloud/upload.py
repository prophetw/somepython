import requests

s = requests.session()
rs = s.get('http://115.com/')
# print(rs.text)

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Content-Length':'55259',
    'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary7MAdK3eLJohCtR5a',
    'Cookie':'115_lang=zh; UID=85475634_A1_1470060979; CID=ed79ee8c46792e48736a474f1c462175; SEID=7df44b0b79296ef71782e2573d62e522cdce168fa3b3ec69c630983717bcd7a994795953605eb06c70f57b67f6784c5ade39e7b7d9f3f6bbb64c2dc1; OOFL=85475634; ssov_85475634=1_85475634_27969c53e3cb79dd3eae569aade3891b',
    'Host':'upload.115.com',
    'Origin':'http://upload.115.com',
    'Referer':'http://upload.115.com/cross.php',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
'''
115 upload post
http://upload.115.com/upload?debugs=1&userid=85475634&ets=1470233780&appid=n&sig=954C29EC9226753822E0850BC20EC379B835D2F8

实际情况

request payload
------WebKitFormBoundary7MAdK3eLJohCtR5a
Content-Disposition: form-data; name="name"

【BT天堂】【BTtiantang.com】[720p]有希望的男人.1.27GB.torrent
------WebKitFormBoundary7MAdK3eLJohCtR5a
Content-Disposition: form-data; name="target"

U_1_0
------WebKitFormBoundary7MAdK3eLJohCtR5a
Content-Disposition: form-data; name="Filedata"; filename="【BT天堂】【BTtiantang.com】[720p]有希望的男人.1.27GB.torrent"
Content-Type: application/octet-stream


------WebKitFormBoundary7MAdK3eLJohCtR5a--





requests.post('http://example.com/example/asdfas', files={'value_1': (None, '12345'), 'value_2': (None, '67890')})

'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, compress',
'Content-Length': '228',
'User-Agent': 'python-requests/2.2.1 CPython/3.3.2 Windows/7',
'Content-Type': 'multipart/form-data; boundary=85e90a4bbb05474ca1e23dbebdd68ed9'

--85e90a4bbb05474ca1e23dbebdd68ed9
Content-Disposition: form-data; name="value_1"

12345
--85e90a4bbb05474ca1e23dbebdd68ed9
Content-Disposition: form-data; name="value_2"

67890
--85e90a4bbb05474ca1e23dbebdd68ed9--



'''
uploadposturl = 'http://upload.115.com/upload?debugs=1&userid=85475634&ets=1470233780&appid=n&sig=954C29EC9226753822E0850BC20EC379B835D2F8'
payload={
    'name':'【BT天堂】【BTtiantang.com】[720p]有希望的男人.1.27GB.torrent',
}
files = {'file': ('1.torrent', open('1.torrent', 'rb'), 'application/octet-stream')}
# files={'name': (None, '1.torrent'), 'target': (None, 'U_1_0'),'Filedata': ('1.torrent', 'Content-Type: application/octet-stream')}
# print(files)
result = s.post(uploadposturl,headers=headers,files=files)
print(result.request.headers)
print(result.request.body)
print(result.text)


