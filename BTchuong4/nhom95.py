import random
def ChonMau():
    n=input('mau cu con/het:')
    return n
def TaoBienSo(n):
    if n=='con':
        for i in range (1,4):
            r=random.randint(65,90)
            chu=chr(r)
            print(chu,end="")
        for i in range (1,4):
            so=random.randint(0,9)
            print(so,end="")
    if n=='het':
        for i in range (1,5):
            so=random.randint(0,9)
            print(so,end="")
        for i in range (1,4):
            r=random.randint(65,90)
            chu=chr(r)
            print(chu,end="")
n=ChonMau()
TaoBienSo(n)