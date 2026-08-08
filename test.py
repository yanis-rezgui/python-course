num1 = int(input("Enter  number 1 : "))
num2 = int(input("Enter number 2 : "))

if num1 < 0:
    print(num1, "is Negratif")
else:
    print(num1, "is positif")

if num2 < 0:
    print(num2, "is negatif")
else:
    print(num2, "is positif")

if num1 >= 0 and num2 >= 0:
    print(num1, " and ", num2, " are positif")
elif num1 < 0 and num2 < 0:
    print(num1, " and ", num2, " are negatif")
else:
    print(num1, " and ", num2, " are not of the same degree")
