"""
sum=0
a=input("enter a nub").split("/")
print(a)
for i in a:
    sum+= int(i)
print("sum of all element is list",sum)
b=input("enter a 2 nub").split(",")
c=eval(b[0])+eval(b[1])
print("sum value is",c)
"""
a=input("enter the expression")
print("result is",eval(a))
b=input("enter nub").split()
for i in b:
    print(type(eval(i)),eval(i))
