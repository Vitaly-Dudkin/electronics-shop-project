import pytest

from src.exception_class import InstantiateCSVError


@pytest.fixture
def exception_class():
    return InstantiateCSVError()


def test_exception_str(exception_class):
    assert str(exception_class) == "Файл item.csv поврежден"
