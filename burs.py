# !python3
# Scrape beers, ABV, and volume from RO's Hopcat site 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

# matches details in each beer entry 
REGEX = r'(.*)\n(\d\.\d+)%.*\n(\w+)\s*\n\$(\d\.\d+)'

# volume dict to match word values to mL values
vol_dict = { 'Lager': 591,
		'Pint': 473,
		'Tulip': 300, #check
		'Weizen': 500,
		'Snifter': 200, #check 
		'Wine': 175 # check
}
			
results_dict = {}

# Set Chromedriver options
# info from this website:
# https://sqa.stackexchange.com/questions/26051/chrome-driver-2-28-chrome-is-being-controlled-by-automated-test-software-noti

path_to_chromedriver = r'C:\Program Files\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--disable-infobars')

browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options = chrome_options)

# Get page object
url = r'https://hopcat.com/beer/royal-oak'
browser.get(url)

# get all div objects of class 'beer-details'
elems = browser.find_elements_by_class_name('beer-details')

with open('burs.txt', 'w') as f:
	for elem in elems:	
		elem_doc = elem.text
		
		prog = re.compile(REGEX)
		
		try:
		
			mo = prog.match(elem_doc)
			
			# get name of beer
			called = mo.group(1)
			
			# get abv
			abv = float(mo.group(2))
			abv_pct = abv / 100
			
			# get vol, have to take multiple steps(?)
			vol = mo.group(3)
			vol = vol_dict[vol]
			vol_num = float(vol)
			
			# get price
			price = float(mo.group(4))
			
			# calculate value index
			vi = float(abv_pct * vol / price)
			
			#f.write('%s, %2f, %2f, %2f, %2f\n\n' % (called, abv_pct, vol_num, price, vi))
		
			f.write('%s: %2f\n' % (called, vi))
			
			results_dict[called] = vi
		except:
			pass

max_value = max(results_dict.values())
max_keys = [k for k, v in results_dict.items() if v == max_value]
print(max_value, max_keys)
	
