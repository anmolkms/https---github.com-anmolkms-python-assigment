#a=10
#b=20.5
#a=True
#b=True
a=int(input('Enter 1st no;'))
b=int(input('Enter 2nd no;'))
sum=a+b
print('add',sum)
print('sub',a-b)
print('multi',a*b)
#if not b==0
if b:
    print('div',a/b)
    print('floor',a//b)
    print('reminder',a%b)
else:
    print("div",0)
    print("floor",0)
    print("reminder",0)
pow=a**b
print('power value :',pow)
