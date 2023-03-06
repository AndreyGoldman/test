import time
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url="https://reqres.in", api_reqres=None):
        self.browser = browser
        self.url = url
        self.api_reqres = api_reqres

    main_page_url = "https://reqres.in"

    def open(self):
        self.browser.get(self.url)

    def reload(self):
        self.browser.refresh()

    def go_to_first_window(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def go_to_second_window(self):
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def get_element_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element

    def get_elements_text(self, how, what):
        elements = self.browser.find_elements(how, what)
        return [element.text for element in elements]

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
