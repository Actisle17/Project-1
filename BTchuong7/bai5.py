nhap= input()
x = int(input())
# Tách chuỗi số thành một danh sách các số nguyên
dsach = [int(num) for num in nhap.split()]
# Tìm vị trí của số X trong danh sách
vitri = [i+1 for i in range(len(dsach)) if dsach[i] == x]
# Kiểm tra nếu không tìm thấy X trong danh sách
if not vitri:
    print(0)
else:
    for i in vitri:
        print(i)