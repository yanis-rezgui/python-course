n = int(input("Veillez entrez le terme : "))

if n < 0:
    print("Impossible")
elif n == 0:
    print("U0 = 6")
else:
    U0 = 6
    Un = 0
    for i in range(1, n + 1):
        Un = 4 * U0 + 10
        U0 = Un

    print("Un = ", Un)
