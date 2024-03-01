from lib.strings import *
from lib.utils import *
import math


class Arco:
    def __init__(self, inscrito, central, arco):
        self.inscrito = inscrito
        self.central = central
        self.arco = arco

    @classmethod
    def inicia(cls):
        print("Digite x para descobrir")
        inscrito = pergunta("Inscrito: ")
        central = pergunta("Central: ")
        arco = pergunta("Arco: ")
        return cls(inscrito, central, arco)

    def transforma_rad_graus(self):
        # 180° -- [pi]rad
        #  x   --    y
        # x = 180y / [pi]
        print(" -- Ignore o π --")
        angulo_rad = pergunta("Qual é o angulo rad? ")
        angulo_graus = 180 * angulo_rad

    def calcula(self):
        ...
