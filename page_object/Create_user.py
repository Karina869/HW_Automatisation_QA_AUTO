from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class RegistrationPage(BasePage):

    def enter_username(self, username: str):
        self._driver.find_element(By.XPATH, '/html//input[@id="signupName"]').send_keys(
            username
        )

    def enter_user_last_name(self, user_last_name: str):
        self._driver.find_element(By.XPATH, '/html//input[@id="signupLastName"]').send_keys(
            user_last_name
        )

    def enter_email(self, email: str):
        self._driver.find_element(By.XPATH, '/html//input[@id="signupEmail"]').send_keys(
            email
        )

    def enter_password(self, password: str):
        self._driver.find_element(By.XPATH, '/html//input[@id="signupPassword"]').send_keys(
            password
        )

    def enter_repeat_password(self, password: str):
        self._driver.find_element(
            By.XPATH, '/html//input[@id="signupRepeatPassword"]'
        ).send_keys(password)

    def click_register_button(self):
        self._driver.find_element(
            By.XPATH, '//ngb-modal-window[@role="dialog"]/div[@role="document"]//app-signup-modal/div[@class="modal-footer"]/button[@type="button"]'
        ).click()

    def assert_user_data(self, expected_user_data: str):
        user_data = self._driver.find_element(
            By.XPATH, '//body/app-root/app-global-layout/div[@class="global-layout"]/div[@class="app-wrapper"]/div[@class="app-content"]/app-panel-layout//app-profile//p[.="Karl Black"]'
        ).text
        assert user_data == expected_user_data


class DeletePage(BasePage):

    def click_remove_my_account_button(self):
        self._driver.find_element(
            By.XPATH, '/html//button[@class="btn btn-danger-bg"]'
        ).click()

    def click_remove_button(self):
        self._driver.find_element(By.XPATH, '/html//button[@class="btn btn-danger"]').click()
