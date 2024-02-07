# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))
# a = b = c = 5
# print(a, b, c)
# a, b, c = 7, "Hello", 9.2
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 5
# b = "7"
# print(a + int(b))
# print(str(a) + b)

# a = 19
# b = 24
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# print("\tстрока \n"
#       "символов")
# print('     строка символов         строка символов         строка символов строка символов '
#       'строка символов    строка символов строка символов строка символов')
# print("\"program\" \n\rC:\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)

# print(46545645645646545612318787974)
# print(4.6545645645646545612318787974)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(5 / 2)
# print(5 // 2)
# print(6 // 2)
# print(6 ** 2)
# print(5 % 4)


# a = 5
# b = 7
# c = 3
# sum1 = a + b + c
# print("Сумма:", sum1)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", sum1 / 3)

# numbers = 6 + 4 * 5 ** 2 + 7
# print(numbers)
#
# numbers = (6 + 4) * (5 ** 2 + 7)
# print(numbers)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12
#
# num *= 4  # num = num * 4
# print(num)  # 48

# a = 30
# b = 10
# print("a:", a)
# print("b:", b)
# a = a + b  # 21
# b = a - b  # 20
# a = a - b  # 1
# # a, b = b, a
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a:", a)  # 2
# print("b:", b)  # 1


# num = 4321  # 1234
# a = num % 10
# print(a)  # 1
# num = num // 10  # 432
# # print("num:", num)
# b = num % 10
# print(b)  # 2
# num = num // 10  # 43
# # print("num:", num)
# c = num % 10
# print(c)  # 3
# num = num // 10  # 4
# # print("num:", num)
# d = num % 10
# print(d)  # 4
# num = a * 1000 + b * 100 + c * 10 + d
# print(num)


# num = 4321  # 1234
# res = num % 10 * 1000  # 1000
# num //= 10  # 432
# res += num % 10 * 100  # 200
# num //= 10  # 43
# res += num % 10 * 10  # 30
# num //= 10  # 4
# res += num % 10  # 4
# print(res)


# print(int(3.8))  # 3
# a = round(3.84646456, 2)
# print(round(3.84646456))  # 4
# print(a, type(a))

# a = '5.2'
# b = 10
# c = int(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", end=" ", sep="---")
# print("Hello")


# name = input("Введите имя: ")
# city = input("Введите город: ")
# print(name, city)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# print("1:", a)
# print("2:", b)
# print("3:", c)
# print("4:", d)
# result = round(((a + b) / (c + d)), 2)
# print(result)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5
# print(type(b1))

#  False => "", 0, 0.0, False, None
#
# print(bool("python"))
# print(bool(""))
# print(bool(10))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
#
# test = None
# print(test, type(test))
# test = 5
# print(test)

# print(7 == 7)
# print(7 == "7")
# print(2 + 5 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("привет" > "ПРИВЕТ")  # 175 > 143

# print(2 < 4 < 9)  # True : True  => True
# print(2 < 4 > 9)  # True : False  => False
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 < 2 or 1 + 3 < 4)  # False and False => False
# print(not 9 - 5)  # False
# print(not 9 - 9)  # True


# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# PEP20
# import this

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = input("Введите 1-сторону")
# b = input("Введите 2-сторону")
# c = input("Введите 3-сторону")
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == b:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# m = int(input("Введите номер месяца: "))
# if m == 1 or m == 2 or m == 12:
#     print("Зима")
# elif 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# password = "admin1"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = 'суббота'
# time = 18
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье' if 9 <= time <= 12:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")


# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# a, b = int(input("Введите первое число")), int(input("Введите второе число"))
#
# print("На ноль делить нельзя!!!" if b == 0 else a / b)

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)  # '9' => 9
#     m = int(m)  # 'fgdfg'
# except ValueError:
#     n = str(n)  # '9'
# finally:
#     print(n + m)

# x = input("Введите первое: ")
# y = input("Введите второе: ")
# try:
#     print(int(x) + int(y))
# except ValueError:
#     print(x + y)

# x = input("Введите первое: ")
# y = input("Введите второе: ")
# try:
#     z = int(x) + int(y)
# except ValueError:
#     z = x + y
# finally:
#     print(z)

# Цикл

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 2
# while i <= 20:
#     print("i = ", i)
#     i += 2


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# print("*" * n)
# print("+-" * int(n / 2))


# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Укажите кол-во символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# 1 - 5 => 1 + 3 + 5 => 9

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# j = 0
# while j < 5:
#     print(" " * j, "*", sep="")
#     j += 1


# i = 0  # 5
# while i < 5:  # 5 < 5
#     j = 0  # 4
#     while j < i:  # 4 < 4
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello":
#     print(i)

# for color in "red", "yellow", "green", 1, 20, 0.3:
#     print(color)

# print(range(9))

# range(start, stop, step)  start=0, step=1

# for i in range(100, 0, -10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(0, h):  # 4
#     for j in range(0, w):  # 16
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:  #
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print([i * 5 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])

# Списки (list)

# num = [9, 3, 8, 4, 1, "Hello", 2.3, True]
# print(num)
# # print(type(num))
# # print(num[0])
# # print(num[2])
# # print(num[-2])
# # print(num[7])
# # print(num[8])
# # num[1] = 100
# # num[2] += 50
# # num[8] = 2
# print(num[len(num) - 1])
# print(num[-1])

# num = []
# print(num)
# print(type(num))


# nums = list(range(1, 100, 2))
# print(nums)  # 2 4 6 8 10 12 14 16 18 20
# print(type(nums))

# nums = list("Hello")
# num = nums * 2
# print(num + [1, 2, 3])

# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(nums[i])

# for i in nums:
#     print(i)

# генератор списков
# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)  # [0, 0, 0, 0, 0]
# b = [i ** 2 for i in range(1, 6)]
# print(b)  # [0, 1, 2, 3, 4]
# c = [c * 3 for c in "list"]
# print(c)  # ['lll', 'iii', 'sss', 'ttt']

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)  # [0, 0, 0]
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# print(range(5))
# print(list(range(5)))
# s = [2, 9, 8, 7, 4, 7, 8, 9, 6]
# for i in range(len(s)):
#     print(i, "->", s[i])
# print(len(s))

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):  # 0 1 2
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):  # 0 1 2 3 4 5 6 7 8
#     print(lst[i], end=" ")
# print()
# for i in lst:  # 10 20 30 40 50 60 70 80 90
#     print(i, end=" ")

# colors = ["red", "blue", "green"]
# for i in range(len(colors)):  # 0 1 2
#     print(colors[i], end=" ")
# print()
# for i in colors:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# count = s = 0
# for i in range(len(n)):  # 0 1 2 3 4
#     if n[i] % 2 == 0:
#         count += 1  # 1 + 1 = 2
#     else:
#         s += n[i]  # 21 + 23 = 44
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i

# print("Кол-во четных элементов списка:", count)
# print("Сумма нечетных элементов списка:", s)

# n = [4, 9, 6]
# print(n)
# i = 2
# print(n[i])
# print(n[i - 1])


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):  # 1 2 3 4
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 9, 3, 1, 2]
# print(a)  # [7, 9, 3, 1, 2]
# print("[0]", id(a[0]))
# print("[1]", id(a[1]))
# a[0], a[1] = a[1], a[0]
# print(a)  # [9, 7, 3, 1, 2]
# print("[0]", id(a[0]))
# print("[1]", id(a[1]))

# Срезы  - список[start:stop:step]
# s = [6, 9, 3, 7, 1, 8]
# print(s, id(s))
# b = s[5:16]
# print(b, id(b))
# i = 5
# while i > 0:
#     print(s[i])
#     i -= 1


# s = "Hello World!"
# print(s[6:-1])

# [1, 2, 3, 4, 5, 6, 7]
# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:3]
# print(s)

# Методы списков
# dir(list)
# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# # s[len(s):] = [12]
# s.append(12)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет любое кол-во элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(-1, 'Hello')  # добавляем элемент (второй параметр) в список в заданный индекс (первый параметр)
# print(s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("Кол-во элементов списка: "))
# for _ in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# # for i in a:  # 5, 9, 2, 1, 4, 3
# #     for j in b:  # 4, 2, 1, 3, 7
# #         if i in c:
# #             continue
# #         if i == j:
# #             c.append(i)
# #             break
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
#
# print(c)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for _ in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0-3
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3, 5)
#     c.append(b[i])
# print(c)

# if len(b) > len(a):
#     for i in range(len(a)):  # 0-3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0-3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3, 5)
#         c.append(a[i])
# print(c)

# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# # n = 2
# # if n in a:
# #     a.remove(n)  # удаление по значению, выбрасывает исключение ValueError - если элемента не существует
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(1)  # удаляет элемент по заданному индексу (IndexError)
# print(second)
# print(a)
# a.clear()  # очищает список
# print(a)


# sp = [int(input("-> ")) for i in range(int(input("Введите количество чисел списка: ")))]
# x = int(input("Введите индекс: "))
# print(sp.pop(x))
# print(sp)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5)  # возвращает количество заданных значений в списке
# print(num)
# ind = a.index(2)  # возвращает индекс заданного значения
# print(ind)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort(reverse=True)  # сортировка списка
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len)
# print(s)
# print(len("Александр"))


# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.sort()
# n = sorted(a, reverse=True)
# print("n =", n)
# print(a)

# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# b.append(120)
# print("a =", a, id(a))
# print("b =", b, id(b))

# Генерация случайных данных

# import random

# print(random.random())  # от 0 до 1 (не включительно)
# print(random.randint(0, 9))  # от 0 до 9 (включительно)
# print(random.randrange(2, 9, 2))  # randrange(start, stop, step)  randrange(2, 9)
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
#
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# mas = ['a', 'b', 'c']
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))

# print(sum(mas))

# s = 0
# for i in mas:
#     s = s + i  # s += i  # s = 0 + 'a'
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# summa = max(mas)  # 100
# print(summa)
# mas.remove(summa)  # [21, 80, 92, 4, 26, 12, 66, 52, 41]
# mas.insert(0, summa)  # [100, 21, 80, 92, 4, 26, 12, 66, 52, 41]
# print(mas)

# mas = [random.randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)


# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# minimum = min(array)
# print("Min:", minimum)
# ind = array.index(minimum)
# print(ind)
# print(array[ind:])
# del array[:ind]
# print(array)

# lst = []
# # if len(lst) == 0
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# # c = a + b
# # print("Третий список:", c)
# # c = []
#
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
# #
# # print(c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
#
# print(c)
#
# d = [min(a), max(a), min(b), max(b)]
# print(d)
# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(m)
#
# print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
#
# matrix = [[0 for x in range(w)] for y in range(h)]
#
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# import random
# w, h = 3, 4
# count = 0
# matrix = [[random.randint(-20,20) for x in range(w)] for y in range(h)]
#
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)

#


# Modules

# from math import sqrt

# from math import pi as pre
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))
# print(math.floor(3.8))
# print(pre)

# r = int(input("Введите радиус окружности: "))
#
# print("Длина окружности равна", round(2 * pi * r, 2))
#
# a = int(input("Введите первый катет: "))
# b = int(input("Введите второй катет: "))
# print(sqrt(a ** 2 + b ** 2))

# import time
#
# seconds = time.time()
# print(seconds)
# print(time.ctime())
# # print(time.ctime(60*60*24*365*55))
# res = time.localtime()
# print(res)
#
# print(time.strftime("%c"))


def change(lst):
    # lst = list(lst.split(" "))
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)


change([1, 2, 3])
change([9, 12, 33, 54, 105])
change(["с", "л", "о", "н"])
figure = input("Выберите фигуру: 1- треугольник, 2- прямоугольник, 3- круг: ")
match figure:
    case "1":
        a = int(input("Введите основание: "))
        h = int(input("Введите высоту: "))
        print("Площадь треугольника равна:", (a*h)/2)