import pytest
from el_shop_class.el_shop_class import Item
from el_shop_class.items_class import Phone, Keyboard

"""Необходимые для тестов фикстуры"""


@pytest.fixture
def class_test():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone_test():
    return Phone("Смартфон", 10000, 20, 2)


@pytest.fixture
def keyboard_test():
    return Keyboard('Dark Project KD87A', 9600, 5)


@pytest.fixture
def instantiate_from_csv():
    return Item.instantiate_from_csv('test.csv')
