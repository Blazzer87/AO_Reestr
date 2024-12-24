import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)            ## автоюс - автоматически внутри каждого теста, скоуп = фанкшен - создание экземляра браузера для каждого теста отдельно
def driver(request):
    options = Options()
    # options.add_argument("--headless")    # безголовый режим
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()