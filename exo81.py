def fx(x):
    return 4 * (x**3) - 13 * (x**2) + x - 60


x = int(input("Entrez x : "))

print("y = ", format(fx(x), ".2f"))
