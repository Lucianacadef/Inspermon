#ABERTURA DE PROGRA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import json
from random import randrange

def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))

#Fugir Batalha|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def fugir_batalha():
    from random import randint
    sorte= randint(1,100)
    fuga = list(range(1,100,2))
    print("Seu número foi {0}".format(numero))
    if sorte in fuga:
        print("Você consiguiu fugir, a sorte está com você")
        print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
        return
    else:
        print("A sorte não está com você!!!")
        
        
        
    
#Fase de Batalha|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
def calcular_batalha(selvagem,ipmon2):
    chance = 0
    for ipmon2 in seu_ipmon:
        vida_ipmon2 = ipmon2["vida"]
        r = 1
        while selvagem["vida"] > 0 and ipmon2["vida"] > 0:
            if r%2 != 0:
                if ipmon2["vida"] == vida_ipmon2/2 and chance == 0:
                    Fugir = input("Você quer fugir da batalha? Sim ou Não:").lower().title()
                    if Fugir == "Sim":
                        fugir_batalha()
                        chance = 1
                    else:
                        print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
                        return
                else:
                    selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
                    print("Round {0}".format(r))
                    print("{0} tem {1} de vida".format(selvagem["nome"],selvagem["vida"]))    
            elif r%2 == 0:
                ipmon2["vida"] = ipmon2["vida"] - (selvagem["poder"] - ipmon2["defesa"])
                print("Round {0}".format(r))
                print("{0} tem {1} de vida".format(ipmon2["nome"],ipmon2["vida"]))
                   
            r += 1             
        if ipmon2["vida"] <= 0:
            print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
            ipmon2["vida"] = vida_ipmon2
            
            
                
        elif selvagem["vida"] <= 0:
            print("{0} ganhou!!! Você ganhou essa batalha".format(ipmon2["nome"]))
            ipmon2["vida"] = vida_ipmon2
            
                     

  
           
     
#Fase 1||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
with open('inspermon_world.json') as arquivo:
    inspermons = json.load(arquivo)

with open('Insperdex.json') as arquivo:
    Insperdex = json.load(arquivo)
    
inspermons_iniciais = [{'nome': 'Pedrodimon', 'poder': 20, 'vida': 200, 'defesa': 9},
                       {'nome': 'Lufreimon', 'poder': 15, 'vida': 300, 'defesa': 14},
                       {'nome': 'Jhonamon', 'poder': 17, 'vida': 150, 'defesa': 12}
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
            
else:
    print("Nos vemos em breve!!!")

            

    
