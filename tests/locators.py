from selenium.webdriver.common.by import By


class Locators:
    # Локатор для кнопки перехода в личный кабинет
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX[href='/account']")

    # Локатор для кнопки "Зарегистрироваться"
    REGISTER_BUTTON = \
        (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and @href='/register' and text()='Зарегистрироваться']")

    # Локатор для поля "Имя"
    NAME_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")

    # Локатор для поля "Email"
    EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name' and @value='']")

    # Локатор для поля "Пароль"
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']")

    # Локатор для кнопки "Зарегистрироваться"
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']")

    # Локатор для поля "Email" в окне входа
    LOGIN_EMAIL_FIELD = (By.XPATH,
                         "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']")
    # Локатор для поля "Пароль" в окне входа
    LOGIN_PASSWORD_FIELD = (By.XPATH,
                            "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']")
    # Локатор для кнопки "Войти" в окне входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH,
                           "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']")

    # Локатор для сообщения об ошибке "Пользователь уже существует"
    ERROR_MESSAGE_USER_EXISTS = (
        By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Такой пользователь уже существует']")

    # Локатор для сообщения об ошибке "Некорректный пароль"
    ERROR_MESSAGE_INVALID_PASSWORD = (
        By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    # Локатор для кнопки "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")

    # Локатор для кнопки "Войти в аккаунт"
    LOGIN_ACCOUNT_BUTTON = (By.XPATH,
                            "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']")

    LOGIN_FROM_REGISTER_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']")

    FORGOT_PASSWORD_LINK = (
        By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']")

    # Локатор для ссылки "Конструктор"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")

    # Локатор для логотипа
    LOGO_LINK = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a[href='/']")

    # Локатор для кнопки "Выход"
    LOGOUT_BUTTON = (By.XPATH,
                     "//li[@class='Account_listItem__35dAP']//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")

    # Локатор для раздела конструктора бургеров
    CONSTRUCTOR_SECTION = (By.CSS_SELECTOR, "section.BurgerIngredients_ingredients__1N8v2")

    # Локаторы для вкладок
    SAUCE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]")
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]")

    # Локаторы для ингредиентов
    SPICY_X_SAUCE = (By.XPATH, "//p[contains(., 'Соус Spicy-X')]")
    PROTOSTOMIA_MEAT = (By.XPATH, "//p[contains(., 'Мясо бессмертных моллюсков Protostomia')]")
    R2D3_BUN = (By.XPATH, "//p[contains(., 'Флюоресцентная булка R2-D3')]")
