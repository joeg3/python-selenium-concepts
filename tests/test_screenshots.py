from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime
import time

def test_element_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    form = driver.find_element(By.TAG_NAME, "form")
    form.screenshot(f"./screenshots/test_element_screenshot_{time.strftime('%Y%m%d-%H:%M:%S')}.png")

def test_page_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    driver.save_screenshot(f"./screenshots/test_page_screenshot_{time.strftime('%Y%m%d-%H:%M:%S')}.png")

def get_current_timestamp_as_string():
    timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")