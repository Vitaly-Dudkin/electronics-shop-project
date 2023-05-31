from src.item import Item


class LanguageMixin:
    _language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value.upper() == "EN" or value.upper() == "RU":
            self._language = value.upper()
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        self.language = "RU" if self.language == "EN" else "EN"
        return self


class KeyBoard(Item, LanguageMixin):

    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language


