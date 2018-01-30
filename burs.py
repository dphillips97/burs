#!python3
# get list of beers from Hopcat Royal Oak and find best value

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
import datetime

def time_gen():	
	
	time_format = datetime.datetime.now().strftime('%d-%m-%y %H:%M')
	
	return time_format
	
def main():
	
	# page to scrape
	url = r'https://hopcat.com/beer/royal-oak'
	
	# create empty results dictionary
	results_dict = {}
	
	# matches details in each beer entry 
	REGEX = r'(.*)\n(\d\.\d+)%.*\n(\w+)\s*\n\$(\d\.\d+)'
	
	# selenium stuff
	path_to_chromedriver = r'C:\Program Files\chromedriver.exe'
	chrome_options = Options()
	chrome_options.add_argument('--disable-infobars')

	# volume dict to match word values to mL values
	vol_dict = { 'Lager': 591,
				'Pint': 473,
				'Tulip': 300, #check
				'Weizen': 500,
				'Snifter': 200, #check 
				'Wine': 175 # check
				}
	
	# set up selenium-controlled browser
	browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options = chrome_options)
	
	#*******************************
	
	# get page object
	browser.get(url)
	
	# get all div objects of class 'beer-details'
	elems = browser.find_elements_by_class_name('beer-details')

	# write the following to file
	with open('burs.txt', 'w') as f:
		
		# add time info line by calling function
		f.write('Generated on: %s\n\n' % time_gen())
		
		# for each class='beer-details'
		for elem in elems:	
			
			elem_doc = elem.text
			
			prog = re.compile(REGEX)
			
			try:
			
				mo = prog.match(elem_doc)
				
				# get name of beer
				called = mo.group(1)
				
				# get abv as float percent
				abv = float(mo.group(2))
				abv_pct = abv / 100
				
				# get vol as float, have to make multiple steps(?)
				vol = mo.group(3)
				vol = vol_dict[vol]
				vol_num = float(vol)
				
				# get price as float
				price = float(mo.group(4))
				
				# calculate value index as float
				vi = float(abv_pct * vol / price)
				
				# write line to text file
				f.write('%s: %2f\n' % (called, vi))
				
				# add record's info to dict
				results_dict[called] = vi
				
			except:
				pass

	# generate values and write to screen		
	max_value = max(results_dict.values())
	max_keys = [k for k, v in results_dict.items() if v == max_value]
	print('The best value is %s with a value of %2f mL alcohol per $1' % (max_keys, max_value))
	
main()

'''
Set Chromedriver options:
 https://sqa.stackexchange.com/questions/26051/chrome-driver-2-28-chrome-is-being-controlled-by-automated-test-software-noti
'''

