import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Examples in this test case are tested onhttps://rahulshettyacademy.com/seleniumPractise/#/ for examples on waits
# Implicit wait: It's like a global timeout
# driver.implicitly_wait(2) # Driver will wait a max of 2 seconds. If everything loaded in 1 second, then the wait ends. 
# That makes this better than sleep(2) which would always be for 2 seconds.
def test_implicit_wait(driver, locator_test_domain5):
    driver.implicitly_wait(2) # In some cases good to have a global wait
    driver.get(locator_test_domain5) # Load url

    driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber") # Narrow choices by typing in 'ber'
    time.sleep(2)
    # For this next line, the implicit wait won't work with find_elements() because selenium will just return a empty list which is valid
    products = driver.find_elements(By.XPATH, "//div[@class='products']/div") # In products div, there are 3 child div, one for each product
    assert len(products) == 3

    for product in products:
        # This is called chaining. We want "//div[@class='products']/div/div/button", but since we already retrieved
        # a list of products with "//div[@class='products']/div", we can chain off of each one with "div/button"
        product.find_element(By.XPATH, "div/button").click() # Note we are using product.find_element(), not driver.find_element()

    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click() # Click on cart
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click() # Click on cart popup

    driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy") # Enter promo code
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click() # Click on promo button to apply discount
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "promoInfo").text # See if promo applied

# Examples in this test case are tested onhttps://rahulshettyacademy.com/seleniumPractise/#/ for examples on waits
# Downside of implicit wait is that every element is waiting even if only one is slow
def test_exlicit_wait(driver, locator_test_domain5):
    driver.implicitly_wait(2)
    driver.get(locator_test_domain5) # Load url

    driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber") # Narrow choices by typing in 'ber'
    time.sleep(2)
    # For this next line, the implicit wait won't work with find_elements() because selenium will just return a empty list which is valid
    products = driver.find_elements(By.XPATH, "//div[@class='products']/div") # In products div, there are 3 child div, one for each product
    assert len(products) == 3

    for product in products:
        # This is called chaining. We want "//div[@class='products']/div/div/button", but since we already retrieved
        # a list of products with "//div[@class='products']/div", we can chain off of each one with "div/button"
        product.find_element(By.XPATH, "div/button").click() # Note we are using product.find_element(), not driver.find_element()

    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click() # Click on cart
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click() # Click on cart popup

    
    driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy") # Enter promo code
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click() # Click on promo button to apply discount
    wait = WebDriverWait(driver, 10) # This is longer than our implicit wait for the page, and only applies to element showing promo
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))) # Wait until promo applied
    driver.find_element(By.CLASS_NAME, "promoInfo").text # See if promo applied 