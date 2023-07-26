from selenium import webdriver
from selenium.webdriver.common.by import By

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