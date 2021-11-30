def banner(lause):
    return lause.upper()
reklaam = str(input("Mida soovite reklaamis kuvada? "))
kordamine = int(input("Mitu korda soovite korrata lauset? "))
for i in range(kordamine):
    print(banner(reklaam))
