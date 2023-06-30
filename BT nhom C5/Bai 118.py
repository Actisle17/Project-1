import random

def createDeck():
    deck = []
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck

def shuffleDeck(deck):
    for i in range(len(deck)):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

# Tạo bộ bài và in ra trước khi xáo trộn
deck = createDeck()
print('Bộ bài trước khi xáo trộn:')
print(deck)

# Xáo trộn bộ bài và in ra sau khi xáo trộn
shuffleDeck(deck)
print('Bộ bài sau khi xáo trộn:')
print(deck)


import random
def bobai():
    L = []
    loailist = ['s', 'h', 'd', 'c']
    giatrilist = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for loai in loailist:
        for giatri in giatrilist:
            L.append(giatri + loai)
    return L
def shuff(L):
    n=len(L)
    for i in range(n):
        j=i
        while j==i:
            j=random.randint(0,n-1)
        L[i],L[j]=L[j],L[i]
L=bobai()
shuff(L)
print("Truoc khi xao tron:",L)
print("Sau khi xao tron:",L)
