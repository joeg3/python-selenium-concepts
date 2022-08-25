from base.base_driver import BaseDriver

class SearchResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver