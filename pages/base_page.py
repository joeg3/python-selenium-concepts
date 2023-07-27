from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from sys import platform

class BasePage():
    def __init__(self, driver, domain, page_url):
        self.driver = driver
        self.domain = domain
        self.page_url = page_url
        print("Opening url: ", self.get_page_url()) 

    def load(self):
        self.driver.get(self.get_page_url())

    def get_page_url(self):
        return self.page_url
    
    def get_page_title(self):
        return self.driver.title
    
    def get_current_url(self):
        return self.driver.current_url
    
    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()
    
    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_clickability(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def wait_for_element_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def wait_for_element_value_text_presence(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text))
    
    def wait_for_element_text_presence(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
    
    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def get_element_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text
    
    def does_element_exist(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            self.driver.find_element(*locator)
        except (NoSuchElementException, TimeoutException):
            return False
        else:
            return True
        
    def does_element_contain_text(self, locator, expected_text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))
            actual_text = self.driver.find_element(*locator).text
            assert actual_text == expected_text
        except (NoSuchElementException, TimeoutException):
            return False
        else:
            return True
        
    def clear_text_field(self, locator):
        """ For fields where standard Selenium clear() method doesn't work """
        element = self.driver.find_element(*locator)
        if platform == "darwin": # Mac
            element.send_keys(Keys.COMMAND, "a")
        else: # Win or Linux
            element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
