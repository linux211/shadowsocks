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
for group in range(258,602):
        print "-------------%s分组----------------\n"%group,commands.getoutput("python chgroup.py -g %s --list|grep  '免费'"%group) 
    #print group
