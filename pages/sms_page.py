import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class SmsPage(BasePage):

    PAGE_URL = Links.SMS_VERIFICATION_PAGE_URL

    sms_code_locator = (By.XPATH, '//input[@name="code"]')
    sms_not_coming_button_locator = (By.XPATH, '//a[contains(@class,"sms_code_form__no_sms")]')
    back_button_locator = (By.XPATH, '//a[contains(@class,"sms_code_form__back")]')


    @allure.step("Ввести СМС пароль")
    def enter_sms_code (self, sms_code_locator, sms_code):
        self.wait.until(EC.element_to_be_clickable(sms_code_locator)).send_keys(sms_code)

    @allure.step("Кликнуть кнопку Не приодит СМС")
    def click_sms_not_coming_button (self, sms_not_coming_button_locator):
        self.wait.until(EC.element_to_be_clickable(sms_not_coming_button_locator)).click()

    @allure.step("Кликнуть кнопку Назад")
    def click_back_button (self, back_button_locator):
        self.wait.until(EC.element_to_be_clickable(back_button_locator)).click()

