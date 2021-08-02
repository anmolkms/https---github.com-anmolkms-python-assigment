a=int(input("1st num"))
b=int(input("2nd num"))
c=int(input("3rd num"))
gtr=0
if a>b and a>c:
    gtr=a
elif b>a and b>c:
    gtr=b
else:
    gtr=c
print('greatest nub is',gtr)
