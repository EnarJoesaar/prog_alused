aasta = int(input("Palun sisestage; millise aasta andmeid vajate: "))

fail = open("C:\\Users\\Enar\\Downloads\\rebane.txt", encoding="UTF-8")

vastuvõetud = []

Kokku = 0
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()    

print(str(aasta) + " aastal oli vastuvõetud " + str(vastuvõetud[2011 - aasta]))
