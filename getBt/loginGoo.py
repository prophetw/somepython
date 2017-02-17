#coding:UTF-8

import requests as rs
from bs4 import BeautifulSoup
import re
import os
import datetime

loginUrl = 'https://accounts.google.com'
googleManageUrl = 'https://accounts.google.com/ManageAccount'

headers = {
    # ":authority":"accounts.google.com",
    # ":method":"GET",
    # ":path":"/",
    # "scheme":"https",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding":"gzip, deflate, sdch, br",
    "accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
    # "cache-control":"no-cache",
    # "pragma":"no-cache",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
# print(headers)

session = rs.session()
firstTouch = session.get(loginUrl, headers=headers)
print('firstTouch headers')
print(firstTouch.headers)
# print(firstTouch.request.headers)

manage = session.get(googleManageUrl,headers=headers)
print('manage set cookies')
print(manage.headers)
# print(manage.request.headers)

# input your name
account = 'wei_wang@foxitsoftware.com'
password = 'P@ssabc123'
inputNameUrl = 'https://accounts.google.com/_/signin/v1/lookup'
data={
"Email":account,
"requestlocation":"https://accounts.google.com/ServiceLogin?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&followup=https%3A%2F%2Faccounts.google.com%2FManageAccount#identifier",
"bgresponse":"!tbaltpdCjs5KQ0CtZ0dE1j51SdSwN_wCAAAAcVIAAAAUmQFcdH54fmhFyotdXFldD2KLVCs0y3q2z8TK-8pcBgCoOpIgrMoY4iwCZ8Vnqy7W5qnFLuVj0lFZFhm1A6McGpJqPTyG7kmbKEjWnbnAyeFPCUM6MKvjhVgmaKIol1FHMC0xv8BH4XibGGO7JMnQTt5Zlp_P2WIQTsmfeVrAcx2qnkXm7HGvvaQk-zdEYMI3fCoGLAvUPEIbIYuwGIWysHiRXmV2jEiwpxdRdAU5OfKOOJs6yRHxfabe5IyKFZ9sGh6LzvE8C5AJo68hLjHaQLcr9CGHVVU01svfFz3JmK8C2Karn5KAxNpG-Z0g9qInyuQc98N1cP_WpTKPQ00eETwggb2iHvrTCOEMaLLHFMioiDExBobNpilMEJ7FQW2OVpyJahoef98xRong6yQWQlWKoBDHXHWpr1kVBeXTp2ubuTQhCL8Cuc3TBfw5h80PS-z2B9Y-JOBzitEdfaUJ",
"Page":"PasswordSeparationSignIn",
"GALX":"JmFEmGD6tDs",
"gxf":"AFoagUVYJrtj81SrwjRX4usvqOKGD62Lug:1487315277369",
"continue":"https://accounts.google.com/ManageAccount",
"followup":"https://accounts.google.com/ManageAccount",
"_utf8":"☃",
"pstMsg":"1",
"checkConnection":"youtube:423:1",
"checkedDomains":"youtube",
"rmShown":"1"
}
s = session.post(inputNameUrl,data=data,headers=headers)
print('input name headers')
print(s.request.headers)
print(s.text)

# input password
passwordData={
"Page":"PasswordSeparationSignIn",
"GALX":"JmFEmGD6tDs",
"gxf":"AFoagUVYJrtj81SrwjRX4usvqOKGD62Lug:1487315277369",
"continue":"https://accounts.google.com/ManageAccount",
"followup":"https://accounts.google.com/ManageAccount",
"ProfileInformation":"APMTqunT2OMTLcaR5kcQQ35euMRr-vJVzuLJi5ZTE4TWHCUN2wZoHqelXHCTsC7gMR9cijGDZOCXv8Fsr2IqGwiozx45zNkD8B4JtqgRDRGH_7DjD-8fP-4TRYzt9K0IT0BwXerF1mzjw7khY6O1w3d2bRID02HL0BG8LPM6Xx6AbS8b84ZdZYKWGj9IBEoy-XPfKKCeK7Eg7wbonqKIyLlQrrnuACkzo8uu8FOna6fTeUpRtI4AMHthf243Cyl-qD0XydpJwKjBizHIXMxE-lKN11KF-hVq8cgG_SICNj99d6dzm5SCRFjDGGnOG6PnDckXoPS0edVV",
"SessionState":"AEThLlxvPKOvoe1vJxN32dbfo7bD-GYGLQiESrEdHM_5NHTlOsjTmEYUBwEMyc9gk5WyLIt0WwDk__-f07HJd78bPaskRpK3ZSdfqGeGF5wVsUCdDCoi-mSn27O9pdqHWxSTglettbYo3aatRf8eCYthB08jxDTIobdwuPBkl-K5VHotdxCGDqG3Q5pEHcq0bFJnWCwhIzCW4fLn-WsoUwAxE2CLG7eKFXjy_7Gg_MSUfJ4snlGpUPKjpoDYliElWF2poeL0bap7k95TX56C_rBnuvZuysHEnm4xZSA99WlkQGPEDtNyeSdmsLnXZQSDpNNOyVehcFSXCXXkyUCkBSFIxaLFFGjkNw",
"_utf8":"☃",
"bgresponse":"!g4ClgKFCjs5KQ0CtZ0dE1j51SdSwN_wCAAAAcVIAAAASmQFcdH54fmhFyotdXFldD2KLVCs0y3q2z8TK-8pcBgCoOpIgrMoY4iwCZ8Vnqy7W5qnFLuVj0lFZFhm1A6McGpJqPTyG7kmbKEjWnbnAyeFPCUM6MKvjhVgmaKIol1FHMC0xv8BH4XibGGO7JMnQTt5Zlp_P2WIQTsmfeVrAcx2qnkXm7HGvvaQk-zdEYMI3fCoGLAvUPEIbIYuwGIWysHiRXmV2jEiwpxdRdAU5OfKOOJs6yRHxfabe5IyKFZ9sGh6LzvE8C5AJo68hLjHaQLcr9CGHVVU01svfFz3JmK8C2Karn5KAxNpG-Z0g9qInyuQc98N1cP_WpTKPQ00eETwggr2kHvp9mjob9MxnRTedhWOTtdWv1xWTEEZPsxSztqAYLf49vnZa9_j1FuWjFl1fXDZO1vMVuZbvaYRgfGd3qemGr6O7BmYpxXhiJHlX7EgeiJzOhQQ1OMSkLPp9",
"pstMsg":"1",
"checkConnection":"youtube:423:1",
"checkedDomains":"youtube",
"identifiertoken":""",
"identifiertoken_audio":""",
"identifier-captcha-input":"",
"Email":"wei_wang@foxitsoftware.com",
"Passwd":"P@ssabc123",
"PersistentCookie":"yes",
"rmShown":"1"
}
postPWDUrl = 'https://accounts.google.com/signin/challenge/sl/password'
passwordResult = session.post(postPWDUrl,data=data,headers=headers)
print('input password headers')
print(passwordResult.request.headers)
# print(passwordResult)

# set cookies twice
# https://accounts.youtube.com/accounts/SetSID?ssdc=1&sidt=ALWU2cs%2BVEFSkdyggtxCX8c%2FlLd6kG6osWMvGhtFZcnJKEArFyIBxNTfFuakUsVl8xTEIlflqfc4ussKLDxb%2FyGrgKEmhbkd0GhU6RGZAMCef8YtigsEBJwbqLoFhib0pCVIUJJAKzy26NF8cQiy9wkeFHO0bddzDLEji%2FI%2FqkHyyZ%2BuWMUSRo2UELzHZSCuUtiN8gui2nuho3VMqg5tEepHXIdNB4iSdK%2FWDS3hiP61IYzdZLI3gcIGxW3YKFOpuVlRHTyvQmXRtOZa2x6bzvPzU636aC0%2Fw%2BcGT4VTUISmNG63Tk1VciI%3D&pmpo=https%3A%2F%2Faccounts.google.com
# https://accounts.google.com.hk/accounts/SetSID?ssdc=1&sidt=ALWU2csoiyuIEFGsy6CdeFbS%2Bnkx1uZkrbiS47G1Bh4kFjrKfV1PkJDY5yCDCWbGBtn4i3tiHzs5E8p0QIGTIbU2UMuvehDpYRjwbaTViRcjCJvsa%2B%2BE%2BQHpfU%2FZJvSR4MYqVXwkEz6b8q%2FQzEGXT0UxlFXHB7ty27qS%2B1Z6zl9NMYmzoJBYqPfcsBpnV3lq%2F1hKgkz%2Bs%2F6l%2FgS2oCt3SG4osLIMMdFey39SPO4gII4yE4MV98aVvUTR%2BipvT6ZVxFo85IGPYsrOr6c%2FKdoGqjBp9Ek9%2B5YnNF4dEz471%2BfrDlIJm%2FAbcNY%3D&pmpo=https%3A%2F%2Faccounts.google.com
# finalResult = session.get('https://myaccount.google.com/?pli=1')
# print(finalResult.content)

dataUrl = 'https://analytics.google.com/analytics/web/?hl=zh-CN#report/conversions-goals-overview/a1680467w127442912p131122512/%3F_u.date00%3D20170205%26_u.date01%3D20170211%26overview_goaloption_ALL-graphOptions.compareConcept%3Danalytics.goal1Completions/'
dataResult = session.get(dataUrl,headers=headers)
print('final headers')
print(dataResult.request.headers)
# print(dataResult.content)