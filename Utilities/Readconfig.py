import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        email = config.get("login data" ,"email")
        return email

    @staticmethod
    def get_data_for_password():
        password = config.get("login data","password")
        return password

    @staticmethod
    def get_login_Url():
        Login_Url = config.get("Application","Login_Url")
        return Login_Url