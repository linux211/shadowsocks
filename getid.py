#encoding=utf-8
__author__ = 'Administrator'
import httplib2
import sys
import urllib
from sgmllib import SGMLParser
import getopt
import os

#从交互中获输入的域名
domain='aisichun.com'


def usage():
    print """
             =========================================================
             语法： getid [参数]...

             功能描述: 显示域名的唯一ID

             参数说明：
             --help                  显示帮助信息
             -h                      显示帮助信息
             -i                      显示输入域名的ID
             ========================================================= """
#初始化URL
def getid():
    url = "http://jslyj.jiasule.com/yjsghdf/group/list/?page=1&domain=%s&username=&site_group=&group=&site_belong=&start=&end=&site_law_sign="%domain

#构造cookie信息
    Cookie = 'csrftoken=nwghgsPotUJJO00OckYJM0zQM8SCTfyo; Hm_lvt_b1fa0002def3d4a3f5a25f52bbb8c1fa=1442973089,1443057588,1443062027,1443428971; jsl_sid=cwq2kz8p6ltcxz6jo2cz2eq7ouh20tpu; otp_key=otp74b627e6066d04ab4b44d69366ee7151'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie':Cookie}

#初始化http请求
    http = httplib2.Http()
    response, content = http.request(url,'GET',headers=headers)
    return content


try:
    opts, args = getopt.getopt(sys.argv[1:], 'hi:',['help'])
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
    elif opt == '-i':
#初始化需要查找的关键字符串的方法
         class ListName(SGMLParser):
	         def __init__(self):
	             SGMLParser.__init__(self)
	             self.xiha = []
	         def start_span (self,attrs):
                  for name,value in attrs:
                    if name == 'id'and len(value) == 24:
                        self.xiha.append(value)
	         def end_span(self):
                  pass
	         def handle_data(self, text):
                  pass
         ln=ListName()
         ln.feed(getid())
         print ''.join(ln.xiha)
    else:
        usage()
        sys.exit()





