from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

class TestLoginUI:
    def test_title(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        act_title=driver.title
        #assert act_title=="OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(act_title)

    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        act_title = driver.find_element(By.XPATH, "//h5[normalize-space()='Login']").text
        assert_that("Login").is_equal_to(act_title)


        #assert act_title=="OrangeHRM"