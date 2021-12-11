import pytest
from trojkat import trojkat


def test_trojkat_egipski_1():
    expected = 50
    result = trojkat(30, 40)
    assert expected == result


def test_trojkat_egipski_2():
    expected = 5
    result = trojkat(3, 4)
    assert expected == result


def test_trojkat_blad():
    with pytest.raises(TypeError):
        trojkat(3, 'string')
