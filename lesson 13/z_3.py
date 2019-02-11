import math
def drob(a):
    ch=a+math.sqrt(a)
    dr=ch/2
    return dr
x=drob(6)+drob(13)+drob(21)
print(x)
