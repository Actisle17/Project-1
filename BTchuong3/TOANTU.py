a=int(input())
b=int(input())
dem=0
for i in range (b-1,a,-1):
    if i%3==0:
        dem=dem+1
        print(i,end=" ")
if dem<1:
    print("NOT FOUND")
        