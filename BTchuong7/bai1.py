L=input()
Inhoa=0
Inthuong=0
Chuso=0
Khac=0
for i in L:
    if i.isupper():
        Inhoa+=1
    elif i.islower():
        Inthuong+=1
    elif i.isdigit():
        Chuso+=1
    else:
        Khac+=1
print("In hoa:",Inhoa) 
print("In thuong:",Inthuong)
print("Chu so:",Chuso)
print("Khac:",Khac)