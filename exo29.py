x = int(input("Veillez entrez un nombre : "))

if x < 0:
    print("Impossible")
elif x == 0:
    print("Le factorielle de 0 est 1")
else:
    fact = 1
    i = x
    while i > 0:
        fact *= i
        i -= 1

    print(f"Le factoriel de {x} est {fact}")
