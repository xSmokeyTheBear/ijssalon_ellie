#Ik weet niet of ik de opdracht op correcte wijze heb opgevangen, het vermoeden is dat handmatig parameter "a" aangepast dient te worden naar de waarde in kolom "argumenten"
#parameter "b" is hierdoor statisch een 2, in verband met de opdracht. 



def mijn_functie_1(a):
 return a*a
                            

print(mijn_functie_1(2))



def mijn_functie_2(a,b):
 uitvoer_lijst = []
 uitvoer_lijst.append(a+b)
 uitvoer_lijst.append(a-b)
 uitvoer_lijst.append(a*b)
 uitvoer_lijst.append(a/b)
 return uitvoer_lijst

print(mijn_functie_2(12,3))
 



