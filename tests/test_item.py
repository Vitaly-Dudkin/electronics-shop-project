"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


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
