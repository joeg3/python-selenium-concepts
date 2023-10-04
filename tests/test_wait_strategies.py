import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_implicit_wait(loading_images_page):
    """ Use implicit wait for images to load """

    loading_images_page.implicitly_wait(10)
    landscape = loading_images_page.find_element(By.ID, "landscape")
    assert "landscape".casefold() in landscape.get_attribute("src").casefold()

def test_explicit_wait(loading_images_page):
    """ Use explicit wait for image to load """

    WebDriverWait(loading_images_page, 10).until(EC.presence_of_element_located((By.ID, "landscape")))
    landscape = loading_images_page.find_element(By.ID, "landscape")
    assert "landscape".casefold() in landscape.get_attribute("src").casefold()
