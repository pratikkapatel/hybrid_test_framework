import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities import read_utils

class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name = read_utils.get_values_from_json("../test_data/data.json","browser")

        if browser_name == "edge":
            self.driver = webdriver.Edge()
        elif browser_name == "ff":
            self.driver = webdriver.Firefox()
        else:
            opt=webdriver.ChromeOptions()
            opt.add_argument("start-maximized")
            self.driver=webdriver.Chrome(opt)

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()