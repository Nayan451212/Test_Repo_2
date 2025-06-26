import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def driver_setup(request):
    print("Browser is open")
    Browser = request.config.getoption("--browser")
    if Browser == "chrome":
        driver = webdriver.Chrome()
    elif Browser == "edge":
        driver = webdriver.Edge()

    elif Browser == "headless":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_option)

    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    print("Browser is close")


@pytest.fixture(params=[
    ("credence1@gamil.com" ,"Credence@123","Login pass"),
    ("credencel@gmail.com" ,"Credence@123","Login fail"),
    ("credence1@gmail.com" ,"Credence@1234","Login fail"),
    ("credencel@gmail.com" ,"Credence@1234","Login fail")
])
def get_data_for_login(request):
    return request.param
