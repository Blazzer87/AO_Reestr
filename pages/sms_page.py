from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class SmsPage(BasePage):

    PAGE_URL = Links.SMS_VERIFICATION_PAGE

    sms_code = (By.XPATH, '//input[@name="code"]')

    def enter_sms_code(self, sms_code):
        self.wait.until(EC.element_to_be_clickable(sms_code)).send_keys(sms_code)


