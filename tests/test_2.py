from base.base_test import BaseTest
import allure
import pytest

@allure.feature("Тест регистрация по телефону")
class TestRegistrationByPhone(BaseTest):

    @allure.title("Регистрация по номеру телефона и паролю")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_registration_by_phone(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.click_registration_button()
        self.registration_page.enter_lastname()
        self.registration_page.enter_firstname()
        self.registration_page.enter_middlename()
        self.registration_page.enter_phone()
        self.registration_page.enter_inn()
        self.registration_page.enter_snils()
        self.registration_page.enter_password()
        self.registration_page.enter_password_again()
        self.registration_page.enter_document()
        self.registration_page.enter_email()
        self.registration_page.click_registration_button()
