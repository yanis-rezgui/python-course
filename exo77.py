import math


def delta(a, b, c):
    return b**2 - 4 * a * c


def solutions(a, b, c):
    d = delta(a, b, c)

    if d > 0:
        print("\nThe equations has two solutions : ")
        print("\nx1 = ", format((-b + math.sqrt(d)) / (2 * a), ".2f"))
        print("\nx2 = ", format((-b - math.sqrt(d)) / (2 * a), ".2f"))
    elif d == 0:
        print("x0 = ", format(-b / (2 * a), ".2f"))
    else:
        print("The equation has no solutions in R.")


a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

solutions(a, b, c)
