#encoding=utf-8
#/usr/bin/python
__author__ = 'Administrator'
import commands
import sys
import re
import os
import getopt
def usage():
    print """
             ==========================================================
             语法： getload [参数]...

             功能描述: 显示主机负载情况

             参数说明:
             --help                  显示帮助信息
             -h                      显示帮助信息
             -g                      显示一个组下面所有的IP地址负载情况
             -i                      显示指定IP地址的负载情况
            ==========================================================
          """

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hg:i:',['help'])
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
         print commands.getoutput("ssh log@%s 'cat /proc/loadavg'|awk '{print $1,$2,$3}'"%arg)
    elif opt == '-g':
        com=commands.getoutput('python getnode.py -g %d --lan'%int(arg))
        iplist=com.split()
        for ip in iplist:
             print "===========%s============"%ip
             print commands.getoutput("ssh log@%s 'cat /proc/loadavg'|awk '{print $1,$2,$3}'"%ip)
    else:
        usage()
        sys.exit()
                     
