st=input("введите слово ")
a=st.count("а")
o=st.count("о")
if  a>o:
    print ("А больше чем О")
elif a<o:
    print ("О больше чем А")
elif a==0 and o==0:
    print ("В слове нету этих букв")
