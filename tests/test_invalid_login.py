import pytest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

@pytest.fixture(scope="module")
def driver():
    # Настраиваем WebDriver с использованием webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def page_url():
    return "https://stellarburgers.nomoreparties.site/"

def test_invalid_login(driver, page_url):
    driver.get(page_url)

    # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )

    # Кликаем на кнопку
    account_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу логина
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу логина не произошел"

    # Заполняем поля логина неверными данными
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys("invalid@mail.com")

    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys("wrongpassword")

    # Нажимаем на кнопку "Войти"
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что не произошло перехода на главную страницу
    assert driver.current_url != "https://stellarburgers.nomoreparties.site/", (
        f"Неожиданный переход на главную страницу: '{driver.current_url}'"
    )

    # Проверка, что остается на странице логина
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", (
        f"Ожидаемый URL: 'https://stellarburgers.nomoreparties.site/login', фактический URL: '{driver.current_url}'"
    )
