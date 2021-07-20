import pandas as pd
from functools import reduce
from time import sleep
import random
from tqdm import tqdm
tqdm.pandas()
import os
wd = os.getcwd()  # lets you navigate using chdir within jupyter/spyder
os.chdir(wd)
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from progressbar import ProgressBar
pbar = ProgressBar()

# selenium libs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# HELPER FUNCTIONS #

def hasXpath(bot, xpath):
    try:
        bot.find_element_by_xpath(xpath)
        return True
    except:
        try:
            bot.find_element_by_css_selector(xpath)
            return True
        except:
            return False


def sleep_for(opt1, opt2):
    time_for = random.uniform(opt1, opt2)
    time_for_int = int(round(time_for))
    sleep(abs(time_for_int - time_for))
    for i in range(time_for_int, 0, -1):
        sleep(1)

def sub_filter(string, substr):
    return [str for str in string if
            any(sub in str for sub in substr)]


def get_result(object_in, href_text_other):
    if object_in == '':
        return ''
    elif href_text_other == "text":
        return object_in.text
    elif href_text_other == "href":
        return object_in.get_attribute('href')
    elif href_text_other == "aria-label":
        return object_in.get_attribute('aria-label')
    else:
        return ''


def get_results(objects_in, href_text_other):
    if objects_in == '':
        return ''
    elif href_text_other == "text":
        return [x.text for x in objects_in]
    elif href_text_other == "href":
        return [x.get_attribute('href') for x in objects_in]
    elif href_text_other == "aria-label":
        return [x.get_attribute('aria-label') for x in objects_in]
    else:
        return ''


def try_find_else_empty(bot, path_in, single_multi, href_text_other):
    if single_multi == "single":
        try:  # get name
            output = bot.find_element_by_css_selector(path_in)
        except:
            try:
                output = bot.find_element_by_xpath(path_in)
            except:
                output = ''
        returned = get_result(output, href_text_other)

        return returned
    elif single_multi == "multi":
        try:  # get name
            output = bot.find_elements_by_css_selector(path_in)
        except:
            try:
                output = bot.find_elements_by_xpath(path_in)
            except:
                output = ''
        returned = get_results(output, href_text_other)

        return returned
    
# returns merged dataframe
def merge_outputs():
    # set directory to where this file is located
    folder_loc = os.path.dirname(os.path.realpath(__file__))
    os.chdir(folder_loc + "/outputs") # in outputs folder
    
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
    
    return(final_df)