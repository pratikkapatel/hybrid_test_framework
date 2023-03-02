import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

class TestLoginUI:

    @pytest.fixture(scope="function",autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_title(self):
        act_title=self.driver.title
        #assert act_title=="OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(act_title)

    def test_header(self):
        act_header = self.driver.find_element(By.XPATH, "//h5[normalize-space()='Login']").text
        assert_that("Login").is_equal_to(act_header)


        #assert act_title=="OrangeHRM"