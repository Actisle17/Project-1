L=[]
while True:
    n=int(input())
    L.append(n)
    if n==0:
        break
L.sort()
print("Cac so da nhap: ",n)
for n in L:
    print(n)