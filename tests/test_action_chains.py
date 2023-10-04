from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with

""" Examples of ActionChains for things like:
    - context click
    - double-click
"""

def test_context_click(dropdown_menu_page):
    action = ActionChains(dropdown_menu_page)
    dropdown2 = dropdown_menu_page.find_element(By.ID, "my-dropdown-2")
    action.context_click(on_element = dropdown2)
    action.perform() # Context click middle dropdown menu
    context_menu2 = dropdown_menu_page.find_element(By.ID, "context-menu-2")
    assert context_menu2.is_displayed() # Verify middle menu displayed

def test_double_click(dropdown_menu_page):
    action = ActionChains(dropdown_menu_page)
    dropdown3 = dropdown_menu_page.find_element(By.ID, "my-dropdown-3")
    action.double_click(on_element = dropdown3)
    action.perform() # Double click right dropdown menu
    context_menu3 = dropdown_menu_page.find_element(By.ID, "context-menu-3")
    assert context_menu3.is_displayed() # Verify right menu displayed

def test_mouse_over(mouseover_page):
    action = ActionChains(mouseover_page)
    image_list = ['compass', 'calendar', 'award', 'landscape']
    for image_name in image_list:
        xpath = f"//img[@src='img/{image_name}.png']"
        image = mouseover_page.find_element(By.XPATH, xpath)
        action.move_to_element(to_element=image)
        action.perform() # move mouse pointer to middle of each image

        caption = mouseover_page.find_element(locate_with(By.TAG_NAME, "div").near(image))
