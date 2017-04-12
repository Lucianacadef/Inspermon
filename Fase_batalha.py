from Fugir_batalha import fugir_batalha
def calcular_batalha(selvagem,ipmon2):
    for ipmon2 in seu_ipmon:
        vida_ipmon2 = ipmon2["vida"]
        r = 1
        while selvagem["vida"] > 0 and ipmon2["vida"] > 0:
            if  ipmon2["vida"] >= vida_ipmon2/2:
                if r%2 != 0:
                    selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
                    print("Round {0}".format(r))
                    print("{0} tem {1} de vida".format(selvagem["nome"],selvagem["vida"]))
                else:
                    Fugir = input("Você quer fugir da batalha? Sim ou Não:").lower().title()
                    if Fugir == "Sim":
                        fugir_batalha
                        
            elif r%2 == 0:
                ipmon2["vida"] = ipmon2["vida"] - (selvagem["poder"] - ipmon2["defesa"])
                print("Round {0}".format(r))
                print("{0} tem {1} de vida".format(ipmon2["nome"],ipmon2["vida"]))
            r += 1
                
        if ipmon2["vida"] <= 0:    
            print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
            
                
        elif ipmon2["vida"] <= 0:
            print("{0} ganhou!!! Você ganhou essa batalha".format(ipmon2["nome"]))
