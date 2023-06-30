import random
a=random.randint(1,49)
b=random.randint(1,49) 
b!=a
c=random.randint(1,49)
c!=b and c!=a
d=random.randint(1,49)
d!=c and d!=b and d!=a 
e=random.randint(1,49)
e!=d and e!=c and e!=b and e!=a
f=random.randint(1,49)
f!=e and f!=d and f!=c and f!=b and f!=a
print(a,b,c,d,e,f)