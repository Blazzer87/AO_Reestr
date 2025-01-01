import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс для инициализации драйвера
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)         # пул фрикуенси для оценки как часто будет опрос старницы на выполненеи условия


    def open(self):
        with allure.step(f"Открывается страница - {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Успешно открыта страница - {self.PAGE_URL}"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def do_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.JPG
        )
