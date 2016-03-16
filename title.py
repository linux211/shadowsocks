#encoding=utf-8
__author__ = 'Administrator'
import httplib2
import sys
import urllib
from sgmllib import SGMLParser
import getopt
import os
import sys
import commands
#def gettitle():
#    url = "http://%s"%domian()
#初始化http请求
#    http = httplib2.Http()
#    response, content = http.request(url,'GET')
#    return content


class ListName(SGMLParser):
       def __init__(self):
           SGMLParser.__init__(self)
           self.xiha = ""
           self.title=[]
       def start_title (self,attrs):
           self.xiha=1
       def end_title(self):
           self.xiha=""
       def handle_data(self, text):
           if self.xiha == 1:
              if  text:
                  self.title.append(text)
              else:
                  self.title.append("no title")
            

def getdd():
    dee=(commands.getoutput("python chgroup.py -g %s --list|awk '{print $1}'"%sys.argv[1])).split()
    for d in dee:
        url = "http://%s"%d
        http = httplib2.Http()
        response, content = http.request(url,'GET')
        ln=ListName()
        ln.feed(content)
        for item in  ln.title:
            print "-----%s-----title is -----\n"%d,item

getdd()
