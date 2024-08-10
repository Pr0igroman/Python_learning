class Calc_area:
    _count = 0

    @staticmethod
    def counter():
        Calc_area._count +=1
    @staticmethod
    def area_geron(a, b, c):
        p = ((a + b + c) // 2)

        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        Calc_area.counter()
        return print(f"Площадь треугольника по формуле Герона со сторонами {a, b, c} равна: {s} ")

    @staticmethod
    def area_triangle(a, h):
        s = (a * h) / 2
        Calc_area.counter()
        return print(f"Площадь треугольника с основанием {a} и высотой {h} равна: {s}")

    @staticmethod
    def area_square(a):
        s = a ** 2
        Calc_area.counter()
        return print(f"Площадь квадрата со стороной {a} равна: {s}")

    @staticmethod
    def area_rectangle(a, b):
        s = a * b
        Calc_area.counter()
        return print(f"Площадь прямоугольника со сторонами {a} и {b} равна: {s}")

    @staticmethod
    def get_count():
        return print(f"Колличество подсчётов площади: {Calc_area._count}")


Calc_area.area_geron(3, 4, 5)
Calc_area.get_count()
Calc_area.area_geron(7, 4, 5)

Calc_area.area_triangle(6, 7)
Calc_area.get_count()
Calc_area.area_square(7)

Calc_area.area_rectangle(2, 6)
Calc_area.get_count()
