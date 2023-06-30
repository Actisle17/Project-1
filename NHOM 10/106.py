def Input():
    n=int(input('n='))
    a=int(input('a='))
    while a <= 4:
        print("Moi nhap lai hơn 4 gia tri:")
        a= int(input('a='))
          
    L=[]
    for i in range(a):
        x=int(input())
        L.append(x)
        
    return L,n
def  Loaibo(L,n):
  B=sorted(L)
  B=B[n : -n]
  print(B)
  return B
L,n=Input()
Loaibo(L,n)