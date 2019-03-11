f = open("gosva.txt","r")
q = open("stol.txt","r")
for i in range(2):
    r=input(" ")
    r+="\n"
    for i in range(10):
        h = f.readline()
        if r==h:
            print(" ",h)
f.close()
q.close()
