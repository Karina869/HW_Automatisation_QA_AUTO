from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self._driver = driver
