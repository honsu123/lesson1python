depth = int(input("Введите глубину ямы: "))
for i in range(depth):
    for num1 in range(depth, depth - i - 1, -1):
        print(num1, end="")
    count = 2 * (depth - i - 1)
    print("." * count, end="")
    for num2 in range(depth - i, depth + 1):
        print(num2, end="")
    print()
