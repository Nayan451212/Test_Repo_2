from selenium.webdriver.common.by import By


class Login_page_class:
    text_email_id = "email"
    text_password_id ="password"
    Click_on_Login_button_class = "btn"
    Click_on_menu_class = "dropdown-toggle"
    Click_on_Logout_css = "a[href='https://automation.credence.in/logout']"


    def __init__(self,driver):
        self.driver = driver


    def Enter_email(self,email):
        Email_id =self.driver.find_element(By.ID,self.text_email_id)
        Email_id.send_keys(email)

    def Enter_password(self,password):
        password_felid =self.driver.find_element(By.ID,self.text_password_id)
        password_felid.send_keys(password)

    def Click_Login(self):
        Login_button = self.driver.find_element(By.CLASS_NAME,self.Click_on_Login_button_class)
        Login_button.click()

    def Click_manu(self):
        Click_on_manu = self.driver.find_element(By.CLASS_NAME,self.Click_on_menu_class)
        Click_on_manu.click()

    def Click_logout(self):
        Click_on_logout = self.driver.find_element(By.CSS_SELECTOR, self.Click_on_Logout_css)
        Click_on_logout.click()


    def verify_manu(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.Click_on_menu_class)
            return "pass"
        except:
            return "Fail"