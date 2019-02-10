u = int(input("Введите какое колличество слов будет в вашем списке: "))
a = [input("Введите слово: ") for i in range (u)]
print(a)
simv = 0
simvslov = 0
slova = 0
slova5 = 0
Max = 0
Min = len(a[0])
PredMax = 0
nomMin = 0
kolsl = 0
for i in range(len(a)):
    for b in range(len(a[i])):
        simv+=1
        simvslov+=1
    if len(a[Max])<len(a[i]):
        Max=i
    if len(a[i])>5:
        slova5+=1
    if a[i][0]=="К" or a[i][0]=="к":
        kolsl+=1
    if Min>len(a[i]):
        Min=len(a[i])
        nomMin = i
    slova+=1
    simvslov = 0
v = len(a[Max])
b = [a[i] for i in range(len(a)) if len(a[i])!=v]
for i in range(len(b)):
    if len(b[i])>len(b[PredMax]):
           PredMax=i
sred=simv/slova
print("Средняя длина слова: %.1f"%sred)
print("Кол-во слов в которых больше пяти букв:",slova5)
print("Кол-во букв в самом большом слове:",len(a[Max]))
print("Номер первого самого маленького слова в списке:",nomMin+1)
print("Колличество символов в слове,больше которого толко самое длинное слово:",len(b[PredMax]))
print("Колличество слов которые начинаються на к или К:",kolsl)
a.sort()
print(a)
