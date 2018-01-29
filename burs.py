# !python3
# Scrape beers, ABV, and volume from RO's Hopcat site 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

REGEX = r'(.*)\n(\d\.\d+%).*\n(\w+)\s*\n\$(\d\.\d+)'
# volume dict
vol_dict = {}

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

# get all div objects
elems = browser.find_elements_by_class_name('beer-details')


with open('burs.txt', 'w') as f:
	for elem in elems:	
		elem_doc = elem.text
		
		prog = re.compile(REGEX)
		
		try:
		
			mo = prog.match(elem_doc)
		
			called = mo.group(1)
			abv = mo.group(2)
			vol = mo.group(3)
			price = mo.group(4)
			
			f.write('%s, %s, %s, %s\n\n' % (called, abv, vol, price))
		
		except:
			
			pass
