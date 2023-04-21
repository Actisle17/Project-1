from random import randint
def mk():
    a = randint(7, 10)
    for i in range(a):
        b=chr(randint(33, 126))
        print(b,end='')
print(mk())