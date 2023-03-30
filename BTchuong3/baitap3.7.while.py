while True:
    n=int(input(""))
    if n<0:
        break
    j=1
    i=1
    while i<=n:
        j=j*i
        i=i+1
    print(j)