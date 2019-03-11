f = open("ex6.txt","w")
l = 0
g = [937,941,947,953,967,971,977,983,991,997]
for i in range(1000,0,-1):
    if i in g and l!=10:
        f.write(str(i)+"\n")
        print(i)
        l+=1
    elif l==10:
        break
f.close()
