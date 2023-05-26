from selenium import webdriver
from selenium.webdriver.common.by import By

# For OCR, install packages: pillow, pytesseract
from PIL import Image
from pytesseract import pytesseract

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
def test_get_text_in_screenshot():
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
    print("\n\n############### Start of text extracted from screenshot ####################")
    print(text)
    print("############### End of text extracted from screenshot ####################")

