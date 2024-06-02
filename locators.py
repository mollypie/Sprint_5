#
# Регистрация / Авторизация
#
REGISTRATION_NAME = './/label[text()="Имя"]/parent::div/input' # поле ввода имени
REGISTRATION_EMAIL = './/label[text()="Email"]/parent::div/input' # поле ввода email
REGISTRATION_PASSWORD = './/input[@type="password" and @name="Пароль"]' # поле ввода пароля

REGISTRATION_BUTTON = './/button[text()="Зарегистрироваться"]' # кнопка "Зарегистрироваться"

LOGIN_BUTTON = './/button[text()="Войти"]' # кнопка "Войти"

LINK_REDIRECT_TO_LOGIN = './/a[@href="/login"]' # ссылка редиректа на страницу авторизации
PASSWORD_TEXT_ERROR = 'input__error.text_type_main-default' # ошибка под полем ввода пароля
#
# Главная
#
MAIN_HEADER = 'text.text_type_main-large.mb-5.mt-10' # заголовок на главной странице

MAIN_REDIRECT_TO_LOGIN = './/button[text()="Войти в аккаунт"]' # кнопка редиректа на страницу авторизации из главной

MAIN_SECTION_BUNS = './/span[text()="Булки"]' # секция выбора булочек
MAIN_SECTION_SAUCES = './/span[text()="Соусы"]' # секция выбора соусов
MAIN_SECTION_TOPPINGS = './/span[text()="Начинки"]' # секция выбора начинок
MAIN_SELECTED_ELEMENT = './/div[contains(@class, "tab_type_current")]' # выбранный элемент бургера
#
# Личный кабинет
#
ACCOUNT_LINK_TO_PROFILE = './/a[@href="/account/profile"]' # ссылка перехода в профиль пользователя
ACCOUNT_BUTTON_EXIT = './/button[text()="Выход"]' # кнопка "Выход"
#
# Шапка
#
HEADER_LINK_TO_ACCOUNT = './/a[@href="/account"]' # ссылка перехода в личный кабинет или на страницу авторизации
HEADER_LINK_TO_CONSTRUCTOR = ('.//a[starts-with(@class, "AppHeader_header__link") '
                              'and @href="/"]') # ссылка для перехода в конструктор
HEADER_LOGO_LINK = './/div[starts-with(@class, "AppHeader_header__logo")]/a' # ссылка-лого для перехода в конструктор
