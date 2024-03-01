import pytest
from Relogio import *


def test_hora_ang_1():
    relogio = Relogio(18, 0)
    relogio.calcula()
    assert relogio.angulo_agudo == 180


def test_hora_ang_2():
    relogio = Relogio(18, 0)
    relogio.calcula()
    assert relogio.angulo_obtuso == 180


def test_hora_min_ang_1():
    relogio = Relogio(18, 15)
    relogio.calcula()
    assert relogio.angulo_agudo == 97.5


def test_hora_min_ang_2():
    relogio = Relogio(18, 15)
    relogio.calcula()
    assert relogio.angulo_obtuso == 262.5


def test_hora_min_24_ang_1():
    relogio = Relogio(22, 20)
    relogio.calcula()
    assert relogio.angulo_agudo == 170


def test_hora_min_24_ang_2():
    relogio = Relogio(22, 20)
    relogio.calcula()
    assert relogio.angulo_obtuso == 190


def test_hora_min_12_ang_1():
    relogio = Relogio(10, 20)
    relogio.calcula()
    assert relogio.angulo_agudo == 170


def test_hora_min_12_ang_2():
    relogio = Relogio(10, 20)
    relogio.calcula()
    assert relogio.angulo_obtuso == 190
