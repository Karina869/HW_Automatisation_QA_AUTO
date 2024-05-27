from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class GaragePage(BasePage):
    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, '//body/app-root/app-global-layout/div[@class="global-layout"]/div[@class="app-wrapper"]/div[@class="app-content"]/app-panel-layout//app-garage//button[@class="btn btn-primary"]'
        ).click()


class AddCarModal(BasePage):

    def select_brand(self, car_brand_name: str):
        self._driver.find_element(By.XPATH, '/html//select[@id="addCarBrand"]').send_keys(
            car_brand_name
        )

    def select_model(self, car_model_name: str):
        self._driver.find_element(By.XPATH, '/html//select[@id="addCarModel"]').send_keys(
            car_model_name
        )

    def set_mileage(self, car_mileage):
        self._driver.find_element(By.XPATH, '/html//input[@id="addCarMileage"]').send_keys(
            car_mileage
        )

    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, '//ngb-modal-window[@role="dialog"]/div[@role="document"]//app-add-car-modal/div[3]/button[2]'
        ).click()


class FuelExpense(BasePage):

    def click_add_fuel_expense_button(self):
        self._driver.find_element(
            By.XPATH, '//body/app-root/app-global-layout/div[@class="global-layout"]/div[@class="app-wrapper"]/div[@class="app-content"]/app-panel-layout/div[@class="panel-layout"]//app-garage//ul[@class="car-list"]//app-car//button[.="Add fuel expense"]'
        ).click()


class AddFuelExpense(BasePage):
    def set_number_of_liters(self, number_of_liters):
        self._driver.find_element(
            By.XPATH, '/html//input[@id="addExpenseLiters"]'
        ).send_keys(number_of_liters)

    def set_total_cost(self, total_cost):
        self._driver.find_element(
            By.XPATH, '/html//input[@id="addExpenseTotalCost"]'
        ).send_keys(total_cost)

    def click_add_button(self):
        self._driver.find_element(
            By.XPATH, '//ngb-modal-window[@role="dialog"]/div[@role="document"]//app-add-expense-modal/div[3]/button[2]'
        ).click()


