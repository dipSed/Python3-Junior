from random import randint
a = []
b = []
for i in range(10):
    k = randint(10,15)
    a.append(k)
print(a)
for i in range(10):
    if a[i]!=13:
        b.append(a[i])
print(b)
