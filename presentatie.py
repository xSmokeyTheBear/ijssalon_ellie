def presenteer(inkomsten, totaal_inkomsten):
 totaal_inkomsten = sum(inkomsten.values())
 for key in inkomsten.keys():
            
    print(key, ":", inkomsten[key])
 print("=============")
 print("Totaal :", totaal_inkomsten)
 return       
            
            




