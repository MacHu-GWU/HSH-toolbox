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

def gen_url(address, zipcode):
    base = "http://www.zillow.com/homes/"
    return base + address.replace(" ", "-") + "-" + zipcode + "_rb/"

