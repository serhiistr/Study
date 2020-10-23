#from random import randint
#
#s = 0
#n = int(input())
#for i in range(n):
#    a = randint(1, 10)
#    s = s + a
#print(s)

#for i in range(1, 10):
#    print("*"*i)

n = int(input())
s = 0
for i in range(n):
    a = int(input())
    s = s + a
    print("current s:", s)
print("total s:", s)
print("Sred arif d:", s/n)