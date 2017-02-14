import os
import sys
from urllib import quote

hash = sys.argv[1].lower()
path = quote(sys.argv[2])
print('hash',hash)
print('save path',path)

command="curl 'http://115.com/web/lixian/?ct=lixian&ac=add_task_bt' " \
        "-H 'Cookie: ssov_85475634=1_85475634_27969c53e3cb79dd3eae569aade3891b; tjj_u=1; tjj_id=148682924093124223824; UID=85475634_A1_1486883601; CID=c12015707225a713e64f9f71e8955475; SEID=ecba941991830653f191fef21dd214b4577e40ae3169136902f0f7fad09919fa2891b5647b81a2b96dd69e3d01b6f505c45303fdb7c217264101ccb9; OOFL=85475634; PHPSESSID=to944ehebgbegbejelqi96ulm1; tjj_repeat=7; 115_lang=zh' " \
        "-H 'Origin: http://115.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8' " \
        "-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.4' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://115.com/?tab=offline&mode=wangpan' -H 'X-Requested-With: XMLHttpRequest' " \
        "-H 'Connection: keep-alive' " \
        "--data " \
        "'info_hash="+hash+"&wanted=&savepath="+path+"&uid=85475634&sign=2c7d421b7a2a63ad186b705a8aadeb3aa04c767a&time=1486885371' --compressed"

os.system(command)