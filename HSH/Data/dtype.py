##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-31             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
[EN] A set of tools for data structure and data type
[CN] 一些与基本数据结构，数据类型有关的工具箱
DtypeConverter 数据类型转换器
OrderedSet 有序集合
SuperSet 能同时intersect, union多个集合

import:
    from HSH.Data.dtype import DtypeConverter, OrderedSet, SuperSet
"""

from __future__ import print_function
import collections
import numpy as np

class UnsupportDtype(Exception):
    """Exception for DtypeConverter"""
    def __str__(self):
        return "supported data type: %s" % ["list", "1darray", "2darray", "set"]
    
class DtypeConverter(object):
    """
    [EN] container level data type converter
    [CN] 以数据容器为对象的数据类型转换器
    将数据容器中的元素的格式按照converter所定义的转换
    usage:
        dc = DtypeConverter() # 初始化实例
        dc.register(converter) # converter是数据类型转换的函数
        converted = dc.convert(iterable, "list") # iterable数据容器的数据类型是list
    """
    def __init__(self):
        self.supported = ["list", "1darray", "2darray", "set"]
        
    def register(self, converter):
        self.converter = converter 
        
    def convert(self, iterable, dtype = None):
        if dtype not in self.supported:
            raise UnsupportDtype
        
        if dtype == "list":
            return map(self.converter, iterable)
        elif dtype == "1darray":
            return np.array(map(self.converter, iterable))
        elif dtype == "2darray":
            return np.array( [map(self.converter, 
                                  row) for row in iterable] )
        elif dtype == "set":
            return set(map(self.converter, iterable))

class OrderedSet(collections.MutableSet):
    """Set that remembers original insertion order."""
    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

class SuperSet(object):
    """SuperSet can operate intersect and union on more than 2 set at one time"""
    @staticmethod
    def intersect_all(list_of_set):
        """intersect a list of set
        list_of_set can be a list or a generator object
        """
        res, flag = set(), 1
        for jihe in list_of_set:
            if flag:
                res.update(jihe)
                flag = 0
            else:
                res.intersection_update(jihe)
        return res
    
    @staticmethod
    def union_all(list_of_set):
        """union a list of set
        list_of_set can be a list or a generator object
        """
        res = set()
        for jihe in list_of_set:
            res.update(jihe)
        return res
    
if __name__ == "__main__":
    def test_DtypeConverter():
        def to_str(i):
            return str(i)
        
        print("{:=^40}".format("test_DtypeConverter"))
        a = [1,2]    
        b = np.array([1,2,3])
        c = np.array([[1,2], [3,4]])
        d = {1,2,3,4}
        
        dc = DtypeConverter()
        dc.register(to_str)
        
        converted = dc.convert(a, "list")
        print(converted, type(converted))
    
        converted = dc.convert(b, "1darray")
        print(converted, type(converted))
    
        converted = dc.convert(c, "2darray")
        print(converted, type(converted))

        converted = dc.convert(d, "set")
        print(converted, type(converted))
    
    test_DtypeConverter()
    
    def test_OrderedSet():
        def orderedSet_UT1():
            print("{:=^30}".format("orderedSet_UT1"))
            s = OrderedSet(list())
            s.add("c")
            s.add("g")
            s.add("a")
            s.discard("g")
            print(s)
            print(list(s))
            
        def orderedSet_UT2():
            print("{:=^30}".format("orderedSet_UT2"))
            s = OrderedSet('abracadaba') # {"a", "b", "r", "c", "d"}
            t = OrderedSet('simsalabim') # {"s", "i", "m", "a", "l", "b"}
            print(s | t) # s union t
            print(s & t) # s intersect t
            print(s - t) # s different t
        
        print("{:=^40}".format("test_OrderedSet"))
        orderedSet_UT1()
        orderedSet_UT2()
        
    test_OrderedSet()
    
    def test_SuperSet():
        def gen(list_of_set):
            for i in list_of_set:
                yield i
        
        print(SuperSet.intersect_all(gen([{1,2,3}, 
                                          {2,3,4}, 
                                          {3,5,6}])))
        print(SuperSet.intersect_all([{1,2,3}, 
                                      {2,3,4}, 
                                      {3,5,6}]))
        print(SuperSet.union_all(gen([{1,2,3}, 
                                      {2,3,4}, 
                                      {3,5,6}])))
        print(SuperSet.union_all([{1,2,3}, 
                                  {2,3,4}, 
                                  {3,5,6}]))