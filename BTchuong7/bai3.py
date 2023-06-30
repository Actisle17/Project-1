import re
chuoi=input()
if len(chuoi)<6 or len(chuoi)>17:
    print("False")
elif not re.search("[a-z]", chuoi):
    print("False")
elif not re.search("[0-9]", chuoi):
    print("False")
elif not re.search("[A-Z]", chuoi):
    print("False")
elif not re.search("[$#@]", chuoi):
    print("False")
else:
    print("True")