sum=0
count=0
while True:
    gia_tri=int(input())
    if gia_tri!=0:
        sum=sum+gia_tri
        count=count+1
    else:
        break
if count==0:
    print("loi")
else:
    print("tbc=",sum/count)