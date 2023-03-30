while True:
    n=int(input(""))
    if n<0:
        break
    j=1
    for i in range (1,n+1):
        j=j*i
    print(j)