import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )




@pytest.fixture(scope="class")
def setup(request):
    browserName = request.config.getoption("browser_name")

    if browserName == "chrome":
        service_obj = Service("C:\\Browser\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browserName == "firefox":
        service_obj = Service("C:\\Browser\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browserName == "IE":
        pass

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(4)
    #return driver  #this line would not work when we need to use "yield"
    # insead of return we can use request.cls.driver = driver
    request.cls.driver = driver # basically we assiging our local driver object to class driver object

    yield
    driver.close()


