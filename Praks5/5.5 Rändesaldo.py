sisse = open("sisseranne.txt", encoding="UTF-8")
valja = open("valjaranne.txt", encoding="UTF-8")

sis = []
val = []
loend = 0
for rida in valja:
    val.append(int(rida)) 
for rida2 in sisse:
    sis.append(int(rida2))

sisse.close()
valja.close()


for i in range(len(sis)):
    sis[i] = sis[i] - val[i]

print(sis)





    




