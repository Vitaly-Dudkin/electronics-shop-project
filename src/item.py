from csv import DictReader
import os.path

PATH_TO_CVS_FILE = os.path.join(os.path.dirname(__file__), "items.csv")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            print('Длина наименования товара должна быть не больше 10 символов')
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        with open(PATH_TO_CVS_FILE, encoding='cp1251') as csv_file:
            data_cvs = DictReader(csv_file)

            for row in data_cvs:
                name, price, quantity = row.values()
                price = cls.string_to_number(price)
                quantity = cls.string_to_number(quantity)
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(str_number):
        if '.' in str_number:
            try:
                return float(str_number)
            except ValueError:
                return f'{str_number} невозможно превратить в число'
        else:
            try:
                return int(str_number)
            except ValueError:
                return f'{str_number} невозможно превратить в число'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
