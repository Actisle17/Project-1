n=int(input("n="))
A=[]
for i in range(n):
    A.append(int(input()))
sum=0
for i in range(n-1):
    if i%2!=0:
        sum=sum+A[i]
print("Tong=",sum,sep="")