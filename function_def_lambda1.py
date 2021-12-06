# nums_1 = [5, 7, 2, 9, 4]
#
# min = nums_1[0]
#
# for el in nums_1:
#     if el < min:
#         min = el
#
# print(min)


def minimal(L):
    min_1 = L[0]
    for el in L:
        if el < min_1:
            min_1 = el
    print(min_1)


nums_1 = [5, 7, 2, 9, 4]

minimal(nums_1)


func_1 = lambda x, y: x * y  # return не надо писать в этом типе функции
print(func_1(3, 2))


