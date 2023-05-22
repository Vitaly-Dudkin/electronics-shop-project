import pytest

from src.phone import *


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone):
    assert str(phone) == "iPhone 14"


def test_add_phone(phone):
    assert phone + phone == 10


# def test_add_item_phone(phone):
#     item1 = Item("Смартфон", 10000, 20)
#     assert item1 + phone == 25

#
# def test_add_incorrect(phone):
#     assert phone + "wee" == 'Сложения ЭК `Phone` возможно только между собой или с ЭК `Item`'
