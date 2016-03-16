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
group=[1,2,3,4,6,8,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,36,37,38,39,40,41,42,43,44,45,46,48,51,57,58,67,108,109,110,111,112,113,114,116,117,118,119,124,219,22,220,221,222,223,224,225,226,227,230,234,235,236,240,241,242,243,244,245,246,247,248,257,258]
print "-----付费分组中有免费的域名,具体分组信息如下------"
for fenzu in group:
    print "-------------%s分组----------------\n"%fenzu,commands.getoutput("python chgroup.py -g %s --list|grep  '免费'"%fenzu)                                                                                                                                           
