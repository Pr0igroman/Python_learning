nums = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
minimum = nums[0]
maximum = 0
summa = 0

for i in nums:
    summa += i

    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
print("Количество чисел: ", len(nums))
print("Среднее арифметическое: ", summa / len(nums))
print("Минимальное число: ", minimum)
print("Максимальное число: ", maximum)
