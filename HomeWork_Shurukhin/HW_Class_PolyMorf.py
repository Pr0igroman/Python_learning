from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def info(self):
        print("=" * 3, "Квадрат", "=" * 3, )
        print(f'Сторона: {self.side}')
        print(f'Цвет: {self.color}')
        Square.perimeter(self)
        Square.area(self)
        Square.draw(self)

    def perimeter(self):
        print(f'Периметр: {self.side * 4}')

    def area(self):
        print(f'Площадь: {self.side * self.side}')

    def draw(self):
        for _ in range(self.side):
            print(self.side * "*")


class Rectangle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width

    def info(self):
        print("=" * 3, "Прямоугольник", "=" * 3, )
        print(f'Высота: {self.height}')
        print(f'Ширина: {self.width}')
        print(f'Цвет: {self.color}')
        Rectangle.perimeter(self)
        Rectangle.area(self)
        Rectangle.draw(self)

    def perimeter(self):
        print(f"Периметр: {(self.width + self.height) * 2}")

    def area(self):
        print(f'Площадь: {self.height * self.width}')

    def draw(self):
        for _ in range(self.height):
            print(f"{"*" * self.width}")


class Triangle(Shape):
    def __init__(self, color, side_a, side_b):
        super().__init__(color)
        self.side_a = side_a
        self.side_b = side_b

    def info(self):
        print("=" * 3, "Треугольник", "=" * 3, )
        print(f'Сторона 1: {self.side_a}')
        print(f'Сторона 2: {self.side_b}')
        print(f'Сторона 2: {self.side_b}')
        print(f'Цвет: {self.color}')
        Triangle.perimeter(self)
        Triangle.area(self)
        Triangle.draw(self)

    def perimeter(self):
        print(f"Периметр: {self.side_a + self.side_b * 2}")

    def area(self):
        s = (self.side_a / 4) * (4 * self.side_b ** 2 - self.side_a ** 2) ** 0.5
        print(f'Площадь: {round(s, 2)}')

    def draw(self):
        for i in range(6):
            print(' ' * (6 - i) + '*' * (2 * i + 1))


square1 = Square("Red", 3)
rect1 = Rectangle("Yellow", 8, 5)
triangle1 = Triangle("Green", 11, 6)
figure = (square1, rect1, triangle1)

for i in figure:
    i.info()
    print("\n\n")
