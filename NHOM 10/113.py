def nhap():
    items=input("nhap loai qua:")
    L=items.split(",")
    return L
def format_list(L):
    if len(L)==0:
        return ""
    elif len(L)==1:
        return L[0]
    elif len(L)==2:
        return L[0]+" and " + L[1]
    else:
        return ", ".join(L[:-1])+" and "+ L[-1]
L=nhap()
print(format_list(L))
