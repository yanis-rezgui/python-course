paga = 50000
pmar = 1000000

année = 0

while pmar > paga:
    pmar += 50000
    paga = paga + paga * 0.08
    année += 1

print("Le nombre d'annee est : ", année)
