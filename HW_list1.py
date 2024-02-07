s = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    x = int(input("Введите число кратное 3: "))
    if x % 3 != 0:
        print(x, "не делится на 3 без остатка.")
    else:
        s.append(x)
print(s)