n = int(input("Veilez entrez un entier"))

if n == 0:
    print("Uniquement comme diviseur")
elif n == 1:
    print("Uniquement 1")
else:
    print(f"Les diviseurs de {n} sont : ")
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            print(i)

    print(n)

    print("\nfin")
