class OnlyInt:
    def __set_name__(self, owner, name):
        self.__name = "_" + name

    def __get__(self, instance, owner):
        print(instance.__dict__)
        # return instance.__dict__[self.__name]
        return getattr(instance, self.__name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.__name} должно быть целым числом!!!")
        # instance.__dict__[self.__name] = value
        setattr(instance, self.__name, value)


class Point3D:
    x = OnlyInt()
    y = OnlyInt()
    z = OnlyInt()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point = Point3D(1, 2, 3)
# point.x = 55646
# point.y = 5.6  line 12, in __set__ raise ValueError(f"{self.__name} должно быть целым числом!!!") ValueError: _y должно быть целым числом!!!
# point.z = "string" line 12, in __set__  raise ValueError(f"{self.__name} должно быть целым числом!!!") ValueError: _z должно быть целым числом!!!
print(point.x)
print(point.y)
print(point.z)



