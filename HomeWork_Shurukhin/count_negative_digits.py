digitsList = [-2, 3, 8, -11, -4, 6, -7]


def count_negative_digits(lst):
    if not lst:
        return 0
    else:
        if lst[0] < 0:
            return 1 + count_negative_digits(lst[1:])
        else:
            return count_negative_digits(lst[1:])


print(count_negative_digits(digitsList))
