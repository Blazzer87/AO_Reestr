import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE_URL

    phone_locator = (By.XPATH, '//input[@name="phone"]')
    password_locator = (By.XPATH, '//input[@name="password"]')
    submit_button_locator = (By.XPATH,'//button[@type="submit"]')
    cpg_button_locator = (By.XPATH, '//button[contains(@class,"cpg")]')
    esia_button_locator = (By.XPATH, '//button[contains(@class,"esia")]')
    ukep_button_locator = (By.XPATH, '//button[contains(@class,"ukep")]')
    sber_button_locator = (By.XPATH, '//button[contains(@class,"sber")]')
    foggot_password_button_locator = (By.XPATH, '//a[contains(@class,"forgot_password")]')
    registration_button_locator = (By.XPATH, '//a[contains(@class,"register")]')

    def enter_phone (self, phone_locator, phone_number):
        with allure.step(f"Ввести телефон - {phone_number}"):
            phone_field = self.wait.until(EC.element_to_be_clickable(phone_locator))
            phone_field.clear()
            assert phone_field.get_attribute("value") == "", "Ошибка, поле номера телефона не было очищено перед вводом"
            phone_field.send_keys(phone_number)

    @allure.step("Ввести пароль")
    def enter_password (self, password_locator, password):
        with allure.step(f"Ввести пароль - {password}"):
            password_field = self.wait.until(EC.element_to_be_clickable(password_locator))
            password_field.clear()
            assert password_field.get_attribute("value") == "", "Ошибка, поле пароля не было очищено перед вводом"
            password_field.send_keys(password)

    @allure.step("Нажать кнопку Войти")
    def click_submit (self, submit_button):
        self.wait.until(EC.element_to_be_clickable(submit_button)).click()

    @allure.step("Нажать Войти через ЦПГ")
    def enter_by_cpg (self, cpg_button_locator):
        self.wait.until(EC.element_to_be_clickable(cpg_button_locator)).click()

    @allure.step("Нажать Войти через ЕСИА")
    def enter_by_esia (self, esia_button_locator):
        self.wait.until(EC.element_to_be_clickable(esia_button_locator)).click()

    @allure.step("Нажать Войти через УКЭП")
    def enter_by_ukep (self, ukep_button_locator):
        self.wait.until(EC.element_to_be_clickable(ukep_button_locator)).click()

    @allure.step("Нажать кнопку Забыли пароль")
    def click_foggot_password_button (self, foggot_password_button_locator):
        self.wait.until(EC.element_to_be_clickable(foggot_password_button_locator)).click()

    @allure.step("Нажать кнопку Зарегистрироваться")
    def click_registration_button (self, registration_button_locator):
        self.wait.until(EC.element_to_be_clickable(registration_button_locator)).click()
