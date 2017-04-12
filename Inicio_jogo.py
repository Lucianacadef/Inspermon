#INICIO|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

from Fugir_batalha import fugir_batalha
from Fase_batalha import calcular_batalha
from random import randrange

def inicio_jogo():
    while True:
            opçoes = input("Escolha uma das duas opções: Dormir ou Passear:").lower().title()
            if opçoes == "Dormir":
                 break
            else:
                numero = randrange(len(inspermons))
                selvagem = inspermons[numero]
                
                print("Você encontrou o inspermon selvagem {0}!".format(selvagem["nome"]))
                if selvagem not in Insperdex:
                    Insperdex.append(selvagem)
                calcular_batalha(selvagem,ipmon2)
