from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
<select class="form-select" name="my-select">
    <option selected>Open this select menu</option>
    <option value="1">One</option>
     <option value="2">Two</option>
     <option value="3">Three</option>
</select>
"""

def test_number_of_options_in_dropdown(web_form_page):
    dropdown = Select(web_form_page.find_element(By.NAME, "my-select"))
    assert len(dropdown.options) == 4

def test_iterate_through_dropdown(web_form_page):
    dropdown = Select(web_form_page.find_element(By.NAME, "my-select"))
    for option in dropdown.options:
        text = option.text
        value = option.get_attribute("value")

def test_select_option_by_visible_text(web_form_page):
    select = Select(web_form_page.find_element(By.NAME, "my-select"))
    select.select_by_visible_text("Two")
    assert "Two" == select.first_selected_option.text
    assert "2" == select.first_selected_option.get_attribute("value")

def test_select_option_by_index(web_form_page):
    select = Select(web_form_page.find_element(By.NAME, "my-select"))
    select.select_by_index(2)
    assert "Two" == select.first_selected_option.text
    assert "2" == select.first_selected_option.get_attribute("value")

def test_select_option_by_value(web_form_page):
    select = Select(web_form_page.find_element(By.NAME, "my-select"))
    select.select_by_value("2")
    assert "Two" == select.first_selected_option.text
    assert "2" == select.first_selected_option.get_attribute("value")

def test_click_on_option(web_form_page):
    """ Selenium Select doesn't really do a 'click', it just sets the html. For a dynamic page """
    """ where options change and you need to mouse click the option, try this approach which locates option """
    """ and clicks instead of locating Select and one of its select methods """
    option_name = "Two" # Determined at run time
    option = web_form_page.find_element(By.XPATH, f"//select[@name='my-select']/option[contains(text(), '{option_name}')]")
    option.click() # We never found the select html, instead located the particular option we wanted and clicked on it.

    # Now look at select that has already been clicked
    select = Select(web_form_page.find_element(By.NAME, "my-select"))
    assert "Two" == select.first_selected_option.text
    assert "2" == select.first_selected_option.get_attribute("value")