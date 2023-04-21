n=int(input("n="))
L=[]
for i in range(n):
    L.append(int(input()))
SND=0
SNDC=0
sochan=0
for i  in L:
    if i>0:
        SND+=1
    if i%2==0:
        SNDC+=i
        sochan+=1
print("SND=",SND,sep="")
if sochan==0:
    print("TBC=0")
else:
    print("TBC=",SNDC/sochan,sep="")