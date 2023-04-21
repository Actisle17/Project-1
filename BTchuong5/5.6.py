A=[]
for i in range(10):
    A.append(int(input()))
B=A.copy()
n=len(B) 
for i in range(0,n-1,2):
    B[i]=A[i+1]
    B[i+1]=A[i]
for i in B:
    print(i,end=" ")