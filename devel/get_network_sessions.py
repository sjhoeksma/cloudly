import os
import sys
import re
import time
import getpass
import datetime
import platform
import base64, pickle

import urllib
import httplib
import subprocess


def _get_network_sessions():

    print 'Active Internet Connections (including servers)'
    
    # XXX resolve services

    try:
        netstat = subprocess.Popen(["/bin/netstat","-atn"], stdout=subprocess.PIPE, close_fds=True).communicate()[0]
    except:
        netstat = subprocess.Popen(["/usr/sbin/netstat","-atn"], stdout=subprocess.PIPE, close_fds=True).communicate()[0]


    print netstat
    
    return "XXX"
    
    
    
_get_network_sessions()

    
