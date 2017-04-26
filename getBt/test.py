#coding:UTF-8
import os
import sys
from urllib import quote

hash = sys.argv[1].lower()
path = quote(sys.argv[2])
print('hash',hash)
print('save path',path)

#  cid uid seid sign time  每次需要更新这5个参数 就可以了

#  cid uid seid  更新这三个就 可以了
#  重新登录 需要更新
#
# time uid 81ba6630b9ff7ff1918281ffe5234b2fa0464681
command="curl 'http://115.com/web/lixian/?ct=lixian&ac=add_task_bt' " \
        "-H 'Cookie: ssov_85475634=1_85475634_27969c53e3cb79dd3eae569aade3891b; tjj_u=1; tjj_id=148760361897543216273; " \
        "UID=85475634_A1_1493042570; CID=9787854af2d4b8f785793153f0b72c7d; " \
        "SEID=e94f7119a603f77abd203ef7039fe20ec3ab36240e0e894ea88fcfc5bd207cd3ec6d8f87570921cffcbb199b210dff3b0bd22c0b4fb4c03ab5c34004; " \
        "OOFL=85475634; PHPSESSID=307mbfsavalp7pmn6m7af673p1; " \
        "tjj_repeat=7; 115_lang=zh' " \
        "-H 'Origin: http://115.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8' " \
        "-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.4' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://115.com/?tab=offline&mode=wangpan' -H 'X-Requested-With: XMLHttpRequest' " \
        "-H 'Connection: keep-alive' " \
        "--data " \
        "'info_hash="+hash+"&wanted=&savepath="+path+"&uid=85475634&sign=0107cd99fa558f6854a865afb42fc4e8&time=1493041574' --compressed"

os.system(command)

# OOFL=85475634;
# UID=85475634_A1_1487507877; CID=5bb0176d7858aee0015498ea0d681ba1;
# SEID=e332794ea58ca705c48d3669d7df649e349a21fed9adddc2a0eedd6eb3ddc8393db04bc155504932c80db814e4c96b62bdf1c37c164715a9d8a9d79d


