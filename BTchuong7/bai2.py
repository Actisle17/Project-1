L=input()
L= " ".join(L.split()) #Xoa khoang trang thua
L=L.replace(" ,",",")#Xoa khoang trang truoc dau phay
L=L.capitalize() #Viet hoa chu cai dau tien
L=L.replace(" ;",";")
L=L.replace(" :",":")
L=L.replace(" .",".")
print(L)