# Import testmod for docctest testing.
from doctest import testmod 

# Function for testing the data retrieving function.
# https://realpython.com/python-doctest/
def test_get_data():       
    """
    >>> import web_scraper
    >>> web_scraper.get_data()
    True
    """
    pass

if __name__ == "__main__":
    testmod(name = "test_get_data", verbose=True)
    
