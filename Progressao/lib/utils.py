from lib.strings import centro, errorMessage


MENU = {
    "N": "Nova",
    "E": "Exibir",
    "D": "Descobrir",
    "S": "Sair",
}


def pergunta(mensagem="", tipo=str, ignora=""):
    if tipo == str:
        tipo_str = "str"
        tipo_value = ""
    elif tipo == int:
        tipo_str = "int"
        tipo_value = 0
    elif tipo == float:
        tipo_str = "float"
        tipo_value = 0
    elif tipo == bool:
        tipo_str = "bool"
        tipo_value = None
    while True:
        print(f"{mensagem}?")
        resposta = input(">> ")
        if resposta == ignora:
            return tipo_value
        try:
            resposta = tipo(resposta)
        except ValueError:
            errorMessage(f"Digite uma resposta {tipo_str}!")
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
