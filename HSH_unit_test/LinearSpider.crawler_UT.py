##encoding=utf8
##version =py27,py34
##author  =sanhe
##date    =2014-10-11

from __future__ import print_function
from HSH.LinearSpider.crawler import Crawler, ignore_iterkeys, ignore_itervalues, ignore_iteritems
import chardet

def UT_crawl_html():
    spider = Crawler()
    # test html download
    url = "https://www.python.org/" 
    print( spider.html(url) )
    
    # test save html to .html
    url = "http://www.archives.com/"
    spider.save_html(url, "www.archives.com.html")
    
    # test file download
    img_url = "https://www.python.org/static/img/python-logo.png" 
    spider.download(img_url, "python-logo.png")
    
    # test download html to .html file
    target_url = "http://www.archives.com/" # www.archives.com 是 utf-8 编码
    with open("before_login.html", "wb") as f: # because requests.text return bytes, so mode has to be "wb"
        html = spider.html(target_url)
        print( type(html), chardet.detect(html) ) # 用于展示在2和3之中requests.text返回的对象类型
        f.write( html )
         
    spider._login(url = "http://www.archives.com/member/", # test html after login
                  payload = {"__uid":"sanhe.hu@theeagleforce.net","__pwd":"efa2014"} )
    with open("after_login.html", "wb") as f:
        f.write( spider.html(target_url))
    
if __name__ == "__main__":
    UT_crawl_html() # 2014-10-11 python2,3 测试通过!