##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
from HSH.DataSci.psmatcher import psm
import pandas as pd, numpy as np

if __name__ == "__main__":
    def psm_UT():
        data = pd.read_csv(r"..\test_data\re78.csv", index_col=0) # read all data
        control, treatment = (data[data["treat"] == 0].values, # split to control and treatment
                              data[data["treat"] == 1].values)
        
        selected_control, selected_control_foreach = psm(control, treatment, 
                                                         use_col = [0, 1, 2, 3, 4, 5], 
                                                         stratified_col = [[1],[3],[0,2,4],[5]], k = 1)
        
        
        for tr, ct in zip(treatment, selected_control_foreach):
            print("==============")
            print(tr.tolist())
            print("------")
            print(ct.tolist())

    psm_UT()