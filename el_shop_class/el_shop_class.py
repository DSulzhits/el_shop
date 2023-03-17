"""Импортируем необходимые модули"""
import csv


class Item:
    """Создаем класс с заданными атрибутами"""
    pay_rate = 1
    item_list = []

    def __init__(self, name: str, price: float, quantity: int):
        """Схема реализации экземпляров класса"""
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.item_list.append(self)

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> list:
        """Создаем метод класса для работы с .csv файлом"""
        csv_items = []
        with open(filename, encoding='UTF-8', newline='') as file:
            file_info = csv.DictReader(file)
            for info in file_info:
                csv_items.append(cls(info['name'], float(info['price']), int(info['quantity'])))
        return csv_items

    @staticmethod
    def is_integer(num) -> bool:
        """Метод для проверки вводимых значений"""
        if isinstance(num, int) or (isinstance(num, float)) and num % 1 == 0:
            return True
        else:
            return False

    @property
    def name(self):
        """Присвоение атрибута чтобы можно было работать с .__name т.к. данный атрибут private"""
        return self.__name

    @name.setter
    def name(self, name_inp: str) -> None:
        """Сеттер для записей атрибутов класса"""
        if len(name_inp) <= 10:
            self.__name = name_inp
        else:
            raise Exception("Наименование товара превышает 10 символов")

    def apply_discount(self):
        """Метод, который изменяет цену"""
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        """Метод расчета итоговой стоимости вида товара"""
        return self.price * self.quantity

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Только предметы класса Item или Phone')

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"
