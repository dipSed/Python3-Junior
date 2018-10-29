from random import randint
t=0
for i in range(1,13):
    print(i,end=" ")
print()
for i in range(1,13):
    print("-",end=" ")
print()
for n in range(3):
    for m in range (4):
        q=randint(2,5)
        w=randint(2,5)
        e=randint(2,5)
        t=t+q+w+e
        print(q,w,e,end=" ")
    print()
print("Общ сумма оценок = ",t)
