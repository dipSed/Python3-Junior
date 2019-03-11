f = open("ex4.txt","w")
for i in range(10):
    a = input(" ")
    f.write(a+"\n")
    print(i+1,"из 10")
print(" ")
f.close()
