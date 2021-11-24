valik = str(input("Palun sisestage failinimi: "))
fail = open(valik, encoding="UTF-8")
lugu = []

loend = 0
for rida in fail:
    loend += 1
    lugu.append(str(rida))
    print(str(round(loend))+ ". "+ rida)
    

failirida = int(input("valige järjekorranumkber: "))
print(str(lugu[-1 + failirida]))
fail.close
