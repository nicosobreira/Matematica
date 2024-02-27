import pytest
from main import *


def test_relo_hora_agudo():
    relogio = Relogio(18, 0)
    relogio.calcula()
    assert relogio.angulo_1 == 180


def test_relo_hora_obtuso():
    relogio = Relogio(18, 0)
    relogio.calcula()
    assert relogio.angulo_2 == 180


def test_relo_hora_min_agudo():
    relogio = Relogio(18, 15)
    relogio.calcula()
    assert relogio.angulo_1 == 97.5


def test_relo_hora_min_obtuso():
    relogio = Relogio(18, 15)
    relogio.calcula()
    assert relogio.angulo_2 == 262.5