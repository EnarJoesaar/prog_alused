from random import randint
poiss = int(input("Mitu pöialpoissi tahab õunu:"))
õunad = 14
i = 1
while i <= poiss:
    õunadearv = randint(1,2)
    print(str(õunadearv))
    i = i + 1
lumi = õunad - i
print("Lumivalgekesele jäi " + (str(lumi)))

