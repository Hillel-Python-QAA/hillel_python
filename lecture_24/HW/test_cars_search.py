import logging

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

# Logger set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# File handler set up
file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
# Console handler set up
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
# Adding handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def auth_headers() -> dict:
    response = requests.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    yield {"Authorization": "Bearer {}".format(response.json()["access_token"])}


@pytest.fixture(scope="session")
def session() -> requests.Session:
    session = requests.Session()
    response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    session.headers.update({"Authorization": "Bearer {}".format(response.json()["access_token"])})
    yield session


def test_get_cars_search_auth_headers(auth_headers):
    response = requests.get(f"{BASE_URL}/cars", headers=auth_headers)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("brand", 5),
        ("price", 0),
        ("year", -1),
        ("engine_volume", 1),
        ("price", 24),
        ("price", 25),
        ("price", -25),
        ("price", 26),
        (None, None),
        ("model", 2),
        (0,0)
    ]
)
def test_get_cars_search_session(session, sort_by, limit):
    params = {
        'sort_by': sort_by,
        'limit': limit
    }
    logger.info(f"Testing API /Cars search with parameters: 'sort_by'='{sort_by}', 'limit'={limit}")

    response = session.get(f"{BASE_URL}/cars", params=params)

    logger.debug(f"Status_code: {response.status_code}")
    logger.debug(f"Content: {response.json()}")

    assert response.status_code == 200
    if limit is None:
        assert len(response.json()) == 25
    elif limit < 0:
        assert len(response.json()) == 25 + limit
    else:
        assert len(response.json()) <= limit


