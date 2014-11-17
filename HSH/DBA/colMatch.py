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

def hist(array):
    """
    [CN]对数组进行频率统计
    [EN]histgram the frequency
    """
    res = dict()
    for i in array:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res

def text_dist(text1, text2):
    """
    [CN]计算两个文本之间的'文本距离'。即a-z,0-9的字母频数统计的欧式距离
    [EN]Calculate text Euclidean dist.
    """
    hist1, hist2 = hist(text1.lower()), hist(text2.lower())
    difference = list()
    for char in "abcdefghijklmnopqrstuvwxyz0123456789":
        difference.append( (hist1.get(char, 0) - hist2.get(char, 0)) ** 2 )
    return sum(difference)

def match_one(pattern, array, tolerance = 4, verbal = True):
    """
    [CN]从array中找到最匹配pattern的那个match
    只有match与pattern的文本距离小于tolerance才会被判定为成功匹配
    [EN]find the matching text of pattern from an array.
    Tolerance = only text_dist < tolerance
    """
    min_dist = 9999
    for text in array:
        if text_dist(pattern, text) < min_dist: # if text_dist smaller than previous one, update min_dist
            min_dist, match = text_dist(pattern, text), text
    if verbal: # VERBAL
        print("pattern = '%s' MATCH array = '%s';, distance = '%s'" % (pattern, match, min_dist) )
    if min_dist > tolerance:
        if verbal: # VERBAL
            print("'%s' found nothing to match." % pattern)
        return None
    else:
        return match

def find_all_match(primary, array, tolerance = 4, verbal = True):
    """
    [CN]对primary中的每个元素，在array中找所匹配的，如果不匹配则匹配None
    """
    res = dict()
    for key in primary:
        match = match_one(key, array, tolerance, verbal = False)
        res[key] = match
    if verbal: # if verbal = True, print comparison
        for key, match in res.items():
            if match:
                print("<%s> - <%s>" % (key, match) )
            else:
                print("\tMATCH NOT FOUND: <%s> - <%s>" % (key, match) )
    return res

def unit_test1():
    a = ["employee name", "enroll date"]
    b = ["employee_name", "enroll_date"]
    for i in a:
        match = match_one(i, b, verbal = False)
        print("<%s> - <%s>" % (i, match) )

def unit_test2():
    a = ["employee name", "enroll date"]
    b = ["employee_name", "employee_gender"]
    matchs = find_all_match(a, b)
    
if __name__ == "__main__":
    unit_test1()
    unit_test2()
    

