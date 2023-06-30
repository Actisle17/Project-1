L=[]
while True:
    n=input()
    if n =='':
        break
    if n not in L:
        L=L+[n]
for n in L:
    print(n)
     