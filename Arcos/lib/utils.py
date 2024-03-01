from lib.strings import centro, errorMessage


def pergunta(mensagem="", tipo=str):
    tipo_str = ""
    if tipo == str:
        tipo_str = "str"
    elif tipo == int:
        tipo_str = "int"
    elif tipo == float:
        tipo_str = "float"
    elif tipo == bool:
        tipo_str = "bool"
    while True:
        print(f"{mensagem}?")
        resposta = input(">> ")
        try:
            resposta = tipo(resposta)
        except ValueError:
            errorMessage(f"Digite uma resposta do tipo{tipo_str}!")
        else:
            return resposta


def clear():
    from os import system, name
    from time import sleep

    sleep(0.2)
    if name == "posix":  # For Unix/Linux/Mac
        system("clear")
    elif name == "nt":  # For Windows
        system("cls")
    else:
        pass


def sair():
    from time import sleep

    sleep(0.2)
    centro("Aperte Enter para parar")
    input()
