import pytest

from el_shop_class.el_shop_class import Item


def test_init(class_test):
    """Тестируем атрибуты класса"""
    assert class_test.name == "Смартфон"
    assert class_test.price == 10000
    assert class_test.quantity == 20


def test_instantiate_from_csv(instantiate_from_csv):
    """Тестируем работу с .csv файлом"""
    assert (len(instantiate_from_csv)) == 5
    assert instantiate_from_csv[4].name == 'Клавиатура'
    assert Item.instantiate_from_csv('123.csv') == 'Отсутствует файл items.csv'
    assert Item.instantiate_from_csv('test_corrupted.csv') == 'Файл item.csv поврежден'


def test_calculate_total_price(class_test):
    """Тест для метода calculate_total_price"""
    assert class_test.calculate_total_price() == 200000


def test_apply_discount(class_test):
    """Тест для метода apply_discount"""
    class_test.pay_rate = 0.5
    class_test.apply_discount()
    assert class_test.price == 5000
    assert class_test.calculate_total_price() == 100000


def test_is_integer():
    """Проверка можно ли считать значения которые вводятся int"""
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_name(class_test):
    """Проверка изменения имени экземпляра класса, а также случая если его длина более 10 символов"""

    class_test.name = "Ноутбук"
    assert class_test.name == "Ноутбук"
    with pytest.raises(Exception):
        class_test.name = "СуперНоутбук"


def test_add(class_test):
    """Тест для метода add"""
    class Demo_class:
        pass

    assert class_test + class_test == 40
    demo = Demo_class
    with pytest.raises(ValueError):
        class_test + demo


def test_repr(class_test):
    """Тест для метода __repr__"""
    assert class_test.__repr__() == 'Item(Смартфон, 10000, 20)'


def test_str(class_test):
    """Тест для метода __str__"""
    assert class_test.__str__() == 'Смартфон'
