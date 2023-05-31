from src.item import Item


class Phone(Item):
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим карт в магазине
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        Phone.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            return 'Данный ЭК можно сложить только с ЭК `Phone` или Item'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @ number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
