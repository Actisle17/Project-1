n=int(input(""))
if 1<=n<=10**6:
    tong=0
    for i in range (1,n+1):
        if i%2!=0:
            tong=tong+i
    print(tong)