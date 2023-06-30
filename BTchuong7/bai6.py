chuoi=input()
phantu=chuoi.split(",") #Tach chuoi boi dau phay
L=[] #Danh sach cac so chia het cho 3
for i in range(len(phantu)):
    thapphan=int(phantu[i],2)  
    if thapphan%3==0:
        L.append(phantu[i])  
if len(L)>0:
    Output=",".join(L)
    print(Output)
else:
    print()