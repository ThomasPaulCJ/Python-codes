st1=input("Enter a string : ")
wd1=input("Enter the word to be replaced : ")
wd2=input("Enter the new word : ")

st2=st1.split()
st3=st2
for i in range (len(st2)):
    if(st2[i]==wd1):
        st3[i]=wd2

print("the string after replacing the word is : ",' '.join(st3))
