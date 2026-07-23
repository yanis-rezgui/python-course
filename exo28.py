n = int(input("Veillez entrez un nombre : "))
S = 0

i = 0

while i <= n:
    S += 10**i
    i += 1

print("La somme est : ", S)
