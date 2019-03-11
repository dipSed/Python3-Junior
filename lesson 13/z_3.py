f = open("ex3.txt","w")
for i in range(1,11):
    f.write(str(i**2)+"\n")
    print(i**2)
f.close()
