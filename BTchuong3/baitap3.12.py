n=int(input())
k=10
j=1
while n>=k:
    k=k*10
    j=j+1
x=10**(j-1)
while x>1/10:
    y=n//x
    if y==0: print('A',end='')
    if y==1: print('B',end='')
    if y==2: print('C',end='')
    if y==3: print('D',end='')
    if y==4: print('E',end='')
    if y==5: print('F',end='')
    if y==6: print('G',end='')
    if y==7: print('H',end='')
    if y==8: print('K',end='')
    if y==9: print('L',end='')
    n=n%x
    x=x/10