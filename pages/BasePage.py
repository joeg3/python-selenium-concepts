from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, driver, domain):
        self.driver = driver
        self.domain = domain

    # Methods common to all pages
    def getPageTitle(self):
        return self.driver.title

    def getCurrentUrl(self):
        return self.domain.current_url

    def  wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        # self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'2 Stop')]")))
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements
