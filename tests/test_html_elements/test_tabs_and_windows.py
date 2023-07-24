from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


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


