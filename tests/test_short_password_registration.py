import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locators
import time

@pytest.fixture(scope="module")
def driver():
    # Настраиваем WebDriver с использованием webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def page_url():
    return "https://stellarburgers.nomoreparties.site/register"

def test_short_password_registration(driver, page_url):
    driver.get(page_url)

    # Заполняем поля формы регистрации
    name_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.NAME_FIELD)
    )
    name_field.send_keys("Тестовое Имя")

    email_field = driver.find_element(*Locators.EMAIL_FIELD)
    email_field.send_keys("test3002@mail.com")

    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys("1234")  # Неполный пароль (меньше 7 символов)

    # Нажимаем на кнопку "Зарегистрироваться"
    submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
    submit_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что появилось сообщение об ошибке "Некорректный пароль"
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ERROR_MESSAGE_INVALID_PASSWORD)
        )
    except TimeoutException:
        print("Ошибка: Сообщение об ошибке 'Некорректный пароль' не появилось")
        raise

    expected_error_message = "Некорректный пароль"
    actual_error_message = error_message.text
    assert actual_error_message == expected_error_message, (
        f"Ожидаемое сообщение: '{expected_error_message}', "
        f"Фактическое сообщение: '{actual_error_message}'"
    )

    # Проверяем, что не произошло перехода на страницу логина
    assert driver.current_url != "https://stellarburgers.nomoreparties.site/login", (
        f"Ожидаемое: не переходить на страницу 'https://stellarburgers.nomoreparties.site/login', "
        f"Фактическое: '{driver.current_url}'"
    )
