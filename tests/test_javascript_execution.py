from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_infinite_scroll():
    """ Selenium Web Driver does not implement scrolling, so we use JavaScript to do it """
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/infinite-scroll.html")
    
    WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements(By.TAG_NAME, 'p')) > 0) # Wait for at least one paragraph on page
    init_num_paras = len(driver.find_elements(By.TAG_NAME, 'p')) # Get number of paragraphs
    last_para = driver.find_element(By.XPATH, f"//p[{init_num_paras}]") # Locate last paragraph

    # Use JavaScript to sroll to last paragraph
    script = "arguments[0].scrollIntoView();"
    driver.execute_script(script, last_para)

    WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements(By.TAG_NAME, 'p')) > init_num_paras) # Wait for more paragraphs on page
    end_num_paras = len(driver.find_elements(By.TAG_NAME, 'p')) # Get number of paragraphs
    
    assert end_num_paras > init_num_paras

def test_color_picker():
    """ Set attributes of an element that otherwise can't be done with selenium """
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

    color_picker = driver.find_element(By.NAME, "my-colors") # Locate color picker
    init_color = color_picker.get_attribute("value")
    print(f"Init color: {init_color}")
    sleep(5)

    # Use JavaScript to set attribute for color
    script = "arguments[0].setAttribute('value', '#ff0000')"
    driver.execute_script(script, color_picker)

    final_color = color_picker.get_attribute("value")
    print(f"Final color: {final_color}")
    sleep(5)

    assert init_color != final_color


    
