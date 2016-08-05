/**
 * Created by wangwei on 16/8/5.
 */
var authType = 0;
var brand_id = 0;
var curBrand;
var brand_title = "";
var rndNum=Math.random();
var isweixin = false;
var ischeckcaptcha = false;
var VPath = "http://v2.10brandchina.com/";
var shareTitle = "欢迎参与十大品牌投票调查!";
var shareDesc = catYear + "年度中国" + catName + "十大品牌评选网络投票_品牌排行网 ";
var shareSummary = "品牌排行网举办的" + catName + "十大品牌投票正在进行中，欢迎参与十大品牌调查投票!";
var shareUrl = DTPath + "vote/startin.php?id=" + catId;
var shareImg = SKPath + "image/sharelogo.gif";
var captcha = "";
var socket=null;
var useSocket=false;
function ajaxData(action,val){
		if(action=='chkcaptcha'){
			$.ajax({
			type: "get",
			async:false,
			url : VPath+"api/captcha.check.2.php?"+val,
			dataType : "jsonp",
			jsonp: "callbackparam",
			jsonpCallback:"_checkcaptcha",
			success : function(json){
				ischeckcaptcha=false;
			   if(json == '0') {
					Dd('ccaptcha').innerHTML = '&nbsp;&nbsp;<img src="'+SKPath+'image/check_right.gif" align="absmiddle"/>';
				} else {
					Dd('captcha').focus;
					Dd('ccaptcha').innerHTML = '&nbsp;&nbsp;<img src="'+SKPath+'image/check_error.gif" align="absmiddle"/>';
				}
			},
			error:function(){ischeckcaptcha=false;}
			});

		}
		else if(action=='vote')
		{
			$.ajax({
			type : "get",
			async:false,
			url : VPath+"vote/7.do.php?"+val,
			dataType : "jsonp",
			jsonp: "callbackparam",
			jsonpCallback:"_toupiao",
			success : function(json){
				vote_result(json);
			},
			error:function(){}
			});
		}
}
function showcaptcha() {
    ischeckcaptcha = false;
    if (Dd("captchapng").style.display == "none") {
        Dd("captchapng").style.display = ""
    }
    if (Dd("captchapng").src.indexOf("loading.gif") != -1) {
		rndNum=""+catId + brand_id+Math.round(Math.random()*100000);
        Dd("captchapng").src = VPath + "api/captchar.vote.png.php?authType=" + authType + "&rnd=" + rndNum+ "&id=" + brand_id
    }
    if (Dd("captcha").value == "点击显示") {
        Dd("captcha").value = ""
    }
    if(useSocket){
        connect()
    }
    Dd("captcha").className = "";
}
function reloadcaptcha() {
    ischeckcaptcha = false;
	rndNum=""+catId + brand_id+Math.round(Math.random()*100000);
    Dd("captchapng").src = VPath + "api/captchar.vote.png.php?authType=" + authType + "&rnd=" + rndNum+ "&id=" + brand_id;
    Dd("ccaptcha").innerHTML = "";
    Dd("captcha").value = ""
}
function checkcaptcha(s) {
	s=s.replace(/\s+/g,"");
    if (ischeckcaptcha) {
        return
    } else {
        ischeckcaptcha = true
    }
    if (!is_captcha(s)) {
        return
    }
    if (s.length < 4) {
        return
    }
	ajaxData('chkcaptcha',"captcha="+s+"&rnd="+rndNum+"&authType="+authType+ "&id="+brand_id);
}
function reloadJS(id, newJS) {
    var oldjs = null;
    var oldjs = document.getElementById(id);
    if (oldjs) {
        oldjs.parentNode.removeChild(oldjs)
    }
    var scriptObj = document.createElement("script");
    scriptObj.src = newJS;
    scriptObj.type = "text/javascript";
    scriptObj.id = id;
    document.body.appendChild(scriptObj)
}
function signUrl(queryString)
{
	timestamp=(new Date().getTime().toString().substr(0,10));
	strs=queryString.split("&");
	strs.sort();
	vals='';
	for (i=0;i<strs.length;i++)
	{
		vals=vals+strs[i].split("=")[1];
	}
	return queryString+'&sign='+hex_md5(vals+timestamp);
}
//
// authType:1
// rnd:403745205686976
// id:52056
//



function vote(id, authV) {
    brand_id = id;
    curBrand = $("#b" + brand_id);
    brand_title = curBrand.find(".bimg").attr("alt");
    shareTitle = "请为" + brand_title + "品牌投上宝贵一票!";
    shareImg = DTPath + "api/getimg.php?url=" + curBrand.find(".bimg").attr("src").substr(28);
	Dd("brandlogo").src = curBrand.find(".bimg").attr("src");
    shareUrl = DTPath + "vote/startin.php?id=" + catId + "&bid=" + brand_id;
    authType = authV;
	if(catId%2==1)
		{
			VPath = "http://v5.10brandchina.com/"
		}
		else
		{
			VPath = "http://v4.10brandchina.com/"
		}
	$(".vote_captcha").show();
	reloadcaptcha();
	$("#vote_captcha_title").html('喜欢就来支持TA ' + brand_title);

	$("#_message").css("display", "none");
}
function vote_captcha_do()
{
	var captchaVal=$("#captcha").val();
	captchaVal=captchaVal.replace(/\s+/g,"");
	if (captchaVal.length < 4) {
		 alert("验证码没输完");
        return
    }
	$(this).attr("disabled", true);
    if(useSocket){
        sendData('vote',JSON.stringify({"itemid":brand_id,"catid":catId,"captcha":uniencode(captchaVal),"auth":authType,"rnd":rndNum}));
    }
    else
    {
        ajaxData('vote',signUrl("itemid="+brand_id+"&catid="+catId+"&captcha="+captchaVal+"&auth="+authType+"&rnd="+rndNum));
    }
}
function vote_result(json){
            resultArr = json.split(",");
            result = resultArr[0];
			if(isweixin) {
               reloadJS("weixinJs2", "http://v2.10brandchina.com/api/weixin/sdk.php?url=" + location.href.split("#")[0].replace(/\&/g, "~"));
			   shareVoteBrand();
            }
			window._bd_share_config = {
				common: {
					bdText: shareDesc + shareTitle,
					bdDesc: shareTitle + shareSummary,
					bdUrl: shareUrl,
					bdPic: shareImg
				},
				share: [{
					"bdSize": 16
				}]
			};
			with(document) {
				0[(getElementsByTagName("head")[0] || body).appendChild(createElement("script")).src = "http://bdimg.share.baidu.com/static/api/js/share.js?cdnversion=" + ~ ( - new Date() / 3600000)]
			}

            if (result == "ok") {
                var piaoNum = resultArr[1];
                curBrand.find("strong").html(piaoNum);
                $(".vote_captcha").hide();
                $(".tp_title").html('投票成功<br /><a href="' + DTPath + "brand/show-htm-itemid-" + brand_id + '.html" target="_blank"><span class="px14 f_blue">' + brand_title + '：<span class="f_red px14">' + piaoNum + '</span></span></a> <span class="px12 f_gray">' + resultArr[2] + "</span>");
                closeStr = '<img onclick="$(\'#_message\').hide();" class="c_p" src="' + SKPath + 'vote/close.jpg" alt="关闭" />';
                if (appTouPiao > 0) {
                    $(".closeArea").html(closeStr + '&nbsp;&nbsp;<a href="http://a.app.qq.com/o/simple.jsp?pkgname=com.pinpaimap" target="_blank"><img src="' + SKPath + 'vote/app_vote.gif" alt="下载品牌排行网App" /></a>')
                } else {
                    $(".closeArea").html(closeStr)
                }
                $("#_message").css("display", "block");
                $(".share_input").find("input").val(shareUrl);

            } else {
				switch(result)
				{
					case "no":
						if (appTouPiao > 0) {
							uiDialogShow("验证码不正确，刷新下再试！")
						} else {
							alert("验证码不正确，刷新下再试！")
						}
						$("#btnSignCheck" + brand_id).removeAttr("disabled");
						$("#btnSignCheck" + brand_id).css("background", "url(" + SKPath + "vote/vote_btn_n.gif)");
						reloadcaptcha();
						break;
					case "no55":
						show_tip("每个行业同一个IP在30分钟只能投一票，请30分钟后再来！")
						break;
					case "no6":
						show_tip("品牌资质审核通过后才可以继续投票，资质审核流程:企业填写“资质审核表”（<a href=\"/about/audit.php?id="+auditId+"\"><span class=\"f_blue\">点击下载</span></a>）填写完毕后回传给投票页面右侧的“行业专员QQ”等待审核通过后就可以继续投票。（" + catName + "行业专员电话：" + toupiaoTel + "  传真：010-80745637）");
						break;
					case "no7":
						show_tip("每个品牌每小时游客最多能投500票，使用App登录会员可以继续投票！ <a href=\"/about/readme.html\"><span class=\"f_blue\">投票规则</span></a>");
						break;
					case "no8":
						show_tip("品牌投票还没有开始或已经结束！");
						break;
					case "no9":
						show_tip("关爱网友健康，现在是睡眠时间【01:00——07：00】请7点后再投！");
						break;
					case "ref":
						location=location;
					break;
					default:
						show_tip("投票失败,有可能是投票太频繁所致，请隔30分钟后再来投！");
				}
		}
}
function show_tip(str) {
    close_captcha();
    if (appTouPiao > 0) {
        uiDialogShow(str)
    } else {
        alert(str)
    }
}
function close_captcha() {
	 $(".vote_captcha").hide();
    $(".imgck").remove();
}
function onCopy(obj) {
    obj.select();
    js = obj.createTextRange();
    js.execCommand("Copy");
    alert("复制成功！")
}
function shareVoteBrand() {
    content = {
		title: catYear + "年度中国" + catName + "十大品牌网络投票,请支持" + brand_title,
		desc: shareDesc,
		link: shareUrl,
		imgUrl: shareImg
     }
    wx.onMenuShareAppMessage(content);
    wx.onMenuShareTimeline(content)
}
function uiDialogClose() {
    $(".ui_dialog").hide();
    $(".ui_dialog_bg").hide()
}
function get_scrollTop_of_body(){
        var scrollTop;
        if(typeof window.pageYOffset != 'undefined'){
            scrollTop = window.pageYOffset;
        }else if(typeof document.compatMode != 'undefined' && document.compatMode != 'BackCompat'){
            scrollTop = document.documentElement.scrollTop;
        }else if(typeof document.body != 'undefined'){
            scrollTop = document.body.scrollTop;
        }
        return scrollTop;
}
function uniencode(text)
{
    text = escape(text.toString()).replace(/\+/g, "%2B");
    var matches = text.match(/(%([0-9A-F]{2}))/gi);
    if (matches)
    {
        for (var matchid = 0; matchid < matches.length; matchid++)
        {
            var code = matches[matchid].substring(1,3);
            if (parseInt(code, 16) >= 128)
            {
                text = text.replace(matches[matchid], '%u00' + code);
            }
        }
    }
    text = text.replace('%25', '%u0025');
    return text;
}
function uiDialogShow(msg) {
    if (isMobile) {
        dTop = document.body.scrollTop + 100;
        dLeft = document.body.scrollLeft + 2
    } else {
        dTop = get_scrollTop_of_body() + 300;
        dLeft = parseInt(document.body.scrollWidth / 2) - 150
    }
    $(".ui_dialog_body").html(msg);
    $(".ui_dialog").show().css({
        "top": dTop,
        "left": dLeft
    });
    $(".ui_dialog_bg").show()
}
function connect()
{
    if(socket==null || socket.readyState!=1)
    {
        if(catId%2==1)
        {
            socket=new WebSocket('ws://v5.10brandchina.com:8008');
        }
        else
        {
            socket=new WebSocket('ws://v4.10brandchina.com:8008');
        }
        socket.binaryType="arraybuffer";
        socket.onmessage=function(msg){
            if(msg.data instanceof ArrayBuffer)
            {
                var arr=new Uint8Array(msg.data);
                var strArr=new Array();
                for(var i=0;i<arr.length;i++){
                    strArr[i] = String.fromCharCode(arr[i]);
                }
                dataStr=strArr.join("");
                var json = jQuery.parseJSON(dataStr);
                var action=json.action;
                var val=json.msg;
                switch(action)
                {
                    case 'auth':
                        sendData('auth',eval(val));
                    break;
                    case 'vote':
                        vote_result(val);
                    break;
                }
            }
        }
        socket.onopen=function(e){sendData('auth',authType);}
        socket.onclose=function(){close_captcha();}
    }
}
function sendData(action,val){
	if(socket && socket.readyState==1)
	{
		var arr=JSON.stringify({'action':action,'val':val}).split("");
		var strArr=new Array();
		for(var i=0;i<arr.length;i++){
			strArr[i] = arr[i].charCodeAt();
		}
		var data=new Uint8Array(strArr);
		socket.send(data.buffer);
	}
	else
	{
		close_captcha();
	}
}
var body = document.documentElement || document.body;
if (isGecko) {
    body = document.body
}
if (isMobile) {
    if (UA.indexOf("micromessenger") != -1) {
        isweixin = true;
        reloadJS("weixinJs2", "http://v2.10brandchina.com/api/weixin/sdk.php?url=" + location.href.split("#")[0].replace(/\&/g, "~"));
    } else {
        if (UA.indexOf("weibo") != -1) {
            var shareConfig = {
                url: shareUrl,
                title: shareDesc + shareTitle,
                appkey: 3269435896,
                pic: shareImg
            };
            var _shareConfig = [];
            for (var i in shareConfig) {
                _shareConfig.push(i + "=" + encodeURIComponent(shareConfig[i] || ""))
            }
            $(".update_toupiao_btn").append('<br/><a href="http://service.weibo.com/share/share.php?' + _shareConfig.join("&") + '" target="_blank"><img src="' + SKPath + 'vote/share_weibo.png" vspace="10"/></a>')

        }
    }
}
$(document).ready(function() {
	reloadJS('md5',"http://img.10brandchina.com/file/script/md5-min.js");
    $("#myKefuClose").click(function() {
        $(".my_kefu_box,.update_toupiao_btn").hide()
    });
    if(typeof(window.WebSocket)!="undefined" && window.WebSocket)//isMobile &&
	{
		useSocket=true;
	}
    urls = location.href.split("#")[0].split("?");
    if (urls.length > 2) {
        url = urls[2];
        if (url.indexOf("lh") != -1 || url.indexOf("wwf") != -1 || url.indexOf("lk") != -1 || url.indexOf("dy") != -1 || url.indexOf("fx") != -1 || url.indexOf("lq") != -1 || url.indexOf("lyt") != -1 || url.indexOf("zln") != -1 || url.indexOf("yzf") != -1) {
            reloadJS("usercount", "http://v1.10brandchina.com/tuiguang/task.php")
        }
    }
});