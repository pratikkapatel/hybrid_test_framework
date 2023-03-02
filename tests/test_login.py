from selenium import webdriver
from assertpy import assert_that

class TestLoginUI:
    def test_title(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        act_title=driver.title
        #assert act_title=="OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(act_title)