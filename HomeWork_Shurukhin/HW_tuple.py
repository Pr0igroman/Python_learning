a = tuple(input("Введите число: "))
lst = []
print(a)

# for i in range(10):
#     if str(i) in a:
#         print("Количество", i, "=", a.count(str(i)))


for i in a:
    if str(i) in a and i not in lst:
        lst.append(i)
        print("Количество", i, "=", a.count(str(i)))
