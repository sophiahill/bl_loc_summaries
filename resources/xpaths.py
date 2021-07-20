# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:11:08 2021

@author: sophi
"""

# getting to locations
consent = './/button[@class="widget-consent-button-later ripple-container"]'
search_box = ".//input[@id='searchboxinput']"
search_but = ".//button[@id = 'searchbox-searchbutton'] "
place_cont = './/a[@class="place-result-container-place-link"]'
place_link = '//a[contains(@href, "https://www.google.com/maps/place/")]'
pane = './/button[@jsaction="pane.rating.category"]'
at_this_place = './/h2[contains(text(),("At this place"))]//../..//div[@role="link"]'

# location summary info
name = './/h1[contains(@class,"title")]//span[1]'
add = ".//button[contains(@aria-label,'Address')]"
pulse = ".//button[contains(@aria-label, 'Plus code')]"
num_rev = './/button[@jsaction="pane.rating.moreReviews"]'
avg_rev = './/ol[@class="section-star-array"]//..//span'
loc_type_path = ".//button[@jsaction='pane.rating.category']|.//span[contains(text(), 'star hotel')]"
find_price = ".//span[contains(@aria-label,'Price:')]"
temp_closed = './/span[contains(text(),"Temporarily closed")]'
perm_closed = './/span[contains(text(),"Permanently closed")]'

# service options
service_options_button = ".//div[contains(@aria-label, 'About')]//button"
so_boxes_path = ".//div[contains(@role, 'region')]"
so_back = ".//button[@aria-label='Back']"

# more info
site = './/button[@data-tooltip="Open website"]'
copy_phone = './/button[@data-tooltip="Copy phone number"]'
health_safety = './/button[contains(@aria-label,"Health & safety")]'
imgs = ".//div//button//img[contains(@decoding, 'async')]"
open_hours = ".//span[contains(@aria-label, 'Show open hours for the week')]"
hide_open_hours = './/div[contains(@aria-label, "Hide open hours")]'

back = './/button[@data-tooltip="Back"]'
