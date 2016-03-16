#!/usr/bin/env python
#  Encoding: utf-8
#  Author:zzzzzz
#  Description:
import commands
import sys
import re
import os
import getopt
os.chdir('/last')
ii=[]
def usage():
    print """
          =====================================================================
         语法： newsitegrp [参数]...
         功能描述: 迁移观察分组中的域名
         help                    显示帮助信息
         -h                      显示帮助信息
         -g                      将输入指定分组域名调整到对应的下个观察分组
        （备注：目前只有0,120,121,122,123观察分组，对应关系0>>120>>121>122>123，
         请输入0,120,121,122参数）
         -a                      动将所有观察分组域名进行调整
         ======================================================================"""

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
    elif opt == '-g':
        if arg == '0':
               i=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'0')
               if int(i) > 200:
                  dee=(commands.getoutput("python chgroup.py -g %s --list|tail -n 1|awk '{print $2,$3}'"%'0')).split()
                  if dee[1] == "免费版":
                     print commands.getoutput("python chgroup.py  -i %s -g 120"%dee[0]) 
                   
               else:
                   print "本组的域名已经少于200，暂时不移动剩余部分"
        elif arg == '120':
               i=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'120')
               if int(i) > 200:
                  de=(commands.getoutput("python chgroup.py -g %s --list|tail -n 1|awk '{print $2}'"%'120')).split()
                  for xx in de:
                     print commands.getoutput("python chgroup.py  -i %s -g 121"%xx)
               else:
                   print "本组的域名已经少于200，暂时不移动剩余部分"
        elif arg == '121':
               i=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'121')
               if int(i) > 200:
                  de=(commands.getoutput("python chgroup.py -g %s --list|tail -n 1|awk '{print $2}'"%'121')).split()
                  for xx in de:
                      print commands.getoutput("python chgroup.py  -i %s -g 122"%xx)
               else:
                   print "本组的域名已经少于200，暂时不移动剩余部分"
        elif arg == '122':
               i=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'122')
               if int(i) > 200:
                  de=(commands.getoutput("python chgroup.py -g %s --list|tail -n 1|awk '{print $2}'"%'122')).split()
                  for xx in de:
                      print commands.getoutput("python chgroup.py  -i %s -g 123"%xx)
               else:
                   print "本组的域名已经少于200，暂时不移动剩余部分"
        elif arg == '123':
               i=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'123')
               if int(i) > 200:
                  de=(commands.getoutput("python chgroup.py -g %s --list|tail -n 1|awk '{print $2}'"%'123')).split()
                  for xx in de:
                      print commands.getoutput("python chgroup.py  -i %s -g 30"%xx)
               else:
                   print "本组的域名已经少于200，暂时不移动剩余部分"
        else:
               usage()
               sys.exit()

    elif opt == '-a':
#步骤一122组到123组
        i122=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'122')
        if int(i122)>200:
            d121=(commands.getoutput("python chgroup.py -g %s --list|tail -n 2|awk '{print $2}'"%'122')).split()
            for xx in d121:
                print commands.getoutput("python chgroup.py  -i %s -g 123"%xx)
        else:
            print "122组的域名已经少于200，暂时不移动剩余部分"
#步骤二121组到122组
        i121=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'121')
        if int(i121)>200:
            d122=(commands.getoutput("python chgroup.py -g %s --list|tail -n 2|awk '{print $2}'"%'121')).split()
            for xx in d122:
                print commands.getoutput("python chgroup.py  -i %s -g 122"%xx)
        else:
            print "121组的域名已经少于200，暂时不移动剩余部分"
#步骤二120组到121组
        i120=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'120')
        if int(i120)>200:
            d120=(commands.getoutput("python chgroup.py -g %s --list|tail -n 2|awk '{print $2}'"%'120')).split()
            for xx in d120:
                print commands.getoutput("python chgroup.py  -i %s -g 121"%xx)
        else:
            print "120组的域名已经少于200，暂时不移动剩余部分"
#步骤二0组到120组
        i0=commands.getoutput("python chgroup.py -g %s --list|wc -l"%'0')
        if int(i0)>200:
            d0=(commands.getoutput("python chgroup.py -g %s --list|tail -n 2|awk '{print $2}'"%'0')).split()
            for xx in d0:
                print commands.getoutput("python chgroup.py  -i %s -g 120"%xx)
        else:
            print "0组的域名已经少于200，暂时不移动剩余部分"
    else:
        usage()
        sys.exit()



