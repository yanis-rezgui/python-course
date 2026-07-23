n = int(input("Veullie entrez un nombre : "))

i = 0
x = 0
S = 0
while i < n:
    if x % 2 != 0:
        S += x**2
        i += 1

    x += 1

print("\nLa somme : ", S)
