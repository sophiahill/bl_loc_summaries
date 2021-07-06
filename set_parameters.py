import os
from path import Path
# set directory to where this file is located
folder_loc = os.path.dirname(os.path.realpath(__file__))
os.chdir(folder_loc)

# Place  chromedriver in the resources folder
browser_path = r"C:/Users/tgoet/Documents/GIthub_personal_temp/chromedriver.exe"

# set rows to scrape in the dataframe
pt1_start_point = 0  # default is 0
# default is 100000000 -- this sets it to the length of the df
pt1_end_point = 100000000

# 1 scraper min, 18 max -- depends on your computer's ability to run multiple chrome browsers
pt1_num_scrapers = 12

# # how many reviews to scrape
# # remember, each review ~4, so 100 is really 25 reviews 
# pt1_reviews_limit = 100000000


pt1_all_places_path = 'input_files/locs_selected.csv'  # file with all the locations


name_col = 'Name Only'
address_col = 'Address Only'

##########################################################################
# just make these absolute paths so computer doesnt give us any bs
browser_path = os.path.abspath(Path(browser_path))
pt1_all_places_path = os.path.abspath(Path(pt1_all_places_path))


