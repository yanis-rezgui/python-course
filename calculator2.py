num1 = int(input("Enter the first number : "))

num2 = int(input("Enter the second number : "))

operator = input("Enter an operator (+,-,*,/) : ")


match operator:
    case "+":
        print("The result is : ", num1 + num2)

    case "-":
        print("The result is : ", num1 - num2)

    case "*":
        print("The result is : ", num1 * num2)
    case "/":
        if num2 == 0:
            print("Error impossible to devide by 0")

        else:
            print("The result is : ", num1 / num2)

    case _:
        print("\nInvalid operator")

print("End :)")
