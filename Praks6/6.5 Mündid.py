def pronks(fail):
    arv = 0
    for münt in fail:
        if int(münt) <= 5:
            arv += int(münt)
    return arv
failinimi = input("Sisestage failinimi ")
fail = open(failinimi, encoding="UTF-8")
print("Hoiupõrsasse läheb " + str(pronks(fail)) + (" senti"))
