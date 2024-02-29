from lib.utils import *


class Relogio:
    def __init__(self, hora, min):
        self.hora = hora
        self.min = min
        self.angulo_1 = 0
        self.angulo_2 = 0
        self.angulo_agudo = 0
        self.angulo_obtuso = 0

    @classmethod
    def inicia(cls):
        def separa_hora():
            # 00:00
            # 01234
            tempo = pergunta("Qual é a hora")
            hora = int(tempo[:2])
            min = int(tempo[:-3])
            return hora, min

        while True:
            print("Escreva a hora assim: 00:00")
            hora, min = separa_hora()
            if hora <= 24 and min <= 60:
                return cls(hora, min)
            else:
                errorMessage("Máximo de: 24h e 60min")

    def calcula(self):
        # Só funciona se os minutos forem divisíveis por 5
        pos_ponteiro_min = self.min / 5

        # Converte 24-h para 12-h
        if self.hora > 12:
            pos_ponteiro_hora = self.hora - 12
        else:
            pos_ponteiro_hora = self.hora

        # Calcula quantas partes existem entre os ponteiros
        # Essas partes são entre os números do relógio
        quantas_partes = pos_ponteiro_hora - pos_ponteiro_min

        # Os minutos "andam" e junto as horas também
        # É preciso calcular essa diferença
        hora, minuto = divmod(self.min, 60)
        variação_angulo_hora = (hora + minuto / 60) * 30

        self.angulo_1 = 30 * quantas_partes + variação_angulo_hora
        self.angulo_2 = 360 - self.angulo_1
        match [self.angulo_1 > 180, self.angulo_1 == 180]:
            case [True, False]:
                self.angulo_agudo = self.angulo_2
                self.angulo_obtuso = self.angulo_1
            case [False, False]:
                self.angulo_agudo = self.angulo_1
                self.angulo_obtuso = self.angulo_2
            case [_, True]:
                self.angulo_obtuso = 180
                self.angulo_agudo = 180
        """
        if self.angulo_1 > 180:
            self.angulo_agudo = self.angulo_2
            self.angulo_obtuso = self.angulo_1
        elif self.angulo_1 < 180:
            self.angulo_agudo = self.angulo_1
            self.angulo_obtuso = self.angulo_2
        else:
            self.angulo_agudo = 180
            self.angulo_obtuso = 180
        """

    def exibe(self):
        print(f"Hora = {self.hora}:{self.min}")
        print(f"Ângulo Agudo = {self.angulo_agudo}")
        print(f"Ângulo Obtuso = {self.angulo_obtuso}")
