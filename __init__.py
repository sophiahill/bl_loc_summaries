# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:18:38 2021

@author: sophi
"""

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from time import sleep
import random
from tqdm import tqdm
tqdm.pandas()
import os
wd = os.getcwd()  # lets you navigate using chdir within jupyter/spyder
os.chdir(wd)
from progressbar import ProgressBar
pbar = ProgressBar()
from multiprocessing import Process

from set_parameters import *
from resources.xpaths import *
from resources.functions import hasXpath, sleep_for, sub_filter, get_result, get_results, try_find_else_empty

# selenium libs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# HELPER FUNCTIONS #

# intializes chrome bot
def initialize_bot():
    chrome_options = Options()
    chrome_options.add_argument('--disable-background-timer-throttling')
    chrome_options.add_argument('--disable-backgrounding-occluded-windows')
    chrome_options.add_argument('--disable-background-timer-throttling')
    chrome_options.add_argument('--disable-renderer-backgrounding')
    chrome_options.add_argument('detach:True')
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--headless') # comment out if you want pop up
    chrome_options.add_argument("--window-size=1080,760")
    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# runs scrapers in parallel by calling scraper class
def a2(search_list, place_name_list, path):
    automate1 = ScrapeGooglePlacesInfoReviewsWithHotels(
        search_list,
        place_name_list,
        path)
    automate1.loc_scrape()

# scraper class - where we do the actual scraping
class ScrapeGooglePlacesInfoReviewsWithHotels:
    def __init__(self, search_list, place_name_list, path):
        self.bot = initialize_bot()
        self.search_list = search_list
        self.place_name_list = place_name_list
        self.cur_path = path

    def loc_scrape(self):
        bot = self.bot
        bot.fullscreen_window()

        # go to url
        url = 'https://www.google.com/maps/?hl=en'
        bot.get(url)  # go to the url
        sleep_for(4, 7)

        for loc in pbar(self.search_list):
            try:
                print()
                
                # if there is a consent reminder
                try:
                    consent_button = bot.find_element_by_xpath(consent)
                    consent_button.click()
                    # print('clicked remind me later button')
                    sleep_for(11, 12)
                except:
                    pass

                loc_url = 'https://www.google.com/maps/search/' + \
                    re.sub('[^a-zA-Z0-9 \n\.]', '',
                           loc).replace('  ', ' ').replace(' ', '+')
                bot.get(loc_url)
                sleep_for(3, 6)

                # check for partial matches
                if hasXpath(bot, place_cont):
                    first_selection = bot.find_element_by_xpath(place_link)
                    first_selection.click()
                    sleep_for(3, 6)
                else:
                    pass

                ###############################################################
                # get location summary info
                ###############################################################

                sleep_for(4, 6)
                
                try:
                    url = str(bot.current_url)
                    urlstring = url.split('!3d')[1]
                    lat = urlstring.split('!4d')[0]
                    lon = urlstring.split('!4d')[1].split('?')[0]
                except:
                    print('Unable to find lat/long')
                    lat = ''
                    lon = ''
                    url = ''

                print("Url: ", url)
                print("Lat, Lon: ", lat, lon)

                # get name
                if hasXpath(bot, name):
                    name_scraped = str(bot.find_element_by_xpath(name).text)
                else:
                    name_scraped = ''
                print("Name: ", name_scraped)

                # address
                if hasXpath(bot, add):
                    address_scraped = str(bot.find_element_by_xpath(add
                            ).get_attribute('aria-label'))
                    if "Address: " in address_scraped:
                        address_scraped = address_scraped.replace(
                            "Address: ", "")
                else:
                    address_scraped = ''
                print("Address: ", address_scraped)

                # pulse code
                if hasXpath(bot, pulse):
                    pulse_address = str(bot.find_element_by_xpath(
                        pulse).get_attribute("aria-label"))
                    pulse_address = pulse_address.replace(
                        "Plus code: ", "")
                else:
                    pulse_address = ''
                print("Pulse address: ", pulse_address)

                # number of reviews
                if hasXpath(bot, num_rev):
                    num_reviews = str(bot.find_element_by_xpath(
                        num_rev).text)
                    try:
                        num_reviews = num_reviews.split()[0]
                    except:
                        num_reviews = ''
                else:
                    num_reviews = ''
                print("Num reviews: ", num_reviews)

                # average review
                if hasXpath(bot, avg_rev):
                    avg_review = str(bot.find_element_by_xpath(avg_rev).text)
                else:
                    avg_review = ''
                print("Avg review: ", avg_review)

                # temporarily closed / permanently closed
                if hasXpath(bot, temp_closed):
                    temp_perm_closed = "Temporarily closed"
                elif hasXpath(bot, perm_closed):
                    temp_perm_closed = "Permanently closed"
                else:
                    temp_perm_closed = ''
                print("Temp_perm_closed: ", temp_perm_closed)

                # loc type
                try:
                    loc_type = str(try_find_else_empty(
                        bot, loc_type_path, 'single', 'text'))
                except:
                    loc_type = ""
                print("Loc type: ", loc_type)

                # price
                if hasXpath(bot, find_price):
                    price = str(bot.find_element_by_xpath(
                        find_price).get_attribute("aria-label"))
                    price = price.replace("Price: ", "")
                else:
                    price = ''
                print("Price: ", price)
                
                # website
                try:
                    website = str(bot.find_element_by_xpath(
                        site).get_attribute('aria-label').replace('Website: ', '').strip())
                except:
                    website = ''
                print("Website: ", website)

                # phone number
                try:
                    phone = str(bot.find_element_by_xpath(
                        copy_phone).get_attribute('aria-label').replace('Phone: ', '').strip())
                except:
                    phone = ''
                print("Phone: ", phone)

                # image
                try:
                    try:
                        img_url = str(bot.find_element_by_xpath(
                        imgs).get_attribute('src'))
                    except:
                        img_url = str(bot.find_elements_by_xpath(
                            imgs)[0].get_attribute('src'))
                except:
                    img_url = ""
                print("Img url: ", img_url)

                # hours
                try:
                    if hasXpath(bot, hide_open_hours):
                        hours = str(bot.find_element_by_xpath(
                            hide_open_hours).get_attribute('aria-label'))
                        if " Hide open hours for the week" in hours:
                            hours = hours.replace(" Hide open hours for the week", "")
                    if len(hours) <= 1:
                        hours = ""
                except:
                    hours = ""
                print("Hours: ", hours)
                    
                # dining and takeout / service options
                # offer_list = []
                so_dict = dict()
                try:
                    if hasXpath(bot, service_options_button):
                        so = bot.find_element_by_xpath(service_options_button)
                        so.click()
                        sleep_for(2, 4)
                        print("service option box clicked")
                        if hasXpath(bot, so_boxes_path):
                            so_boxes = bot.find_elements_by_xpath(so_boxes_path)
                            # end dict is category: options
                            # ex. key value -
                            # Highlights: ["Great coffee", "Great tea selection"]
                            print("got boxes")
                            for i in range(len(so_boxes)):
                                offer_list = []
                                # extract the name of each box to save as a column name
                                title = str(so_boxes[i].get_attribute("aria-label"))
                                offerings_path = so_boxes_path + "[" + str(i + 1) + "]//div[2]//div"
                                if hasXpath(bot, offerings_path):
                                    offerings = bot.find_elements_by_xpath(offerings_path)
                                    # for each mini box in service box, get things and save as list
                                    for o in offerings:
                                        each_offer = str(o.get_attribute("aria-label"))
                                        offer_list.append(each_offer)
                                    so_dict[title] = offer_list
                        # click back
                        if hasXpath(bot, so_back_button):
                            so_back_button = bot.find_element_by_xpath(so_back)
                            so_back_button.click()
                            sleep_for(1, 2)
                except:
                    if hasXpath(bot, so_back):
                        so_back_button = bot.find_element_by_xpath(so_back)
                        so_back_button.click()
                        sleep_for(1, 2)

                print("Service options: ", so_dict)
                
                sleep_for(2, 3)

                ###############################################################
                # exporting dataframe to csv
                ###############################################################
                
                # create export dataframe from dict
                d = {"loc searched": [str(loc)],
                     "loc_url": [url],
                     "lat": [lat],
                     "lon": [lon],
                     "name_only": [name_scraped],
                     "address_only": [address_scraped],
                     "pulse_address": [pulse_address],
                     "loc_type": [loc_type],
                     "num_reviews": [num_reviews],
                     "avg_review": [avg_review],
                     "temp_perm_closed": [temp_perm_closed],
                     "price_level": [price],
                     "website": [website],
                     "hours": [hours],
                     "phone_number": [phone],
                     "img_url": [img_url]}
                    
                export_data = pd.DataFrame.from_dict(d)

                # adding service options to export_data
                if len(list(so_dict.keys())) > 0:
                    so_df = pd.DataFrame([so_dict])
                    # combine side by side
                    export_data = pd.concat([export_data, so_df], axis = 1)

                # EXPORTING #
                # cleaning export path if necessary
                cur_path = self.cur_path.replace('\\', '/')

                # get rid of special characters and spaces in pulse address
                address_clean = str(
                    re.sub('[^a-zA-Z0-9 \n\.]', '_', address_scraped)).replace(" ", '')
                # same for name
                # name_scraped_clean = str(re.sub('[^a-zA-Z0-9 \n\.]', '_', name_scraped)).replace(" ", '')
                loc_scraped_clean = str(
                    re.sub('[^a-zA-Z0-9 \n\.]', '_', loc)).replace(" ", '')
                out_name = loc_scraped_clean + '_' + address_clean + '.csv'

                # export master df
                # export_data.to_csv(out_name, header=None, index=None, sep='||\t', mode='a')
                export_data.to_csv(cur_path + "/" + out_name,
                                   encoding='utf-8-sig',
                                   index=False)
                print('txt:    ' + str(out_name) + '  exported.. next item')
                
                sleep_for(2, 3)
            except:
                continue

        bot.quit()
        
def run_scraper():
    # run scrapers in parallel if num_scrapers > 1 (using multiprocessing)
    scrapers = {}
    for i in range(num_scrapers):
        name = "p" + str(i)
        scrapers[name] = Process(target=a2,
                                 args=(search_list[i],
                                       place_name_list[i],
                                       path))
        scrapers[name].start()

    for i in range(1, num_scrapers):
        scrapers[name].join()