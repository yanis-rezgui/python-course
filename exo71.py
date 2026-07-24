def affTable(x):

    print(f"\nLa table de {x} est: ")
    for i in range(10):
        print(f"{x}*{i + 1} = {x*(i+1)}")


p = 1
while p != 0:
    x = int(input("\nVeillez choisir un nombre : "))

    affTable(x)
    p = int(input("\nTapez 0 pour arreter : "))
