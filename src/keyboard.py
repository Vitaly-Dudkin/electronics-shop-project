from src.item import Item


class LanguageMixin:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    # @language.setter
    # def language(self, value):
    #     if value in ('EN', 'RU'):
    #         self.__language = value
    #     else:
    #         raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self


class KeyBoard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language
