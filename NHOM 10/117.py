import sys
#khởi tạo biến
n = 0
x_sum = 0
y_sum = 0
xy_sum = 0
x_tongbinhphuong = 0
#đầu vào từ người dùng
while True:
    x_str = input("Nhập tọa độ x: ")
    if x_str == "":
        break
    y_str = input("Nhập tọa độ y: ")
    try:
        x = float(x_str)
        y = float(y_str)
    except ValueError:
        print("Đầu vào không hợp lệ")
        sys.exit(1)
    #Cập nhật tổng
    n += 1
    x_sum += x
    y_sum += y
    xy_sum += x * y
    x_tongbinhphuong += x ** 2
# Tính độ dốc
m = (xy_sum - x_sum * y_sum / n) / (x_tongbinhphuong - x_tongbinhphuong / n)
b = y_sum / n - m * x_sum / n

print("y = {}x + {}.".format(round(m,2), round(b,2)))