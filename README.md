# burs.py
This program is mainly for web scraping practice with selenium. 

High-level overview:

1. Get divs from Hopcat Royal Oak website
2. Use regex to get names, ABV, volume, price
3. Clean up data (convert glass sizes to mL using dict)
4. Calculate value index (not really an index): (vol * abv / price)
5. Return greatest value 
