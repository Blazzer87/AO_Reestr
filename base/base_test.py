import pytest

from pages.login_page import *
from pages.sms_page import *
from pages.registration_page import *

class BaseTest:

    login_page: LoginPage
    sms_page: SmsPage
    registration_page: RegistrationPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.sms_page = SmsPage(driver)


