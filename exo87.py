import stats

N1 = float(input("Entrez la note 1 : "))

N2 = float(input("Entrez la note 2 : "))

N3 = float(input("Entrez la note 3 : "))

N4 = float(input("Entrez la note 4 : "))

N5 = float(input("Entrez la note 5 : "))

S = stats.addition(N1, N2, N3, N4, N5)

print("\nLa somme est: ", format(S, ".2f"))

M = stats.moyenne(N1, N2, N3, N4, N5)

print("\nLa moyenne est : ", format(M, ".2f"))
