from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.google_home_page import HomePage

# With Page Object Model
# We can test for different urls, browsers, test data
def test_google_search_by_clicking_button(driver_for_script, domain, test_data):
    home_page = HomePage(driver_for_script, domain)
    home_page.load()

    search_result_page = home_page.search_by_clicking_button(test_data['search_term'])
    page_title = search_result_page.get_page_title()
    assert test_data['search_result'] in page_title

def test_google_search_by_hitting_enter_key(driver_for_script, domain, test_data):
    home_page = HomePage(driver_for_script, domain)
    home_page.load()
    search_result_page = home_page.search_by_hitting_enter_key(test_data['search_term']) #home_page.googleSearch(test_data['search_term'])
    page_title = search_result_page.get_page_title()
    assert test_data['search_result'] in page_title
