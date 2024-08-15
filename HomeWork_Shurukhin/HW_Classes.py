class Pair:
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b

    def summa(self):
        return print(f"Сумма: {self._a + self._b}")

    def multiply(self):
        return print(f"Произведение: {self._a * self._b}")

    def set_value(self, a: int = None, b: int = None):
        if a is not None and b is not None:
            self._a = a
            self._b = b
        elif a is not None:
            self._a = a
        elif b is not None:
            self._b = b

    def get_value(self):
        return print(f"{self._a}\n{self._b}")


class RightTriangle(Pair):

    def hypotenuse(self):
        hypo = (self._a ** 2 + self._b ** 2) ** 0.5
        return round(hypo, 2)

    def view_hypotenuse(self):
        print(f"Гипотенуза ABC: {RightTriangle.hypotenuse(self)}")

    def triangle(self):
        return print(f"Прямоугольный треугольник ABC: {self._a, self._b, RightTriangle.hypotenuse(self)}")

    def area_triangle(self):
        s = (self._a * self._b) / 2
        return print(f"Площадь ABC: {s}")


triangle1 = RightTriangle(5, 8)
triangle1.view_hypotenuse()
triangle1.triangle()
triangle1.area_triangle()
print()
triangle1.summa()
triangle1.multiply()
print()
print()
triangle2 = RightTriangle(10, 20)
triangle2.view_hypotenuse()
triangle2.triangle()
triangle2.area_triangle()
print()
triangle2.summa()
triangle2.multiply()
print()
triangle2.set_value(15, 20)
triangle2.summa()
triangle2.multiply()
triangle2.set_value(b=50)
triangle2.get_value()
triangle2.triangle()
