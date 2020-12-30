from django import urls
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param', [
    'login',
    'logout',
    'register'
])
def test_rendering_pages(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200  # Success


# @pytest.mark.django_db
# def test_user_signup(client, user_data):
#     user_model = get_user_model()
#     assert user_model.objects.count() == 0
#     signup_url = urls.reverse('login')
#     resp = client.post(signup_url, user_data)
#     assert user_model.objects.count() == 1

