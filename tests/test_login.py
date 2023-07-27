import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen

class Test_Login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    
    logger = LogGen.loggen()

    def test_home_page_title(self, ytdriver):
        self.logger.info("********* test_home_page_title() ************")
        self.logger.info("********* Verifying Home Page Title ************")
        self.driver = ytdriver
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home Page test passed ************")
        else:
            self.driver.save_screenshot("./screenshots/" + "test_home_page_title.png")
            self.driver.close()
            self.logger.error("********* Home Page test failed ************")
            assert False

    def test_login(self, ytdriver):
        self.logger.info("********* test_login() ************")
        self.logger.info("********* Verifying Login ************")
        self.driver = ytdriver
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* Login test passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("********* Login test failed ************")
            assert False
