def parfait(n):
    i = 1

    if n == 1:
        return False
    cpt = 0
    while i <= n // 2:
        if n % i == 0:
            cpt += i

        i += 1

    if cpt == n:
        return True
    else:
        return False


n = int(input("Entrez un nombre : "))

if parfait(n):
    print(n, " est parfait")
else:
    print(n, " n'est pas parfait")
