# https://realpython.com/python-doctest/
# # import testmod for testing 
from doctest import testmod 

# function for testing the data retrieving function.
def test_get_data():       
    """
    >>> import web_scraper
    >>> web_scraper.get_data()
    True
    """
    pass

if __name__ == "__main__":
    testmod(name = "test_get_data", verbose=True)
    
