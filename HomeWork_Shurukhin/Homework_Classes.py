class Car:

    def __init__(self, model, year, manufacturer, engine_power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, '*'))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}"
              f"\nМощность двигателя: {self.engine_power} л.с.\nЦвет автомобиля: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        print(self.model)

    def set_year(self, year):
        self.year = year

    def get_year(self):
        print(self.year)

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        print(self.manufacturer)

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def get_engine_power(self):
        print(self.engine_power)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        print(self.color)

    def set_price(self,price):
        self.price = price

    def get_price(self):
        print(self.price)


id1 = Car("X7 M50i", "2021", "BWM", "530", "White", "10790000")
id1.print_info()
id1.set_model("модель")
id1.set_year("год")
id1.set_manufacturer("производитель")
id1.set_engine_power("мощность двигателя")
id1.set_color("цвет")
id1.set_price("цена")

id1.get_model()
id1.get_year()
id1.get_manufacturer()
id1.get_engine_power()
id1.get_color()
id1.get_price()


id1.print_info()