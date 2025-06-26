import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_Object.Login_Page import Login_page_class
from Utilities.Logger import log_class
from Utilities.Readconfig import ReadConfigClass


class Test_Login_User:

   email = ReadConfigClass.get_data_for_email()
   password = ReadConfigClass.get_data_for_password()
   log = log_class.loggen_method()

   def test_CredKart_title_001(self,driver_setup):

       # driver = webdriver.Chrome()
       driver = driver_setup
       self.log.info("open login Url")
       driver.get("https://automation.credence.in/login")


       if driver.title == "CredKart":
           self.log.info("Check Credkart title")
           print("you are landed on correct page")
           self.log.info("asser is true")
           assert True

       else:
           print("you ara not landed on correct page")
           self.log.info("assert False")
           assert False


   def test_login_page_002(self,driver_setup):
        self.log.info("Open login url")
        driver = driver_setup
        driver.get("https://automation.credence.in/login")
        self.lp = Login_page_class(driver)

        self.log.info("email")
        self.lp.Enter_email(self.email)
        self.log.info("password")
        self.lp.Enter_password(self.password)

        self.log.info("Click login")
        self.lp.Click_Login()
        self.log.info("wait for five second")
        wait = WebDriverWait(driver,5)

        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
            driver.find_element(By.XPATH,"/html/body/div/div[1]/p[1]")
            print("login  is successfully")
            self.log.info("Taking screen shrot pass")
            driver.save_screenshot( ".\\Screenshorts\\login Successfully.png")
            assert "pass"
        except:
            print("login is failed")
            self.log.info("Taking screen shot fail")
            driver.save_screenshot(".\\Screenshorts\\login page failed.png")
            assert "fail"





