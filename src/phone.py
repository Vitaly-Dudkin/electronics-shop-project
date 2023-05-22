from src.item import *


class Phone:
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
        self.number_of_sim = number_of_sim
        self.name = name
        self.price = price
        self.quantity = quantity
        Phone.all.append(self)

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Phone) or isinstance(other, Item):
            return self.quantity + other.quantity
