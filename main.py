from el_shop_class.el_shop_class import Item


def main():
    # item1 = Item("Смартфон", 10000, 20)
    # item2 = Item("Ноутбук", 20000, 5)
    # print(item1.calculate_total_price())
    # print(item2.calculate_total_price())
    # Item.pay_rate = 0.8
    # item1.apply_discount()
    # print(item1.price)
    # print(item2.price)
    # print(Item.item_list)

    # item3 = Item('Телефон', 10000, 5)
    # print(item3.name)
    # item3.name = 'Смартфон'
    # print(item3.name)
    # # item3.name = 'СуперСмартфон'
    Item.instantiate_from_csv('items.csv')
    print(len(Item.item_list))
    item1 = Item.item_list[0]
    print(item1.name, item1.price, item1.quantity)
    item2 = Item.item_list[2]
    print(item2.name, item2.price, item2.quantity)
    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))



if __name__ == "__main__":
    main()
