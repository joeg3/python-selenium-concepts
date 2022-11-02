#from telnetlib import EC
from time import sleep
import pytest
import unittest

from selenium.webdriver.common.by import By

from pages.google_home_page import HomePage

from ddt import ddt, data, unpack, file_data

from utilities.utils import Utils

# @pytest.mark.usefixtures('setup')
# @ddt
# @file_data('../testdata/testdata_class.yaml') # Requires PyYAML package
# class TestSearchGoogle(unittest.TestCase): # ddt needs unittest.TestCase as a parameter here

#     # Do test class setup here
#     @pytest.fixture(autouse=True)
#     def class_setup(self):
#         self.ut = Utils()

# With Page Object Model
def test_google_search(driver, domain):
    home_page = HomePage(driver, domain)
    home_page.load()
    home_page.wait_for_element_to_be_clickable(By.NAME, 'q')
    #home_page.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'2 Stop')]")
        
    # Here we have a call for each element
    #home_page.enterSearchFieldText('Python')
    #home_page.clickSearchButton()

    # Instead we can combine in one page object method
    search_result_page = home_page.googleSearch('Python')

    #search_result_page = SearchResults(self.driver)
    page_title = search_result_page.getPageTitle()
    assert "Python" in page_title

    #self.ut.assertThatIsUsedOften() # Example of using a utility function

    # # Use data driven testing
    # @data(("Python", "Python"), ("Dog", "Dog"))
    # @unpack
    # def test_google_search_ddt(self, search_term, search_result):
    #     home_page = HomePage(self.driver)
    #     home_page.wait_for_element_to_be_clickable(By.NAME, 'q')
    #     #home_page.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'2 Stop')]")
        
    #     # Here we have a call for each element
    #     #home_page.enterSearchFieldText('Python')
    #     #home_page.clickSearchButton()

    #     # Instead we can combine in one page object method
    #     search_result_page = home_page.googleSearch(search_term)

    #     #search_result_page = SearchResults(self.driver)
    #     page_title = search_result_page.getPageTitle()
    #     assert search_result in page_title

    # # Use data file
    # #@file_data('../testdata/testdata.json')
    # @file_data('../testdata/testdata.yaml') # Requires PyYAML package
    # def test_google_search_ddt_with_data_file(self, search_term, search_result):
    #     home_page = HomePage(self.driver)
    #     home_page.wait_for_element_to_be_clickable(By.NAME, 'q')
    #     #home_page.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'2 Stop')]")
        
    #     # Here we have a call for each element
    #     #home_page.enterSearchFieldText('Python')
    #     #home_page.clickSearchButton()

    #     # Instead we can combine in one page object method
    #     search_result_page = home_page.googleSearch(search_term)

    #     #search_result_page = SearchResults(self.driver)
    #     page_title = search_result_page.getPageTitle()
    #     assert search_result in page_title