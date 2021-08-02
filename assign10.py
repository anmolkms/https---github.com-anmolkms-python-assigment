from random import *
l=list()
for i in range(20):
    a=randint(0,30)
    l.append(a)
print(l)
j=0
for j in l:
    if l.count(j)>=1:
       # print(j)
        l.remove(j)
        for w in l:
            print(w)
            
        print(l)
        
