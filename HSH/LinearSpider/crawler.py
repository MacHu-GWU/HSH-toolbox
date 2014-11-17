##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""Http Crawler
Repack of requests
"""

from __future__ import print_function
import requests
import sys
import os
import random

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    reload(sys); # change the system default encoding = utf-8
    eval("sys.setdefaultencoding('utf-8')")

class Crawler(object):
    """Simple http Crawler class
    """
    def __init__(self):
        self.user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"]
        self.auth = None # initialize the self.auth. Then if there"s no login, Crawler.html can work in regular mode
    
    def _gen_header(self):
        """generate a random header
        """
        headers = {"User-Agent": random.choice(self.user_agents),
                   "Accept":"text/html;q=0.9,*/*;q=0.8",
                   "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
                   "Accept-Encoding":"gzip",
                   "Connection":"close",
                   "Referer":None}
        return headers
    
    def _login(self, url, payload, timeout = 6):
        """website log in
            url = login_page_url
            payload = {key1: acc, key2: password}
        """
        self.auth = requests.Session()
        try:
            self.auth.post(url, data=payload, timeout=timeout)
            print("successfully logged in to %s" % url)
            return True
        except:
            return False
    
    def html(self, url, timeout = 6):
        """return the html of the url
        Notice:
            ressponse.text always returns bytes (in python2, it calls str; in python3 it calls bytes)
        THUS:
            always encoding the bytes into utf-8 is a good choice
        """
        if not self.auth: # if no login needed, then self.c = None, then not self.c = True
            ## regular get html, use requests.get
            try:
                response = requests.get(url, headers = self._gen_header(), timeout = timeout)
                return response.text.encode("utf-8") # if success, return html
            except:
#                 print("%s time out!" % url) # <=== 测试时才用
                return None # if failed, return none
        else: # if login needed, use self.auth.get
            try:
                response = self.auth.get(url, headers = self._gen_header(), timeout = timeout)
                return response.text.encode("utf-8") # if success, return html
            except:
#                 print("%s time out!" % url) <=== 测试时才用
                return None # if failed, return none
    
    def save_html(self, url, save_as, timeout = 10):
        """save the html to save_as, which is a .html local file
        """
        html = self.html(url)
        if html:
            with open(save_as, "wb") as f:
                f.write(html)
            
    def download(self, url, save_as, timeout = 10):
        """download the file by url to the path of save_as
        """
        if not self.auth:
            try:
                response = requests.get(url, headers = self._gen_header(), timeout = timeout, stream=True)
                with open(save_as, "wb") as f:
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        f.write(block)
            except:
                pass
        else:
            try:
                response = self.auth.get(url, headers = self._gen_header(), timeout = timeout, stream=True)
                with open(save_as, "wb") as f:
                    for block in response.iter_content(1024): # use buffer to download
                        if not block:
                            break
                        f.write(block)
            except:
                pass
            
def ignore_iterkeys(dictionary, ignore = ["ref"]): # data 在线性爬虫中用于默认储存task.todo的传递信息，详情见Readme.MD
    """iter dict keys, ignore the key in the "ignore" list"""
    for key in dictionary:
        if key not in ignore:
            yield key

def ignore_itervalues(dictionary, ignore = ["ref"]):
    """iter dict keys, ignore the key in the "ignore" list"""
    for key in dictionary:
        if key not in ignore:
            yield dictionary[key]
            
def ignore_iteritems(dictionary, ignore = ["ref"]):
    """iter dict keys, ignore the key in the "ignore" list"""
    for key in dictionary:
        if key not in ignore:
            yield key, dictionary[key]