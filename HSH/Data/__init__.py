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

from .dtype import DtypeConverter, OrderedSet, SuperSet
from .excel2db import excel2sqlite
from .hashutil import md5_str, md5_obj, md5_file, hash_obj
from .inv_index import inv_index
from .iterable import flatten, flatten_all, nth, shuffled, grouper, grouper_dict, grouper_list
from .iterable import running_windows, cycle_running_windows, cycle_slice
from .js import load_js, dump_js, prt_js
from .pk import load_pk, dump_pk, obj2str, str2obj
from .timewrapper import TimeWrapper
