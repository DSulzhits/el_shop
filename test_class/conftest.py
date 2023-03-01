import pytest
from el_shop_class.el_shop_class import Item
"""Необходимые для тестов фикстуры"""

@pytest.fixture
def test_class():
    name = "Смартфон"
    price = 10000
    quantity = 20
    return name, price, quantity

@pytest.fixture
def instantiate_from_csv():
    filename = 'test.csv'
    Item.instantiate_from_csv(filename)
    item1 = Item.item_list[3]
    return Item.instantiate_from_csv(filename), item1

