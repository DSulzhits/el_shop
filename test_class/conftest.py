import pytest


@pytest.fixture
def test_class():
    name = "Смартфон"
    price = 10000
    quantity = 20
    return name, price, quantity
