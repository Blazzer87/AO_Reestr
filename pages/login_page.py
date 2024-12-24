from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    phone_locator = (By.XPATH, '//input[@name="phone"]')
    password_locator = (By.XPATH, '//input[@name="password"]')
    submit_button_locator = (By.XPATH,'//button[@type="submit"]')

    def enter_phone (self, phone):
        self.wait.until(EC.element_to_be_clickable(phone)).clear()
        phone.send_keys(phone)

    def enter_password (self, password):
        self.wait.until(EC.element_to_be_clickable(password)).clear()
        password.send_keys(password)

    def click_submit (self, submit_button):
        self.wait.until(EC.element_to_be_clickable(submit_button)).click()


