from selenium import webdriver
from selenium.webdriver.common.by import By

""" Examples for locating elements by CSS Selector

    HTML TERMINOLOGY
    - HTML element: <p class="my-class" id="my-id">My paragraph</p>
    - Element tag name: p
    - Attributes: class, id
    - Attribute values: my-class, my-id
    - Content: My paragraph

    Basic CSS Selector format: //tagname[@attribute='value']
"""

def test_basic_locate(web_form_page):
    """ Locate by tag and id with xpath selector """
    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">

    # Standard way to locate by xpath, and assert in one line
    assert not web_form_page.find_element(By.XPATH, "//input[@type='hidden']").is_displayed()

    # You can also grab the element and put it in a variable and assert later
    my_element = web_form_page.find_element(By.XPATH, "//input[@type='hidden']")
    assert not my_element.is_displayed()

def test_locate_from_html_root(web_form_page):
    """ Locate by path from html root, not recommended """

    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">

    # Absolute xpath starts with single slash /
    assert web_form_page.find_element(By.XPATH, "/html/body/main/div/form/div/div/label/input").is_displayed()

def test_locate_by_radio_button_status(web_form_page):
    """ Locate by xpath selector """
    # HTML elements we are locating:
    # <input class="form-check-input" type="radio" name="my-radio" id="my-radio-1" checked>
    # <input class="form-check-input" type="radio" name="my-radio" id="my-radio-2">
    r1 = web_form_page.find_element(By.XPATH, "//*[@type='radio' and @checked]")
    assert r1.get_attribute("id") == "my-radio-1"
    assert r1.is_selected()

    r2 = web_form_page.find_element(By.XPATH, "//*[@type='radio' and not(@checked)]")
    assert r2.get_attribute("id") == "my-radio-2"
    assert not r2.is_selected()