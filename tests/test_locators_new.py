import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# <input name="txtUsername" id="txtUserName" type="text">
# Element (tag name): input
# Attributes: name, id, type
# Values: txtUsername, text

###################################### NEW LOCATOR TESTS ###################################################
"""
Two things to focus on:
1) Identify (locate) elements
2) Perform action on element

Two types of locators:
1) Built-in Locators
- Id
- Name
- Linktext and Partial linktext
- ClassName
- TagName

2) Customized Locators
- CSS Selector (uses html elements and attributes)
    - Tag and Id
    - Tag and Class
    - Tag and Attribute
    - Tag, Class, and Attribute
- XPath (does not rely on html)
    - Absolute XPath
    - Relative XPath
"""
def test_locate_by_id():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com")
    driver.maximize_window()

    driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

def test_locate_by_link_text():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Register").click()

def test_locate_by_partial_link_text():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com")
    driver.maximize_window()

    driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()