import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\Drivers\chromedriver_win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.TAG_NAME, "button").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_edge(self):
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.TAG_NAME, "button").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()



