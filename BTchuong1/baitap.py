def Input():
    n=int(input('n='))
    L=[]
    for i in range (1, n+1):
        a=int(input(""))
        L.append(a)
    x=int(input("x="))
    return L, x
def FirstAndLast(L):
    L1=[L[0],L[-1]]
    print(L1)
def Search(L,x):
    if x in L:
        print("True")
    else:
        print("False")
L,x= Input()
FirstAndLast(L)
Search(L, x)