from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

def test_open_tab():
    ORIG_TAB_URL = "https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html"
    NEW_TAB_URL = "https://bonigarcia.dev/selenium-webdriver-java/web-form.html"

    driver = webdriver.Chrome()
    driver.get(ORIG_TAB_URL)

    assert 1 == len(driver.window_handles)
    assert driver.current_url == ORIG_TAB_URL
    sleep(2)

    driver.switch_to.new_window("Tab") # Driver now points to blank new tab, I don't think it matters what you have for text string argument
    driver.get(NEW_TAB_URL) # Load url in new tab
    assert 2 == len(driver.window_handles)
    assert driver.current_url == NEW_TAB_URL
    new_tab_handle = driver.current_window_handle # Store handle for new tab for later use
    
    orig_tab_handle = driver.window_handles[0]
    driver.switch_to.window(orig_tab_handle)
    sleep(2)

    driver.close() # Close original tab
    sleep(2)
    assert 1 == len(driver.window_handles)
    driver.switch_to.window(new_tab_handle) # Driver pointing to closed orig tab, need to point it to remaining tab
    assert driver.current_url == NEW_TAB_URL