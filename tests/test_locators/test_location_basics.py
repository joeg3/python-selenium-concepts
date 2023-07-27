from selenium import webdriver
from selenium.webdriver.common.by import By

""" There are eight basic location strategies:
    tag name, link text, partial link text, name, id, class name, css selector, xpath
    Tests in this file cover: tag name, link text, partial link text, name, id, class name

    - HTML element: <p class="my-class" id="my-id">My paragraph</p>
    - Element tag name: p
    - Attributes: class, id
    - Attribute values: my-class, my-id
    - Content: My paragraph
    
"""

def test_locate_by_html_tag_name():
    """ Locate by HTML tag name (a, p, div, etc.) """
    
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    text_area = driver.find_element(By.TAG_NAME, "textarea")
    assert text_area.get_dom_attribute("rows") == "3"

def test_locate_by_name():
    """ Locate by the element 'name' attribute """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    element = driver.find_element(By.NAME, "my-text")
    assert element.is_enabled() # Assert element is enabled (user can type in it)

def test_locate_by_id():
    """ Locate by the element 'id' attribute """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    element = driver.find_element(By.ID, "my-text-id")

    # The 'type' attribute is standard, so it's also a property in the DOM
    assert element.get_attribute("type") == "text"
    assert element.get_dom_attribute("type") == "text"
    assert element.get_property("type") == "text" # DOM property

    # The 'myprop' attribute is not standard, so it's not available as a DOM property
    assert element.get_attribute("myprop") == "myvalue"
    assert element.get_dom_attribute("myprop") == "myvalue"
    assert element.get_property("myprop") == None

def test_locate_by_class_name():
    """ Locate by the element 'class' attribute """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    elements = driver.find_elements(By.CLASS_NAME, "form-control")
    assert len(elements) > 0
    assert elements[0].get_attribute("name") == "my-text" # Assert first element found by class is same as input text located earlier

def test_locate_by_link_text():
    """ Locate by the link text and partial link text """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    link_by_text = driver.find_element(By.LINK_TEXT, "Return to index")
    assert link_by_text.tag_name == "a"
    assert link_by_text.value_of_css_property("cursor") == "pointer"

    link_by_partial_text = driver.find_element(By.PARTIAL_LINK_TEXT, "index")
    assert link_by_text.location == link_by_partial_text.location
    assert link_by_text.rect == link_by_partial_text.rect







def test_locate_by_xpath_selector():
    """ Locate by xpath selector """
    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    url = f"{base_url}/web-form.html"

    driver = webdriver.Chrome()
    driver.get(url)

    # Syntax for XPath queries: //tagname[@attribute='value']
    # Element we are locating: <input type="hidden" name="my-hidden">
    hidden_element = driver.find_element(By.XPATH, "//input[@type='hidden']")
    assert hidden_element.is_displayed() == False

    # More elements we are locating:
    # <input class="form-check-input" type="radio" name="my-radio" id="my-radio-1" checked>
    # <input class="form-check-input" type="radio" name="my-radio" id="my-radio-2">
    r1 = driver.find_element(By.XPATH, "//*[@type='radio' and @checked]")
    assert r1.get_attribute("id") == "my-radio-1"
    assert r1.is_selected()

    r2 = driver.find_element(By.XPATH, "//*[@type='radio' and not(@checked)]")
    assert r2.get_attribute("id") == "my-radio-2"
    assert not r2.is_selected()
