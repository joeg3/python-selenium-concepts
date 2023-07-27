from selenium.webdriver.common.by import By

class HeaderNav:
    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    def goto_about_page(self):
        self.map.about_link.click()

class HeaderNavMap:
    def __init__(self, driver):
        self.driver = driver

    @property
    def about_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'About')