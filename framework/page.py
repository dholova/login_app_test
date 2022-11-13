import time

from selenium.common.exceptions import NoSuchElementException
import selenium

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            raise e
        except NotImplementedError as e:
            raise e

    def click_element(self, *locator):
        try:
            return self.find_element(*locator).click()
        except NotImplementedError:
            raise NotImplementedError

    def input_element(self, text_, *locator):
        try:
            e = self.find_element(*locator)
            self.driver.implicitly_wait(10)
            e.clear()
            e.send_keys(text_)
        except NotImplementedError:
            raise NotImplementedError
