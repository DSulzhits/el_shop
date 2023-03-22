from el_shop_class.el_shop_class import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_inp):
        if sim_inp > 0:
            self.__number_of_sim = sim_inp
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"Phone({self.name}, {self.price}, {self.quantity}, {self.number_of_sim})"
