from random import shuffle
c=[]
def tao_bo_bai():
    for i in ['s', 'h', 'd', 'c']:
        for x in ['2','3','4','5','6','7','8','9','10','T','J','Q','K','A']:
            c.append(i+x)
    return c
    
def chia_bai(moi_ng):
    bai = tao_bo_bai()
    shuffle(bai)
    t = [[] for _ in range(moi_ng)]
    for i in range(moi_ng):
        for j in range(13):
            t[i].append(bai.pop())
    return t, bai

if __name__ == '__main__':
    moi_ng = 4
    t, c = chia_bai(moi_ng)
    for i in range(moi_ng):
        print("Nguoi " + str(i+1) + ":", end="")
        for card in t[i]:
            print(card + " ", end="")
        print()
    print("cac la bai con lai:", end=" ")
    for card in c:
        print(card + " ", end="")
    print() 
