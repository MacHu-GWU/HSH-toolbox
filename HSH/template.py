##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-18             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
The 
Usage:
    create any python file
"""

from __future__ import print_function
from datetime import datetime

template1 = \
'''##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =%s             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""Description of this scripts
"""

from __future__ import print_function






if __name__ == "__main__":
    
    



    pass
''' % datetime.strftime(datetime.now(), "%Y-%m-%d")

templates = {1 : template1}

def ct(template_id = 1):
    """create a python scripts using this template
    """
    print(templates[template_id])