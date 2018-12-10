st=input("введите слово ")
a=st.count(",")
n=0
for i in st:
    if i.isdigit():
        n+=1
if  a>n:
    print ("Запятых больше")
elif a<n:
    print ("Цифр больше")
elif a==n:
    print ("Цифр больше")
