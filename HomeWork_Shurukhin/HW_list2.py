n = int(input("Введите количество элементов списка: "))
lst = []
for i in range(n):
    lst.append(int(input("->")))
k = int(input("Введите индекс: "))
c = int(input("Введите значение: "))
lst.insert(k, c)
print(lst)
