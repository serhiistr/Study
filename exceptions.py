x = 0

while x == 0:
    try:
        x = float(input("Введите число: "))
        x += 5
        print(x)
    except ValueError:
        print("Введите лучше число!")

