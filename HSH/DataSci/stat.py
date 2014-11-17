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
Import:
    from HSH.Data.stat import clear_outlier_onetime, clear_outlier_literally
"""
from __future__ import print_function
import numpy as np

def find_outlier(np_array, outlier_criterion = 2):
    """return outliers in np_array
    [Args]
    ------
    np_array: 1d numpy.ndarray samples
    
    outlier_criterion: sample with n of standard deviation bias 
        from mean value will be considered as outlier
    
    [Returns]
    ---------
    outliers in np_array
    """
    if type(np_array) != np.ndarray:
        np_array = np.array(np_array)
    m, std = np_array.mean(), np_array.std()
    return np_array[ np.where( abs(np_array - m) > outlier_criterion * std )]

def clear_outlier_onetime(np_array, outlier_criterion = 2):
    """remove outliers by criterion then returns.
    [Args]
    ------
    np_array: 1d numpy.ndarray samples
    
    outlier_criterion: sample with n of standard deviation bias 
        from mean value will be considered as outlier
    
    [Returns]
    ---------
    np_array with all outliers deleted
    """
    if type(np_array) != np.ndarray:
        np_array = np.array(np_array)
    m, std = np_array.mean(), np_array.std()
    return np_array[ np.where( abs(np_array - m) <= outlier_criterion * std )]

def clear_outlier_literally(np_array, outlier_criterion = 2):
    """recurrsively remove outliers, until there's no outliers at all. Then return.
    [Args]
    ------
    np_array: 1d numpy.ndarray samples
    
    outlier_criterion: sample with n of standard deviation bias 
        from mean value will be considered as outlier
    
    [Returns]
    ---------
    np_array with all outliers deleted
    """
    if type(np_array) != np.ndarray:
        np_array = np.array(np_array)
    while 1:
        n_before = np_array.size
        np_array = clear_outlier_onetime(np_array, outlier_criterion)
        if n_before == np_array.size:
            return np_array


    
if __name__ == "__main__":
    def unit_test1():
        data = np.array([3, 2.9, 3.1, 4.2, 2.7, 3.5, 6.8, 12.7])
        print(clear_outlier_onetime(data) )
        print(clear_outlier_literally(data) )
        print(find_outlier(data) )
        
#     unit_test1()
    
    def unit_test2():
        array = np.array([73.6377, 74.0481, 73.98, 73.9835, 73.9818, 73.9538, 74.1053, 75.6359, 75.8413, 75.8234, 75.8134, 75.7582, 75.7287, 75.6379, 75.6192, 75.5904, 75.5556, 75.5416, 75.5109, 75.5118, 75.4709, 75.4576, 75.4405, 75.509, 75.5417, 75.5488, 75.5133, 75.4863])

    unit_test2()
