n=input('Nhap: ')
L=[]
def chuyen_doi(n):
    L = n.split()
    for i in range(len(L)):
        t = L[i]
        d = ''
        if not t[-1].isalpha():
            d = t[-1]
            t = t[:-1]
        
        viet = ''
        if t[0].isupper():
            viet = 'title'
            t = t.lower()
        
        if t[0] in 'aeiou':
            t = t + 'yay'
        else:
            t = t[1:] + t[0] + 'ay'
        
        if viet == 'title':
            t = t.title()
        t = t + d
        
        L[i] = t
    pig_latin = ' '.join(L)
    return pig_latin

print(n,'se tro thanh',chuyen_doi(n))
