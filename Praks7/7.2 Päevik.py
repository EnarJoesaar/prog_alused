from datetime import datetime
sisu = str(input("Sisesta sissekande tekst: "))
kuupäev_kellaeg = datetime.today()
print("Kuupäev ja kellaeg: " + str(kuupäev_kellaeg))
f = open("paevik.txt", "a")
f.write(str(kuupäev_kellaeg) + "\n")
f.write(sisu + "\n")
f.write("\n")
f.close()

