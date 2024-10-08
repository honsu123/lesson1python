n = int(input("Введите колличество чисел: "))
count = 0
for i in range(n):
    number = int(input("Введите число: "))
    if number > 1:
        for y in range (2, number):
            if number % y == 0:
                break
        else:
            count += 1
print("Количество простых чисел: ", count)