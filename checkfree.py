#!/usr/bin/env python
#  Encoding: utf-8
#  Author:luol2@knownsec.com
#  Description:
from __future__ import division
import threading
import urllib2
import getopt
import time
import json
import sys
import os
import commands
reload(sys)
sys.setdefaultencoding('utf-8')
group=[0,5,7,9,10,30,31,32,33,34,50,52,53,54,55,56,59,60,61,62,63,64,65,66,120,121,122,123]
print "-----免费分组中有付费的域名,具体分组信息如下------"
for fenzu in group:
    print "-------------%s分组----------------\n"%fenzu,commands.getoutput("python chgroup.py -g %s --list|grep -E 'CDN|创|专业|抗'"%fenzu)
