from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '[href*="basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button[class*="btn-add-to-basket"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_NAME = (By.CSS_SELECTOR, '.alert-success strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_NOW = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner>p')