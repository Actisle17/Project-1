def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def Search(L):
    L.sort()
    max=L[-1]
    min=L[0] 
    return max,min
def Output(max,min):
    print(max,min) 
L=Input()
max,min=Search(L)  
Output(max,min)  