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
config = {
   "ii":"",
   "t":"",
   "bz":"",
         }
def usage():
    print """
             =========================================================
             语法： jiahei [参数]...

             功能描述: 一键拖黑域名，输入项务必输入完整

             参数说明：
             --help                  显示帮助信息
             -h                      显示帮助信息
             -i                      输入域名
             --t                     输入拖黑时间2,6,12,48小时
             -d                      输入备注操作
             -n                      输入拖黑的用户名，可以拖黑整个用户名下的域名
             ========================================================= """

def postdata(ii,t,bz):
    url = "http://jslyj.jiasule.com/yjsghdf/black/add/"
#构造cookie信息
    Cookie = 'csrftoken=p4Wkiw0wsyokc9Y3D2p0Fv9mANAIUQD5; Hm_lvt_b1fa0002def3d4a3f5a25f52bbb8c1fa=1450430130,1450686265,1450773213,1450856117; jsl_sid=s1rfpum8rnoumg9ez757rn59elcjbhcy; otp_key=otp1ecfa334c84080e8437c30dfff43a688'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie':Cookie}
    values={
'domain':'%s'%ii,
'status':'1',
'description':'%s'%bz,
'limit_type':'0',
'auto':'0',
'time':'%s'%t,
'dns_disabled':'0',
'credit':'1',
'credit_size':''
           }
#初始化http请求
    http = httplib2.Http()
    response, content = http.request(url,'POST',urlencode(values),headers=headers)
    return content

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hi:d:',['help','t='])
except getopt.GetoptError:
    usage()
    sys.exit()

if len(opts) == 0:
    usage()
    sys.exit()

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit()
    elif opt in ['-i']:
         config["ii"]=arg
    elif opt in ['-n']:
         de=(commands.getoutput("python getdomain.py -i %s"%arg)).split() 
         for d in de:
             config["ii"]=d
    elif opt in ['--t']:
         if arg not in ['2','6','12','48']:
            usage()
            sys.exit()
         else:
            config["t"]=arg
    elif opt in ['-d']:
         config["bz"]=arg
    else:
       usage()
       sys.exit()
postdata(config["ii"],config["t"],config["bz"])
