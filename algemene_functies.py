#Ik weet niet of ik de opdracht op correcte wijze heb opgevangen, het vermoeden is dat handmatig parameter "a" aangepast dient te worden naar de waarde in kolom "argumenten"
#parameter "b" is hierdoor statisch een 2, in verband met de opdracht. 

b = 2

def mijn_functie_1(a):
 global b 
 return a ** b

teruggeefwaarde = mijn_functie_1(4)
                            

print(teruggeefwaarde)

def mijn_functie_2(c,d):
 return c + d, c - d, c * d, c / d 

teruggeefwaarde2 = mijn_functie_2(12,3)

print(teruggeefwaarde2)
 



