from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_Obj = Service("C:\\Browser\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service_Obj,options=options)
driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.quit()
