from csv import DictReader
import os.path

PATH_TO_CVS_FILE = os.path.join(os.path.dirname(__file__), "items.csv")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
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
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('длина наименования товара должна быть не больше 10 симвовов')
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
        try:
            if any(i for i in str_number if i.isalpha()):
                return f'{str_number} не должно содержать буквы'
            if any(char in str_number for char in ',;<>@"#$%^&*()!=+/?'):
                return f'{str_number} не должно содержать символы'
            if str_number.count('.') == 1:
                return float(str_number)
            if str_number.isdigit:
                return int(str_number)
        except Exception:
            raise Exception()

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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return "Данный ЭК можно сложить только с ЭК `Phone`"
