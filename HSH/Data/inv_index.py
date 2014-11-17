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
index: a dict
"""

from __future__ import print_function
from six import iteritems

def inv_index(pos_index):
    """
    [Args]
    ------
    pos_index: normal index dictionary
        key: value = item_id: indices
    """
    invert_index = dict()
    for item_id, indices in iteritems(pos_index):
        for index in indices:
            if index not in invert_index:
                invert_index[index] = set({item_id})
            else:
                invert_index[index].add(item_id)
    return invert_index

if __name__ == "__main__":
    def test_inv_index():
        print("{:=^40}".format("test_inv_index"))
        pos_index = {"let it go": {"mp3", "pop", "dance"},
                     "can you feel the love tonight": {"acc", "pop", "movie"},
                     "Just dance": {"pop", "dance", "club"}}
        print(inv_index(pos_index))
    
    test_inv_index()