class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(round(self.sec // other.sec))

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec == other.sec:
            print("True")
            return True
        print("False")
        return False

    def __ne__(self, other):
        # return not self.__eq__(other)
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec != other.sec:
            print("True")
            return True
        print("False")
        return False

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec < other.sec:
            print("True")
            return True
        print("False")
        return False

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec > other.sec:
            print("True")
            return True
        print("False")
        return False

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec <= other.sec:
            print("True")
            return True
        print("False")
        return False

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec >= other.sec:
            print("True")
            return True
        print("False")
        return False


c1 = Clock(601)  # 601
print(c1.get_format_time())  # 00:10:01
c2 = Clock(601)  # 200
print(c2.get_format_time())  # 00:03:20
# c3 = c1 - c2
# print(c3.get_format_time())  # 00:06:41
# c4 = c1 * c2
# print(c4.get_format_time())  # 09:23:20
# c5 = c1 // c2
# print(c5.get_format_time())  # 00:00:03
# c6 = c1 % c2
# print(c6.get_format_time())  # 00:00:01
# c1 -= c2
# print(c1.get_format_time())  # 00:06:41
# c1 *= c2
# print(c1.get_format_time())  # 09:23:20 (в условиях задачи 22:13:20, но это ошибка, т.к с1 переопределяется)
# c1 //= c2
# print(c1.get_format_time()) # 00:00:03
# c1 %= c2
# print(c1.get_format_time()) # 00:00:01

c7 = (c1 > c2)
c8 = (c1 >= c2)
c9 = (c1 < c2)
c10 = (c1 <= c2)
