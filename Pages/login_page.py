from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong login page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FILED).send_keys ("qwe123QWE!@#qwe")
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys ("qwe123QWE!@#qwe")
        submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        submit.click()
