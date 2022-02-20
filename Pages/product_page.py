from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        price = self.get_price()
        item_name = self.get_item_name()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        self.solve_quiz_and_get_code()
        self.check_success_alert()
        self.check_basket_price()

    def get_item_name(self):
        return str(self.browser.find_element(*ProductPageLocators.ITEM_NAME).text)

    def get_price(self):
        return str(self.browser.find_element(*ProductPageLocators.PRICE).text)

    def check_success_alert(self):
        item_name = self.get_item_name()
        success_alert = str(self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text)
        expected_alert = item_name + " has been added to your basket."
        assert expected_alert == success_alert, "Error in success message"

    def check_basket_price(self):
        price = self.get_price()
        basket_price = str(self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text)
        assert basket_price == price, "Basket price differ from item price"
