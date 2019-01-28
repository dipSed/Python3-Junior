from random import randint
n = int(input("Введите колличество чисел в списке: "))
a = int(input("Введите минимальное генирируемое число: "))
b = int(input("Введите мксимальное генирируемое число: "))
a = [randint(a,b) for i in range(n)]
print(a)
