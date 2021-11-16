ringidearv = int(input("Sisesta ringide arv:"))
porgandid = 0
ring = 1
while ring <= ringidearv:
    if ring % 2 == 0:
        porgandid = porgandid + ring
    ring = ring + 1
print("Porgandite koguarv  on " +  str(porgandid))
