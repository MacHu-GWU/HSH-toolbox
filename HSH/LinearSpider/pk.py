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
This module is re-pack of some pickle utility functions
    1. load object from pickle file
    2. dump object to pickle file

compatible: python2 and python3

import:
    from HSH.Data.pk import load_pk, dump_pk, obj2str, str2obj
"""

from __future__ import print_function
import pickle
import base64
import sys
import os, shutil
import time

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    pk_protocol = 2
else:
    pk_protocol = 3

def load_pk(fname, enable_verbose = True):
    """load object from pickle file"""
    if enable_verbose:
        print("\nLoading from %s..." % fname)
        st = time.clock()
    obj = pickle.load(open(fname, "rb"))
    if enable_verbose:
        print("\tComplete! Elapse %s sec." % (time.clock() - st) )
    return obj

def dump_pk(obj, fname, pickle_protocol = pk_protocol, replace = False, enable_verbose = True):
    """dump object to pickle file
    [Args]
    ------
    fname: save as file name
    
    pickle_protocol: pickle protocol version. 
        For PY2, default is 2, for PY3, default is 3. But if you want create 2&3 compatible pickle,
        use 2, but slower.
        
    replace: boolean, default False
        if True, when you dumping json to a existing file, it silently overwrite it.
        Default False setting is to prevent overwrite file by mistake
        
    enable_verbose: boolean, default True. Triggle for message
    """
    if enable_verbose:
        print("\nDumping to %s..." % fname)
        st = time.clock()
    
    if os.path.exists(fname): # if exists, check replace option
        if replace: # replace existing file
            pickle.dump(obj, open(fname, "wb"), protocol = pickle_protocol)
        else: # stop, print error message
            raise Exception("\tCANNOT WRITE to %s, it's already exists" % fname)
    else: # if not exists, just write to it
        pickle.dump(obj, open(fname, "wb"), protocol = pickle_protocol)
        
    if enable_verbose:
        print("\tComplete! Elapse %s sec" % (time.clock() - st) )

def safe_dump_pk(obj, fname, pickle_protocol = pk_protocol, enable_verbose = True):
    """
    [EN]Function dump_pk has a fatal flaw. When replace = True, if the program is interrupted by 
    any reason. It only leave a incomplete file. (Because fully writing take time). And it silently
    overwrite the file with the same file name.
    
    1. dump pickle to a temp file.
    2. rename it to #fname, and overwrite it.
    
    [CN]dump_pk函数在当replace=True时，会覆盖掉同名的文件。但是将编码后的字符串写入pickle是需要时间的，
    如果在这期间发生异常使程序被终止，那么会导致原来的文件已经被覆盖，而新文件还未完全被写入。这样会导致
    数据的丢失。
    safe dump pk函数则是建立一个 前缀 + 文件名的临时文件，将pickle写入该文件中，当写入完全完成之后，将该文件
    重命名覆盖原文件。这样即使中途程序被中断，也仅仅是留下了一个未完成的临时文件而已，不会影响原文件。
    
    """
    temp_fname = "safe_dump_pk_temp.tmp"
    dump_pk(obj, temp_fname, pickle_protocol = pk_protocol, replace = True, enable_verbose = enable_verbose)
    shutil.move(temp_fname, fname)


def obj2str(obj, pickle_protocol = pk_protocol):
    """convert arbitrary object to database friendly string, using base64encode algorithm"""
    return base64.b64encode(pickle.dumps(obj, protocol = pickle_protocol))

def str2obj(textstr):
    """recovery object from base64 encoded string"""
    return pickle.loads(base64.b64decode(textstr))
    