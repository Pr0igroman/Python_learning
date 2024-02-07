k = int(input("Введите количество копеек от 1 до 99: "))
if k == 1 or (20 < k <= 99 and k % 10 == 1):
    print(k, "КОПЕЙКА")
elif 2 <= k <= 4 or (k > 20 and (k % 10 == 2 or k % 10 == 3 or k % 10 == 4)):
    print(k, "КОПЕЙКИ")
elif k > 99:
    print("Вы ввели неверное значение =(")
else:
    print(k, "КОПЕЕК")
