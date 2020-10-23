a = [43, 65, 3, 43, 8]

#обход по значению
#for i in a:
#    print(i, a.index(i))


#обход по индексам
#n = len(a)
#for i in range(n):
#    print(i, a[i])
#    a[i]+=5
#print(a)


#Исключить все дубли из списка
#a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
#b = []
#
#for i in a:
#    if not i in b: #если элемента не в списке b - то добавляем
#        b.append(i)
#print(b)


#a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
#chet = []
#nechet = []
#
#n = len(a)
#for i in range(n):
#    if a[i]%2 == 0:
#        chet.append(i)
#    else:
#        nechet.append(i)
#print(chet)
#print(nechet)


#s = "helLLo 5656world"
#for i in s:
#    if i>="a" and i<="z":
#        print(i, "small")
#    elif "A"<=i<="Z":
#        print(i, "big")
#    else:
#        print(i)

vowels = "aeiou"
s = "jkfdetauyeey"
n = len(s)
for i in range(n-1):
    if s[i] in vowels and s[i+1] in vowels:
        print(s[i], s[i+1])