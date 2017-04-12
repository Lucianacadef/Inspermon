def calcular_batalha(selvagem,ipmon2):
    for ipmon2 in seu_ipmon:
        vida_ipmon2 = ipmon2["vida"]
        vida_selvagem = selvagem["vida"]
        r = 1
        while r <= 200:
            while selvagem["vida"] > 0 and ipmon2["vida"] > 0:
                if r%2 != 0:
                    if ipmon2["poder"] - selvagem["defesa"] > 0:
                        selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
                        print("Round {0}".format(r))
                        print("{0} tem {1} de vida".format(selvagem["nome"],selvagem["vida"]))
                    else:
                        selvagem["vida"] = selvagem["vida"] 
                        print("Round {0}".format(r))
                        print("{0} tem {1} de vida".format(selvagem["nome"],selvagem["vida"]))
                        
                    
                elif r%2 == 0:
                    if selvagem["poder"] - ipmon2["defesa"] > 0:
                        if  ipmon2["vida"] >= vida_ipmon2/2:
                            ipmon2["vida"] = ipmon2["vida"] - (selvagem["poder"] - ipmon2["defesa"])
                            print("Round {0}".format(r))
                            print("{0} tem {1} de vida".format(ipmon2["nome"],ipmon2["vida"]))
                        else:
                            Fugir = input("Você quer fugir da batalha? Sim ou Não:").lower().title()
                            if Fugir == "Sim":
                                fugir_batalha()
                    else:
                        ipmon2["vida"] = ipmon2["vida"] 
                        print("Round {0}".format(r))
                        print("{0} tem {1} de vida".format(ipmon2["nome"],ipmon2["vida"]))
                                   
            r += 1
            if r == 200:
                print("Acabou o tempo!!!")
                if selvagem_vida - selvage["vida"] < ipmon2_vida - iomon2["vida"]:
                    print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
                    return
                elif selvagem_vida - selvage["vida"] > ipmon2_vida - iomon2["vida"]:
                    print("{0} ganhou!!! Você ganhou essa batalha".format(ipmon2["nome"]))
                    return
                else:
                    print("Empatou!!!! Parabéns pela batalha!!!")
                    return
                
            if ipmon2["vida"] <= 0:
                ipmon2["vida"] = vida_ipmon2
                print("{0} ganhou!!! Você perdeu essa batalha".format(selvagem["nome"]))
                
                    
            elif ipmon2["vida"] <= 0:
                ipmon2["vida"] = vida_ipmon2
                print("{0} ganhou!!! Você ganhou essa batalha".format(ipmon2["nome"]))

       
