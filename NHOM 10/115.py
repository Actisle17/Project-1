
def nhap():
    cumtu=input("nhap:")
    words=cumtu.split()
    return words
def pig_latin(word):
    nguyenam = "aeiou"
    if word[0] in nguyenam:
        return word + "way"

    else:
        for i in range(len(word)):
            if word[i] in nguyenam:
                return word[i:] + word[:i] + "ay"
words=nhap()            
for i in range(len(words)):
    words[i] = pig_latin(words[i])
   

print("pig latin: ", " ".join(words))