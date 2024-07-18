import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_forgot_password_and_login(driver, login_url):
    driver.get(login_url)

    # Ждем, пока ссылка "Восстановить пароль" не станет видимой, максимум 5 секунд
    forgot_password_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
    )

    # Кликаем на ссылку "Восстановить пароль"
    forgot_password_link.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу восстановления пароля
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password")
    )
    assert (
        driver.current_url
        == "https://stellarburgers.nomoreparties.site/forgot-password"
    ), "Переход на страницу восстановления пароля не произошел"

    # Нажимаем на кнопку "Войти"
    login_from_forgot_password_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.LOGIN_FROM_REGISTER_LINK)
    )
    login_from_forgot_password_link.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу логина
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    assert (
        driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    ), "Переход на страницу логина не произошел"

    # Заполняем поля логина
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys("test30011@mail.com")

    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys("B1234567b1")

    # Нажимаем на кнопку "Войти"
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на главную страницу
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )
    assert (
        driver.current_url == "https://stellarburgers.nomoreparties.site/"
    ), "Переход на главную страницу не произошел"
