#!/usr/bin/env python
#  Encoding: utf-8
#  Author:luol2@knownsec.com
#  Description:
from __future__ import division
import threading
import urllib2
from urllib import urlencode 
import httplib2
import getopt
import time
import json
import sys
import os
import commands
reload(sys)
sys.setdefaultencoding('utf-8')
def getid():
    i= (commands.getoutput("groupinfo -b |grep '免费版'|awk '{print $2}'")).split()
    for ii in i:
        print postdata(ii)



def postdata(ii):
    url = "http://jslyj.jiasule.com/yjsghdf/audit/advanced/"
#构造cookie信息
    Cookie = 'csrftoken=sAKa7Hys9qPsc77x3FEeH0rDWSTQzajU; Hm_lvt_b1fa0002def3d4a3f5a25f52bbb8c1fa=1450430130,1450686265,1450773213,1450856117; jsl_sid=7qbk020o1i8b1qflmnduj0akdvw8xba9; otp_key=otp6c9e295c60c2b252cd74de8c8300f23e'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie':Cookie}
    values={
'id':'%s'%ii,
'site_law_value':'0_5',
'site_law_type':'',
'site_group':'1',
'site_law_note':'原来是大客户分组,付费到期后没有续期，迁移到1号分组,并显示违规需要缴费处理,有大攻击　by周力',
'csrfmiddlewaretoken':'sAKa7Hys9qPsc77x3FEeH0rDWSTQzajU',
'site_law_sign':'site_law_sign_5'
           }
#初始化http请求
    http = httplib2.Http()
    response, content = http.request(url,'POST',urlencode(values),headers=headers)
    return content

getid()
#print postdata('563b48feeb5fcf0f5f23cc44') 
