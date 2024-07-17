import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locators

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def page_url():
    return "https://stellarburgers.nomoreparties.site/"

def test_fillings_scroll(driver, page_url):
    driver.get(page_url)

    # Проверяем наличие раздела конструктора бургеров
    constructor_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
    )
    assert constructor_section.is_displayed(), "Раздел конструктора бургеров отсутствует"

    # Нажимаем на кнопку "Начинки"
    fillings_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.FILLINGS_TAB)
    )
    fillings_tab.click()
    time.sleep(2)  # Пауза для визуальной проверки

    # Проверяем, что произошел скролл до элемента "Мясо бессмертных моллюсков Protostomia"
    protostomia_meat = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.PROTOSTOMIA_MEAT)
    )
    assert protostomia_meat.is_displayed(), "Скролл до раздела 'Начинки' не произошел"
