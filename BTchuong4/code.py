#Nhập A B, tính tổng trong khoảng A và B
A=int(input())
B=int(input())
if A<=B and A>0 and B>0:
    s=0
    for i in range(A+1,B+1):
        s=s+i
    print(s)
        
        
#Đếm số chia hết cho 3 và 5
n=int(input())
if 0<=n<=10**6:
    dem=0
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            dem=dem+1
    print(dem)

#In ra số chẵn
n=int(input())
if n>=0 and n<=10**6:
    s=0
    for i in range(1,n+1):
        if i%2==0:
            s=s+i
    print(s)
    

#else if
a=float(input())
b=float(input())
n=float(input())
if a+b==n:
    print("+")
elif a-b==n:
    print("-")
elif a*b==n:
    print("*")
elif a/b==n and b!=0:
    print("/")
else:
    print("NO")

#bài 4
n=int(input())
s=0
a=list(str(n))
k=len(str(n))
ch=0
if k>1:
    for i in range(k-2,k,1):
        ch=ch+int(a[i])
    print(ch)
else:
    print('0')