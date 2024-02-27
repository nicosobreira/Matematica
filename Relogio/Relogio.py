class Relogio:

    def __init__(self, hora, min):
        self.hora = hora
        self.min = min
        self.angulo_2 = 0
        self.angulo_1 = 0
        self.angulo_agudo = 0
        self.angulo_obtuso = 0

    @classmethod
    def inicia(cls):
        hora = int(input("Hora: "))
        min = int(input("Minuto: "))
        return cls(hora, min)

    def calcula(self):
        pos_ponteiro_min, _ = divmod(self.min, 5)
        if self.hora > 12:
            pos_ponteiro_hora = self.hora - 12
        else:
            pos_ponteiro_hora = self.hora
        quantas_partes = abs((pos_ponteiro_hora - pos_ponteiro_min))

        hora, minuto = divmod(self.min, 60)
        variação_angulo_hora = (hora + minuto / 60) * 30

        self.angulo_1 = 30 * quantas_partes + variação_angulo_hora
        self.angulo_2 = 360 - self.angulo_1

    def exibe(self):
        if self.angulo_1 > 180:
            self.angulo_agudo = self.angulo_2
            self.angulo_obtuso = self.angulo_1
        elif self.angulo_1 < 180:
            self.angulo_agudo = self.angulo_1
            self.angulo_obtuso = self.angulo_2
        else:
            self.angulo_obtuso = 180

        print(f"Hora: {self.hora}:{self.min}")
        print(f"Ângulo Agudo: {self.angulo_agudo}")
        print(f"Ângulo Obtuso: {self.angulo_obtuso}")
