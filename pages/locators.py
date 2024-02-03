from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".login_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > h1 + p")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages> .alert:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".navbar-inverse > div >a")