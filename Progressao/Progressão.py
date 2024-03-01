from lib.utils import *
from lib.strings import *


class Progressao:

    def __init__(self, termo: float, razao: float):
        self.termo = termo
        self.razao = razao
        self.progressao = [self.termo]
        self.formula = ""

    @classmethod
    def novo(cls):
        termo = pergunta("Qual é o termo", float)
        razao = pergunta("Qual é a razão", float)
        return cls(termo, razao)

    def cria(self, maximo=100, round_num=2):
        num = self.termo
        for _ in range(maximo):
            num += self.razao
            self.progressao.append(round(num, round_num))

    def update(self):
        self.cria()
        self.descobre_formula()

    def exibe(self, por_linha=10, sep="_", color={"color": "None", "style": "Dark"}):
        # TODO se "self.termo" = x e "self.razao" = 0
        # Exibir: x _ x _ ... Ou algo assim
        largura_max = len(str(self.progressao[-1]))
        c = 0
        for _, num in enumerate(self.progressao):
            print(str(num).rjust(largura_max), end="")
            c += 1
            if c == por_linha:
                print()
                c = 0
            else:
                print(
                    f" {colors(sep, color['color'], style=color['style'])} ", end="")
        print()

    def descobre_elemento(self):
        elemento = pergunta("Qual elemento quer descobrir", float)
        an = self.termo + (elemento - 1) * self.razao

        print(f"O {elemento}º elemento da PA é: {colors(an, style='Bold')}")

    def descobre_formula(self, simbolo="n"):
        termo_sub_razao = self.termo - self.razao
        if termo_sub_razao < 0:
            termo_sub_razao_str = f"- {-termo_sub_razao}"
        elif termo_sub_razao > 0:
            termo_sub_razao_str = f"+ {termo_sub_razao}"
        else:
            termo_sub_razao_str = f""

        if self.razao == 0:
            razao_str = ""
        else:
            razao_str = self.razao
        self.formula = f"{razao_str}{simbolo} {termo_sub_razao_str}"

    def title(self):
        def se_não_existir_faça(op_1, op_2="None", type=str, end="\n", color={"color": "None", "style": "Dark"}):
            if type == str:
                type_mode = ""
            elif type == int or type == float:
                type_mode = 0
            else:
                type_mode = None

            if op_1 == type_mode:
                print(
                    f" {colors(str(op_2), color['color'], style=color['style'])}", end="")
            else:
                print(f" {op_1}", end="")
            print(end=end)

        showText(colors("Progressão Aritmética", "Blue"))
        print(colors("PA:", "Red").rjust(15), end="")
        se_não_existir_faça(self.formula, "None", str)

        print(f"1º Termo =", end="")
        se_não_existir_faça(self.termo, "0", int, end=" : ")

        print("Razão =", end="")
        se_não_existir_faça(self.razao, "0", float)
        lineDark()

    def menu(self):
        self.title()
        for op, mensa in MENU.items():
            centro(f"{op}", end="", length=15)
            print(mensa)
        lineDark()
        opção = pergunta("Qual opção", str).upper()
        if opção in [k for k in MENU.keys()]:
            return opção
        return None
