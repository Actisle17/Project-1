def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        L.append(int(input()))
    return L
def Search(L):
    min=L[0]
    max=L[0]
    for x in L:
        if x<min:
            min=x
        elif x>max:
            max=x
    return min,max
def Output(min,max):
    print(max,min)
L=Input()
min,max=Search(L)
Output(min,max)