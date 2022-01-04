valik = open(input("Palun sisestage failinimi: ") , encoding="UTF-8")

 
tõde = 0   
õigus = 0  
 
valik = valik.read().upper().replace("Ä" , "AE").replace("Õ" , "OE").replace("Ü" , "UE")


print(valik)
 
valik.close()