import pytest

@pytest.fixture
def user_data():
    return {'email': 'user_email', 'name': 'user_name', 'password': 'pass'}