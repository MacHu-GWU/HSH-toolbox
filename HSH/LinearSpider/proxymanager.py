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

from __future__ import print_function
from bs4 import BeautifulSoup as BS4
import pandas as pd
import requests
import sys
import random, itertools

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    reload(sys); # change the system default encoding = utf-8
    eval("sys.setdefaultencoding('utf-8')")
    
class ProxyManager(object):
    """
    [EN]
    [CN]代理管理器
    在爬虫程序中，为了不因为短时间内对服务器太多次的访问而导致被block，所以采用代理技术隐瞒自己的IP是
    重要技巧。假如我们在网上找到了10个代理，但并不是每个代理都够稳定能用，所以我们需要采用计算代理健康
    度的方法来评估哪个代理能用，哪个代理不能用。
    
    健康度评估算法：
        每个代理有三个属性: 成功次数，尝试次数，健康度
        每次使用代理，如果成功，则成功次数和尝试次数+1
        每次使用代理，如果失败，则成功次数和尝试次数+1
        健康度在尝试次数小于5次时都是1.0，如果尝试次数多于五次，则健康度 = 成功次数/尝试次数
        
    
    """
    def __init__(self):
        self._equip_proxy()
        self.current_proxy = None
        
    def __str__(self):
        return str(self.proxy)
    
    def _equip_proxy(self, maximum_num_of_proxy = 10):
        """load latest availble proxy from www.us-proxy.org
        """
        ### get www.us-proxy.org homepage html
        user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"]
        header = {"Accept":"text/html;q=0.9,*/*;q=0.8",
                  "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
                  "Accept-Encoding":"gzip",
                  "Connection":"close"}
        header["User-Agent"] = random.choice(user_agents)
        response = requests.get("http://www.us-proxy.org/", 
                                headers = header)
        html = response.text.encode("utf-8")
        
        ### analyze the html, save useful proxy.
        ips = list()
        res = list()
        
        soup = BS4(html)
        table = soup.find("table", id = "proxylisttable")
        for tr in table.tbody.find_all("tr"):
            ip, port, code, country, anonymity, google, https, last_check = [td.text for td in tr.find_all("td")]
            ### === EDIT THE FOLLOWING RULES CAN FILTER THE PROXY YOU WANT 
            if anonymity == "elite proxy":
                ips.append("http://%s:%s" % (ip, port))
                res.append([0.0, 0.0, 1.0])
                if len(res) >= maximum_num_of_proxy: # if got enough useful proxy, then step out
                    break
        
        self.proxy = pd.DataFrame(res, index = ips, columns = ["success", "tried", "health"])
        
    def generateone(self):
        """randomly choose a proxy with health greater than 0.75
        """
        health_proxy = self.proxy[self.proxy["health"] >= 0.75].index
        self.current_proxy = random.choice(health_proxy)
        return {"http": self.current_proxy}

    def update_health(self, successed):
        """update proxy health after you using proxy to visit any url
        successed: boolean, the http request using the proxy succeed or not
        """
        if self.current_proxy:
            ip = self.current_proxy
        else:
            raise Exception("ERROR: never generate any proxy; please use self.generateone method first")
        
        if successed: # if is successful, tried + 1, success + 1
            self.proxy.loc[ip, ["success", "tried"]] += 1.0
            if self.proxy.loc[ip, "tried"] >= 5: # if tried more than 10 times, then we keep update successful rate
                self.proxy.loc[ip, "health"] = float(self.proxy.loc[ip, "success"])/self.proxy.loc[ip, "tried"]
        else: # if failed, tried + 1, success remain
            self.proxy.loc[ip, "tried"] += 1.0
            if self.proxy.loc[ip, "tried"] >= 5: # if tried more than 10 times, then we keep update successful rate
                self.proxy.loc[ip, "health"] = float(self.proxy.loc[ip, "success"])/self.proxy.loc[ip, "tried"]