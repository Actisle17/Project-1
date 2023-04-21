n=int(input("n="))
L=[]
for i in range(n):
    L.append(int(input()))
M=list(set(L))
for i in M:
    print(i,end="")