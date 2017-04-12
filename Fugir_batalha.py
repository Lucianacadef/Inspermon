from random import randint
numero = randint(1,100)
fuga = list(range(1,100,2))
print(fuga)
def fugir_batalha():
    Fugir = input("Você quer fugir da batalha? Sim ou Não:").lower().title()
    if Fugir == "Sim":
        if numero in fuga :
            print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
            return
    
