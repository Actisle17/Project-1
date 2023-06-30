L=[]
n=int(input())
for i in range(n):
    k=int(input())
    L+=[k]
def count(L):
    s=0
    for j in L:
        s+=1
    print(s)
count(L)