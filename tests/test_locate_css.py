from selenium import webdriver
from selenium.webdriver.common.by import By

""" Examples for locating elements by CSS Selector

    HTML TERMINOLOGY
    - HTML element: <p class="my-class" id="my-id">My paragraph</p>
    - Element tag name: p
    - Attributes: class, id
    - Attribute values: my-class, my-id
    - Content: My paragraph

    Basic CSS Selector format: tagname[attribute='value']
"""

def test_basic_locate():
    """ Locate by tag and id with css selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">

    # Standard way to locate by css, and assert in one line
    assert driver.find_element(By.CSS_SELECTOR, "input[id='my-text-id']").is_displayed()

    # You can also grab the element and put it in a variable and assert later
    my_element = driver.find_element(By.CSS_SELECTOR, "input[id='my-text-id']")
    assert my_element.is_displayed()

def test_locate_by_tag_and_id():
    """ Locate by tag and id with css selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">

    assert driver.find_element(By.CSS_SELECTOR, "input[id='my-text-id']").is_displayed() # Standard way to locate by css
    assert driver.find_element(By.CSS_SELECTOR, "input#my-text-id").is_displayed() # Use '#' shorthand for ID attribute
    assert driver.find_element(By.CSS_SELECTOR, "#my-text-id").is_displayed() # Don't need tag name if id is unique

    # You can also grab the element and put it in a variable
    my_element = driver.find_element(By.CSS_SELECTOR, "input[id='my-text-id']")
    assert my_element.is_displayed()

def test_locate_by_tag_and_class():
    """ Locate by tag and class with css selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">

    assert driver.find_element(By.CSS_SELECTOR, "input[class='form-control']").is_displayed() # Standard way to locate by css
    assert driver.find_element(By.CSS_SELECTOR, "input.form-control").is_displayed() # Use '.' shorthand for class attribute
    assert driver.find_element(By.CSS_SELECTOR, ".form-control").is_displayed() # Don't need tag name if class is unique

def test_locate_by_tag_and_attribute():
    """ Locate by tag and attribute with css selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">

    assert driver.find_element(By.CSS_SELECTOR, "input[myprop='myvalue']").is_displayed() # Use for any attribute
    assert driver.find_element(By.CSS_SELECTOR, "[myprop='myvalue']").is_displayed() # Don't need tag name if attribute is unique

def test_locate_by_tag_and_class_and_attribute():
    """ Locate by tag and class and attribute with css selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # HTML: <input id="my-text-id" class="form-control" type="text" name="my-text" myprop="myvalue">
    # For locating by any attribute, use this syntax: html_tag.class_value[attr=value]

    assert driver.find_element(By.CSS_SELECTOR, "input.form-control[myprop='myvalue']").is_displayed() # Use for tag, class, and attribute
    
def test_locate_by_checkbox_status():
    """ Locate by css selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # HTML elements we are locating:
    # <input class="form-check-input" type="checkbox" name="my-check" id="my-check-1" checked>
    # <input class="form-check-input" type="checkbox" name="my-check" id="my-check-2">
    cb1 = driver.find_element(By.CSS_SELECTOR, "[type=checkbox]:checked")
    assert cb1.get_attribute("id") == "my-check-1"
    assert cb1.is_selected()

    cb2 = driver.find_element(By.CSS_SELECTOR, "[type=checkbox]:not(:checked)")
    assert cb2.get_attribute("id") == "my-check-2"
    assert not cb2.is_selected()