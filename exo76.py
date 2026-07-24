import math


def diametre(r):
    return r * 2


def perimetre(r):
    return 2 * math.pi * r


def surface(r):
    return math.pi * (r**2)


r = float(input("Entrez le rayon : "))

print("Le diametre : ", format(diametre(r), ".2f"))
print("Le perimetre : ", format(perimetre(r), ".2f"))
print("La surface : ", format(surface(r), ".2f"))
