import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_register_and_login(driver, page_url):
    driver.get(page_url)

    # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )

    # Кликаем на кнопку "Личный кабинет"
    account_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу логина
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    assert (
        driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    ), "Переход на страницу логина не произошел"

    # Нажимаем на кнопку "Зарегистрироваться"
    register_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    )
    register_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу регистрации
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/register")
    )
    assert (
        driver.current_url == "https://stellarburgers.nomoreparties.site/register"
    ), "Переход на страницу регистрации не произошел"

    # Нажимаем на кнопку "Войти" на странице регистрации
    login_from_register_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.LOGIN_FROM_REGISTER_LINK)
    )
    login_from_register_button.click()
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

    # Кликаем на кнопку "Личный кабинет" повторно
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )
    account_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу профиля
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
    )
    assert (
        driver.current_url
        == "https://stellarburgers.nomoreparties.site/account/profile"
    ), "Переход на страницу профиля не произошел"
