ngay=int(input())
toi=int(input())
cuoituan=int(input())
tonga=ngay+toi+cuoituan
tongb=ngay+toi+cuoituan
if ngay>=100:
    tonga=(25*(ngay-100)+(15*toi)+(20*cuoituan))
if ngay>=250:
    tongb=(45*(ngay-250)+(35*toi)+(25*cuoituan))
print(tonga)
print(tongb)