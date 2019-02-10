from random import randint
a = [randint(1,10) for i in range(24)]
t = {}
print(a)
for el in a:
    if el in t:
        t[el]+=1
    else:
        t[el]=1
print(t)
