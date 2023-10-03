from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

""" WebDriver has no distinction between windows and tabs. """
""" Doing something that opens a new window or tab focuses on it. """
""" But WebDriver doesn't know what's active. """

def test_open_tab():
    ORIG_TAB_URL = "https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html"
    NEW_TAB_URL = "https://bonigarcia.dev/selenium-webdriver-java/web-form.html"

    driver = webdriver.Chrome()
    driver.get(ORIG_TAB_URL)

    assert 1 == len(driver.window_handles)
    assert driver.current_url == ORIG_TAB_URL
    sleep(2)

    driver.switch_to.new_window("Tab") # Driver now points to blank new tab, I don't think it matters what you have for text string argument
    driver.get(NEW_TAB_URL) # Load url in new tab
    assert 2 == len(driver.window_handles)
    assert driver.current_url == NEW_TAB_URL
    new_tab_handle = driver.current_window_handle # Store handle for new tab for later use
    
    orig_tab_handle = driver.window_handles[0]
    driver.switch_to.window(orig_tab_handle)
    sleep(2)

    driver.close() # Close original tab
    sleep(2)
    assert 1 == len(driver.window_handles)
    driver.switch_to.window(new_tab_handle) # Driver pointing to closed orig tab, need to point it to remaining tab
    assert driver.current_url == NEW_TAB_URL

def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    driver.find_element(By.ID, "my-alert").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Hello world!"
    alert.accept()
def test_confirm():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    driver.find_element(By.ID, "my-confirm").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm = driver.switch_to.alert
    assert confirm.text == "Is this correct?"
    confirm.dismiss()

def test_prompt():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    driver.find_element(By.ID, "my-prompt").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    prompt = driver.switch_to.alert
    prompt.send_keys("Fred")
    assert prompt.text == "Please enter your name"
    prompt.accept()

def test_modal_window():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    driver.find_element(By.ID, "my-modal").click()
    close = driver.find_element(By.XPATH, "//button[text() = 'Close']")
    assert close.tag_name == "button"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close))
    close.click()

def test_open_new_browser_window(web_form_page):
    orig_window = web_form_page.current_window_handle # Starting page in browser
    assert len(web_form_page.window_handles) == 1
    sleep(2)

    web_form_page.switch_to.new_window("window") # open new window
    web_form_page.get("https://www.google.com")
    sleep(2)
    assert len(web_form_page.window_handles) == 2
    web_form_page.close() # close new window
    sleep(2)

    web_form_page.switch_to.window(orig_window) # switch back to original window, could also have used web_form_page.window_handles[0] instead of orig_window variable
    assert len(web_form_page.window_handles) == 1
    sleep(2)

def test_open_new_browser_tab(web_form_page):
    orig_tab = web_form_page.current_window_handle # Starting page in browser
    assert len(web_form_page.window_handles) == 1
    sleep(2)

    web_form_page.switch_to.new_window("tab") # open new tab
    web_form_page.get("https://www.ibm.com")
    sleep(2)
    assert len(web_form_page.window_handles) == 2
    web_form_page.close() # close new tab
    sleep(2)

    web_form_page.switch_to.window(orig_tab) # switch back to original tab, could also have used web_form_page.window_handles[0] instead of orig_window variable
    assert len(web_form_page.window_handles) == 1
    sleep(2)

def test_iterate_through_tabs(web_form_page):
    orig_tab = web_form_page.current_window_handle # Starting page in browser
    web_form_page.switch_to.new_window("tab") # open new tab
    web_form_page.get("https://www.ibm.com")
    web_form_page.switch_to.new_window("tab") # open new tab
    web_form_page.get("https://www.google.com")
    sleep(2)
    assert len(web_form_page.window_handles) == 3
    
    count = 0
    first_page = None
    # Iterate through handles, but would have to .switch_to_window() each time for browser to iterate tabs
    for handle in web_form_page.window_handles:
        print(f"Tab name: {web_form_page.title}, URL: {web_form_page.current_url}")
        count += 1
        sleep(2)
        if handle == orig_tab:
            first_page = handle

    web_form_page.switch_to.window(first_page)
    assert count == 3
    sleep(2)


