num_student = int(input("Введите количество студентов: "))
name_student = []
second_name_student = []
score = []

for i in range(num_student):
    name_student.append(input("Введите имя студента: "))
    second_name_student.append(input("Введите фамилию студента: "))
    score.append(int(input("Введите оценку студента: ")))
    print("Студент", name_student[i], second_name_student[i], "с оценкой", score[i], "добавлен.")

avg = sum(score) / num_student

print("Средний балл", round(avg), ". Студенты с баллом выше среднего: ")
for i in range(num_student):
    if avg < score[i]:
        print(name_student[i] + second_name_student[i] + "\n")
    else:
        continue
#
# Начал смотреть следующий урок и понял, что можно было решить чуть проще через словарь.
