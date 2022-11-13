import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .page import Page


class LoginPage(Page):
    def login_page(self):
        btn = self.click_element(By.ID, 'com.ajaxsystems:id/login')

    def enter_email(self, mail):
        btn = self.input_element(mail, By.ID, 'com.ajaxsystems:id/login')

    def enter_password(self, password):
        btn = self.input_element(password, By.ID, 'com.ajaxsystems:id/password')

    def login_try(self, is_correct_data):
        btn = self.click_element(By.ID, 'com.ajaxsystems:id/next')
        time.sleep(7)
        try:
            self.find_element(By.ID, 'com.ajaxsystems:id/next')
            if is_correct_data:
                assert False, "No login after correct data entered"
        except NoSuchElementException:
            if not is_correct_data:
                assert False, "Login after incorrect data entered"

            self.cancel_button()

    def cancel_button(self):
        try:
            btn = self.click_element(By.ID, 'com.ajaxsystems:id/cancel_button')
            time.sleep(10)
        except NoSuchElementException:
            assert False, 'No view after login'





