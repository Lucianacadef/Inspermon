#ABERTURA DE PROGRA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import json
from random import randrange

def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))


def mostra_ipmon2(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))
    print("level = {0}".format(ipmon["level"]))
    print("Experiência = {0}\n".format(ipmon["xp"]))

#Salvar Jogo|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def JogoSalvar():
    
    with open ("jogador_salvo.json", "w") as arquivo1:
        json.dump(seu_ipmon, arquivo1)
        
        
    with open ("Insperdex_salvo.json", "w") as arquivo2:
        json.dump(Insperdex, arquivo2)
   

    with open ("Insper_World_salvo.json", "w") as arquivo3:
        json.dump(inspermons, arquivo3)
        
    
    



        
        
    
#Experiencia batalha||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def ganha_xp():
   for ipmon2 in seu_ipmon:
        ipmon2["level"] =  ipmon2["level"] + 1
        ipmon2["poder"] = ipmon2["poder"] + 10
        ipmon2["vida"] =  ipmon2["vida"] + 20
        ipmon2["defesa"] =  ipmon2["defesa"] + 10

        if ipmon2["level"] == 2:      
            ipmon2["nome"] =  ipmon2["nome"][0:len(ipmon2["nome"])-3] + "plast"
            
            ipmon_lv2 = [{'nome': 'Pedrodiplast', 'poder': 30, 'vida': 230, 'defesa': 19},
                        {'nome': 'Lufreiplast', 'poder': 25, 'vida': 280, 'defesa': 24},
                        {'nome': 'Jhonaplast', 'poder': 27, 'vida': 260, 'defesa': 22},
                        {'nome': 'Wesplast', 'poder': 28, 'vida': 250, 'defesa': 21},
                        {'nome': 'Arthiplast', 'poder': 29, 'vida': 240, 'defesa': 23},
                        {'nome': 'Pdrosanplast', 'poder': 26, 'vida': 270, 'defesa': 20},
                        {'nome': 'Iagoplast', 'poder': 31, 'vida': 220, 'defesa': 18},
                        {'nome': 'kevinplast', 'poder': 32, 'vida': 260, 'defesa': 25},
                        {'nome': 'Luigiplast', 'poder': 33, 'vida': 270, 'defesa': 26},
                        {'nome': 'Pedroazamplast', 'poder': 34, 'vida': 280, 'defesa': 27},
                        {'nome': 'Alexalmeiplast', 'poder': 35, 'vida': 290, 'defesa': 28},
                        {'nome': 'Gabrielgoplast', 'poder': 36, 'vida': 300, 'defesa': 29},
                        {'nome': 'Vitorcarplast', 'poder': 37, 'vida': 310, 'defesa': 30},
                        {'nome': 'Manocamplast', 'poder': 38, 'vida': 310, 'defesa': 31}]
            
            for ipmon in ipmon_lv2:
                 if ipmon not in inspermons:
                     inspermons.append(ipmon)
    
                
        elif ipmon2["level"] == 4:
             ipmon2["nome"] =  ipmon2["nome"][0:len(ipmon2["nome"])-5] + 'silver'
             
             ipmon_lv4 = [{'nome': 'Pedrodisilver', 'poder': 50, 'vida': 270, 'defesa': 39},
                          {'nome': 'Lufreisilver', 'poder': 45, 'vida': 320, 'defesa': 44},
                          {'nome': 'Jhonasilver', 'poder': 47, 'vida': 300, 'defesa': 42},
                          {'nome': 'Wessilver', 'poder': 48, 'vida': 290, 'defesa': 41},
                          {'nome': 'Arthisilver', 'poder': 49, 'vida': 280, 'defesa': 43},
                          {'nome': 'Pdrosansilver', 'poder': 46, 'vida': 310, 'defesa': 40},
                          {'nome': 'Iagosilver', 'poder': 51, 'vida': 260, 'defesa': 38},
			  {'nome': 'Lucicosilver', 'poder': 39, 'vida': 270, 'defesa': 39},
                          {'nome': 'Rodrreysilver', 'poder': 40, 'vida': 320, 'defesa': 44},
                          {'nome': 'Gilemessilver', 'poder': 41, 'vida': 300, 'defesa': 42},
                          {'nome': 'Esterquinsilver', 'poder': 42, 'vida': 290, 'defesa': 41},
                          {'nome': 'Davidfolsilver', 'poder': 43, 'vida': 280, 'defesa': 43},
                          {'nome': 'Brunsilver', 'poder': 44, 'vida': 310, 'defesa': 40}]
             
             for ipmon in ipmon_lv4:
                 if ipmon not in inspermons:
                     inspermons.append(ipmon)
                
        elif ipmon2["level"] >= 8:
            ipmon2["nome"] =  ipmon2["nome"][0:len(ipmon2["nome"])-6] + 'gold'

            ipmon_lv8 = [{'nome': 'Pedrodigold', 'poder': 90, 'vida': 350, 'defesa': 79},
                         {'nome': 'Lufreigold', 'poder': 85, 'vida': 400, 'defesa': 84},
                         {'nome': 'Jhonagold', 'poder': 87, 'vida': 380, 'defesa': 82},
                         {'nome': 'Wesgold', 'poder': 88, 'vida': 370, 'defesa': 81},
                         {'nome': 'Arthigold', 'poder': 89, 'vida': 360, 'defesa': 83},
                         {'nome': 'Pdrosangold', 'poder': 86, 'vida': 390, 'defesa': 80},
                         {'nome': 'Iagogold', 'poder': 91, 'vida': 340, 'defesa': 78},
			 {'nome': 'gold', 'poder': 67, 'vida': 350, 'defesa': 79},
                         {'nome': 'Fayreslegend', 'poder': 100, 'vida': 500, 'defesa': 100}]
    
            for ipmon in ipmon_lv8:
                 if ipmon not in inspermons:
                     inspermons.append(ipmon)
            
        for ipmon in seu_ipmon:
            mostra_ipmon2(ipmon)
        print("Você conseguiu evoluir seu Inspermon")
        JogoSalvar()
    
        


          

#Fugir Batalha|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
def fugir_batalha():
    
    from random import randint
    sorte= randint(1,100)
    print("Seu número foi {0}".format(sorte))
    
    if sorte%2 != 0:
        for ipmon2 in seu_ipmon:
            print("Você consiguiu fugir, a sorte está com você")
            ipmon2["vida"] = 0
        
    else:
        print("Você não tirou um número ímpar, a  sorte não está com você!!!")
        while True:
            continuar = input("Vamos congtinuar, escreva 'Vamos':").lower().title()
            if continuar != "Vamos":
                continue
            else:
                break
            
    

        
        
        
    
#Fase de Batalha|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
def calcular_batalha(selvagem,ipmon2):
    chance = 0
    for ipmon2 in seu_ipmon:
        vida_selvagem = selvagem["vida"]
        vida_ipmon2 = ipmon2["vida"]
        r = 1
        if selvagem["defesa"] > ipmon2["poder"] and ipmon2["defesa"] > selvagem["poder"]:
            print("Empate!!! {0} e {1} Ipmons poderosos".format(ipmon2["nome"],selvagem["nome"]))
            
        elif selvagem["defesa"] > ipmon2["poder"] and ipmon2["defesa"] < selvagem["poder"]:
            print("{0} muito poderoso!!! Você não consigirá derrotá-lo".format(selvagem["nome"]))

        elif selvagem["defesa"] < ipmon2["poder"] and ipmon2["defesa"] > selvagem["poder"]:
            print("{0} aniquilou seu adversário!!! Você ganhou essa batalha".format(ipmon2["nome"]))
            ipmon2["xp"] = ipmon2["xp"] + 1
    
        else:         
            while selvagem["vida"] > 0 and ipmon2["vida"] > 0:
                if r%2 != 0:
                    if ipmon2["vida"] <= vida_ipmon2/2 and chance == 0:
                        Fugir = input("Você quer fugir da batalha? Sim ou Não:").lower().title()
                        if Fugir == "Sim":
                            fugir_batalha()
                            chance = 1
                        
                        elif Fugir == "Não":
                            selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
                            print("Round {0}".format(r))
                            print("{0} tem {1} de vida".format(selvagem["nome"],selvagem["vida"]))
                            chance = 1

                        else:
                            print("Essa opção não é valida")
                            continue
                              

                    else:
                        selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
                        print("Round {0}".format(r))
                        print("{0} tem {1} de vida".format(selvagem["nome"],selvagem["vida"]))
                            

                elif r%2 == 0:
                    from random import randint
                    sorte= randint(1,10)
                    print("Round {0}".format(r))
                    if sorte == 7:
                         print("Parbéns!!! {0} desviou do ataque".format(ipmon2["nome"]))
                         continuar = input("Será que terá sorte novamente?")
                    else:
                        ipmon2["vida"] = ipmon2["vida"] - (selvagem["poder"] - ipmon2["defesa"])
                        print("{0} tem {1} de vida".format(ipmon2["nome"],ipmon2["vida"]))
                       
                r += 1             

            if ipmon2["vida"] <= 0:
                print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
                
                
            elif selvagem["vida"] <= 0:
                print("{0} ganhou!!! Você ganhou essa batalha".format(ipmon2["nome"]))
                ipmon2["xp"] = ipmon2["xp"] + 1
            
            
        ipmon2["vida"] = vida_ipmon2
        selvagem["vida"] = vida_selvagem
        while ipmon2["xp"] == 2*ipmon2["level"]:
            Evoluir = input("Vamos evoluir seu Inspermon?").lower().title()
            if Evoluir == "Sim":
                ganha_xp()
                return
            elif Evoluir == "não":
                pass
            else:
                continue
        
        for ipmon in Insperdex:
            print("Sua Insperdex é essa:")
            mostra_ipmon(ipmon)
            
        for ipmon in seu_ipmon:
            print("Seu Ipmon é esse:")
            mostra_ipmon2(ipmon)
            
        JogoSalvar()
     
#Fase 1||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
while True:
    Iniciar = input("Deseja Carregar o Jogo ou Jogar um novo? Escreva Novo ou Carregar:").lower().title()
    if Iniciar == "Novo":
        with open('inspermon_world.json') as arquivo:
            inspermons = json.load(arquivo)


        with open('Insperdex.json') as arquivo:
            Insperdex = json.load(arquivo)
    
        seu_ipmon = []    
        inspermons_iniciais = [{'nome': 'Pedrodimon', 'poder': 20, 'vida': 210, 'defesa': 9, 'level' : 1, 'xp': 0},
                               {'nome': 'Lufreimon', 'poder': 15, 'vida': 260, 'defesa': 14, 'level' : 1, 'xp' : 0},
                               {'nome': 'Jhonamon', 'poder': 17, 'vida': 240, 'defesa': 12, 'level' : 1, 'xp' : 0}
                               ]
        while True:
            inicio = input("Bem vindo ao Inspermon!!! Você se encontra no Insper World, onde várias criaturas estranhas aqui habitam. Você está preparado para essa aventura? Sim ou Não:").lower().title()


            if inicio == "Sim":
                print("Esses são os seus Inspermons:")
                for ipmon in inspermons_iniciais:
                    mostra_ipmon2(ipmon)
                    
                escolha = input("Escolha com qual você deseja iniciar o jogo.").lower().title()
                for ipmon2 in inspermons_iniciais:
                    if ipmon2["nome"] == escolha:
                        print("Seu inspermon inicial é {0}". format(ipmon2["nome"]))
                        Insperdex.append(ipmon2)
                        seu_ipmon.append(ipmon2)
                break
            elif inicio == "Não":
                print("Nos vemos em breve!!!")
                break

            else:
                print("Essa não é uma opção válida") 
                continue
        break
                        
    elif Iniciar == "Carregar":
        
        with open('jogador_salvo.json') as arquivo:
            seu_ipmon = json.load(arquivo)
            for ipmon in seu_ipmon:
                mostra_ipmon2(ipmon)
        
        
        with open('Insper_World_salvo.json') as arquivo:
            inspermons = json.load(arquivo)
            for ipmon in inspermons:
                mostra_ipmon(ipmon)


        with open('Insperdex_salvo.json') as arquivo:
            Insperdex = json.load(arquivo)
        break
    else:
        print("Essa não é uma opção válida")
        continue
                               
while True:
    
    opçoes = input("Escolha uma das duas opções: Dormir ou Passear:").lower().title()
    
    if opçoes == "Dormir":
         print("Nos vemos em breve!!!")
         JogoSalvar()
         break
        
    elif opçoes == "Passear":
        numero = randrange(len(inspermons))
        selvagem = inspermons[numero]
        print("Você encontrou o inspermon selvagem {0}!".format(selvagem["nome"]))
        for ipmon2 in seu_ipmon:
            if selvagem not in Insperdex and selvagem["nome"] != ipmon2["nome"]:
                Insperdex.append(selvagem)
        while True:
            Batalhar = input("Vamos batalhar? Sim ou Não:").lower().title()
            if Batalhar == "Sim":
                calcular_batalha(selvagem,ipmon2)
                break
            elif Batalhar == "Não":
                break
            else:
                print("Essa não é uma opção válida")
                continue
                
    else:
        
        print("Essa não é uma opção válida") 
        continue



            

    
