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
from HSH.Misc.shgeo import dist, ApiKeyManager, geocode_one

def example1():
    """
    [EN]calculate two locations' distance
    [CN]计算两个坐标之间的距离
    """
    cd1 = (38.953165, -77.396170) # EFA
    cd2 = (38.899697, -77.048557) # GWU
    print(dist(cd1, cd2)) # 可以加参数 unit = "mile" or "km" or "feet"

example1()

def example2():
    """
    [EN]cyclically generate an api_key, call self.nextkey() to get api_key
    [CN]api_key循环器。初始化之后每self.nextkey()即可循环输出一个api_key
    """
    api_keys = ["api_key1",
                "api_key2",
                "api_key3"]
    akm = ApiKeyManager(api_keys)
    for i in range(10):
        print(akm.nextkey())

example2()

def example3():
    """
    [CN]用geocode_one来geocoding地址的具体数据
    """
    from HSH.Misc.logger import Log
    log = Log()
    api_keys = ["your_own_api_key1",
                "your_own_api_key2",
                "your_own_api_key3"]
    akm = ApiKeyManager(api_keys)
    address = "hello world, I am a python programmer"
    try:
        data = geocode_one(address, akm.nextkey(), max_try = 2) # 尝试#max_try次还未成功则放弃
                                                                # 并raise异常。默认只尝试一次
                                                                # 用于节约api_key使用次数
        print(data)
    except Exception as e:
        log.write(e, e.__class__.__name__)
        
example3()