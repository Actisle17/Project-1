chuoi = input()
for kihieu in chuoi.split():
    if "@" in kihieu and "." in kihieu:
        print("Email:", kihieu)
        break
else:
    print()