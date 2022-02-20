from .base_page import BasePage
from .locators import BasePageLocators
from .locators import CartPageLocators


class BasketPage(BasePage):
    def go_to_cart_page(self):
        link = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        link.click()

    def check_basket_empty(self):
        assert not self.is_element_present(*CartPageLocators.BASKET_ITEMS), \
            "Items are present in a basket"

    def check_message_that_basket_empty(self):
        empty_message = str(self.browser.find_element(*CartPageLocators.MESSAGE_BASKET_EMPTY).text)
        assert "Your basket is empty" in empty_message, "Wrong empty basket message"
