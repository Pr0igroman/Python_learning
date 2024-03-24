fio = "никонов валерий анатольевич" # input("Введите ФИО: ).split()

fio = fio.split()
res = f"{fio[0].title()} {fio[1][0].capitalize()}. {fio[2][0].capitalize()}."

print(res)

