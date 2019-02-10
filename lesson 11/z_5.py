a = []
b = []
for i in range(10):
    k = randint(-10,10)
    a.append(k)
print(a)
for i in range(10):
    if a[i]<0:
        b.append(a[i])
print(b)
