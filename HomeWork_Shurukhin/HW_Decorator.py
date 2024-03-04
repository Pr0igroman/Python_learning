def decorate_sum(func):
    def wrap(*args):
        total = func(*args)
        length = len(args)
        print()
        print("Сумма чисел", ",".join(map(str, args)), "=", total, "\nСреднее арифметическое чисел ",
              ",".join(map(str, args)), "=", total / length)

    return wrap


@decorate_sum
def summa(*args):
    return sum(args)


summa(2, 3, 3, 4)
