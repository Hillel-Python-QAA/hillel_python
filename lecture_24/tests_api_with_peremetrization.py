import pytest
import requests


# Фабрика для створення об'єктів "користувач"
class UsersFactory:
    @staticmethod
    def create_user(name, email):
        return {"name": name, "email": email}


# URL для REST API
BASE_URL = "http://127.0.0.1:7070/users"


# Тести для REST API з використанням фабрики та параметризації
@pytest.fixture
def api_url(request):
    return BASE_URL + request.param


@pytest.mark.parametrize("api_url", ["/1", "/2"], indirect=True)
def test_get_user(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200
    user_data = response.json()
    assert "name" in user_data
    assert "email" in user_data


@pytest.mark.parametrize("api_url", ["/create"], indirect=True)
def test_create_user(api_url):
    user_data = UsersFactory.create_user("John Doe", "john.doe@example.com")
    response = requests.post(api_url, json=user_data)
    assert response.status_code == 201
    user_id = response.json()["id"]
    assert user_id is not None


@pytest.mark.parametrize("api_url", ["/delete/1", "/delete/2"], indirect=True)
def test_delete_user(api_url):
    response = requests.delete(api_url)
    assert response.status_code == 204
