import pytest

from el_shop_class.el_shop_class import Item


def test_atributes(test_class):
    """Тестируем атрибуты класса"""
    name, price, quantity = test_class
    item = Item(name, price, quantity)
    total_price = item.calculate_total_price()
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20
    assert total_price == 200000
    Item.pay_rate = 0.5
    item.apply_discount()
    total_price = item.calculate_total_price()
    assert item.price == 5000
    assert total_price == 100000


def test_instantiate_from_csv(instantiate_from_csv):
    """Тестируем работу с .csv файлом"""
    item_list, item = instantiate_from_csv
    assert len(item_list) == 5
    assert item.name == 'Кабель'


def test_is_integer():
    """Проверка можно ли считать значения которые вводятся int"""
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False


def test_name(test_class):
    """Проверка изменения имени экземпляра класса, а также случая если его длина более 10 символов"""
    name, price, quantity = test_class
    item = Item(name, price, quantity)
    item.name = "Ноутбук"
    assert item.name == "Ноутбук"
    with pytest.raises(Exception):
        item.name = "СуперНоутбук"

