from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



def test_webdriver_methods():
    """ A concise listing of web driver methods without asserts """

    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    #url = f"{base_url}/login-form.html"
    url = f"{base_url}"

    driver = webdriver.Chrome()
    driver.get(url) # Loads web page in browser

    driver.session_id  # Gets the unique session id created by the driver to track the browser session
    driver.current_url # Gets the url currently loaded in browser
    driver.title       # Gets the contents of the <title> tag of current page (tab title)
    driver.page_source # Gets HTML source of current page

    driver.minimize_window()
    driver.maximize_window()
    mid_screen = [1440, 900]
    driver.set_window_size(mid_screen[0], mid_screen[1])

    # The two ways to locate web elements
    driver.find_element(By.LINK_TEXT, "Web form")  # find_element() returns first occurrance (if any) of given node in the DOM
    driver.find_elements(By.CLASS_NAME, "row")     # find_elements() returns a list of DOM nodes
    
    # Go to another page to demonstrate navigation
    driver.find_element(By.LINK_TEXT, "Web form").click()
    driver.back()
    driver.refresh()
    driver.forward()

    # driver.navigate?
    # driver.get_window_handle
    # driver.get_window_handles
    # driver.switch_to
    # driver.manage

    driver.close() # Close current window, quitting browser if no other windows open
    driver.quit()  # Close all windows and quit the browser

def test_assert_webdriver_methods():
    """ A test showing the web driver methods in use with assertions """

    base_url = "https://bonigarcia.dev/selenium-webdriver-java"
    #url = f"{base_url}/login-form.html"
    url = f"{base_url}/"

    driver = webdriver.Chrome()

    driver.get(url) # Loads web page in browser

    assert driver.session_id is not None
    assert driver.current_url == url
    assert driver.title == "Hands-On Selenium WebDriver with Java"
    assert "</html>".casefold() in driver.page_source.casefold()

    driver.minimize_window()
    driver.maximize_window()
    mid_screen = [1440, 900]
    driver.set_window_size(mid_screen[0], mid_screen[1])

    # The two location methods: find_element() and find_elements()
    assert driver.find_element(By.LINK_TEXT, "Web form").is_displayed()
    rows = driver.find_elements(By.CLASS_NAME, "row")
    assert len(rows) > 0

    # Go to another page to demonstrate navigation
    driver.find_element(By.LINK_TEXT, "Web form").click()
    driver.back()
    driver.refresh()
    driver.forward()

    # driver.navigate?
    # driver.get_window_handle
    # driver.get_window_handles
    # driver.switch_to
    # driver.manage

    driver.close() # Close current window, quitting browser if no other windows open
    driver.quit()  # Close all windows and quit the browser
    
# Running in 'head' mode is where browser is open and you can see actions
# Running in 'headless' mode the test still runs, but you won't see anything. Maybe faster
def test_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized") # This can be done with selenium too
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(2)
    driver.get("https://www.ibm.com") # Load url
    driver.quit()
