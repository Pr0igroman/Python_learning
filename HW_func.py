from math import pi


def triangle():
    a = int(input("Введите основание: "))
    h = int(input("Введите высоту: "))
    return print("Площадь треугольника равна:", (a * h) / 2)


def rectangle():
    a = int(input("Введите длину: "))
    b = int(input("Введите ширину: "))
    return print("Площадь прямоугольника равна: ", a * b)


def circle():
    r = int(input("Введите радиус: "))
    return print("Площадь круга равна:", pi * r ** 2)


figure = int(input("Выберите фигуру: 1 - треугольник, 2 - прямоугольник, 3 - круг: "))
if figure == 1:
    triangle()
elif figure == 2:
    rectangle()
elif figure == 3:
    circle()
else:
    print("Нет такой фигуры")