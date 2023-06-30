#Mot danh sach va mot tu, chen phan tu vao truoc moi phan tu trong danh sach
#In: dong 1 day tu cach nhau 1 khoang trang, dong 2 1 tu
#Out: In danh sach moi
#Red Green Black / Blue -> Blue Red Blue Green Blue Black
a=str(input())
b=str(input())
A=[]
B=a.split(" ")
i=0
while i<len(B):
    A=A+b.split()+[B[i]]
    i=i+1
print(A)

print('---')

# n = input()
# a = input()
# n = n.split()
# A = []
# for i in n:
#     A = A + [a]
#     A = A + [i]
# print(A)