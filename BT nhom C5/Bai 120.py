def is_sorted(lst):
#     """
#     Kiểm tra xem một danh sách đã được sắp xếp theo thứ tự tăng dần hoặc giảm dần hay không.
#     """
    if len(lst) <= 1:
        return True
    
    ascending = True
    descending = True
    
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            ascending = False
        if lst[i] < lst[i+1]:
            descending = False
            
    return ascending or descending

def nhap():
    n=int(input("n="))
    L=[]
    for i in range(n):
        L+=[int(input())]
    return L,n
def sort(L):
    incr=True
    decr=True
    if len(L)<=1:
        return True
    for j in range(len(L)-1):
        if L[j]>L[j+1]:
            incr=False  
        if L[j]>L[j+1]:
            decr=False    
    return incr or decr 
L,n=nhap()
if sort(L):
    print("Danh sách đã được sắp xếp.")
else:
    print("Danh sách chưa được sắp xếp.")
