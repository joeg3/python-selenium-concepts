from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pages_alt.base.pagebase import PageBase

class AboutPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver) # Invokes PageBase __init__() which sets up HeaderNav
        self.map = AboutPageMap(driver)

    def goto(self):
        self.headernav.goto_about_page()
        return self

class AboutPageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def contact_us_link(self) -> WebElement:
        return self._driver.find_element(By.LINK_TEXT, 'Contact us')