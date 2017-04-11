#Fase de Batalha
def calcular_batalha(selvagem,ipmon2):
    for ipmon2 in Insperdex:
        while selvagem["vida"] and ipmon2["vida"] > 0:
            r = 1
           
            if r%2 != 0:
                
                selvagem["vida"] = selvagem["vida"] - (ipmon2["poder"] - selvagem["defesa"])
           
            elif r%2 == 0:
                
                ipmon2["vida"] = ipmon2["vida"] - (selvagem["poder"] - ipmon2["defesa"])
            print ("Round {0}".format(r))
            r = r + 1
           
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
