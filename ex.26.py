
# a = [3, 4, 5, 3, 6, 7, 3, 2]
#
# while 3 in a:
#     a.remove(3)
#
# print(a)


# a = [3, 4, 4, 4, 6, 7, 3, 2]
# a = list(set(a))
# print(a)

# добавление в множество
# a = {54, 32, 54, 3, 4, 5, 2}
# a.add(9)
# a.add(4)
# a.update({5, 6, 7})
# a.update(range(5, 10))
# a.update("hello")
# print(a)

# удаление из множества
# a = {54, 32, 54, 3, 4, 2}
# a.discard(4)
# a.remove(3)
# print(a.pop())
# a.clear()
# print(a)

# операции над множествамми
# a = {54, 32, 54, 3, 4, 2}
# print(len(a))
# print(4 in a, 7 in a)
# print(4 in a, 7 not in a)

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
c = {10, 11, 12}
print(a & b) #пересечение множества
a&= c
print(a, c)

