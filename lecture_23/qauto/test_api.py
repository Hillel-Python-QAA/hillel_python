from lecture_23.qauto.api import API, s
import pytest


def test_signin_positive():
    user_data = {
        "email": "yuri.gr.bond@gmail.com",
        "password": "E5YvjATAPb7@Uz4",
        "remember": False
    }

    response = API.auth.signin(s, user_data)
    response_json = response.json()
    assert response.status_code == 200, "Wrong status code"
    assert response_json["status"] == "ok", "Key 'status' is not ok"


def test_get_current_user_cars(session):
    response = API.cars.cars_get(s)
    response_json = response.json()
    assert response.status_code == 200, "Wrong status code"
    assert response_json["status"] == "ok", "Key 'status' is not ok"
    assert response_json["data"].__len__() == 2
