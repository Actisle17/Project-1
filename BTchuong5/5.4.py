n=int(input("n="))
A=[]
for i in range(n):
    A.append(int(input()))
B=A[::-1]
print(B)
B.sort()
print(B)