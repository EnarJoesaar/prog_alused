ainepunktid = int(input("Sisestage ainepunktide arv:"))
nädalate_arv = int(input("Sisestage nädalate arv:"))
esimene_vastus = ainepunktid * 26
teine_vastus = esimene_vastus / nädalate_arv
print(round(teine_vastus))