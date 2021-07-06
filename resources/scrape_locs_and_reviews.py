# -*- coding: utf-8 -*-
"""
Created on Oct 2018

@edited by: Theo G
"""

##############################################################################
# imports
##############################################################################
from selenium import webdriver
from time import sleep
import pandas as pd
import re
import random
from tqdm import tqdm
tqdm.pandas()
from os import chdir, getcwd
wd = getcwd()  # lets you navigate using chdir within jupyter/spyder
chdir(wd)
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from progressbar import ProgressBar
pbar = ProgressBar()
import time

from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--disable-background-timer-throttling')
chrome_options.add_argument('--disable-backgrounding-occluded-windows')
chrome_options.add_argument('--disable-background-timer-throttling')
chrome_options.add_argument('--disable-renderer-backgrounding')
chrome_options.add_argument('detach:True')
chrome_options.add_argument('--headless')

##############################################################################
# functions
##############################################################################


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
        # sys.stdout.write(str(i) + ' ')
        # sys.stdout.flush()
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


class ScrapeGooglePlacesInfoReviewsWithHotels:

    def __init__(self, search_list, place_name_list, bot_path):
        self.bot = webdriver.Chrome(
            executable_path=bot_path, chrome_options=chrome_options)
        self.search_list = search_list
        self.place_name_list = place_name_list

    def loc_scrape(self):
        bot = self.bot
        bot.fullscreen_window()

        # go to url
        url = 'https://www.google.com/maps/?hl=en'
        bot.get(url)  # go to the url
        sleep_for(4, 7)

        for loc in pbar(self.search_list):
            try:

                # if there is a consent reminder
                try:
                    consent_button = bot.find_element_by_xpath(
                        '//button[@class="widget-consent-button-later ripple-container"]')
                    consent_button.click()
                    # print('clicked remind me later button')
                    sleep(random.uniform(11, 12))
                except:
                    pass

                # enter the location and press enter
                print(loc)
                search_field = bot.find_element_by_xpath(
                    "//input[@id='searchboxinput']")

                # clear anything currently in the search field
                search_field.clear()
                sleep_for(1, 2)

                search_field.send_keys(loc)  # enter the location name
                sleep_for(1, 3)
                search_button = bot.find_element_by_xpath(
                    "//button[@id = 'searchbox-searchbutton'] ")
                search_button.click()  # click the search button
                sleep_for(6, 8)

                # check for partial matches
                if hasXpath(bot, '//a[@class="place-result-container-place-link"]'):
                    first_selection = bot.find_element_by_xpath(
                        '//a[@class="place-result-container-place-link"]')
                    first_selection.click()
                    sleep_for(3, 6)
                else:
                    pass

                # check if "At this place bullshit exists at the bottom" -- if so, click
                if hasXpath(bot, '//button[@jsaction="pane.rating.category"]') == False:
                    if hasXpath(bot, "//h2[contains(text(),('At this place'))]"):
                        try:
                            selection_this_place = bot.find_element_by_xpath(
                                '//h2[contains(text(),("At this place"))]//../..//div[@role="link"]')
                            selection_this_place.click()
                            sleep_for(3, 6)
                        except:
                            pass

                ###############################################################
                # get location summary info
                ###############################################################
                name_scraped = try_find_else_empty(bot,
                                                   '//h1[contains(@class, "header-title")]', 'single', 'text')

                address_scraped = try_find_else_empty(bot,
                                                      "//button[@data-item-id='address']//div//div//div[contains(@class, 'gm2-body-2')]", 'single', 'text')

                pulse_address = try_find_else_empty(bot,
                                                    "[data-section-id='ol'] span.widget-pane-link", 'single', 'text')

                num_reviews = try_find_else_empty(
                    bot, '//button[@jsaction="pane.rating.moreReviews"]', 'single', 'text')

                avg_review = try_find_else_empty(
                    bot, "//ol[contains(@class, 'section-star-array')]", 'single', 'text')

                loc_type = try_find_else_empty(
                    bot, '//button[@jsaction="pane.rating.category"]', 'single', 'text')

                price_level = try_find_else_empty(
                    bot, "//span[contains(@aria-label,'Price:')]", 'single', 'text')

                # temp / permenantely closed
                # temp_perm_closed = try_find_else_empty(bot,
                #     '//span[@class="section-rating-term"]//span//span[contains(text(),"Temporarily closed") or contains(text(),"Permanently closed")]',
                #     'single','text')
                if hasXpath(bot, '//span[contains(text(),"Temporarily closed")]'):
                    temp_perm_closed = "Temporarily closed"
                elif hasXpath(bot, '//span[contains(text(),"Permanently closed")]'):
                    temp_perm_closed = "Permanently closed"
                else:
                    temp_perm_closed = ''

                # dining and takeout
                try:
                    curbside_parent = bot.find_element_by_xpath(
                        '//div[@class="section-editorial-attribute-container"]')
                    curbside_child_img = curbside_parent.find_elements_by_xpath(
                        '//img[contains(@class,"section-editorial-attribute-icon")]')
                    curbside_child_img = str(
                        [x.get_attribute('src') for x in curbside_child_img])
                    curbside_child_name = curbside_parent.find_elements_by_xpath(
                        '//div[contains(@class,"section-editorial-attribute-text")]')
                    curbside_child_name = str(
                        [x.text for x in curbside_child_name])
                except:
                    curbside_child_img = ''
                    curbside_child_name = ''		

                # get current url for lon lat
                try:
                    url = bot.current_url
                    urlstring = url.split('!3d')[1]
                    lat = urlstring.split('!4d')[0]
                    longi = urlstring.split('!4d')[1].split('?')[0]
                except:
                    lat = ''
                    longi = ''

                # website
                try:
                    website = bot.find_element_by_xpath(
                        '//button[@data-tooltip="Open website"]').get_attribute('aria-label').replace('Website: ', '').strip()
                except:
                    website = ''

                # phone number
                try:
                    phone = bot.find_element_by_xpath(
                        '//button[@data-tooltip="Copy phone number"]').get_attribute('aria-label').replace('Phone: ', '').strip()
                except:
                    phone = ''

                # health and safety
                try:
                    health_and_safety = bot.find_element_by_xpath(
                        '//button[contains(@aria-label,"Health & safety")]').get_attribute('aria-label')
                except:
                    health_and_safety = ''


                try:
                    img_urls = bot.find_element_by_xpath(
                        "//div[contains(@class, 'section-hero-header')]//img").get_attribute('src')
                except:
                    img_urls = 'https://www.enisa.europa.eu/topics/trainings-for-cybersecurity-specialists/online-training-material/images/whitakergroupgooglelocationicon.png/image'


                # opening hours
                # click button
                # try:
                if hasXpath(bot, "//div[contains(@jsaction, 'pane.openhours')]"):
                    hours_button = bot.find_element_by_xpath(
                        "//div[contains(@jsaction, 'pane.openhours')]")
                elif hasXpath(bot, "//span[contains(text(), 'See more hours')]//..//..//..//..//..//..//.."):
                    hours_button = bot.find_element_by_xpath(
                        "//span[contains(text(), 'See more hours')]//..//..//..//..//..//..//..")
                hours_button.click()
                sleep_for(1, 3)
                hours_all = bot.find_elements_by_xpath(
                    '//div[contains(@aria-label, "Hide open hours")]')
                hours_all = hours_all[0].get_attribute('aria-label')
                # try to get happy hours
                # try:
                #     happy_hour_button = bot.find_element_by_xpath('//span[contains(text(), "Happy hour")]//..//..//..//..')
                #     happy_hour_button.click()
                #     sleep_for(1,3)
                #     happy_hour = bot.find_elements_by_xpath(
                #         '//div[contains(@aria-label, "Hide open hours")]')
                #     happy_hour = happy_hour[1].get_attribute('aria-label')
                # except:
                #     happy_hour = ''
                # exit this window of hours of operation
                try:
                    hours_back_button = bot.find_element_by_xpath('//button[@data-tooltip="Back"]')
                    hours_back_button.click()
                    print('clicked back button')
                    sleep_for(2,4)
                except:
                    pass
                    url = 'https://www.google.com/maps/?hl=en'
                    bot.get(url)  # go to the url
                    sleep_for(4, 7)
                # except:
                #     hours_all = ''
                #     happy_hour = ''



                ###############################################################
                # get reviews and such
                ###############################################################

                # create dataframe to append everything to
                export_data = pd.DataFrame()

                # lets add in the stuff we already scraped.. general info
                export_data['loc_searched'] = pd.Series(
                    str(loc))  # we have to make one row first
                export_data['lat'] = lat  # then we can add in other columns
                export_data['long'] = longi
                export_data['name_only'] = name_scraped
                export_data['address_only'] = address_scraped
                export_data['pulse_address'] = pulse_address
                export_data['num_reviews'] = num_reviews
                export_data['loc_type'] = loc_type
                export_data['price_level'] = price_level
                export_data['temp_perm_closed'] = temp_perm_closed
                # export_data['loc_type_inputted'] = loc_type_item
                export_data['avg_review'] = avg_review
                export_data['curbside_child_img'] = curbside_child_img
                export_data['curbside_child_name'] = curbside_child_name
                export_data['website'] = website
                export_data['hours_all'] = hours_all
                export_data['phone'] = phone
                export_data['health_and_safety'] = health_and_safety
                export_data['happy_hour'] = '' # happy_hour
                export_data['img_urls'] = img_urls

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
                export_data.to_csv(out_name, encoding='utf-8',
                                   header=True, index=False)
                # # print('txt:    ' + str (out_name) + '  exported.. next item')
                # sleep_for(2, 3)
            except:
                continue

        bot.quit()
