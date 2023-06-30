
# Định nghĩa hàm chuyển đổi biểu thức trung tố thành biểu thức hậu tố
def trungto_hauto(expression):
    thu_tu = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    uu_tien = []
    hau_to = []
    for token in expression:
        if token.isdigit():
            hau_to.append(token)
        elif token in thu_tu:
            while uu_tien and uu_tien[-1] != '(' and thu_tu[token] <= thu_tu[uu_tien[-1]]:
                hau_to.append(uu_tien.pop())
            uu_tien.append(token)
        elif token == '(':
            uu_tien.append(token)
        elif token == ')':
            while uu_tien and uu_tien[-1] != '(':
                hau_to.append(uu_tien.pop())
            uu_tien.pop()
    while uu_tien:
        hau_to.append(uu_tien.pop())
    return hau_to
def danhgia_hauto(expression):
    values = []
    for token in expression:
        if token.isdigit():
            values.append(int(token))
        else:
            right = values.pop()
            left = values.pop()
            if token == '+':
                values.append(left + right)
            elif token == '-':
                values.append(left - right)
            elif token == '*':
                values.append(left * right)
            elif token == '/':
                values.append(left / right)
            elif token == '^':
                values.append(left ** right)
    return values[0]

# Đọc biểu thức trung tố từ người dùng
expression = input("Nhập một biểu thức toán học ở dạng trung tố: ")

# Chuyển đổi biểu thức trung tố thành biểu thức hậu tố
postfix_expression = trungto_hauto(expression)

# Đánh giá biểu thức hậu tố
result = danhgia_hauto(postfix_expression)

# In kết quả
print("Kết quả của biểu thức là:", result)