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


def test_add_incorrect(phone):
    assert phone + "wee" == "Данный ЭК можно сложить только с ЭК `Phone` или Item"


def test_get_number_of_sim(phone):
    assert phone.number_of_sim == 2


def test_set_number_of_sim(phone):
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5


def test_set_number_of_sim_incorrect(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    with pytest.raises(ValueError):
        phone.number_of_sim = 1.5
    with pytest.raises(ValueError):
        phone.number_of_sim = -1