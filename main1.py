# print("Привет!!!")

# name = "admin"

# print("Hello " + name)
# a = 1
# b = 2
# print(a, b)
#
# a, b = b, a
# print(a, b)
#
# a = 10
# b = 20
#
# id(a) == id(b)
# id(b) == id(a)
#
# print(a, b)

# a = 5
# b = 9
# c = 15
# print("Сумма: " + str(a + b + c))
# print("Произведение: " + str(a * b * c))
# print("Среднее арифметическое: " + str((a + b + c) / 3))
# list[a, b, c]
# sum(list, start=0)


# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# print(int(3.8))
# print(round(3.8))

# name = "Виктор"
# age = 28
#
# print("Меня зовут", name, ". Мне", age, "лет" )
# print("Меня зовут " + name + ". Мне " + str(age) + " лет" )
# print("Меня зовут", name, ".Мне", age, "лет",  sep="---", end="\n"  )
# print("Hello")

# name = input('Введите имя: ')
# city = input('Введите город: ')
# print(name,city)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)

# a,b,c,d = int(input("Введите первое число: ")),int(input("Введите второе число: ")),int(input("Введите третье число: ")),int(input("Введите четвертое число: "))
# res1 = a + b
# res2 = c+d
# res3 = round(res1 / res2, 2)
# print(res3)
#
# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
# print(b2 + 5)

# print(7 == 7)
# print(7 == "7")
# print((2 + 5 != 7))
#
# print((2 < 4 < 9))

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 or 1 + 3 == 4)


# a = 25
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print(("a = b"))


# a = int(input("Введите первую сторону треугольника: "))
# b = int(input("Введите вторую сторону треугольника: "))
# c = int(input("Введите третью сторону треугольника: "))
#
# if a == b == c:
#     print("Это равносторонний треугольник")
# elif a == b or b == c or a == c:
#     print(("Это равнобедренный треугольник"))
# else:
#     print(("Это разносторонний треугольник"))

# day = int(input("Введите номер дня недели: "))
#
# if 1 <= day <= 5:
#     if day == 1:
#         print("Это рабочий день - Понедельник")
#     elif day == 2:
#         print("Это рабочий день - Вторник")
#     elif day == 3:
#         print("Это рабочий день - Среда")
#     elif day == 4:
#         print("Это рабочий день - Четверг")
#     elif day == 5:
#         print("Это рабочий день - Пяяяятница!!!")
# elif day == 6 or day == 7:
#     if day == 6:
#         print("Это выходной - Суббота")
#     else:
#         print("Это выходной - Воскресенье")
# else:
#     print("Такого дня недели не существует")

# k = int(input("Введите количество ворон: "))
#
# if k == 1:
#     print("На ветке:", k , "ворона")
# elif 2 <= k <= 4:
#     print("На ветке:", k , "вороны")
# elif 5 <= k <= 9 or k == 0:
#     print("На ветке:", k , "ворон")
# else:
#     print("Вышли за диапозон")
# while True:
# for k in range(100):


# x = int(input("Введите номер месяца: "))
#
# if x == 1 or x == 2 or x == 12:
#     print("Зима")
# elif 3 <= x <= 5:
#     print("Весна")
# elif 6 <= x <= 8:
#     print("Лето")
# elif 9 <= x <= 11:
#     print("Осень")
# else:
#     print("Ошибка! Такого месяца не существует")

# password = "user"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print(("Пароль неверен"))

# day = "Суббота"
# time = 11
#
# match day:
#     case "Понедельник" | "Вторник" | "Среда" | "Четверг" | "Пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case "Суббота" | "Воскресенье" if 9 <= time <= 12:
#         print("Рабочий день")
#     case "Суббота" | "Воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
#
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))


# a, b = int(input("Введите первое число: ")), int(input("Ввведите второе число: "))
#
# print("На ноль делить нельзя!!!" if b == 0 else a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
#
# except ValueError:
#     print("Что-то пошло не так")
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
#     print(n + m)
# except ValueError:
#     print(n + m)
#
# finally:
#     "Конец программы"

i = 1
while i < 10:
    j = 1
    while j < 1:
        print(i, end="")
        j += 1
    print()
    i += 1

