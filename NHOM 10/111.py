print('Nhap:')
n=input()
L=[]
def loai_bo(n):
    ki_tu = [',', '.', '?', '-', '\'', '!', ';', ':']
    for p in ki_tu:
        n = n.replace(p, ' ')
    L = n.split()
    return L
L= loai_bo(n)
print(L)

