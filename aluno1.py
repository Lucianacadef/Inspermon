#ABERTURA DE PROGRA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import json

def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))


with open('inspermon_world.json') as arquivo:
    inspermons = json.load(arquivo)
   
   
      
#BATALHA INSPERMON\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def calcular_batalha(selvagem,ipmon2):
    for ipmon2 in Insperdex:
        while selvagem["vida"] and ipmon2["vida"] > 0:
            selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
            ipmon2["vida"] = ipmon2["vida"] - (selvagem["poder"] - ipmon2["defesa"])
            if ipmon2["vida"] <= 0:
                print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
                break
            else:
                print("{0} ganhou!!! Você ganhou essa batalha".format(ipmon2["nome"]))
                if selvagem not in Insperdex:
                    Insperdex.append(selvagem)
                    print(Insperdex)
                break
            return calcular_batalha(selvagem,ipmon2)
    
#Fase 1:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
with open('Insperdex.json') as arquivo:
    Insperdex = json.load(arquivo)  
inspermons_iniciais = [{'nome': 'Pedrodimon', 'poder': 20, 'vida': 200, 'defesa': 12}, {'nome': 'Lufreimon', 'poder': 15, 'vida': 300, 'defesa': 14}, {'nome': 'Jhonamon', 'poder': 10, 'vida': 150, 'defesa': 15}]
inicio = input("Bem vindo ao Inspermon!!! Você se encontra no Insper World, onde várias criaturas estranhas aqui habitam. Você está preparado para essa aventura? Sim ou Não:").lower().title()

if inicio == "Sim":
    print("Esses são os seus Inspermons:")
    for ipmon in inspermons_iniciais:
        mostra_ipmon(ipmon)
    escolha = input("Escolha com qual você deseja iniciar o jogo.").lower().title()
    for ipmon2 in inspermons_iniciais:
        if escolha in ipmon2.values():
            ipmon2 == escolha
            print("Seu inspermon inicial é {0}". format(ipmon2["nome"]))
            Insperdex.append(ipmon2)
            
    while True:
        opçoes = input("Escolha uma das duas opções: Dormir ou Passear:").lower().title()
        if opçoes == "Dormir":
             break
        else:
            from random import randint
            numero = randint(0,len(inspermons))
            for selvagem in inspermons:
                selvagem == numero
                print("Você encontrou o inspermon selvagem {0}!".format(selvagem["nome"]))
                calcular_batalha(selvagem,ipmon2)
                break
else:
    print("Nos vemos em breve!!!")

            

    
