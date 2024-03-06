import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin","admin123"),
                              ("adm","admin123"),
                              ("Admin","adm"),
                              ("adm","adm")
                              ]
                             )
    def test_Login(self,user,pwd):
        self.serv_obj=Service("C:\\Drivers\\chromedriver_win64\\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(15)

        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.TAG_NAME, "button").click()  # Signin
        try:
            self.status=self.driver.find_element(By.CSS_SELECTOR,"img[alt='client brand banner']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False


