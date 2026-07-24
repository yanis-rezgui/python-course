def premier(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    else:
        i = 2
        while i <= x // 2:
            if x % i == 0:
                return False
            else:
                i += 1

        return True


p = 1

while p != 0:
    x = int(input("Veillez entrez un nombre : "))

    if premier(x):
        print(x, " est premier")
    else:
        print(x, " n'est pas premier")
