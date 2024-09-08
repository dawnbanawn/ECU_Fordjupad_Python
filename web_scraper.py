from bs4 import BeautifulSoup
import logging
import sqlite3
# This helps sending http requests.
import requests
# This Helps get the correct date/time.
import datetime


# Logging configuration.
LOG_FILENAME = 'log.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# Create a connection to the sqlite database.
# https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
con = sqlite3.connect("database.db")
# Cursor helps to execute SQL statements. 
cur = con.cursor()

# Url for a website to scrape from.
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

# Function to scrape, find specific data, and save it in lists.
def get_data():
    # Sending http requests to the url, which returns the content of the page.
    req = requests.get(url)
    # Parse with the right type of parser, used for structuring the data.
    doc = BeautifulSoup(req.text, "html.parser")
    # Find the correct html elements containing name/price.
    # Global so that the variable can be used in other functions out of scope.
    global nameResult
    nameResult = doc.find_all("a", {"class": "title"})
    global priceResult
    priceResult= doc.find_all("h4", {"class": "price"})
    
    # Returns a True to separate doctest script if both variables are populated equally large lists. 
    if isinstance(nameResult, list) == True and isinstance(priceResult, list) == True and len(nameResult) > 1 and len(priceResult) > 1 and len(nameResult) == len(priceResult):
        return True
    else:
        return False

# Function to save scraped data to the database.
def save_to_database():
    # for loop with index to cycle through one of the equally long lists
    # save the data in the database in the correct columns, with the current date aswell.
    # The $ is removed from price, and price is converted from text to float to be inserted in the REAl column in the database.
    for idx, item in enumerate(nameResult):
        cur.execute(
            "INSERT INTO laptops(name, price, date) VALUES(?, ?, ?)",
                    (nameResult[idx].decode_contents(), float(priceResult[idx].decode_contents()[1:]), datetime.datetime.now()))

    # Commit the changes to the database.
    con.commit()

# Exception is raised and logged if getting data doesnt succeed.
try:
    # Call function to get the data.
    get_data()
except:
    logging.debug('Get data did not succeed!')
    raise Exception('Get data did not succeed!')
# If getting data went well, the next step is to try and save the data to sqlite.
else: 
    # Exception is raised and logged if saving to database doesnt succeed.
    try:
        # Call function to save to database.
        save_to_database()
    except:
        logging.debug('Saving to database did not succeed!')
        raise Exception('Saving to database did not succeed!')
    else:
        logging.info('Task completed!')
        











