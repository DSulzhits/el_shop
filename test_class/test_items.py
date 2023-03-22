import pytest
from el_shop_class.items_class import Phone, Keyboard


def test_init_phone(phone_test):
    assert phone_test.name == "Смартфон"
    assert phone_test.price == 10000
    assert phone_test.quantity == 20
    assert phone_test.number_of_sim == 2
    with pytest.raises(ValueError):
        phone_test = Phone("Смартфон", 10000, 20, 0)


def test_number_of_sim_phone(phone_test):
    phone_test.number_of_sim = 1
    assert phone_test.number_of_sim == 1
    with pytest.raises(ValueError):
        phone_test.number_of_sim = 0


def test_init_keyboard(keyboard_test):
    assert keyboard_test.language == "EN"
    with pytest.raises(AttributeError):
        keyboard_test.language = "CH"


def test_change_language_keyboard(keyboard_test):
    keyboard_test.change_language()
    assert keyboard_test.language == "RU"
    keyboard_test.change_language()
    assert keyboard_test.language == "EN"
