f = open("ex1.txt","w")
d = input(" ")
for i in range(len(d),0,-1):
    k = d[i-1]
    f.write(k+"\n")
    print(k)
f.close()
