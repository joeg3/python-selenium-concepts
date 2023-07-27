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

# Examples in this test case are tested on https://rahulshettyacademy.com/angularpractice
def test_locators1(driver, locator_test_domain1):
    driver.get(locator_test_domain1) # Load url

    # ************************ Selenium Locators ***************************
    # Available locators: ID, XPATH, CSS_SELECTOR, NAME, LINK_TEXT, PARTIAL_LINK_TEXT. You can't select by type or value elements.
    # XPath and CSSSelector can be used to locate any element on the page, whereas others like id, name, class need to have the element defined.
    # Better to use name, class, id, but these are dependent on if developer used them.

    # NAME
    driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')

    # ID
    driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
    driver.find_element(By.ID, 'exampleCheck1').click() # checkbox

    # XPATH
    # XPath format: //tagname[@attribute='value']
    # So for this elememt: <input class='btn btn-success' type='submit' value='Submit'>
    # The tagname is 'input', and attributes are: class, type, value
    # So for this input element, the XPath is: //input[@type='submit']
    driver.find_element(By.XPATH, "//input[@type='submit']").click() # Click submit button

    # CLASS_NAME
    # For this element:
    # <div class="alert alert-success alert-dismissible">...</div>
    # It has three class names separated by spaces. You can use only one of the three classes if you want:
    message = driver.find_element(By.CLASS_NAME, 'alert-success').text # Returns text of element
    assert 'Success!' in message

    # CSS_SELECTOR
    # CSS Selector format: tagname[attribute='value']
    # Note: slightly different from XPath, no // on front and no @ in front of attribute
    # So for this elememt: <input class="form-control ng-pristine ng-invalid ng-touched" minlength="2" name="name" required="" type="text">
    # The tagname is 'input', and attributes are: class, minlength, name, value, type
    # So for this input element, the CSS Selector is: input[name='name']
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Fred')

    # CSS_SELECTOR by id shortcut: #id
    # <input class="form-check-input" id="inlineRadio1" name="inlineRadioOptions" type="radio" value="option1" style="" xpath="1">
    # For id you can just use shortcut #inlineRadio1 instead of input[id='inlineRadio1']
    driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click() # For selecting by id with CSS, a preceding # means id and you don't need the tag or attribute name

    # CSS_SELECTOR by classname shortcut: .classname
    # <div class="alert alert-success alert-dismissible">...</div>
    # For class name you can just preceed with a dot: .alert-success instead of input[class='alert-success']
    driver.find_element(By.CSS_SELECTOR, ".alert-success").text # For selecting by class name with CSS, a preceding . means class name, and you don't need the tag or attribute name

    # Click a checkbox
    driver.find_element(By.ID, 'exampleCheck1').click() # Checkbox

    # Static Dropdown where the values in the dropdown are hardcoded
    # Use Select class with dropdowns to get methods for list of values returned
    # Select class corresponds with <select> element on page. When you see <select>, use Select
    dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
    val = dropdown.select_by_index(0) # Select from list by index
    dropdown.select_by_visible_text('Female') # Select by text displayed in dropdown
    #dropdown.select_by_value('MN') # Example page doesn't have values in dropdown

    # Multiple elements of same type
    driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('Hello') # This is the 3rd element with type='text' (Indexed by 1, not 0)
    driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear() # Removes text from element

# Examples in this test case are tested on https://rahulshettyacademy.com/client
def test_locators2(driver, locator_test_domain2):
    driver.get(locator_test_domain2) # Load url

    # LINK_TEXT and PARTIAL_LINK_TEXT
    # For element <a _ngcontent-wgd-c43="" class="forgot-password-link" href="/client/auth/password-new" xpath="1">Forgot password?</a>
    # Find by link text
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Forgot') # By.LINK_TEXT is preferred
    driver.find_element(By.LINK_TEXT, 'Forgot password?').click()


    # XPATH by traversing hierarchy
    # Find based on parent tags using XPath for cases where target element can't be uniquely identified on its own
    # Form Element:
    # <form _ngcontent-wgd-c43="" novalidate="" class="ng-pristine ng-invalid ng-touched" xpath="1">
    #   <div _ngcontent-wgd-c43="" class="form-group">
    #     <label _ngcontent-wgd-c43="" for="email">Email</label>
    #     <input _ngcontent-wgd-c43="" type="email" formcontrolname="userEmail" id="userEmail" placeholder="email@example.com" class="form-control ng-pristine ng-invalid ng-touched"><!---->
    #   </div>
    #   <div _ngcontent-wgd-c43="" class="form-group mb-4"><label _ngcontent-wgd-c43="" for="password">Password</label><input _ngcontent-wgd-c43="" type="password" formcontrolname="userPassword" id="userPassword" placeholder="enter your passsword" class="form-control ng-untouched ng-pristine ng-invalid"><!----></div><input _ngcontent-wgd-c43="" name="login" id="login" type="submit" value="Login" class="btn btn-block login-btn"></form>
    # Traverse from parent form to child div with /, and index the first div with [1] since multiple: //form/div[1]
    driver.find_element(By.XPATH, '//form/div[1]/input').send_keys('demo@gmail.com') # email

    # CSS_SELECTOR by traversing hierarchy
    # Unlike XPATH, don't need the first two slashes //, and single slashes between elements should be spaces and use nth-child() notation
    driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys('Hello@1234') # password

    driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Hello@1234') # confirm password

    # XPATH by element text
    # Can get element using XPATH based on element text, in this case button text, use text()
    # <button _ngcontent-wgd-c46="" type="submit" class="btn btn-custom btn-block" style="background-color: #96161f; color: white;" xpath="1">Save New Password</button>
    driver.find_element(By.XPATH, "//button[@type='submit']").click() # click button
    # driver.find_element(By.XPATH, "//button[text()='Save New Password']").click() # same, but locating by button text

# Examples in this test case are tested on https://rahulshettyacademy.com/dropdownsPractise for auto-suggestive dropdowns
# These are the dropdowns where the options narrow as you type
# For auto dropdowns, they do not use the <select> tag, so you can't use the Select class
# <input type="text" id="autosuggest" class="inputs ui-autoocmplete-input valid" placeholder="Type to Select" autocomplete="off">
def test_locators3(driver, locator_test_domain3):
    driver.get(locator_test_domain3) # Load url

    driver.find_element(By.ID, 'autosuggest').send_keys('ind') # Pop-up appears with elements that have 'ind'
    time.sleep(2) # Hack

    # Now get all items in pop-up, they are all similar to this:
    # <li class="ui-menu-item" role="presentation" css="1">
    #   <a id="ui-id-67" class="ui-corner-all" tabindex="-1">British Indian Ocean Territory</a>
    # </li>
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") # Note find_elements() is plural and returns a list, and we are getting <a>, the child of <li>
    assert 3 == len(countries)

    for country in countries:
        if country.text == 'India': # Similar to grabbing text from any selenium element
            country.click()
            break # We clicked on the one we want, skip the rest

    # When page first loaded, dropdown didn't have any values
    # After clicked the drop down if got populated and we selected one
    assert "India" == driver.find_element(By.ID, "autosuggest").get_attribute('value') # Value attribute in a text box gets a value when you type, or in this case when you select one of the values

# Examples in this test case are tested on https://rahulshettyacademy.com/AutomationPractice
# This shows how to select a checkbox from a list of them that is variable and you don't know the order or number of them
def test_locators4(driver, locator_test_domain4):
    driver.get(locator_test_domain4) # Load url

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checlbox']")

    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "option2":
            checkbox.click()
            assert checkbox.is_selected()
            break
    
    # Here we know the radio buttons won't change, so we don't need to iterate through them.
    radios = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
    radios[2].click()
    assert radios[2].is_selected()

    # Display box
    assert driver.find_element(By.ID, "displayed-text").is_displayed()
    driver.find_element(By.ID, "hide-textbox").click() # Hide displayed text
    assert not driver.find_element(By.ID, "displayed-text").is_displayed()

    # Alert pop-up - by default, the selenium driver doesn't have knowledge of pop-ups
    name = "Fred"
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name) # Enter name in text box
    driver.find_element(By.ID, "alertbtn").click()
    alert = driver.switch_to.alert # Driver is switched to alert, cannot see browser
    alert_text = alert.text # Grab text from alert pop-up
    assert "Hello Fred" in alert_text
    alert.accept() # Click OK button on alert (this alert only has OK button)
    # alert.dismiss() # If alert has OK and Cancel buttons, .accept() clicks OK, and .dismiss() clicks Cancel

def test_sum_validation(driver, locator_test_domain5):
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

    # Apply promotion to cart
    driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy") # Enter promo code
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click() # Click on promo button to apply discount
    wait = WebDriverWait(driver, 10) # This is longer than our implicit wait for the page, and only applies to element showing promo
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))) # Wait until promo applied

    # Validate sum
    prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p") # Get cost from 5 column of table
    sum = 0
    for price in prices:
        sum = sum + int(price.text) # price is a web element, so still need to get text out of it and convert to integer

    total_from_page = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
    assert sum == total_from_page

    # Validate discount
    discount_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
    assert discount_amount < total_from_page
    
def test_search_results(driver, locator_test_domain5):
    driver.implicitly_wait(2)
    driver.get(locator_test_domain5) # Load url

    expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
    actual_list = []

    driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber") # Narrow choices by typing in 'ber'
    time.sleep(2)

    products = driver.find_elements(By.XPATH, "//div[@class='products']/div") # In products div, there are 3 child div, one for each product
    assert len(products) == 3

    for product in products:
        actual_list.append(product.find_element(By.XPATH, "h4").text)
        product.find_element(By.XPATH, "div/button").click() # Note we are using product.find_element(), not driver.find_element()

    assert expected_list == actual_list

def test_mouse_hover(driver, locator_test_domain4):
    driver.implicitly_wait(2)
    driver.get(locator_test_domain4) # Load url

    action = ActionChains(driver)
    # action.drag_and_drop() # supply source and target

    # Two steps. First you need to move the mouse to the element, then you need to right-click
    action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() # For all of these actions, you always need .perform() on end
    #action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  # Right click
    action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
    
def test_open_frame(driver, locator_test_domain6):
    # You will have to look for an <iframe> tag
    # Like with browser tabs, you have to switch the driver to the frame
    driver.implicitly_wait(2)
    driver.get(locator_test_domain6 + "/iframe") # Load url
    
    driver.switch_to.frame("mce_0_ifr") # "mce_0_ifr" is the id of the frame, name of the frame will work too
    driver.find_element(By.ID, "tinymce").clear() # Clear text box
    driver.find_element(By.ID, "tinymce").send_keys("Hello World")

    # Switch back to parent
    driver.switch_to.default_content() # default_content is normal browser scope
    driver.find_element(By.CSS_SELECTOR, "h3").text

# Selenium does not provide a way to scroll, we have to use JavaScript
# In Chrome Inspector, go to Console tab
# Enter in console: window.scrollTo(0,600) # Where 600 is the height
# This uses the JavaScript window object that has many methods
# To scroll to bottom: window.scrollBy(0,document.body.scrollHeight)
# Where document.body.scrollHeight is the height of the page, so if you scroll down the distance of the page height, you'll be at bottom
def test_using_javascript(driver, locator_test_domain4):
    driver.implicitly_wait(2)
    driver.get(locator_test_domain4) # Load url

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # execute_script() runs JavaScript in browser, don't forget the ';' at end
    driver.execute_script("window.scrollBy(0,500);")

    driver.get_screenshot_as_file("screen.png")

#@pytest.mark(skip='Currently failing')
def test_sort(driver, locator_test_domain5):
    driver.implicitly_wait(2) # In some cases good to have a global wait
    driver.get(locator_test_domain5 + "offers") # Load url

    expected_sorted_list = []
    unsorted_list_from_browser = driver.find_elements(By.XPATH, "//tr/td[1]") # Get first column
    for item in unsorted_list_from_browser:
        expected_sorted_list.append(item.text)
    expected_sorted_list.sort()
    print(expected_sorted_list)

    actual_sorted_list = []
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click() # Click on column header to sort
    sorted_list_from_browser = driver.find_elements(By.XPATH, "//tr/td[1]") # Get first column
    for item in sorted_list_from_browser:
        actual_sorted_list.append(item.text)
    
    assert len(actual_sorted_list) == len(expected_sorted_list) + 1
    # This fails because there are only 5 of many items on webpage, so when I grab the original items before sorting,
    # they are completely different items after sorting, not just different ordering
    # Tutorial first did sort and then compared to sorting the python list:


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