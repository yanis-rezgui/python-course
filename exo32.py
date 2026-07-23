n = int(input("Entrez l'age de amel : "))
S = 0

for i in range(1, n + 1):
    S += 500 + (i * 3)

print(f"Le total dans le compte de amel est : {S}")
