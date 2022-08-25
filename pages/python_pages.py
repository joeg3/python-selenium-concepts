# Module for pages on python.org

class PythonHomePage:
    landing_url = ''

    def __init__(self, browser, domain):
        self.browser = browser
        self.domain = domain

    def load(self):
        self.browser.get(self.get_landing_page_url())

    def get_title(self):
        title = self.browser.title
        return title

    def get_landing_page_url(self):
        url = self.domain + self.landing_url
        return url