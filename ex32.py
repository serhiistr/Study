# Создание словарей

a = {"moscow", "piter", "penza"}

# "moscow" - 495,
# "piter" - 812,
# "penza" - 8412

# d = {
#     # key:value,
#     "moscow": 495,
#     "piter": 812,
#     "penza": 8412
# }
# print(d)


# Создание словарей второй вариант- если в качестве ключей используются строковые типы

# r = dict(moscow=495, piter=812, penza=8412)
# print(r)

# Создание словарей третий вариант- если в качестве ключей используются вложенные списки
# a = [["moscow", 495], ["piter", 812], ["penza", 8412]]
# t = dict(a)
# q = dict.fromkeys(["a", "b", "c", "d"], 100)
# print(q)

# b = {}
# d = {
#     # key:value,
#     1: 45,      #1 - индекс ключа, 45 - значение
#     2: "two",
#     3: "three"
# }
# print(d)


# person = {}
# s = "IVANOV IVAN Samara SGU 5 4 5 5 4 3 5"
# s = s.split()
# person["lastname"] = s[0]
# person["firstname"] = s[1]
# person["city"] = s[2]
# person["university"] = s[3]
# person["marks"] = []
#
# for i in s[4:]:
#     person["marks"].append(int(i))
# print(s)
# print(person)
#
#
d = {
    # key:value,
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}
# print(d)
# #del d[1]
# print(d)
#
# print(len(d))
# print(1 in d, 5 in d, 7 not in d)
# print(d.get(1, "no"))  # получает значение ключа, если нету такого индекса, то выводим "no"
# print(d.pop(2))  # удаляет элемент
# print(d)
#
# print(d.keys()) # получаем значение всех ключей нашего словаря
# for key in d.keys():
#      print(key, d[key])
#
# print(d.values()) # можем вернуть все значения нашего словаря
# for values in d.values():
#      print(values)

print(d.items()) # возвращает коллекцию в котрой есть все пары (индекс и значение)
for key, value in d.items():
     print(key, value)
