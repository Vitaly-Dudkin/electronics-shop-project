import pytest

from src.keyboard import KeyBoard


@pytest.fixture()
def kb():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_name(kb):
    assert str(kb) == "Dark Project KD87A"


def test_language(kb):
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_change_lang_twice(kb):
    # # Сделали EN -> RU -> EN
    kb.change_lang().change_lang()
    assert str(kb.language) == "EN"


def test_incorrect(kb):
    with pytest.raises(AttributeError):
        kb.language = 'CH'



