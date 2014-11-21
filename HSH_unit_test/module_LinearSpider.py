##encoding=utf8

from __future__ import print_function
from HSH.LinearSpider.proxymanager import ProxyManager
from HSH.LinearSpider.crawler import Crawler
from bs4 import BeautifulSoup as BS4


class ProxyManager_unittest():
    @staticmethod
    def _equip_proxy():
        pm = ProxyManager()
        pm._equip_proxy() # see if successfully get latest available proxy from www.us-proxy.org
        print(pm)
    
    @staticmethod
    def dump_pxy():
        print("{:=^100}".format("dump_pxy"))
        pm = ProxyManager()
        pm.dump_pxy()
        
    @staticmethod
    def load_pxy():
        print("{:=^100}".format("load_pxy"))
        pm = ProxyManager()
        print("{:=^60}".format("before"))
        print(pm)
        pm.load_pxy()
        print("{:=^60}".format("after"))
        print(pm)
        
    @staticmethod
    def generate_one():
        pm = ProxyManager()
        pm._equip_proxy()
        print(pm.generate_one()) # sample proxies = {"http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080",}
        print(pm.current_proxy) # see if proxy manager saved the most recent proxy to self.current_proxy
    
    @staticmethod
    def update_health():
        pm = ProxyManager()
        pm._equip_proxy()
        try:
            pm.update_health(1)
        except Exception as e:
            print(e)
            
        print(pm.generate_one())
        pm.update_health(1)
        print(pm)


class Crawler_unittest():
    @staticmethod
    def set_referer():
        print("{:=^100}".format("set_referer"))
        spider = Crawler()
        print(spider)
        spider.set_referer("https://www.python.org/")
        print(spider)
        
    @staticmethod
    def enable_proxy():
        print("{:=^100}".format("enable_proxy"))
        spider = Crawler()
        spider.enable_proxy()
        print(spider)
        
    @staticmethod
    def html_WITHOUt_proxy():
        """test normal http request"""
        url = "http://docs.python-requests.org/"
        spider = Crawler()
        html = spider.html(url)
        print(BS4(html).prettify())
        
    @staticmethod
    def html_WITH_proxy():
        """test random proxy mechanism"""
        url = "http://docs.python-requests.org/"
        spider = Crawler()
        spider.enable_proxy()
        for i in range(100):
            html = spider.html(url)
            print(i, spider.pm.current_proxy)
            if html:
                print("\tSUCCESS")
                spider.pm.update_health(1)
            else:
                print("\tFAILED")
        print(spider)
        
        
if __name__ == "__main__":
#     ProxyManager_unittest._equip_proxy()
#     ProxyManager_unittest.dump_pxy()
#     ProxyManager_unittest.load_pxy()
#     ProxyManager_unittest.generate_one()
#     ProxyManager_unittest.update_health()

#     Crawler_unittest.set_referer()
#     Crawler_unittest.enable_proxy()
#     Crawler_unittest.html_WITHOUt_proxy()
#     Crawler_unittest.html_WITH_proxy()

    
    print("COMPLETE")