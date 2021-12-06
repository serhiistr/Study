#
# def test_func():
#     print("HI", end="")
#     print("!")
#
# test_func()

# def test_func(word):
#     print(word, end="")
#     print("!")
#
#
# test_func("HI")
# test_func(5)


def summa(a, b):
    res = a+b
    print("Result", res)


summa(2, 3.0)
summa("H", "I")


def summa_1(a, b):
    res = a+b
    print("Result", res)


res_1 = summa_1(2, 3)
print(res_1)


def summa_2(a, b):
    res = a+b
    return res   #если поставить return то дальше можно работатть с полученным числом


res_2 = summa_2(2, 3)
print(res_2*2)

