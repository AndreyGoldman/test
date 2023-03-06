from tests.pages.main_page import MainPage


class TestMainPage:

    def test_click_list_user(self, browser, api_reqres):
        # Данные
        main_page = MainPage(browser, api_reqres=api_reqres)
        # Тест
        main_page.open()

        main_page.click_on_list_user()

        main_page.should_be_status_code_200_and_valid_body_from_response_list_users(api_reqres, 2)

    def test_click_single_user(self, browser, api_reqres):
        # Данные
        main_page = MainPage(browser, api_reqres=api_reqres)
        # Тест
        main_page.open()

        main_page.click_on_single_user()

        main_page.should_be_status_code_200_and_valid_body_from_response_single_users(api_reqres, 2)

    def test_click_list_resource(self, browser, api_reqres):
        # Данные
        main_page = MainPage(browser, api_reqres=api_reqres)
        # Тест
        main_page.open()

        main_page.click_on_list_resource()

        main_page.should_be_status_code_200_and_valid_body_from_response_list_resource(api_reqres)

    def test_click_single_resource(self, browser, api_reqres):
        # Данные
        main_page = MainPage(browser, api_reqres=api_reqres)
        # Тест
        main_page.open()

        main_page.click_on_single_resource()

        main_page.should_be_status_code_200_and_valid_body_from_response_single_resource(api_reqres, 2)

    def test_click_delete_user(self, browser, api_reqres):
        # Данные
        main_page = MainPage(browser, api_reqres=api_reqres)
        # Тест
        main_page.open()

        main_page.click_on_delete_user()

        main_page.should_be_status_code_200_and_valid_body_from_response_delete_user()
