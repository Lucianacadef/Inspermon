#Fase de Batalha
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
