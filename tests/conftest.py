import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    # Настраиваем WebDriver с использованием webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def page_url():
    return "https://stellarburgers.nomoreparties.site/"


@pytest.fixture(scope="module")
def register_url():
    return "https://stellarburgers.nomoreparties.site/register"


@pytest.fixture(scope="module")
def login_url():
    return "https://stellarburgers.nomoreparties.site/login"
