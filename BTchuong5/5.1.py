def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    x=int(input("x="))
    return x,L
def firstAndLast(L):
    new_L=[L[0],L[-1]]
    print(new_L)
    return new_L
def Search(L,x):
    if x in L:
        return True
    return False
x,L=Input()
new_L=firstAndLast(L)
if Search(L,x):
    print("True")
else:
    print("False")