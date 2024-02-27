class Relogio:

    def __init__(self, hora, min):
        self.hora = hora
        self.min = min
        self.angulo_obtuso = 0
        self.angulo_agudo = 0

    @classmethod
    def inicia(cls):
        hora = int(input("Hora: "))
        min = int(input("Minuto: "))
        return cls(hora, min)

    def calcula(self):
        pos_ponteiro_min, resto = divmod(self.min, 10) 
        print(pos_ponteiro_min)
        quantas_vezes = abs((self.hora - 12) - pos_ponteiro_min) 
        
        hora, minuto = divmod(self.min, 60)
        angulo_por_min = (hora + minuto / 60) * 30
        
        print(angulo_por_min)
        print(quantas_vezes)
        print(f"angulo_por_min = {angulo_por_min}")
        
        if self.hora == 0:
            angulo_por_hora = 0
        else:
            angulo_por_hora = 30 * quantas_vezes + angulo_por_min
        #print(f"partes_de_hora = {partes_de_hora}")
        #print(f"diferenca = {diferenca}")
        print(f"angulo_por_hora = {angulo_por_hora}")
        self.angulo_obtuso = angulo_por_hora + angulo_por_min
        self.angulo_agudo = 360 - self.angulo_obtuso
        print(f"angulo agudo: {self.angulo_agudo}")
        print(f"angulo obtuso: {self.angulo_obtuso}")

def main():
    relogio = Relogio.inicia()
    relogio.calcula()


if __name__ == "__main__":
    main()