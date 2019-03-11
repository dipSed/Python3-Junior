from random import randint
f = open("ex7.txt","w")
r = 0
for i in range(1,21):
    q = randint(1,10)
    a = int(input(str(i)+"*"+str(q)+"= "))
    if i*q==a:
        f.write(str(a)+" true"+"\n")
        r+=1
    else:
        f.write(str(a)+" false"+"\n")
f.write("\n")
f.write(str(r)+" "+"\n")
f.close()
