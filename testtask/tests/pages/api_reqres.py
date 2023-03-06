import json


class ApiReqres:

    def __init__(self, api_reqres):
        self.api_reqres = api_reqres

    def list_users(self, page):
        return self.api_reqres.get_request(f"api/users?page={page}")

    def single_users(self, user_id):
        return self.api_reqres.get_request(f"api/users/{user_id}")

    def list_resource(self):
        return self.api_reqres.get_request("api/unknown")

    def single_resource(self, resource_id):
        return self.api_reqres.get_request(f"api/unknown/{resource_id}")

    def create_users(self, name, job):
        return self.api_reqres.post_request("api/users", data=json.dumps({"name": name, "job": job}))

    def update_users_put(self, user_id):
        return self.api_reqres.put_request(f"api/users/{user_id}", data=json.dumps({"name": "morpheus", "job": "zion resident"}))

    def update_users_patch(self, user_id):
        return self.api_reqres.patch_request(f"api/users/{user_id}", data=json.dumps({"name": "morpheus", "job": "zion resident"}))

    def delete_user(self, user_id):
        return self.api_reqres.delete_request(f"api/users/{user_id}")

    def register_user(self, email, password):
        return self.api_reqres.post_request("api/register", data=json.dumps({"email": email, "password": password}), headers={'Content-Type': 'application/json'})

    def register_user_without_email(self, password):
        return self.api_reqres.post_request("api/register", data=json.dumps({"password": password}))

    def register_user_without_password(self, email):
        return self.api_reqres.post_request("api/register", data=json.dumps({"email": email}), headers={'Content-Type': 'application/json'})

    def login_user(self, email, password):
        return self.api_reqres.post_request("api/login", data=json.dumps({"email": email, "password": password}), headers={'Content-Type': 'application/json'})

    def login_user_without_password(self, email):
        return self.api_reqres.post_request("api/login", data=json.dumps({"email": email}), headers={'Content-Type': 'application/json'})

    def login_user_without_email(self, password):
        return self.api_reqres.post_request("api/login", data=json.dumps({"password": password}), headers={'Content-Type': 'application/json'})

    def delayed_response(self, delay):
        return self.api_reqres.get_request(f"api/users?delay={delay}")

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_list_users(list_users, body, page):
        assert list_users.status_code == 200
        if type(page) == int:
            assert body == page
        else:
            assert body == 1

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_with_existing_single_users(single_user, body, user_id):
        assert single_user.status_code == 200
        assert body == user_id

    @staticmethod
    def should_be_response_status_404_and_valid_body_from_request_with_non_existing_single_users(single_user):
        assert single_user.status_code == 404

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_with_existing_list_resource(list_resource, body):
        assert list_resource.status_code == 200
        assert body == 1

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_with_single_exist_resource(single_resource, body, resource_id):
        assert single_resource.status_code == 200
        assert body == resource_id

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_with_single_non_exist_resource(single_resource, body):
        assert single_resource.status_code == 404
        assert list(body) == []

    @staticmethod
    def should_be_response_status_201_and_valid_body_from_request_create_user_with_valid_data(create_user):
        assert create_user.status_code == 201

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_update_user(update_user):
        assert update_user.status_code == 200

    @staticmethod
    def should_be_response_status_204_and_valid_body_from_request_delete_user(delete_user):
        assert delete_user.status_code == 204

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_register_user(register_user):
        assert register_user.status_code == 200

    @staticmethod
    def should_be_response_status_400_and_valid_body_from_request_register_user_without_pass(register_user, body):
        assert register_user.status_code == 400
        assert body == 'Missing password'

    @staticmethod
    def should_be_response_status_400_and_valid_body_from_request_register_user_without_email(register_user, body):
        assert register_user.status_code == 400
        assert body == 'Missing email or username'

    @staticmethod
    def should_be_response_status_200_and_valid_body_from_request_login_user(login_user):
        assert login_user.status_code == 200

    @staticmethod
    def should_be_response_status_400_and_valid_body_from_request_login_user_without_pass(login_user, body):
        assert login_user.status_code == 400
        assert body == 'Missing password'

    @staticmethod
    def should_be_response_status_400_and_valid_body_from_request_login_user_without_email(register_user, body):
        assert register_user.status_code == 400
        assert body == 'Missing email or username'
