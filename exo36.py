n = int(input("Veillez entrez un nombre : "))

if n <= 1:
    print(f"{n} n'est pas premier")
else:
    i = 2
    premier = True
    while i <= n // 2 and premier:
        if n % i == 0:
            print(n, " n'est pas premier")
            premier = False
        else:
            i += 1

    if premier:
        print(n, " est premier")
