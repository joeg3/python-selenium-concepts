from selenium import webdriver
from selenium.webdriver.common.by import By

# For OCR, install packages: pillow, pytesseract
from PIL import Image
from pytesseract import pytesseract
import easyocr

import time

def test_element_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    form = driver.find_element(By.TAG_NAME, "form")
    form.screenshot(f"./screenshots/test_element_screenshot_{time.strftime('%Y%m%d-%H:%M:%S')}.png")

def test_page_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    driver.save_screenshot(f"./screenshots/test_page_screenshot_{time.strftime('%Y%m%d-%H:%M:%S')}.png")

# def test_page_screenshot_base64():
#     driver = webdriver.Chrome()
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
#     str = driver.get_screenshot_as_base64()
#     print(str)
#     #driver.get_screenshot_as_base64(f"./screenshots/test_page_screenshot_{time.strftime('%Y%m%d-%H:%M:%S')}.png")


### OCR
# Prerequisite
# Install Tesseract
# https://tesseract-ocr.github.io/tessdoc/Installation.html
# Mac: brew install tesseract
def test_get_text_in_screenshot_tesseract():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

    # Get screenshot
    screenshot_file = f"./screenshots/screenshot_to_ocr_{time.strftime('%Y-%m-%d_%H%M%S')}.png"
    driver.save_screenshot(screenshot_file)

    # Do OCR
    # Path to tesseract application installed previously
    # path_to_tesseract = r'C\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_tesseract = r'/opt/homebrew/bin/tesseract'

    # Point tesseract command to installed tesseract program
    pytesseract.tesseract_cmd = path_to_tesseract

    # Open image with PIL
    img = Image.open(screenshot_file)

    # Extract text from image
    text = pytesseract.image_to_string(img)
    print("\n\n############### Start of tesseract text extracted from screenshot ####################")
    print(text)
    print("############### End of tesseract text extracted from screenshot ####################")
    target_text = "Practice"
    assert target_text in text, f"Could not find {target_text} in screenshot"

def test_get_text_in_screenshot_easyocr():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

    # Get screenshot
    screenshot_file = f"./screenshots/screenshot_to_ocr_{time.strftime('%Y-%m-%d_%H%M%S')}.png"
    driver.save_screenshot(screenshot_file)

    # Search for text in screenshot
    reader = easyocr.Reader(['en']) # Can read multiple languages, we're just doing English
    result_array = reader.readtext(screenshot_file, detail=0) # detail=0 simplifies output, otherwise you get text box coordinates [x,y], text and model confident level for each piece of text

    print("\n\n############### Start of easyocr text extracted from screenshot ####################")
    print(result_array)
    print("############### End of easyocr text extracted from screenshot ####################")

    target_text = "Practice"
    for phrase in result_array:
        if target_text in phrase:
            return
    assert False, f"Could not find text '{target_text}' in screenshot"
