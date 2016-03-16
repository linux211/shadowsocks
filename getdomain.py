#encoding=utf-8
__author__ = 'Administrator'
import httplib2
import sys
import urllib
from sgmllib import SGMLParser
import getopt
import os

#从交互中获输入的域名


def usage():
    print """
             =========================================================
             语法： getdomain [参数]...

             功能描述: 通过用户名获取对应下的域名

             参数说明：
             --help                  显示帮助信息
             -h                      显示帮助信息
             -i                      显示输入用户名
             ========================================================= """
#初始化URL
def getid():
    url = "http://jslyj.jiasule.com/yjsghdf/group/list/?domain=&username=%s&site_group=&group=&site_law_sign=&site_belong=&source=&site_bandwidth=all&start=&end=&filter=搜索"%xihaha

#构造cookie信息
    Cookie = 'csrftoken=p4Wkiw0wsyokc9Y3D2p0Fv9mANAIUQD5; Hm_lvt_b1fa0002def3d4a3f5a25f52bbb8c1fa=1450430130,1450686265,1450773213,1450856117; jsl_sid=s1rfpum8rnoumg9ez757rn59elcjbhcy; otp_key=otp1ecfa334c84080e8437c30dfff43a688'
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
         xihaha=arg
#初始化需要查找的关键字符串的方法
         class ListName(SGMLParser):
	         def __init__(self):
	             SGMLParser.__init__(self)
	             self.xiha = []
	         def start_td (self,attrs):
                  for name,value in attrs:
                    if name == 'title':
                        self.xiha.append(value)
	         def end_td(self):
                  pass
	         def handle_td(self, text):
                  pass
         ln=ListName()
         ln.feed(getid())
         print '\n'.join(ln.xiha)
    else:
        usage()
        sys.exit()





