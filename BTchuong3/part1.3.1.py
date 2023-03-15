a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
if max<b:
    max=b
elif max<c:
    max=c
print("SLN=",max)
min=a
if min>b:
    min=b
elif min>c:
    min=c
print("SBN",min)    