s = 0


def squre(a, b, c):
    global s

    def squre_rectangle(first, second):
        return first * second

    s = 2 * (squre_rectangle(a, b) + squre_rectangle(b, c) + squre_rectangle(a, c))

    return s


squre(int(input("Введите длину ребра 'a': ")), int(input("Введите длину ребра 'b': ")),
      int(input("Введите длину ребра 'c': ")))
print(s)

# def squre(a, b, c):
#     def squre_rectangle(first, second):
#
#         return first * second
#
#     s = 2 * (squre_rectangle(a, b) + squre_rectangle(b, c) + squre_rectangle(a, c))
#
#     return print(s)
#
#
# squre(int(input("Введите длину ребра 'a': ")), int(input("Введите длину ребра 'b': ")),
#       int(input("Введите длину ребра 'c': ")))
