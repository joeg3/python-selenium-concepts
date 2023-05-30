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


