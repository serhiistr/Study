while True:
    a = input()
    if a == "exit":
        break
    if len(a)<5:
        continue
    print(a, len(a))


#a, b = map(int, input().split())
#
#while b > 0:
#    c = a % b
#    a = b
#    b = c
#print(a)