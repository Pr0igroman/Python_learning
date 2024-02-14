value = {"John":
             {"N": 3056,
              "S": 8463,
              "E": 8441,
              "W": 2694},
         "Tom":
             {"N": 4832,
              "S": 6786,
              "E": 7374,
              "W": 3612},
         "Anne":
             {"N": 5239,
              "S": 4802,
              "E": 5820,
              "W": 1859},
         "Fiona":
             {"N": 3904,
              "S": 3645,
              "E": 8821,
              "W": 2451},
         }

key = True
key1 = True
values = True


for k in value.keys():
    print(k)
    for v in value[k].keys():
        print(v, " : ", value[k][v], sep="")

while key:
    name = input("Введите имя: ")
    if name not in value:
        print("Нет такого имени!")

    else:
        key = False
        while key1:
            region = input("Введите регион: ")
            if region not in value[name]:
                print("Нет такого региона!")
            else:
                key1 = False
                print(value[name][region])

                try:
                    value[name][region] = int(input("Введите новое значение: "))
                    print(value[name])


                except ValueError:
                    print("Возможно вы ввели не число. Введите числовое значение.")
