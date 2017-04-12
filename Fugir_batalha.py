
def fugir_batalha():
    from random import randint
    numero = randint(1,100)
    fuga = list(range(1,100,2))
    print("Seu número foi {0}".format(numero)
    if numero in fuga:
        print("Você consiguiu fugir, a sorte está com você")
        print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
        return
    else:
        print("A sorte não está com você!!!")
        
    
