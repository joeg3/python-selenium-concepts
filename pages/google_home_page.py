from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.google_search_results_page import SearchResults
from utilities.highlighter import highlight

class HomePage(BasePage):
    def __init__(self, driver, domain):
        self.driver = driver
        self.domain = domain
        self.url_path = ''
        self.page_url = self.domain + self.url_path
        super().__init__(driver, domain, self.page_url)

    SEARCH_FIELD = (By.NAME, 'q')
    SEARCH_BUTTON = (By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")

    def search_by_clicking_button(self, text):
        self.wait_for_element_visibility(self.SEARCH_FIELD)
        search_field = self.find(self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(text)
        self.find(self.SEARCH_BUTTON).click()
        return SearchResults(self.driver, self.domain)

    def search_by_hitting_enter_key(self, text):
        self.wait_for_element_visibility(self.SEARCH_FIELD)
        search_field = self.find(self.SEARCH_FIELD)
        highlight(search_field, 3, "blue", 5)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)
        return SearchResults(self.driver, self.domain)
