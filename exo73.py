def bissextile(an):
    if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
        return True
    else:
        return False


an = int(input("Veillez entrez une année : "))

if bissextile(an):
    print(f"{an} est bissextile")
else:
    print(f"{an} n'est pas bissextile")
