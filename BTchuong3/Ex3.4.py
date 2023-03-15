a=int(input())
b=int(input())
c=int(input())
s=(a*2+b*3+c)/6
if s<3:
    print("Kem")
elif 3<=s<5:
    print("Yeu")
elif 5<=s<6:
    print("Trung binh")
elif 6<=s<7:
    print("Trung binh kha")
elif 7<=s<8:
    print("Kha")
elif 8<=s<9:
    print("Gioi")
else:
    print("Xuat sac")