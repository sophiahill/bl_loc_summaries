# -*- coding: utf-8 -*-
"""
Created on Dec 2019

@edited by: Theo G
"""

from tqdm import tqdm
from multiprocessing import Process
import pandas as pd
from pathlib import Path
import numpy as np
import sys
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
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
# from scrape_locs_and_reviews import ScrapeGooglePlacesInfoReviewsWithHotels
from scrape_locs_and_reviews import ScrapeGooglePlacesInfoReviewsWithHotels


def a2(loc_type_list_in, place_name_list, browser):
    automate1 = ScrapeGooglePlacesInfoReviewsWithHotels(
        loc_type_list_in, place_name_list, browser)
    automate1.loc_scrape()


def run_multi_locs(pt1_start_point, pt1_end_point,
                   pt1_num_scrapers,
                   apdf_path, browser_path, name_col, address_col):

    # read in all the places to scrape
    apdf = pd.read_csv(apdf_path, encoding='utf-8')  # latin1
    # set end point for scraper if end point is not set yet
    # if 'pt1_end_point' not in globals():
    #   pt1_end_point = len(apdf)
    if pt1_end_point == 100000000:
        pt1_end_point = len(apdf)

    apdf = apdf[pt1_start_point:pt1_end_point]
    print(apdf)
    apdf = apdf.fillna('')
    # clean all columns of new lines
    apdf = apdf.replace(r'\n', ' ', regex=True)

    print(str(len(apdf)))
    # keep only needed cols
    apdf = apdf[[name_col, address_col]]
    apdf = apdf.drop_duplicates()

    apdf['search_list'] = apdf[name_col] + ', ' + apdf[address_col]
    place_name_list = apdf[name_col].tolist()
    search_list = apdf['search_list'].tolist()
    print(str(len(search_list)))

    place_name_list = np.array_split(place_name_list, pt1_num_scrapers)
    search_list = np.array_split(search_list, pt1_num_scrapers)

    if pt1_num_scrapers == 1:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p1.start()
        p1.join()
    elif pt1_num_scrapers == 2:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    elif pt1_num_scrapers == 3:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
    elif pt1_num_scrapers == 4:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
    elif pt1_num_scrapers == 5:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
    elif pt1_num_scrapers == 6:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
    elif pt1_num_scrapers == 7:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
    elif pt1_num_scrapers == 8:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
    elif pt1_num_scrapers == 9:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
    elif pt1_num_scrapers == 10:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
    elif pt1_num_scrapers == 11:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
    elif pt1_num_scrapers == 12:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
    elif pt1_num_scrapers == 13:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p13 = Process(target=a2, args=(search_list[12], place_name_list[
            12], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p13.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
        p13.join()
    elif pt1_num_scrapers == 14:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p13 = Process(target=a2, args=(search_list[12], place_name_list[
            12], browser_path))
        p14 = Process(target=a2, args=(search_list[13], place_name_list[
            13], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p13.start()
        p14.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
        p13.join()
        p14.join()
    elif pt1_num_scrapers == 15:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p13 = Process(target=a2, args=(search_list[12], place_name_list[
            12], browser_path))
        p14 = Process(target=a2, args=(search_list[13], place_name_list[
            13], browser_path))
        p15 = Process(target=a2, args=(search_list[14], place_name_list[
            14], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p13.start()
        p14.start()
        p15.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
        p13.join()
        p14.join()
        p15.join()
    elif pt1_num_scrapers == 16:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p13 = Process(target=a2, args=(search_list[12], place_name_list[
            12], browser_path))
        p14 = Process(target=a2, args=(search_list[13], place_name_list[
            13], browser_path))
        p15 = Process(target=a2, args=(search_list[14], place_name_list[
            14], browser_path))
        p16 = Process(target=a2, args=(search_list[15], place_name_list[
            15], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p13.start()
        p14.start()
        p15.start()
        p16.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
        p13.join()
        p14.join()
        p15.join()
        p16.join()
    elif pt1_num_scrapers == 17:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p13 = Process(target=a2, args=(search_list[12], place_name_list[
            12], browser_path))
        p14 = Process(target=a2, args=(search_list[13], place_name_list[
            13], browser_path))
        p15 = Process(target=a2, args=(search_list[14], place_name_list[
            14], browser_path))
        p16 = Process(target=a2, args=(search_list[15], place_name_list[
            15], browser_path))
        p17 = Process(target=a2, args=(search_list[16], place_name_list[
            16], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p13.start()
        p14.start()
        p15.start()
        p16.start()
        p17.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
        p13.join()
        p14.join()
        p15.join()
        p16.join()
        p17.join()
    elif pt1_num_scrapers == 18:
        p1 = Process(target=a2, args=(search_list[0], place_name_list[
                     0], browser_path))
        p2 = Process(target=a2, args=(search_list[1], place_name_list[
                     1], browser_path))
        p3 = Process(target=a2, args=(search_list[2], place_name_list[
                     2], browser_path))
        p4 = Process(target=a2, args=(search_list[3], place_name_list[
                     3], browser_path))
        p5 = Process(target=a2, args=(search_list[4], place_name_list[
                     4], browser_path))
        p6 = Process(target=a2, args=(search_list[5], place_name_list[
                     5], browser_path))
        p7 = Process(target=a2, args=(search_list[6], place_name_list[
                     6], browser_path))
        p8 = Process(target=a2, args=(search_list[7], place_name_list[
                     7], browser_path))
        p9 = Process(target=a2, args=(search_list[8], place_name_list[
                     8], browser_path))
        p10 = Process(target=a2, args=(search_list[9], place_name_list[
            9], browser_path))
        p11 = Process(target=a2, args=(search_list[10], place_name_list[
            10], browser_path))
        p12 = Process(target=a2, args=(search_list[11], place_name_list[
            11], browser_path))
        p13 = Process(target=a2, args=(search_list[12], place_name_list[
            12], browser_path))
        p14 = Process(target=a2, args=(search_list[13], place_name_list[
            13], browser_path))
        p15 = Process(target=a2, args=(search_list[14], place_name_list[
            14], browser_path))
        p16 = Process(target=a2, args=(search_list[15], place_name_list[
            15], browser_path))
        p17 = Process(target=a2, args=(search_list[16], place_name_list[
            16], browser_path))
        p18 = Process(target=a2, args=(search_list[17], place_name_list[
            17], browser_path))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p11.start()
        p12.start()
        p13.start()
        p14.start()
        p15.start()
        p16.start()
        p17.start()
        p18.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        p11.join()
        p12.join()
        p13.join()
        p14.join()
        p15.join()
        p16.join()
        p17.join()
        p18.join()
