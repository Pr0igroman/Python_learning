i = 0
length = input("Введите количество символов(цифрой) ")
while type(length) != int:
    try:
        length = int(length)
    except ValueError:
        length = input("Введите количество символов(цифрой) ")
symbol = input("Введите символ ")
orientation = input("Введите '1' для горизонтального расположения или '2' для вертикального расположения ")
match orientation:
    case "1":
        while i < length:
            print(symbol, end=" ")
            i += 1
    case "2":
        while i < length:
            print(symbol, end="\n")
            i += 1
    case _:
        print("неверная ориентация\nделаю по умолчанию")
        while i < length:
            print(symbol, end=" ")
            i += 1

