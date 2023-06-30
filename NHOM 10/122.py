def token(day):
    tokens = []
    i = 0
    while i < len(day):
        if day[i].isspace():  # bỏ qua khoảng trắng
            i += 1
            continue
        elif day[i] in "+-*/^()":  # toan tu va dau ngoac don
            tokens.append(day[i])
            i += 1
        else:  # numbers
            start = i
            while i < len(day) and day[i].isdigit():
                i += 1
            tokens.append(day[start:i])
    return tokens
day = input()
tokens = token(day)
print(tokens)