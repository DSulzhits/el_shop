from el_shop_class.el_shop_class import Item
from el_shop_class.items_class import Phone, Keyboard


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
    # # print(item3.name)
    # # # item3.name = 'СуперСмартфон'
    # Item.instantiate_from_csv('test.csv')
    # print(len(Item.item_list))
    # item1 = Item.item_list[0]
    # print(item1.name, item1.price, item1.quantity)
    # # item2 = Item.item_list[2]
    # # print(item2.name, item2.price, item2.quantity)
    # # print(Item.is_integer(5))
    # # print(Item.is_integer(5.0))
    # # print(Item.is_integer(5.5))
    # item1 = Item("Смартфон", 10000, 20)
    # print(repr(item1))
    # print(item1)
    # phone1 = Phone("iPhone 14", 120_000, 10, 2)
    # item1 = Item("Asus_Ultrabook", 200_000, 15)
    # print(phone1)
    # print(phone1 + phone1)
    # print(item1 + item1)
    # print(item1 + phone1)
    # print(repr(phone1))

    # class Demo_class:
    #     pass
    #
    # demo = Demo_class
    # print(item1 + demo)
    # print(phone1 + demo)
    # print(repr(phone1))
    # phone1.number_of_sim = 0
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    print(kb)
    print(kb.language)
    kb.change_language()
    print(kb.language)
    kb.language = 'CH'


if __name__ == "__main__":
    main()
