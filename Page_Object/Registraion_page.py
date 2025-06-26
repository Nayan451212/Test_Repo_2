from selenium.webdriver.common.by import By

from Page_Object.Login_Page import Login_page_class


class Registration_page_class(Login_page_class):
    text_name_id = "name"
    text_confirm_password_name = "password_confirmation"
    click_button_submit_class = "btn"


    def Enter_name(self,name):
        self.driver.find_element(By.ID,self.text_name_id).send_keys(name)

    def Enter_confirm_password(self,password_confirmation):
        self.driver.find_element(By.NAME,self.text_confirm_password_name).send_keys(password_confirmation)

    def submit_button(self):
        self.driver.find_element(By.CLASS_NAME,self.click_button_submit_class).click()
