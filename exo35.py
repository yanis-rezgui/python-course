n = 0

while n < 2:
    n = int(input("\nVeillez entrez un entier : "))

U0 = 0
U1 = 1

print("U0 = ", U0)
print("U1 = ", U1)

for i in range(2, n + 1):
    print(f"U{i} = {U1 + U0}")
    temp = U0 + U1
    U0 = U1
    U1 = temp
