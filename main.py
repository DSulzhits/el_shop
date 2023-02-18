from el_shop_class import el_shop_class


def main():
    item1 = el_shop_class.Item("Смартфон", 10000, 20)
    item2 = el_shop_class.Item("Ноутбук", 20000, 5)
    print(item1.calculate_total_price())
    print(item2.calculate_total_price())
    el_shop_class.Item.pay_rate = 0.8
    item1.apply_discount()
    print(item1.full_price())
    print(item2.full_price())
    print(el_shop_class.Item.item_list)


if __name__ == "__main__":
    main()
