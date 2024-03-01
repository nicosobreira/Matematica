def cria_pa(termo=0, razao=0, repetir=100):
    numeros = [termo]
    for _ in range(0, repetir):
        termo += razao
        numeros.append(termo)
    return numeros


def exibe_pa(numeros=[], por_linha=5):
    largura_max = len(str(numeros[-1]))
    c = 0
    for count in range(0, len(numeros)):
        str_num = str(numeros[count])
        print(str_num.rjust(largura_max), end="")
        c += 1
        if c == por_linha:
            print()
            c = 0
        else:
            print(" - ", end="")
    print()


def descobre_termo(numeros=[], razao=0, elemento=1):
    termo_1 = numeros[0]
    an = termo_1 + (elemento - 1) * razao
    print(f"A fórmula da PA é: {razao}n + {termo_1 - razao}")
    print(f"O {elemento}º elemento da PA é: {an}")


def decisao(pergunta=""):
    resposta = input(f"{pergunta}? [S/N] ").upper()
    match resposta:
        case "S":
            return True
        case "N":
            return False


def main():
    termo = int(input("Qual termo? "))
    razao = int(input("Qual razão? "))

    quant_numeros = int(input("Quantos números? "))
    numeros = cria_pa(termo, razao, quant_numeros)
    elemento = int(input("Qual posição quer descobrir? "))
    descobre_termo(numeros, razao, elemento)
    exibe_pa(numeros, 10)


if __name__ == "__main__":
    main()
