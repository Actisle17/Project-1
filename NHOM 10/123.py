def tachphantu(n):
    T = []
    i = 0
    while i < len(n):
        if n[i].isdigit(): 
            t = ""
            while i < len(n) and (n[i].isdigit() or n[i] == "."):
                t += n[i]
                i += 1
            T.append(t)
        elif n[i] in ['+', '-', '*', '/', '(', ')']: 
            T.append(n[i])
            i += 1
        elif n[i].isspace():
            i += 1
            return None
    return T
def pre(chr):
    if chr == '+' or chr == '-' or chr=='*' or chr=='/':
        return chr
    else:
        return None 
def chuyendoi(T):
    chr = []
    so = []
    for t in T:
        if t.isdigit():
            so.append(t)
        elif t in ['+', '-', '*', '/']: 
            while chr and chr[-1] != '(' and pre(t) < pre(chr[-1]):
                so.append(chr.pop())
            chr.append(t)
        elif t == '(':
            chr.append(t) 
        elif t == ')': 
            while chr and chr[-1] != '(':
                so.append(chr.pop())
            if chr and chr[-1] == '(':
                chr.pop()
    while chr: 
        so.append(chr.pop())
    return so


n = input()
T = tachphantu(n)
t= chuyendoi(T)
print(t)
