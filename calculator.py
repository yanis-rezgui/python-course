number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2 : "))

print("Number 1 : ", number1)
print("Number 2 : ", number2)

operator = input("Enter an operator : ")


match operator:
    case "+":
        print("\nThe result is : ", (number1 + number2))

    case "-":
        print("\nThe result is : ", (number1 - number2))

    case "*":
        print("\nThe result is : ", number1 * number2)
    case "/":
        if number2 == 0:
            print("Error impossible to devide by 0")
        else:
            print(f"\nThe result is : {number1/number2:.2f}")
    case _:
        print("\nInvalid operator")
