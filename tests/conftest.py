import pytest

@pytest.fixture(params=["", "Первая\nВторая", "   ", "Привет", "a\r\nb"])
def text_value(request):
    return request.param
