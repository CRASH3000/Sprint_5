from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time


def test_empty_fields_registration(driver, register_url):
    driver.get(register_url)

    # Нажимаем на кнопку "Зарегистрироваться" без заполнения полей
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)
    )
    submit_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что не произошло перехода на страницу логина
    assert driver.current_url != "https://stellarburgers.nomoreparties.site/login", (
        f"Ожидаемое: не переходить на страницу 'https://stellarburgers.nomoreparties.site/login', "
        f"Фактическое: '{driver.current_url}'"
    )
