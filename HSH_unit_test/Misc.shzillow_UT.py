##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

from __future__ import print_function
from HSH.Misc.shzillow import  zillow_property_detail
# from HSH.Misc.logger import Log

if __name__ == "__main__":
    address, zipcode = "5522 SEQUIN DR", "77388"
    try:
        print(zillow_property_detail(address, zipcode))
    except Exception as e:
        print(e)