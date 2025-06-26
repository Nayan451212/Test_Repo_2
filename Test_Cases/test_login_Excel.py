import time

from Page_Object.Login_Page import Login_page_class
from Utilities.Excle_Utilities import Excel_utilities


class Test_CredKart_login_Excel_class:

    excel_file = ".\\Test_Data\\CretKart_Test_Data.xlsx"
    sheet_name = "login_data"

    def test_CredKart_login_excel_010(self,driver_setup):
        self.driver = driver_setup
        self.driver.get("https://automation.credence.in/login")
        self.lp = Login_page_class(self.driver)


        self.count_row = Excel_utilities.count_data_Excel(self.excel_file,self.sheet_name)
        result_list =[]
        for i in range(2 , self.count_row + 1):
            self.driver.get("https://automation.credence.in/login")

            email = Excel_utilities.read_Excel_data(self.excel_file, self.sheet_name, i, 2)
            password = Excel_utilities.read_Excel_data(self.excel_file, self.sheet_name, i, 3)
            expected_result = Excel_utilities.read_Excel_data(self.excel_file, self.sheet_name, i, 4)
            # self.log.info(f"Enter email-->{email}")
            self.lp.Enter_email(email)
            # self.log.info(f"Enter password-->{password}")
            self.lp.Enter_password(password)
            # self.log.info("Click login button")
            self.lp.Click_Login()
            # self.log.info("Verify login")
            if self.lp.verify_manu() == "pass":
                # self.log.info("login pass")
                # self.log.info("Taking screenshot")
                # self.driver.save_screenshot( f".\\Screenshots\\test_verify_login_param_005_login_pass_{email}_{password}.png")
                # self.log.info("Click menu button")
                self.lp.Click_manu()
                # self.log.info("Click logout button")
                self.lp.Click_logout()
                actual_result = "login pass"
            else:
                # self.log.info("login fail")
                # self.log.info("Taking screenshot")
                # self.driver.save_screenshot(f".\\Screenshots\\test_verify_login_param_005_login_fail_{email}_{password}.png")
                actual_result = "login fail"

            Excel_utilities.write_Excel_data(self.excel_file, self.sheet_name, i, 5, actual_result)

            if expected_result == actual_result:
                result_list.append("pass")
                test_status = "pass"
            else:
                result_list.append("fail")
                test_status = "pass"
            Excel_utilities.write_Excel_data(self.excel_file, self.sheet_name, i, 6, test_status)

        if "fail" in result_list:
            # self.log.info("test_verify_login_excel_006 is passed")
            assert True
        else:
            # self.log.info("test_verify_login_excel_006 is failed")
            assert False
        # self.log.info("test_verify_login_excel_006 is completed")














