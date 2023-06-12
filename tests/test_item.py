"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.phone import *


@pytest.fixture
def item():
    return Item("Test Item", 10.0, 5)


def test_init(item):
    assert item.name == "Test Item"
    assert item.price == 10.0
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_reset_discount(item):
    Item.pay_rate = 1.0
    assert Item.pay_rate == 1.0


def test_name_setter_incorrect(item):
    with pytest.raises(Exception):
        item.name = "FULLHDTV_stopwatchingtv"


def test_name_setter_correct(item):
    item.name = 'PS4'
    assert item.name == 'PS4'


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[3].price == 50.0
    assert Item.all[4].quantity == 5


def test_instantiate_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('file_not_exist')


def test_str_number_int_float(item):
    assert item.string_to_number('9') == 9
    assert item.string_to_number('9.0') == 9.0


def test_str_number(item):
    assert item.string_to_number('12.3e') == '12.3e не должно содержать буквы'
    assert item.string_to_number('12,3') == '12,3 не должно содержать символы'
    assert item.string_to_number('12.3') == 12.3
    assert item.string_to_number('12') == 12


def test_str_number_exception(item):
    with pytest.raises(Exception):
        item.string_to_number('12.]')


def test_repr(item):
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add(item):
    phone = Phone('IPhone', 12000, 5, 2)
    assert item + phone == 10


def test_add_incorrect(item):
    assert item + 5 == 'Данный ЭК можно сложить только с ЭК `Phone`'
