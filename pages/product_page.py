import math
from .locators import ProductPageLocators
from selenium.common import NoAlertPresentException, NoSuchElementException

from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "There's no <add to basket> button"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()

    def calculate_value(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_for_product_added(self):
        self.get_product_name_compare()
        self.get_product_price_compare()

    def get_product_name_compare(self):
        product_name_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        # product_name_in_page = ' '.join(product_name_in_page.split()[0:2])
        assert product_name_in_page == product_name_in_message, \
            f"Products names are not similar: in page: {product_name_in_page}, in message {product_name_in_message}"

    def get_product_price_compare(self):
        pass