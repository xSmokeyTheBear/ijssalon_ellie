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

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for bedrag in inkomsten:
     totaal += bedrag
     btw_bedrag = totaal * btw
     uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
     return totaal


def laag_en_hoog():
     mijn_lijst = 220, 430, 125, 160, 205, 90, 345
     mijn_lijst = max(mijn_lijst), min(mijn_lijst)
     print(mijn_lijst)

laag_en_hoog()

def gemiddelde(mijn_lijst):
     mijn_lijst = 220, 430, 125, 160, 205, 90, 345
     aantal = len(mijn_lijst)
     totaal = 0
     for element in mijn_lijst:
      totaal += element
      gemiddelde = totaal / aantal
      uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
      return mijn_lijst


def meervoudig():
     invoer_lijst = 10, 5, 3, 2, 1, 2, 9 
     invoer_lijst = max(invoer_lijst), min(invoer_lijst)
     print(invoer_lijst)
    
meervoudig()
     




     
     

