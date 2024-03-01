import pytest
from main import Progressao


def test_cria_positivo_int():
    progressao = Progressao(5, 3)
    progressao.cria(4)
    assert progressao.progressao == [5, 8, 11, 14, 17]


def test_cria_negativo_int():
    progressao = Progressao(-4, -2)
    progressao.cria(4)
    assert progressao.progressao == [-4, -6, -8, -10, -12]


def test_cria_constant_int():
    progressao = Progressao(3, 0)
    progressao.cria(4)
    assert progressao.progressao == [3, 3, 3, 3, 3]


def test_cria_positivo_float():
    progressao = Progressao(5.5, 3.2)
    progressao.cria(4)
    assert progressao.progressao == [5.5, 8.7, 11.9, 15.1, 18.3]


def test_cria_negativo_float():
    progressao = Progressao(-4.7, -2.1)
    progressao.cria(4)
    assert progressao.progressao == [-4.7, -6.8, -8.9, -11.0, -13.1]


def test_cria_constant_float():
    progressao = Progressao(3.3, 0)
    progressao.cria(4)
    assert progressao.progressao == [3.3, 3.3, 3.3, 3.3, 3.3]