from random import randint
n = int(input("Введите макс степень числа 2: "))
t = 0
a = [2**(i+1) for i in range(n)]
print(a)
