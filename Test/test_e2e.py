import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilies.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):


        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        # //a[@href='/angularpractice/shop'] --> xpath
        # a[href*='/angularpractice/shop'] --> CSS selector

        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        print(products)
        for product in products:
            # print(product.text)
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            print(product_name)
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        # driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        success_text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

        assert "Success! Thank you!" in success_text

        time.sleep(4)






