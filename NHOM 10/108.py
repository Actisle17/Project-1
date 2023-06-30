soam=[]
so0=[]
soduong=[]
while True:
    n=input("n=")
    if n=="":
        break
    else:
        n=int(n)
    if n<0:
        soam.append(n)
    elif n==0:
        so0.append(n) 
    else:
        soduong.append(n)
for n in soam:
    print(n) 
for z in so0:
    print(z) 
for p in soduong:
    print(p)                        
    