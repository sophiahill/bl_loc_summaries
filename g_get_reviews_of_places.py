# -*- coding: utf-8 -*-
"""
Created on Jan 2020

@edited by: Theo G
"""

from tqdm import tqdm
import os
from os import chdir, getcwd
wd = getcwd()  # lets you navigate using chdir within jupyter/spyder
chdir(wd)
tqdm.pandas()
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from progressbar import ProgressBar
pbar = ProgressBar()

# set directory to where this file is located
folder_loc = os.path.dirname(os.path.realpath(__file__))
os.chdir(folder_loc)

from set_parameters import *
from resources.run_multi_locs_info import run_multi_locs

# make folder to save files into
if not os.path.exists('outputs'):
    os.makedirs('outputs')
os.chdir('outputs')


if __name__ == '__main__':
    run_multi_locs(pt1_start_point, pt1_end_point, pt1_num_scrapers,
                   pt1_all_places_path, browser_path, name_col, address_col)
