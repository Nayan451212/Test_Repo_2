from traceback import print_tb

from faker.proxy import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_Object.Login_Page import Login_page_class
from Page_Object.Registraion_page import Registration_page_class
from Utilities.Readconfig import ReadConfigClass


class Test001:

    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()

    def test_CredKart_title_003(self, driver_setup):
        # driver = webdriver.Chrome()
        driver = driver_setup
        driver.get("https://automation.credence.in/login")

        if driver.title == "CredKart":
            print("you are landed on correct page")
            assert True

        else:
            print("you ara not landed on correct page")
            assert False


    def test_login_page_004(self, driver_setup):
        driver = driver_setup
        driver.get("https://automation.credence.in/login")
        self.lp = Login_page_class(driver)

        self.lp.Enter_email(self.email)

        self.lp.Enter_password(self.password)

        self.lp.Click_Login()

        wait = WebDriverWait(driver, 5)

        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
            driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
            print("login  is successfully")
            driver.save_screenshot(".\\Screenshorts\\login Successfully.png")

            self.lp.Click_manu()
            self.lp.Click_logout()

            assert "pass"
        except:
            print("login is failed")
            driver.save_screenshot(".\\Screenshorts\\login page failed.png")

            assert "fail"

    def test_Registration_page_005(self, driver_setup):
        driver = driver_setup
        driver.get("https://automation.credence.in/register")
        name = Faker().name()
        email = Faker().email()

        self.rp = Registration_page_class(driver)

        self.rp.Enter_name(name)

        self.rp.Enter_email(email)

        self.rp.Enter_password("Credence@123")

        self.rp.Enter_confirm_password("Credence@123")

        self.rp.submit_button()

        if self.rp.verify_manu() == "pass":
            print("user Registration successfully")
            driver.save_screenshot(".\\Screenshorts\\ user registration .png")
            self.rp.Click_manu()
            self.rp.Click_logout()
            assert True
        else:
            print("user not registration successfully")
            driver.save_screenshot(".\\Screenshorts\\ user not registration.png")

