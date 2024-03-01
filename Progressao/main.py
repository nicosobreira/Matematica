from Progressão import *

# TODO a[n] = a[1] + (n - 1) * r
# Com 3 valores da fórmula é possível descobrir o 4º
# Implementar um método para fazer isso

# TODO formatar números float


def main():
    progressao = Progressao.novo()
    progressao.update()
    # TODO Melhorar o processo de criação de uma nova progressão
    # Quando se cria um "novo" tem que usar o "update",
    # TALVEZ seja melhor assim
    while True:
        clear()
        escolha = progressao.menu()
        match escolha:
            case "N":
                progressao = progressao.novo()
                progressao.update()
            case "E":
                progressao.exibe()
                sair()
            case "D":
                progressao.descobre_elemento()
                sair()
            case "S":
                print("Volte Sempre!")
                break
            case _:
                errorMessage("Escolha uma resposta válida")
                sair()


if __name__ == "__main__":
    main()
