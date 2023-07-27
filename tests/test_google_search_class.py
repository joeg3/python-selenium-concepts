import pytest

from pages.google_home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.usefixtures('driver_for_class')
class TestGoogleSearch(BaseTest):

    def test_google_search_by_clicking_button(self, domain, test_data):
        home_page = HomePage(self.driver, domain)
        home_page.load()

        search_result_page = home_page.search_by_clicking_button(test_data['search_term'])
        page_title = search_result_page.get_page_title()
        assert test_data['search_result'] in page_title

        # search_result_page = home_page.search_by_clicking_button(test_data['search_term']) #home_page.googleSearch(test_data['search_term'])
        # page_title = search_result_page.getPageTitle()
        # assert test_data['search_result'] in page_title

    def test_google_search_by_hitting_enter_key(self, driver_for_class, domain, test_data):
        home_page = HomePage(driver_for_class, domain)
        home_page.load()

        search_result_page = home_page.search_by_hitting_enter_key(test_data['search_term']) #home_page.googleSearch(test_data['search_term'])
        page_title = search_result_page.get_page_title()
        assert test_data['search_result'] in page_title

        # search_result_page = home_page.search_by_hitting_enter_key(test_data['search_term']) #home_page.googleSearch(test_data['search_term'])
        # page_title = search_result_page.getPageTitle()
        # assert test_data['search_result'] in page_title

    # def test_search_field_visible(self, driver_for_class, domain_for_class):
    #     home_page = HomePage(driver_for_class, domain_for_class)
    #     assert home_page.is_search_field_exist()

    # """ Should be able to just pass in self? """
    # # def test_search_field_visible(self):
    # #     home_page = HomePage(self.driver_for_class, self.domain_for_class)
    # #     assert home_page.is_search_field_exist()

    # def test_home_page_title(self, driver_for_class, domain_for_class):
    #     self.home_page = HomePage(driver_for_class, domain_for_class)
    #     assert "Google" == self.home_page.get_home_page_title("Google")

    # def test_search(self, driver_for_class, domain_for_class):
    #     self.home_page = HomePage(driver_for_class, domain_for_class)
    #     self.home_page.do_search("Minnesota")

