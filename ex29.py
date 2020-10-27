# a = [[0, 2, 4, 6], [1, 5, 9, 14], [3, 10, 17, 19]]
#
# print(len(a))
#
# print(a[2])
#
# # Берем число 19 из списка. Указывыаем номер подсписка и номер эелемента который берем. ОТвет 19
# print(a[2][3])
# print(a[0][1])

# b = [[0, 2, 4, 6], [1, 5, 9, 14], [3, 10, [4, 5, 7, 11], 17, 19]]
# print(b[2][2][1])

# b = ["hello", "hi", "world"]
# print(b[2])
# print(b[2][1])

#
# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 14],
#     [3, 10, 17, 19]
# ]

# Первый вариант обхода списка
# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()

# Второй вариант обхода по индексам.
# for i in range(3):
#     for j in range(4):
#         a[i][j] +=5
#         print(a[i][j], end=" ")
#     print()

# for i in range(3):
#     s=0
#     for j in range(4):
#         s = s + a[i][j]
#     print(s)

a = []
n = int(input())  # string
m = int(input())  # row

for i in range(n):
    b = []
    for i in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)
