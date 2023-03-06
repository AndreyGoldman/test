from .pages.api_reqres import ApiReqres
import pytest


class TestApi:
    @pytest.mark.parametrize('page', [2, "test"])
    def test_list_users_with_valid_parameters_page(self, api_reqres, page):
        # Данные
        api = ApiReqres(api_reqres)
        # Тест
        list_users = api.list_users(page)

        page_number = api.list_users(page).json()["page"]

        api.should_be_response_status_200_and_valid_body_from_request_list_users(list_users, page_number, page)

    @pytest.mark.parametrize('user_id', [4, 8766])
    def test_single_user_with_exist_user_id(self, api_reqres, user_id):
        # Данные
        api = ApiReqres(api_reqres)
        # Тест
        single_user = api.single_users(user_id)
        user_id_from_response = None
        if user_id == 4:
            user_id_from_response = api.single_users(user_id).json()["data"]["id"]

        if user_id == 4:
            api.should_be_response_status_200_and_valid_body_from_request_with_existing_single_users(single_user, user_id_from_response, user_id)
        else:
            api.should_be_response_status_404_and_valid_body_from_request_with_non_existing_single_users(single_user)

    def test_list_resource(self, api_reqres):
        # Данные
        api = ApiReqres(api_reqres)
        # Тест
        list_source = api.list_resource()

        page_number = api.list_resource().json()["page"]

        api.should_be_response_status_200_and_valid_body_from_request_with_existing_list_resource(list_source, page_number)

    @pytest.mark.parametrize('resource_id', [3, 9876])
    def test_single_exist_resource(self, api_reqres, resource_id):
        # Данные
        api = ApiReqres(api_reqres)
        # Тест
        single_resource = api.single_resource(resource_id)
        id_resource_from_response = None
        response = None

        if resource_id == 3:
            id_resource_from_response = api.single_resource(resource_id).json()["data"]["id"]
        else:
            response = api.single_resource(resource_id).json()

        if resource_id == 3:
            api.should_be_response_status_200_and_valid_body_from_request_with_single_exist_resource(single_resource, id_resource_from_response, resource_id)
        else:
            api.should_be_response_status_200_and_valid_body_from_request_with_single_non_exist_resource(single_resource, response)

    def test_create_user_with_valid_data(self, api_reqres):
        # Данные
        name = "test"
        job = "qa"
        api = ApiReqres(api_reqres)
        # Тест
        create_user = api.create_users(name, job)

        api.should_be_response_status_201_and_valid_body_from_request_create_user_with_valid_data(create_user)

    @pytest.mark.parametrize('method', ["put", "patch"])
    def test_update_with_put_method_user(self, api_reqres, method):
        # Данные
        user_id = 3
        api = ApiReqres(api_reqres)
        # Тест
        if method == "put":
            update_user = api.update_users_put(user_id)
        else:
            update_user = api.update_users_put(user_id)

        api.should_be_response_status_200_and_valid_body_from_request_update_user(update_user)

    def test_delete_exist_user(self, api_reqres):
        # Данные
        user_id = 4
        api = ApiReqres(api_reqres)
        # Тест
        delete_user = api.delete_user(user_id)

        api.should_be_response_status_204_and_valid_body_from_request_delete_user(delete_user)

    def test_register_with_valid_data(self, api_reqres):
        # Данные
        email = "eve.holt@reqres.in"
        password = "pistol"
        api = ApiReqres(api_reqres)
        # Тест
        register_user = api.register_user(email, password)

        api.should_be_response_status_200_and_valid_body_from_request_register_user(register_user)

    def test_register_without_email(self, api_reqres):
        # Данные
        password = "email@example.com"
        api = ApiReqres(api_reqres)
        # Тест
        register_user = api.register_user_without_email(password)

        error_message = api.register_user_without_email(password).json()["error"]

        api.should_be_response_status_400_and_valid_body_from_request_register_user_without_email(register_user, error_message)

    def test_register_without_password(self, api_reqres):
        # Данные
        email = "ivan"
        api = ApiReqres(api_reqres)
        # Тест
        register_user = api.register_user_without_password(email)

        error_message = api.register_user_without_password(email).json()["error"]

        api.should_be_response_status_400_and_valid_body_from_request_register_user_without_pass(register_user, error_message)

    def test_login_with_valid_data(self, api_reqres):
        # Данные
        email = "eve.holt@reqres.in"
        password = "pistol"
        api = ApiReqres(api_reqres)
        # Тест
        login_user = api.login_user(email, password)

        api.should_be_response_status_200_and_valid_body_from_request_login_user(login_user)

    def test_login_without_email(self, api_reqres):
        # Данные
        password = "email@example.com"
        api = ApiReqres(api_reqres)
        # Тест
        login_user = api.login_user_without_email(password)

        error_message = api.login_user_without_email(password).json()["error"]

        api.should_be_response_status_400_and_valid_body_from_request_login_user_without_email(login_user, error_message)

    def test_login_without_password(self, api_reqres):
        # Данные
        email = "ivan"
        api = ApiReqres(api_reqres)
        # Тест
        login_user = api.login_user_without_password(email)

        error_message = api.login_user_without_password(email).json()["error"]

        api.should_be_response_status_400_and_valid_body_from_request_login_user_without_pass(login_user, error_message)
