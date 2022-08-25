from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver
from pages.google_search_results_page import SearchResults

class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SEARCH_FIELD = 'q'
    SEARCH_BUTTON = 'btnK'

    def getSearchField(self):
        return self.driver.find_element(By.NAME, self.SEARCH_FIELD)

    def getSearchButton(self):
        return self.driver.find_elements(By.NAME, self.SEARCH_BUTTON)[-1] # There are two 'btnK' elements, find_elements() gets a list, and [-1] returns the last one

    def enterSearchFieldText(self, txt):
        #self.getSearchField().click()
        self.getSearchField().send_keys(txt)
        #self.getSearchField().send_keys(Keys.ENTER) # We are instead clicking Search button
    
    def clickSearchButton(self):
        submit_button = self.driver.find_elements(By.NAME, 'btnK')[-1] # There are two 'btnK' elements, find_elements() gets a list, and [-1] returns the last one
        self.getSearchButton().click()

    # Combines the entering of text and click
    # Also links to result page by returning reference to it
    def googleSearch(self, txt):
        self.enterSearchFieldText(txt)
        self.clickSearchButton()
        search_result_page = SearchResults(self.driver)
        return search_result_page

    # Original way we did it. Not sure if breaking out into SEARCH_FIELD, getSearchField(), and enterSearchFieldText() is worth it
    def search_field(self, search_str):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.send_keys(search_str)

    # Also original way
    def click_search(self):
        submit_button = self.driver.find_elements(By.NAME, 'btnK')[-1] # There are two 'btnK' elements, find_elements() gets a list, and [-1] returns the last one
        submit_button.click()