from random import randint
a = []
b = []
for i in range(10):
    k = randint(10,15)
    a.append(k)
print(a)
k = int(input("Введите индекс числа который уберем из списка a: "))
for i in range(10):
    if a[i]!=k:
        b.append(a[i])
print(b)
