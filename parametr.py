import sys

print(sys.argv)

arguments = sys.argv[1:]

print(arguments)

a = int(arguments[0])
b = int(arguments[1])

result = a * b

print("Результат:", result)