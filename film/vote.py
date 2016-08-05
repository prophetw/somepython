import requests
import hashlib
md5 = hashlib.md5()
# md5.update('what you want to md5 code')
# md5.hexdigest()   这个是结果

VPath = "http://v4.10brandchina.com/"
itemid = 52056
brand_id = 52056
catId = 40374
authType = 1

# 验证码 图片 获得
# get VPath + "api/captchar.vote.png.php?authType=" + authType + "&rnd=" + rndNum+ "&id=" + brand_id
# rndNum 计算
# rndNum=""+catId + brand_id+Math.round(Math.random()*100000)
'''
ajaxData('vote',signUrl("itemid="+brand_id+"&catid="+catId+"&captcha="+captchaVal+"&auth="+authType+"&rnd="+rndNum));

function signUrl(queryString) { 
timestamp=(new Date().getTime().toString().substr(0,10)); 
strs=queryString.split("&"); 
strs.sort(); 
vals=''; 
for (i=0;i<strs.length;i++) 	{ 
	vals=vals+strs[i].split("=")[1]; 
	} 
	return queryString+'&sign='+hex_md5(vals+timestamp); }
'''
captchaValue = 'pwyz'
rnd='403745205696139'


val = 'itemid=52056&catid=40374&captcha=pwyz&auth=1&rnd=403745205696139&sign=e6f346b166128cc13fa1743833480397'


voteUrl = VPath+'vote/7.do.php?'
data={
    'itemid':itemid,
    'catid':catId,
    'captcha':captchaValue,
    'rnd':rnd
}



r = requests.get()


