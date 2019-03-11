from random import randint
f = open("ex5.txt","w")
a = []
for i in range(20):
    aappend(randint(-20,20))
print(a)
for i in range(20):
    if a[i]<0:
        f.write(str(a[i])+"\n")
        print(a[i])
f.close()
