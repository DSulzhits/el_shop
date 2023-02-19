from el_shop_class import el_shop_class


def test_atributes(test_class):
    name, price, quantity = test_class
    item = el_shop_class.Item(name, price, quantity)
    full_price = item.full_price()
    total_price = item.calculate_total_price()
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20
    assert full_price == 10000
    assert total_price == 200000
    el_shop_class.Item.pay_rate = 0.5
    item.apply_discount()
    total_price = item.calculate_total_price()
    assert item.price == 5000
    assert total_price == 100000

