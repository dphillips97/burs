# !python3
# Scrape beers, ABV, and volume from RO's Hopcat site 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

# Set Chromedriver options
# info from this website:
# https://sqa.stackexchange.com/questions/26051/chrome-driver-2-28-chrome-is-being-controlled-by-automated-test-software-noti

path_to_chromedriver = r'C:\Program Files\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--disable-infobars')

browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options = chrome_options)

# Get page object
url = 'https://hopcat.com/beer/royal-oak'
browser.get(url)

p_list = browser.find_elements_by_tag_name('div')

for i in p_list:
	print(i.text)
