n = 1

while n != 0:
    print("\n-----Menu------")
    print("\nTapez un pour + .")
    print("\nTapez 2 pour - .")
    print("\nTapez 3 pour * .")
    print("\nTapez 4 pour / .")
    choix = int(input("Choisissez un nombre : "))

    num1 = float(input("Choisissez le premier nombre : "))
    num2 = float(input("Choisissez le deuxieme nombre : "))

    match (choix):
        case 1:
            print("\nThe result is : ", num1 + num2)
        case 2:
            print("\nThe result is : ", num1 - num2)
        case 3:
            print("\nThe result is: ", num1 * num2)
        case 4:
            if num2 == 0:
                print("Division par 0 impossible")
            else:
                print("\nLe resultat est : ", format(num1 / num2, ".2f"))

        case _:
            print("\nOperateur invalide")

    n = int(input("\nTapez 0 pour arreter : "))
