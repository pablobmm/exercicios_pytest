import pytest

@pytest.fixture(params=[
    {"role": "admin", "access": True},
    {"role": "editor", "access": True},
    {"role": "guest", "access": False}
])
def user_data(request):
    return request.param

def test_access_control(user_data):
    role = user_data["role"]
    has_access = user_data["access"]
    
    if role == "guest":
        assert has_access is False
    else:
        assert has_access is True