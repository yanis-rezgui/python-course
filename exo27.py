n = int(input("Veillez entrez un nombre n : "))
S = 0

for i in range(1, n + 1):
    S = S + 1 / i

print("La somme est : ", format(S, ".2f"))
