from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс для инициализации драйвера
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4, poll_frequency=1) # пул фрикуенси для оценки как часто будет опрос старницы на выполненеи условия

    def open(self):
        self.driver.get(self.Page_Url)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.Page_Url))
