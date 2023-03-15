a=int(input("Tieu thu="))
if 1<=a<=100:
    giatien=a*550
elif 101<=a<=150:
    giatien=100*550+(a-100)*750
elif 151<=a<=200:
    giatien=100*550+50*750+(a-150)*950
elif 201<=a:
    giatien=100*550+50*750+50*950+(a-200)*1350
VAT=giatien*0.1
print("Phaitra=",giatien+VAT,sep="")