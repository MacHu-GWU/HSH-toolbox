##encoding=utf8

from __future__ import print_function
from HSH.Data import *

def test_import():
    """
    from .dtype import DtypeConverter, OrderedSet, SuperSet
    from .hashutil import md5_str, md5_obj, md5_file, hash_obj
    from .inv_index import inv_index
    from .iterable import flatten, flatten_all, nth, shuffled, grouper, grouper_dict, grouper_list
    from .iterable import running_windows, cycle_running_windows, cycle_slice
    from .js import load_js, dump_js, prt_js
    from .pk import load_pk, dump_pk
    from .timewrapper import TimeWrapper
    """    
    print(DtypeConverter, OrderedSet, SuperSet)
    print(md5_str, md5_obj, md5_file, hash_obj)
    print(inv_index)
    print(flatten, flatten_all, nth, shuffled, grouper, grouper_dict, grouper_list)
    print(running_windows, cycle_running_windows, cycle_slice)
    print(load_js, dump_js, prt_js)
    print(load_pk, dump_pk)
    print(TimeWrapper)
    
test_import()