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
    from HSH.Data.pk import load_pk, dump_pk
"""

from __future__ import print_function
import pickle
import sys
import os
import time

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    pk_protocol = 2
else:
    pk_protocol = 3

def load_pk(fname):
    """load object from pickle file"""
    print("\nLoading from %s..." % fname)
    st = time.clock()
    obj = pickle.load(open(fname, "rb"))
    print("\tComplete! Elapse %s sec." % (time.clock() - st) )
    return obj

def dump_pk(obj, fname, pickle_protocol = pk_protocol, replace = False):
    """dump object to pickle file
    pickle_protocol = 2 can write to python2 readable pickle file, but slower
    Replace existing file when replace = True"""
    print("\nDumping to %s..." % fname)
    
    st = time.clock()
    
    if os.path.exists(fname): # if exists, check replace option
        if replace: # replace existing file
            pickle.dump(obj, open(fname, "wb"), protocol = pickle_protocol)
        else: # stop, print error message
            print("\tCANNOT WRITE to %s, it's already exists" % fname)
    else: # if not exists, just write to it
        pickle.dump(obj, open(fname, "wb"), protocol = pickle_protocol)
    print("\tComplete! Elapse %s sec" % (time.clock() - st) )