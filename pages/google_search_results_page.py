from pages.base_page import BasePage

class SearchResults(BasePage):
    def __init__(self, driver, domain):
        self.driver = driver
        self.domain = domain
        self.url_path = ''
        self.page_url = self.domain + self.url_path
        super().__init__(driver, domain, self.page_url)
