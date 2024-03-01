import pytest
from main import pergunta


def test_pergunta_int(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: 1)
    resp = pergunta("Digite um número int: ", int)
    assert isinstance(resp, int)


def test_pergunta_str(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "a")
    resp = pergunta("Digite uma str: ")
    assert isinstance(resp, str)


def test_pergunta_inválido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    resp = pergunta("Digite um número int: ", str)
    assert isinstance(resp, str)
