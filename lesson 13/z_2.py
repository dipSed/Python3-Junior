from random import randint
f = open("ex2.txt","w")
for i in range(15):
    h = randint(50,100)
    f.write(str(h)+"\n")
    print(h)
f.close()
