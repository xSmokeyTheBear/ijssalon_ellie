# let op, ik heb het element aardbei moeten gebruiken om het zelfde resultaat te krijgen als in de opdracht, niet het element vanille.
# vanille, 4 * 0.8 is 3.2 en niet 2.400000000004 zoals bij de waarde van aardbei. 



prijzen = {
       "aardbei" : "3",
       "vanille" : "4",
     "chocolade" : "5"
}

aanbieding     =  3 * 0.8
reclame_tekst  = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts €{aanbieding}")
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")


for el in reclame_tekst4:
    if len (el) > 5:
     print((el).upper()) 
    if len (el) < 5:
      print((el).lower())


