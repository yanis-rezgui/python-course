def nbrChiffres(x):
    cpt = 0
    while x != 0:
        x = x // 10
        cpt += 1

    return cpt


p = 1

while p != 0:
    x = int(input("Veillez entrez un nombre : "))
    print(f"\nLe nombre de chiffres de {x} est : {nbrChiffres(x)}")

    p = int(input("Tapez 0 pour arréter : "))
