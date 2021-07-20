# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:27:28 2021

@author: sophi
"""

############################################################
# MERGING ALL CSVS IN OUTPUTS FOLDER 
############################################################

# import libs
import os
import pandas as pd
import numpy as np
from functools import reduce

# set directory to where this file is located
folder_loc = os.path.dirname(os.path.realpath(__file__))
os.chdir(folder_loc + "/outputs") # in outputs folder

# want to keep all and make blank elems where no elem for that df col

# get files, turn into list of dataframes
files = os.listdir()
dfs = list(map(pd.read_csv, files))
# convert all columns to type string -> avoid ValueError
dfs = [df.astype(str) for df in dfs]

# use reduce to apply merge to all dataframes
large = reduce(lambda left, right: pd.merge(left, right, how = "outer"), dfs)
# replace nan with empty string
large_df = large.replace("nan", "", regex = True)
# drop any duplicates
final_df = large_df.drop_duplicates()

# output large merged csv to outputs folder
large_df.to_csv("MERGED.csv", index = False, encoding = "utf-8-sig")

print("Saved 'MERGED.csv' to outputs folder")
