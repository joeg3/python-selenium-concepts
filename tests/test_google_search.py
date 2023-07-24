from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.google_home_page import HomePage

# Basic test with a script, not using Page Objects. This doesn't even use fixtures
# for driver, and is locked into hard coded browser, url, and test data
def test_google_search(config):
    browser_arg = config['test-browser']
    opts = webdriver.ChromeOptions()
    if browser_arg == "chrome-headless":
        opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    driver.get('https://google.com')
    driver.find_element(By.NAME, 'q').send_keys('packers')
    driver.find_element(By.NAME, 'btnK').submit()

    assert 'packers' in driver.title

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
