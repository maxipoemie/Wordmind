import random
nog_een_keer_spelen = ""
def spel_input():
    poging_teller = 0
    gerade_woord = ""
    woorden = ["bom", "kat", "kast", "raar", "schip", "stoel", "banaan", "piraat", "grassen", "boompje", "achterlijke", "paddenstoel", ]
    geheim_woord = random.choice(woorden)
    woordlen = len(geheim_woord)
    display_woord = ""
    for n in range(woordlen):
        display_woord += "-"
    while gerade_woord != geheim_woord:
        print("Geheim woord: ", display_woord)
        display_woord = ""
        teller = 0
        poging_teller += 1
        gerade_woord = input("Wat is het geheime woord? ")
        if len(gerade_woord) == woordlen:
            for i in gerade_woord:
                if gerade_woord[teller] == geheim_woord[teller]:
                    display_woord += geheim_woord[teller]
                    teller += 1
                elif gerade_woord[teller] in geheim_woord:
                    display_woord += "?"
                    teller += 1
                elif gerade_woord[teller] != geheim_woord[teller]:
                    display_woord += "-"
                    teller += 1
        else:
            print("Het geraden woord heeft niet evenveel letters als het geheime woord.")
            teller += 1
    print("Het raden koste", poging_teller, "poging(en).")




naam  = input("Wat is je naam? ")
while nog_een_keer_spelen != "n":
    spel_input()
    nog_een_keer_spelen = input("Wil je nog een keer spelen? j/n ")
print("Tot ziens!")

