import pytest
from el_shop_class.items_class import Phone


def test_init(phone_test):
    assert phone_test.name == "Смартфон"
    assert phone_test.price == 10000
    assert phone_test.quantity == 20
    assert phone_test.number_of_sim == 2
    with pytest.raises(ValueError):
        phone_test = Phone("Смартфон", 10000, 20, 0)


def test_number_of_sim(phone_test):
    phone_test.number_of_sim = 1
    assert phone_test.number_of_sim == 1
    with pytest.raises(ValueError):
        phone_test.number_of_sim = 0


def test_repr(phone_test):
    assert phone_test.__repr__() == 'Phone(Смартфон, 10000, 20, 2)'
