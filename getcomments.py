import requests as rs
s = rs.Session()
#获取cookies
s.get('')


rqheaders = {
	"Host":"music.163.com",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding":"gzip, deflate",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"Referer":"http://music.163.com/song?id=35403523",
	"Cookie":"_ntes_nnid=ab008d1775f46afab55bbd40a7eae6a0,1440999120826; vinfo_n_f_l_n3=cf9ee7c8a67d8bfd.1.0.1440999120839.0.1441000148097; __oc_uuid=9abcc6a0-4fa1-11e5-8bcd-43486c014d92; _ntes_nuid=ab008d1775f46afab55bbd40a7eae6a0; __utma=187553192.1163080188.1440999121.1440999121.1440999121.1; __utmz=187553192.1440999121.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; P_INFO=wangjiawei1312@126.com|1442300553|0|other|11&16|anh&1442039546&other#anh&341400#10#0#0|&0|blog|wangjiawei1312@126.com; NTES_PASSPORT=f8xjc641bGWp7L8VUJUfkP9nBgBAiA81IA9DzRXXsqEUfUERhD3fQRQyrm8t06Vwy6E2SjRtb8R9Q4ji6bY18KwYYavqTA1I_IXWdclj5bpFR; NTES_REPLY_NICKNAME=wangjiawei1312%40126.com%7Cwangjiawei1312%7C%7C%7C%7Cf8xjc641bGWp7L8VUJUfkP9nBgBAiA81IA9DzRXXsqEUfUERhD3fQRQyrm8t06Vwy6E2SjRtb8R9Q4ji6bY18KwYYavqTA1I_IXWdclj5bpFR%7C1%7C-1; __utma=94650624.1497516740.1445413631.1445413631.1445647903.2; __utmz=94650624.1445647903.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=51c327b6959b4d97aa3b32ea2f4a0d16451bcee56a19579529dca32ef81908fc4fac56dcd29e2aacb8a5a97a564a549a2a360542b8e9e9d7b3f296886d017f52e19b6e035e14d16ad8a1f90e606943e22953c9a0a6418bf8494e212d0c208c5fa2dfb7ae8f941c31e99c77255281e153113bb7e34b1a48ad1b66c4827f8c6c7166afa7b1%3A1445649702427; _iuqxldmzr_=25; __utmb=94650624.9.10.1445647903; __utmc=94650624; visited=true",
	"Connection":"keep-alive",
	"Pragma":"no-cache",
	"Cache-Control":"no-cache",
	"Content-Length":"484"
}
posturl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_35403523/?csrf_token='
postdata = {
	'params':'q2Qaoc4MkLaeiHMuIyVF3wt2J7BKQWlb+1PfAOlhzsEsB0Va2G3t6G2xBnv9emAyjCI+nBUKX9L/gOoag0buIbAdV42acdmdYV7K+ABv1VQ+uBrIHpAuIt33QGZSM7qpy/zPXGUI/fjcNDfGfjBY2NzJpXiJws3koipv+wKZTsIJynpkaU9OcZfCJCIFFYo+',
	'encSecKey':'aa1ef6cdcfd1495a2eaa90ac2d4f5dea653e58fa247eaa52502acd35a44f0a7806f678097c416135c772ef12b3d767f994ef4149421e008c3a2f067153e6e26940b2267cb7dbe88c27183a5b7e9c45680d351c00ae95e2ad19ecde7a3caf096cbd5b1bef9b22b67d8a143d8a8cbf5a696fbc7df80eb3d218911396a557cd207b'
}





