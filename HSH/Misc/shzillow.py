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

"""
shzillow is a zillow property data crawler create by Sanhe

Import:
    from HSH.Misc.shzillow import zillow_property_detail
"""
from __future__ import print_function
try:
    from ..LinearSpider.crawler import Crawler
except:
    from HSH.LinearSpider.crawler import Crawler
    
from bs4 import BeautifulSoup as BS4

class HttpError(Exception):
    def __init__(self, address, zipcode, url):
        self.address= address
        self.zipcode = zipcode
        self.url = url
        self.index = "Zillow Crawler HttpError"
        
    def __str__(self):
        return "Failed to get http response from url = %s,  address = %s, zipcode = %s" % (self.address, 
                                                                                           self.zipcode, 
                                                                                           self.url)

class ExtractorError(Exception):
    def __init__(self, address, zipcode, url):
        self.address= address
        self.zipcode = zipcode
        self.url = url
        self.index = "Zillow Crawler ExtractorError"
        
    def __str__(self):
        return "Failed to analysis address = %s, zipcode = %s from url = %s" % (self.address, 
                                                                                self.zipcode, 
                                                                                self.url)

def gen_url(address, zipcode):
    base = "http://www.zillow.com/homes/"
    return base + address.replace(" ", "-") + "-" + zipcode + "_rb/"

def zillow_property_detail(address, zipcode):
    url = gen_url(address, zipcode) # generate query's http url
    spider = Crawler()
    html = spider.html(url) # fetch html
    if html: # if good html, analysis it
        try:
            soup = BS4(html)
            dt = soup.find("dt", class_ ="property-data")
            info = dt.text.strip()
            span = soup.find("span", itemprop = "addressLocality")
            city = span.text.strip()
            span = soup.find("span", itemprop = "addressRegion")
            state = span.text.strip()
            return address, city, state, zipcode, info
        except: # if something wrong in analysis, raise ExtractorError
            raise ExtractorError(address, zipcode, url)
    else: # if bad html, raise HttpError
        raise HttpError(address, zipcode, url)