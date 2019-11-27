from random import randint
import json

def game(zacetno, koncno):
    skrito = randint(zacetno, koncno - 1)
    print(zacetno, skrito, koncno)
    izbrana_stevilka = -1
    isTrue = False
    seznam_ugibanj = []
    while izbrana_stevilka!=skrito:
        if isTrue == True:
            print("Žal vaša številka ni prava. Poskusite znova.")
        izbrana_stevilka = vprasaj_stevilko()
        isTrue = True
        seznam_ugibanj.append(izbrana_stevilka)
    print("Čestitam! Zadeli ste skrito število!")
    
    return seznam_ugibanj

def vprasaj_stevilko():
    stevilka = int(input("Izberi številko med 1 in 100\n"))
    return stevilka

def zapisi_v_datoteko(ime_osebe, rezultat_igre):
    with open(ime_osebe, "w") as output_file:
        niz = json.dumps(rezultat_igre)
        output_file.write(niz)

def vprasaj_osebo():
    return input("Napiši svoje ime:\n")

if __name__ == "__main__":
    ime_osebe = vprasaj_osebo()
    ugibanja = game(1, 100)
    print(ugibanja)
    zapisi_v_datoteko(ime_osebe+".txt", ugibanja)