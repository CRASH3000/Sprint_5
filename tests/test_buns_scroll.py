import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_sauce_and_buns_scroll(driver, page_url):
    driver.get(page_url)

    # Проверяем наличие раздела конструктора бургеров
    constructor_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
    )
    assert (
        constructor_section.is_displayed()
    ), "Раздел конструктора бургеров отсутствует"

    # Нажимаем на кнопку "Соусы"
    sauce_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.SAUCE_TAB)
    )
    sauce_tab.click()
    time.sleep(2)  # Пауза для визуальной проверки

    # Проверяем, что произошел скролл до элемента "Соус Spicy-X"
    spicy_x_sauce = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.SPICY_X_SAUCE)
    )
    assert spicy_x_sauce.is_displayed(), "Скролл до раздела 'Соусы' не произошел"

    # Нажимаем на кнопку "Булки"
    buns_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.BUNS_TAB)
    )
    buns_tab.click()
    time.sleep(2)  # Пауза для визуальной проверки

    # Проверяем, что произошел скролл до элемента "Флюоресцентная булка R2-D3"
    r2d3_bun = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.R2D3_BUN)
    )
    assert r2d3_bun.is_displayed(), "Скролл до раздела 'Булки' не произошел"
