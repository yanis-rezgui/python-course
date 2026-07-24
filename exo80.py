def aff(nom, salaire=3000):
    print("\nLe nom : ", nom)
    print("\nLe salaire : ", salaire, "€")


nom = input("Entrez le nom : ")
salaire = int(input("Entrez le salaire : "))

aff(nom, salaire)
aff("Yanis")
