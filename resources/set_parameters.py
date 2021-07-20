########################################################
# LIBRARIES
########################################################
import os
from path import Path
import pandas as pd
import numpy as np

# set directory to where this file is located
folder_loc = os.path.dirname(os.path.realpath(__file__))
os.chdir(folder_loc)

########################################################
# PARAMETERS
########################################################

def set_params(scrapers = 1, input_file = "inputs/locs_selected.csv", 
               name_col = "Name Only", address_col = "Address Only"):
    # set rows to scrape in the dataframe
    start_point = 0  # default is 0
    # default is 100000000 -- this sets it to the length of the df
    end_point = 100000000
    
    # 1 scraper min, 18 max -- depends on your computer's ability to run multiple chrome browsers
    num_scrapers = scrapers
    
    # # how many reviews to scrape
    # # remember, each review ~4, so 100 is really 25 reviews 
    # pt1_reviews_limit = 100000000
    
    # file with all the locations
    all_places = input_file
    
    name = name_col
    address = address_col
    
    # just make these absolute paths so computer doesnt give us any bs
    #browser_path = os.path.abspath(Path(browser_path))
    all_places_path = os.path.abspath(Path(all_places))

########################################################
# INITIALIZATION
########################################################

    # read in all the places to scrape
    apdf = pd.read_csv(all_places_path, encoding='utf-8-sig')  # latin1
    # set end point for scraper if end point is not set yet
    if end_point == 100000000:
        end_point = len(apdf)
    
    apdf = apdf[start_point:end_point]
    apdf = apdf.fillna('')
    # clean all columns of new lines
    apdf = apdf.replace(r'\n', ' ', regex=True)
    
    # keep only needed cols
    apdf = apdf[[name, address]]
    apdf = apdf.drop_duplicates()
    
    apdf['search_list'] = apdf[name] + ', ' + apdf[address]
    place_name_list = apdf[name].tolist()
    search_list = apdf['search_list'].tolist()
    
    place_name_list = np.array_split(place_name_list, num_scrapers)
    search_list = np.array_split(search_list, num_scrapers)
    
    # OUTPUT LOCATION #
    # make folder to save exported files into
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    os.chdir('outputs') # where the outputted restaurant csvs will go
    path = os.getcwd() 
