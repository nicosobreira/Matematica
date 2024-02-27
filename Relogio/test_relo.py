import pytest
from relo import *


def test_relo_hora_agudo():
    relogio = Relogio(18, 0)
    relogio.calcula()
    assert relogio.angulo_agudo == 180


def test_relo_hora_obtuso():
    relogio = Relogio(18, 0)
    relogio.calcula()
    assert relogio.angulo_obtuso == 270


def test_relo_hora_min_agudo():
    relogio = Relogio(18, 15)
    relogio.calcula()
    assert relogio.angulo_agudo == 97.5


def test_relo_hora_min_obtuso():
    relogio = Relogio(18, 15)
    relogio.calcula()
    assert relogio.angulo_agudo == 262.5