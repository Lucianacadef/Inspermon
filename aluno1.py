#ABERTURA DE PROGRA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import json
from Inicio_jogo import inicio_jogo
from Fase_batalha import calcular_batalha
from random import randrange
from Fugir_batalha import fugir_batalha

def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))
   
     
#Fase 1||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

with open('inspermon_world.json') as arquivo:
    inspermons = json.load(arquivo)

with open('Insperdex.json') as arquivo:
    Insperdex = json.load(arquivo)
    
inspermons_iniciais = [
    {'nome': 'Pedrodimon', 'poder': 20, 'vida': 200, 'defesa': 12},
    {'nome': 'Lufreimon', 'poder': 15, 'vida': 300, 'defesa': 14},
    {'nome': 'Jhonamon', 'poder': 10, 'vida': 150, 'defesa': 15}
]
seu_ipmon = []
inicio = input("Bem vindo ao Inspermon!!! Você se encontra no Insper World, onde várias criaturas estranhas aqui habitam. Você está preparado para essa aventura? Sim ou Não:").lower().title()


if inicio == "Sim":
    print("Esses são os seus Inspermons:")
    for ipmon in inspermons_iniciais:
        mostra_ipmon(ipmon)
    escolha = input("Escolha com qual você deseja iniciar o jogo.").lower().title()
    for ipmon2 in inspermons_iniciais:
        if ipmon2["nome"] == escolha:
            print("Seu inspermon inicial é {0}". format(ipmon2["nome"]))
            Insperdex.append(ipmon2)
            seu_ipmon.append(ipmon2)
    print(seu_ipmon)
    inicio_jogo()
else:
    print("Nos vemos em breve!!!")

            

    
