from pages.BasePage import BasePage

class SearchResults(BasePage):
    def __init__(self, driver, domain):
        super().__init__(driver, domain)
        self.driver = driver
        self.domain = domain