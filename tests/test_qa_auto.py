from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from page_object.garage import AddCarModal, AddFuelExpense
from page_object.home_page import HomePage
from page_object.Create_user import RegistrationPage


def test_sing_up(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_sing_up_button()

    registration_page = RegistrationPage(driver)

    registration_page.enter_username("Karl")
    registration_page.enter_user_last_name("Black")
    registration_page.enter_email("karllllll_bbbbbbbllaaaacckkkk@gmail.com")
    registration_page.enter_password("Qwert12345")
    registration_page.enter_repeat_password("Qwert12345")
    registration_page.click_register_button()
    registration_page.assert_user_data("Karl Black")

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '/html//input[@id="signupName"]'))
    )

    add_car_modal = AddCarModal(driver)
    add_car_modal.select_brand("Audi")
    add_car_modal.select_model("Q7")
    add_car_modal.set_mileage(100)
    add_car_modal.click_add_car_button()

    add_fuel_expense = AddFuelExpense(driver)
    add_fuel_expense.set_number_of_liters(10)
    add_fuel_expense.set_total_cost(100)
    add_fuel_expense.click_add_button()
