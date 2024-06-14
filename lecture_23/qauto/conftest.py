import pytest
import requests
from lecture_23.qauto.api import base_api_url, s


@pytest.fixture(scope='session')
def session():
    user_data = {
        "email": "yuri.gr.bond@gmail.com",
        "password": "E5YvjATAPb7@Uz4",
        "remember": False
    }

    return s.post(base_api_url + "/auth/signin", json=user_data)
