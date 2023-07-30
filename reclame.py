from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
  korte_lijst = laag_en_hoog(invoer_lijst_2)
  uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
  return uitvoer

def aanbieding_1(smaak, prijs, korting):
     korting = prijs * korting
     aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - korting} euro."
     return aanbieding

print(aanbieding_1("aardbei", 4.0, 0.1))

ma = 220
di = 430
wo = 125
do = 160
vr = 205
za = 90
zo = 345

def inkomsten_totaal():
    global ma, di, wo, do, vr, za, zo
    inkomsten = ma + di + wo + do + vr + za + zo
    btw = 0.09 * inkomsten
    return f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."

print(inkomsten_totaal()) 

def laag_en_hoog():
     mijn_lijst = 220, 430, 125, 160, 205, 90, 345
     mijn_lijst = max(mijn_lijst), min(mijn_lijst)
     print(mijn_lijst)

laag_en_hoog()

def gemiddelde():
     global ma, di, wo, do, vr, za, zo
     werkdagen = ma + di + wo + do + vr + za + zo 
     mijn_lijst = werkdagen / 7 
     return f"De gemiddelde inkomsten deze week zijn {mijn_lijst} euro."

print (gemiddelde())

def meervoudig():
     invoer_lijst = 10, 5, 3, 2, 1, 2, 9 
     invoer_lijst = max(invoer_lijst), min(invoer_lijst)
     print(invoer_lijst)
    
meervoudig()
     




     
     

