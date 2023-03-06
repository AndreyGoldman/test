from .base_page import BasePage
import json
from .api_reqres import ApiReqres
from .locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    def __init__(self, browser, api_reqres=None):
        super().__init__(browser, BasePage.main_page_url, api_reqres)

    def click_on_list_user(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_LIST_USERS)).click()

    def click_on_single_user(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_SINGLE_USERS)).click()

    def click_on_list_resource(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_LIST_RESOURCE)).click()

    def click_on_single_resource(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_SINGLE_RESOURCE)).click()

    def click_on_delete_user(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_DELETE_USERS)).click()

    def click_on_register_user(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_REGISTER_USERS)).click()

    def click_on_login_user(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_LOGIN_USERS)).click()

    def click_on_delayed_response(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*MainPageLocators.RESPONSE_200_STATUS))
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(MainPageLocators.SELECT_DELAYED_RESPONSE)).click()

    def should_be_status_code_200_and_valid_body_from_response_list_users(self, api_reqres, page):
        assert self.is_element_present(*MainPageLocators.RESPONSE_200_STATUS)
        assert self.is_element_present(*MainPageLocators.RESPONSE_BODY)
        api = ApiReqres(api_reqres)
        assert api.list_users(page).json() == json.loads(self.browser.find_element(*MainPageLocators.RESPONSE_BODY).get_attribute('outerText'))

    def should_be_status_code_200_and_valid_body_from_response_single_users(self, api_reqres, user_id):
        assert self.is_element_present(*MainPageLocators.RESPONSE_200_STATUS)
        assert self.is_element_present(*MainPageLocators.RESPONSE_BODY)
        api = ApiReqres(api_reqres)
        assert api.single_users(user_id).json() == json.loads(self.browser.find_element(*MainPageLocators.RESPONSE_BODY).get_attribute('outerText'))

    def should_be_status_code_200_and_valid_body_from_response_list_resource(self, api_reqres):
        assert self.is_element_present(*MainPageLocators.RESPONSE_200_STATUS)
        assert self.is_element_present(*MainPageLocators.RESPONSE_BODY)
        api = ApiReqres(api_reqres)
        assert api.list_resource().json() == json.loads(self.browser.find_element(*MainPageLocators.RESPONSE_BODY).get_attribute('outerText'))

    def should_be_status_code_200_and_valid_body_from_response_single_resource(self, api_reqres, resource_id):
        assert self.is_element_present(*MainPageLocators.RESPONSE_200_STATUS)
        assert self.is_element_present(*MainPageLocators.RESPONSE_BODY)
        api = ApiReqres(api_reqres)
        assert api.single_resource(resource_id).json() == json.loads(self.browser.find_element(*MainPageLocators.RESPONSE_BODY).get_attribute('outerText'))

    def should_be_status_code_200_and_valid_body_from_response_delete_user(self):
        assert self.is_element_present(*MainPageLocators.RESPONSE_200_STATUS)
        assert self.is_element_present(*MainPageLocators.RESPONSE_BODY)
