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
This module is re-pack of some json utility functions
    1. load json object from file
    2. dump json object to file. Replace existing file when replace = True
    3. pretty print json object
    
compatibility: python2 and python3

prerequisites: None

import:
    from HSH.Data.js import load_js, dump_js, prt_js
"""

from __future__ import print_function
import json
import sys
import os
import time

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    read_mode, write_mode = "rb", "wb"
else:
    read_mode, write_mode = "r", "w"
    
def load_js(fname, enable_verbose = True):
    """load dict object from file"""
    if enable_verbose:
        print("\nLoading from %s..." % fname)
        st = time.clock()
        
    if os.path.exists(fname): # exists, then load
        js = json.load(open(fname, read_mode) )
        if enable_verbose:
            print("\tComplete! Elapse %s sec." % (time.clock() - st) )
        return js
    
    else:
        if enable_verbose:
            print("\t%s not exists! cannot load! Create an empty dict instead" % fname)
        return dict()

def dump_js(js, fname, fastmode = False, replace = False, enable_verbose = True):
    """dump dict object to file.
    [Args]
    ------
    fname: save as file name
    
    fastmode: boolean, default False
        if True, then dumping json without sorting keys and pretty indent. It is faster
    
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
            if fastmode: # no sort and indent, do the fastest dumping
                json.dump(js, open(fname, write_mode))
            else:
                json.dump(js, open(fname, write_mode), sort_keys=True, indent=4,separators=("," , ": ") )
        else: # stop, print error message
            raise Exception("\tCANNOT WRITE to %s, it's already exists" % fname)
                
    
    else: # if not exists, just write to it
        if fastmode: # no sort and indent, do the fastest dumping
            json.dump(js, open(fname, write_mode))
        else:
            json.dump(js, open(fname, write_mode), sort_keys=True, indent=4,separators=("," , ": ") )
            
    if enable_verbose:
        print("\tComplete! Elapse %s sec" % (time.clock() - st) )
    

def prt_js(js):
    """print dict object with pretty format"""
    print(json.dumps(js, sort_keys=True, indent=4, separators=("," , ": ")) )