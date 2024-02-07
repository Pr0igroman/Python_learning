from math import pi

figure = input("Выберите фигуру: 1- треугольник, 2- прямоугольник, 3- круг: ")
match figure:
    case "1":
        a = int(input("Введите первую сторону: "))
        b = int(input("Введите вторую сторону: "))
        c = int(input("Введите третью сторону: "))
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("Площадь треугольника равна:", round(s, 5))
    case "2":
        a = int(input("Введите длину: "))
        b = int(input("Введите ширину: "))
        s = a * b
        print("Площадь прямоугольника равна: ", s)
    case "3":
        r = int(input("Введите радиус: "))
        s = pi * r ** 2
        print("Площадь круга равна:", round(s, 5))
    case _:
        print("Нет такой фигуры")
