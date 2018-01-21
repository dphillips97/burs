# !python3
# Scrape beers, ABV, and volume from RO's Hopcat site 

#For testing, save beer list to text file first
# Use regex to parse
# export to excel

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import openpyxl


# Set Chromedriver options
# info from this website:
# https://sqa.stackexchange.com/questions/26051/chrome-driver-2-28-chrome-is-being-controlled-by-automated-test-software-noti
def startup():
	path_to_chromedriver = r'C:\Program Files\chromedriver.exe'
	chrome_options = Options()
	chrome_options.add_argument('--disable-infobars')

	browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options = chrome_options)

	# Get page object
	url = 'https://hopcat.com/beer/royal-oak'
	browser.get(url)

	#p_list = browser.find_elements_by_tag_name('div')
	p_list = browser.find_elements_by_class('beer-details')
	return p_list

	#div class = 'beer-details item-title-color'
	# get this more specific div class
	# parse text into chunks after price (last item in list)
	
def beer_lister(p_list):	
	with open ('beer.txt', 'w') as f:

		print('Len: %i' % len(p_list))
		for i in p_list:
			for k in range(100):
				f.write(i.text)
'''
def spreadsheet():
	# create master row iterator
	row_iter = 2
	
	# create spreadsheet
	wb = openpyxl.Workbook()
	sheet = wb.active
	
	sheet['A1'] = 'name'
	sheet['B1'] = 'abv'
	sheet['C1'] = 'size'
	sheet['D1'] = 'cost'
	
	wb.save()
	
	#get data from text file
	with open('beer.txt', 'r') as f:
		mo = re.match(r'(.*)\n(\d\.\d%).*\n(.*)\n(\$\d\.\d+)')
		
		try:
			name = mo.group(1)
			abv = mo.group(2)
			size = mo.group(3) 
			cost = mo.group(4)
			
			
			
		except:
			pass
'''			
			
				
p_list_return = startup()				
beer_doc = beer_lister(p_list_return)
