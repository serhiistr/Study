# Создание словарей

a = {"moscow", "piter", "penza"}

# "moscow" - 495,
# "piter" - 812,
# "penza" - 8412

d = {
    # key:value,
    "moscow": 495,
    "piter": 812,
    "penza": 8412
}
print(d)


# Создание словарей второй вариант- если в качестве ключей используются строковые типы

r = dict(moscow=495, piter=812, penza=8412)
print(r)

# Создание словарей третий вариант- если в качестве ключей используются вложенные списки
a = {["moscow"], ["piter"], ["penza"]}

