from random import randint
a = []
p = 0
n = 0
for i in range(1,21):
    c = randint(1,10)
    print("Чему будет равно произведение чисел:",i,"*",c)
    k = int(input(" "))
    a.append(k)
    if k==i*c:
        p+=1
    else:
        n+=1
print(a)
print("Кол-во правильных:",p,"Кол-во неправильных:",n)
