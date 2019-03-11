f = open("ex8.txt","w")
i = input(" ")
f.write(i)
f.close()
k = []
f = open("exx.txt","r")
for el in f:
    e = el.split()
    print(e)
f.close()
