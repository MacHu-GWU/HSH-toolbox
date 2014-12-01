##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-26             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
========================================= Definition ==============================================
nodetree 数据结构抽象表示
|---root
    |---a1 = {attr1: value1, attr2: value2}
        |---b1 = {attr1: value1, attr2: value2}
            |---c1 = {attr1: value1, attr2: value2}
            |---c2
            |---c3
            |---c4
        |---b2
        |---b3
    |---a2
        
节点树(nodetree)定义：
    从根节点出发, 每个节点之下都有若干个子节点(children), 和有且只有一个父节点(father)（除了根节点）. 
    例如b1的子节点有c1, c2, c3, c4; 而b1的父节点是a1. 每一个子节点也可以看作是一个节点树. 
    
枝(branch)的定义：
    节点下所有子节点的集合被称作枝

key的定义：    
    每个节点都有一个相对于同一个枝上其他子节点唯一的key, 用来唯一标识这个节点. 例如: 在a1节点的枝下, 
    有b1, b2, b3三个子节点, 其中b1, b2, b3就是key. 
    
路径(path)的定义
    对于任意节点, 都可以从根节点出发, 通过一系列的key对其进行访问; 而这一系列的key所组成的列表, 被称作
    路径. 例如c1的路径可以从root出发, 通过a1,b1, c1被访问到. 所以c1的路径就是 [a1, b1, c1]. 由于内部
    实现采用了字典结构, 所以每次访问的时间复杂度是常数级. 
    
深度(depth)的定义
    对于任意节点, 路径的长度就是深度. 比如b1节点的深度是2, c1节点的深度是3.值得一提的是, 根节点本身的深度
    定义为0.

============================================ Usage ================================================
树结构是一种高效的数据结构, 具有以下特点

节点访问
--------
1. 只要知道节点的路径, 能以常量时间访问到任意节点
    节点的访问通过 node[key1][key2][key3]... 进行. 由字典数据结构实现. 
    
2. 每个节点有1个父节点, 若干个子节点, 节点本身带一定的数据信息, 以字典形式储存
    对节点的属性访问通过 node.lastname, node.firstname


节点的属性
----------
1. 节点自带几个特殊属性。
    node.key 节点key, node.depth 节点深度, node.path 节点路径
    
2. len(node) 返回该节点下的子节点的个数


节点的添加与删除
---------------
1. 提供 node.add_children(key, attr1 = value1, attr2 = value2, ...) 方法, 用来添加子节点

2. 提供 node.kill_children(path) 方法，用来删除子节点以及其下面所有的子节点


遍历方法
--------
1. 可以使用 for children_node in node: 来对子节点进行遍历
    例如 for node in a1: 返回 node = b1, b2, b3... （这里的a1, b1, ...均指节点本身，不是指key）
    
2. 提供 for k in node.keys():, for v in node.values():, for k, v in node.items(): 这些类似字典语法
    的迭代器。

3. 提供 for node_at_depth in node.iterlevel(depth) 方法，对处于某一层深度的所有子节点进行遍历


逻辑方法
--------
1. 提供 key in node 用于判断key是否是该节点下的任意子节点


读写方法
--------
1. 提供 node.to_dict() 方法将节点树转化成python字典

2. 提供 node.prettyprint() 方法将节点树打印成人类可读的文本

3. 提供 node.dump(file_name) 方法将节点数存成json文件

4. 提供 node.load(file_name) 方法把文件中的json字典解析成节点树
"""

from __future__ import print_function
try:
    from .js import load_js, dump_js, prt_js, js2str
except:
    from js import load_js, dump_js, prt_js, js2str

class Node(object):
    def __init__(self, data = {"!!": dict()}, key = "root", depth = 0, path = list() ):
        object.__setattr__(self, "data", data)
        object.__setattr__(self, "key", key)
        object.__setattr__(self, "depth", depth)
        object.__setattr__(self, "path", path)
        
    def __str__(self):
        return "key = %s, depth = %s, info = %s, path = %s" % (self.key,
                                                               self.depth, 
                                                               str(self.data["!!"]),
                                                               self.path)
    
    def __setattr__(self, attribute_name, attribute_value):
        """implement Node.attribute_name = attribute_value behavior
        """
        self.data["!!"][attribute_name] = attribute_value        

    def __getattr__(self, attribute_name):
        """implement Node.attribute_name behavior
        """
        return self.data["!!"][attribute_name]

    def __setitem__ (self, key, value):
        """implement Node[key] = value behavior
        """
        self.data[key] = value
        
    def __getitem__(self, key):
        """implement Node[key] behavior
        """
        return self.data[key]    
        
    def __iter__(self):
        """implement for node in Node: iterator
        """
        return (self[key] for key in self.data if key != "!!")

    def __len__(self):
        """find how many children it has
        """
        return len(self.data) - 1
    
    def __contains__(self, key):
        """exam if any of children's key equal to #key
        """
        return key in self.data
    
    def keys(self):
        """iterator yield childrens key
        """
        return (key for key in self.data if key != "!!")
    
    def values(self):
        """iterator yield childrens
        """
        return (self[key] for key in self.data if key != "!!")
    
    def items(self):
        """iterator yield children key and children it self
        """
        return ( (key, self[key]) for key in self.data if key != "!!")

    def iterlevel(self, level):
        """iterator yield node at specific depth
        if level = 0, yield it self
        else yield all node if nodes.depth == #level
        """
        if level == 0:
            yield self
        else:
            for node in self:
                if node.depth == level:
                    yield node
                else:
                    for node in node.iterlevel(level):
                        yield node
    
    def len_on_level(self, level):
        """相对level
        """
        counter = 0
        for node in self.iterlevel(level + self.depth):
            counter += 1
        return counter
    
    def stats_on_level(self, level):
        num_of_emptynode, total = 0, 0
        for node in self.iterlevel(level + self.depth):
            if len(node) == 0:
                num_of_emptynode += 1
            total += 1
        print("On level %s, number of empty node = %s, total node = %s" % (level, 
                                                                           num_of_emptynode, 
                                                                           total))
    
    def add_children(self, key, **kwarg):
        """Add a children with key and attributes. If children already EXISTS, OVERWRITE it.
        depth and path are automatically assigned.
        
        [Args]
        ------
        key: children's key
        
        **kwage: attributes assignment argument.
            e.g. name = "Tom", age = 32
        """
        self.data[key] = Node(data = {"!!": dict()},
                              key = key, 
                              depth = self.depth+1, 
                              path = list(self.path) )
        self.data[key].path.append(key)
        for name, value in kwarg.items():
            self.data[key].__setattr__(name, value)

    def ac(self, key, **kwarg):
        """abbreviation of self.add_children"""
        self.add_children(key, **kwarg)
  
    def _locate(self, reversed_path):
        """locate a node by reversed_path
        Private method used in get_father method. You should never call this method explicitly
        """
        if len(reversed_path)>=1:
            key = reversed_path.pop()
            return self[key]._locate(reversed_path)
        else:
            return self
    
    def get_father(self, node):
        """get a father of a node
        for example: 
            if node.path = ["1", "2", "3"], node.key = "3"
            then the father_node.path = ["1", "2"], father_node.key = "2"
        """
        path = list(node.path)
        path.pop()
        return self._locate(path[::-1])
    
    def gf(self, node):
        """abbreviation of self.get_father"""
        return self.get_father(node)
    
    def delete(self, node):
        del self.get_father(node).data[node.key]
    
    def deletelevel(self, level):
        for node in [node for node in self.iterlevel(level)]:
            self.delete(node)
        
    def to_dict(self):
        """represent it self as a python dictionary
        """
        d = {"!!": self.data["!!"]}
        for k, v in self.items():
            d[k] = v.to_dict()
        return d
    
    def prettyprint(self):
        """print human readable text represent itself
        """
        prt_js(self.to_dict())
    
    def dump(self, fname, fastmode = False, replace = False, enable_verbose = True):
        """dump itself to a json file
        fastmode: if True, writting is faster, but not human readable
        replace: if True, will overwrite the file with same #fname silently
        enable_verbose: if False, will not print time cost information
        """
        dump_js(self.to_dict(), fname, fastmode, replace, enable_verbose)
    
    @staticmethod
    def from_dict(dictionary, key = "root", depth = 0, path = list()):
        """reform a Node object from a dictionary
        """
        nn = Node({"!!": dictionary["!!"]}, key, depth, path)
        for k, v in dictionary.items():
            
            if k != "!!":
                temp_path = list(path)
                temp_path.append(k)
                nn.data[k] = Node.from_dict(v,
                                            key = k, 
                                            depth = depth +1,
                                            path = temp_path)
        return nn
                
    @staticmethod
    def load(fname):
        """load the node from a json file
        """
        return Node.from_dict(load_js(fname, enable_verbose = False))

if __name__ == "__main__":
    
    nn = Node() # 初始化一个node
    nn.name = "united states"
    nn.population = 300000000
    nn.add_children("VA", name = "virginia", population = 100000)
    nn.add_children("MD", name = "maryland", population = 200000)
    
    nn["VA"].add_children("arlington", name = "arlington county", population = 5000)
    nn["VA"].add_children("vienna", name = "vienna county", population = 1500)
    
    nn["VA"]["arlington"].add_children("riverhouse", name = "RiverHouse 1400", population = 437)
    nn["VA"]["arlington"].add_children("crystal plaza", name = "Crystal plaza South", population = 681)
    nn["VA"]["arlington"].add_children("loft", name = "loft hotel", population = 216)
    
    nn["MD"].add_children("bethesta", name = "montgomery country", population = 5800)
    nn["MD"].add_children("germentown", name = "fredrick country", population = 1400)
    
    def test1():
        print("{:=^100}".format("test for set item, get item"))
        global nn
        
        print(nn)
        print(nn["VA"])
        print(nn["MD"])
        print(nn["VA"]["arlington"])
        print(nn["VA"]["vienna"])
    
        print("{:=^100}".format("test for set item, get item"))
        print(nn.name, nn.population)
        print(nn["VA"].name, nn["VA"].population)
        print(nn["MD"].name, nn["MD"].population)
        print(nn["VA"]["arlington"].name, nn["VA"]["arlington"].population)
        print(nn["VA"]["vienna"].name, nn["VA"]["vienna"].population)
        
#     test1()
    
    def test2():
        """Node的for loop
        1. for i in Node(), 实际是对除了用来保存节点metadata的 "!!"以外的其他子节点的key进行循环
        2. for k, v in Node().items, 实际上是对 key, Node()[key]进行循环(除了"!!"), 和字典的行为一致
        """
        print("{:=^100}".format("test for loop behavior"))
        global nn
        
        print("\n{:=^60}".format("default for loop, iter children nodes"))
        for node in nn: ## VA, MD
            print(node)
          
        print("\n{:=^60}".format("iter keys, behaive like dict.iterkeys"))
        for key in nn.keys():
            print(key)
          
        print("\n{:=^60}".format("iter values, behaive like dict.itervalues"))
        for node in nn.values():
            print(node)
          
        print("\n{:=^60}".format("iter key, value pair, behaive like dict.iteritems"))
        for key, node in nn.items():
            print("key: {0}, node: {1}".format(key, node))
        
        print("\n{:=^60}".format("iter on specific depth level"))
        for node in nn.iterlevel(3):
            print(node)
            
#     test2()
    
    def test3():
        """_locate, get_father等节点路径相关的方法
        """
        print("{:=^100}".format("test locate node by reversed_path"))
        global nn
        
        print(nn._locate(["riverhouse", "arlington", "VA"]) )
        print(nn._locate(["arlington", "VA"]) )
    #     print(nn._locate(["arlington"]) ) # raise error 因为arlington无法和根节点建立联系
        
        print("{:=^100}".format("test get father of a node"))
        for n1 in nn:
            for n2 in n1:
                print(nn.get_father(n2))
                for n3 in n2:
                    print(nn.get_father(n3))
                    
#     test3()
    
    def test4():
        """Node I/O to file
        """
        print("{:=^40}".format("test for dump"))
        
        global nn
        prt_js(nn.to_dict())
        nn.dump("task.json", replace=True)
        
        print("{:=^40}".format("test for load"))
        nn = Node.load("task.json")
        print(nn)
        print(nn["VA"])
        print(nn["VA"]["arlington"])
        print(nn["VA"]["arlington"]["riverhouse"])
        prt_js(nn.to_dict() )
        ##check if the original json match the Node decode from the json.
        print(js2str(nn.to_dict()) == js2str(load_js("task.json", enable_verbose = False)))
        
#     test4()

    def test5():
        """测试len, 和 in 的行为
        """
        global nn
#         print(len(nn))
#         print(len(nn["VA"]))
#         print(len(nn["VA"]["arlington"]))
        
#         print(nn.len_on_level(0))
#         print(nn.len_on_level(1))
#         print(nn.len_on_level(2))
#         print(nn.len_on_level(3))
#         print(nn.len_on_level(4)) # there's no node depth = 4
        
        print(nn["VA"].len_on_level(2))
        
#         print("VA" in nn)
        
#     test5()

    def test6():
        """delete behavior, delete the whole level
        """
        global nn
        print("{:=^40}".format("before"))
        nn.prettyprint()
#         nn.delete(nn["VA"]["vienna"])
#         print("{:=^40}".format("after"))
#         nn.prettyprint()
        
        nn.deletelevel(2)
        print("{:=^40}".format("after"))
        nn.prettyprint()
        
    test6()