from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

""" There are eight basic location strategies:
    tag name, link text, partial link text, name, id, class name, css selector, xpath
    Tests in this file cover: tag name, link text, partial link text, name, id, class name

    - HTML element: <p class="my-class" id="my-id">My paragraph</p>
    - Element tag name: p
    - Attributes: class, id
    - Attribute values: my-class, my-id
    - Content: My paragraph
    
"""

def test_locate_by_html_tag_name(web_form_page):
    """ Locate by HTML tag name (a, p, div, etc.) """
    
    text_area = web_form_page.find_element(By.TAG_NAME, "textarea")
    assert text_area.get_dom_attribute("rows") == "3"

def test_locate_by_name(web_form_page):
    """ Locate by the element 'name' attribute """
    
    element = web_form_page.find_element(By.NAME, "my-text")
    assert element.is_enabled() # Assert element is enabled (user can type in it)

def test_locate_by_id(web_form_page):
    """ Locate by the element 'id' attribute """

    element = web_form_page.find_element(By.ID, "my-text-id")

    # The 'type' attribute is standard, so it's also a property in the DOM
    assert element.get_attribute("type") == "text"
    assert element.get_dom_attribute("type") == "text"
    assert element.get_property("type") == "text" # DOM property

    # The 'myprop' attribute is not standard, so it's not available as a DOM property
    assert element.get_attribute("myprop") == "myvalue"
    assert element.get_dom_attribute("myprop") == "myvalue"
    assert element.get_property("myprop") == None

def test_locate_by_class_name(web_form_page):
    """ Locate by the element 'class' attribute """
    
    elements = web_form_page.find_elements(By.CLASS_NAME, "form-control")
    assert len(elements) > 0
    assert elements[0].get_attribute("name") == "my-text" # Assert first element found by class is same as input text located earlier

def test_locate_by_link_text(web_form_page):
    """ Locate by the link text and partial link text """

    link_by_text = web_form_page.find_element(By.LINK_TEXT, "Return to index")
    assert link_by_text.tag_name == "a"
    assert link_by_text.value_of_css_property("cursor") == "pointer"

    link_by_partial_text = web_form_page.find_element(By.PARTIAL_LINK_TEXT, "index")
    assert link_by_text.location == link_by_partial_text.location
    assert link_by_text.rect == link_by_partial_text.rect
    