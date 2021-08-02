a=input("Enter true/false,t/f,1/0-")
if a.lower()=="true" or "t" or "1":
    a= True
elif a.lower()=="false" or "f" or "0":
    a= False
else:
    print("invalid entry") 
z=int(a)
print("value in int is :-",z)
b=float(a)
print("value in float is-",b)
c=str(a)
print("value in str is-",c)
e=complex(a)
print("value in complex is-",e)
print(type(e))
