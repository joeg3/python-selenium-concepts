from xml import dom
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.google_search_results_page import SearchResults

class HomePage(BasePage):
    def __init__(self, driver, domain):
        super().__init__(driver, domain)
        self.driver.get(domain)

    url_path = ''

    # Locators
    SEARCH_FIELD = 'q'
    SEARCH_BUTTON = 'btnK'

    ################################### Start Naveen
    SEARCH_FIELD2 = (By.NAME, 'q')
    SEARCH_BUTTON2 = (By.CSS_SELECTOR, "div[class='FPdoLc lJ9FBc'] input[name='btnK']")

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_search_field_exist(self):
        return self.is_visible(self.SEARCH_FIELD2)

    def do_search(self, text):
        self.do_send_keys(self.SEARCH_BUTTON2, text)
        self.do_click(self.SEARCH_BUTTON2)



    ################################### End Naveen

    def getSearchField(self):
        return self.driver.find_element(By.NAME, self.SEARCH_FIELD)

    def getSearchButton(self):
        return self.driver.find_elements(By.NAME, self.SEARCH_BUTTON)[-1] # There are two 'btnK' elements, find_elements() gets a list, and [-1] returns the last one

    def enterSearchFieldText(self, txt):
        #self.getSearchField().click()
        self.getSearchField().send_keys(txt)
        #self.getSearchField().send_keys(Keys.ENTER) # We are instead clicking Search button

    def wait_for_search_field_clickability(self):
        self.wait_for_element_to_be_clickable(By.NAME, 'q')
    
    def clickSearchButton(self):
        submit_button = self.driver.find_elements(By.NAME, 'btnK')[-1] # There are two 'btnK' elements, find_elements() gets a list, and [-1] returns the last one
        self.getSearchButton().click()

    # Combines the entering of text and click
    # Also links to result page by returning reference to it
    def googleSearch(self, txt):
        self.enterSearchFieldText(txt)
        self.clickSearchButton()
        search_result_page = SearchResults(self.driver, self.domain)
        return search_result_page

    # Original way we did it. Not sure if breaking out into SEARCH_FIELD, getSearchField(), and enterSearchFieldText() is worth it
    def search_field(self, search_str):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.send_keys(search_str)

    # Also original way
    def click_search(self):
        submit_button = self.driver.find_elements(By.NAME, 'btnK')[-1] # There are two 'btnK' elements, find_elements() gets a list, and [-1] returns the last one
        submit_button.click()

    # Actions
    def load(self):
        self.driver.get(self.get_landing_page_url())

    def get_landing_page_url(self):
        return self.domain + self.url_path