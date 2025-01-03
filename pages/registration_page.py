import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):

    PAGE_URL = Links.REGISTRATION_PAGE_URL

    lastname_locator = (By.XPATH, '//input[@name="lastName"]')
    firstname_locator = (By.XPATH, '//input[@name="firstName"]')
    middlename_locator = (By.XPATH,'//input[@name="middleName"]')
    not_middlename_checkbox_locator = (By.XPATH, '//label[contains(@class, "middle_name__checkbox")]')
    phone_locator = (By.XPATH, '//input[@name="phone"]')
    inn_locator = (By.XPATH, '//input[@name="inn"]')
    snils_locator = (By.XPATH, '//input[@name="snils"]')
    password_locator = (By.XPATH, '//input[@name="password"]')
    password_again_locator = (By.XPATH, '//input[@name="passwordAgain"]')
    another_document_checkbox_locator = (By.XPATH, '//label[contains(@class, "another_doc")]')
    document_locator = (By.XPATH, '//input[@name="document"]')
    email_locator = (By.XPATH, '//input[@name="email"]')
    submit_button_locator = (By.XPATH, '//button[@type="submit"]')
    cancel_button_locator = (By.XPATH, '//a[contains(@class,"registration_form__cancel")]')


    def enter_lastname (self, lastname_locator, lastname):
        with allure.step(f"Ввести Фамилию - {lastname}"):
            lastname_field = self.wait.until(EC.element_to_be_clickable(lastname_locator))
            lastname_field.clear()
            assert lastname_field.get_attribute("value") == "", "Ошибка, поле Фамилия не было очищено перед вводом"
            lastname_field.send_keys(lastname)

    def enter_firstname (self, firstname_locator, firstname):
        with allure.step(f"Ввести Имя - {firstname}"):
            firstname_field = self.wait.until(EC.element_to_be_clickable(firstname_locator))
            firstname_field.clear()
            assert firstname_field.get_attribute("value") == "", "Ошибка, поле Имя не было очищено перед вводом"
            firstname_field.send_keys(firstname)

    def enter_middlename (self, middlename_locator, middlename):
        with allure.step(f"Ввести Отчество - {middlename}"):
            middlename_field = self.wait.until(EC.element_to_be_clickable(middlename_locator))
            middlename_field.clear()
            assert middlename_field.get_attribute("value") == "", "Ошибка, поле Отчество не было очищено перед вводом"
            middlename_field.send_keys(middlename)

    @allure.step("Кликнуть чекбокс Нет Отчества")
    def click_not_middle_name_checkbox(self, not_middlename_checkbox_locator):
        self.wait.until(EC.element_to_be_clickable(not_middlename_checkbox_locator)).click()

    def enter_phone (self, phone_locator, phone):
        with allure.step(f"Ввести Телефон - {phone}"):
            phone_field = self.wait.until(EC.element_to_be_clickable(phone_locator))
            phone_field.clear()
            assert phone_field.get_attribute("value") == "", "Ошибка, поле Телефон не было очищено перед вводом"
            phone_field.send_keys(phone)

    def enter_inn (self, inn_locator, inn):
        with allure.step(f"Ввести ИНН - {inn}"):
            inn_field = self.wait.until(EC.element_to_be_clickable(inn_locator))
            inn_field.clear()
            assert inn_field.get_attribute("value") == "", "Ошибка, поле ИНН не было очищено перед вводом"
            inn_field.send_keys(inn)

    def enter_snils (self, snils_locator, snils):
        with allure.step(f"Ввести СНИЛС - {snils}"):
            snils_field = self.wait.until(EC.element_to_be_clickable(snils_locator))
            snils_field.clear()
            assert snils_field.get_attribute("value") == "", "Ошибка, поле СНИЛС не было очищено перед вводом"
            snils_field.send_keys(snils)

    def enter_password (self, password_locator, password):
        with allure.step(f"Ввести Пароль - {password}"):
            password_field = self.wait.until(EC.element_to_be_clickable(password_locator))
            password_field.clear()
            assert password_field.get_attribute("value") == "", "Ошибка, поле Пароль не было очищено перед вводом"
            password_field.send_keys(password)

    def enter_password_again (self, password_again_locator, password_again):
        with allure.step(f"Ввести ПарольСнова - {password_again}"):
            password_again_field = self.wait.until(EC.element_to_be_clickable(password_again_locator))
            password_again_field.clear()
            assert password_again_field.get_attribute("value") == "", "Ошибка, поле ПарольСнова не было очищено перед вводом"
            password_again_field.send_keys(password_again)

    def enter_document (self, document_locator, document):
        with allure.step(f"Ввести Телефон - {document}"):
            document_field = self.wait.until(EC.element_to_be_clickable(document_locator))
            document_field.clear()
            assert document_field.get_attribute("value") == "", "Ошибка, поле Документ не было очищено перед вводом"
            document_field.send_keys(document)

    @allure.step("Кликнуть чекбокс Иной Документ")
    def click_another_document_checkbox(self, another_document_checkbox_locator):
        self.wait.until(EC.element_to_be_clickable(another_document_checkbox_locator)).click()

    def enter_email (self, email_locator, email):
        with allure.step(f"Ввести Email - {email}"):
            email_field = self.wait.until(EC.element_to_be_clickable(email_locator))
            email_field.clear()
            assert email_field.get_attribute("value") == "", "Ошибка, поле Почта не было очищено перед вводом"
            email_field.send_keys(email)

    @allure.step("Кликнуть кнопку Зарегистрироваться")
    def click_registration_button (self, submit_button_locator):
        self.wait.until(EC.element_to_be_clickable(submit_button_locator)).click()

    @allure.step("Кликнуть кнопку Отмена")
    def click_cancel_button(self, cancel_button_locator):
        self.wait.until(EC.element_to_be_clickable(cancel_button_locator)).click()