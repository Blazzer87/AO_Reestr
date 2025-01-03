from base.base_test import BaseTest
import allure
import pytest

@allure.feature("Тест авторизации по телефону")
class TestAuthorizationByPhone(BaseTest):

    @allure.title("Авторизация по номеру телефона и паролю")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_autorization_by_phone(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_phone()
        self.login_page.enter_password()
        self.login_page.click_submit()
        self.sms_page.enter_sms_code()
