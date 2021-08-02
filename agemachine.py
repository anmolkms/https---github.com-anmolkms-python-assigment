#notimes=int(input("enter the time:"))
#count=1
#while count<=notimes:
choice='y'
while choice.lower()=="yes" or choice.lower()=="y":
    age=int(input("enter age"))
    gender=input("enter gender")
    if age>65:
        if gender=="f":
            print('hi grandmaa')
        else:
            print('hi grandfather')
    elif age>31 and age<65:
        if gender=="f":
            print('hi anty')
        else:
            print('hi uncle')
    elif age>=18 and age<30:
        if gender=="f":
            print('hi didi')
        else:
            print('hi bhai')
    else:
        print('hi kid')
    choice=input("do want to continue(yes/y/no/y)")
#count==1
else:
    print('you can go now')
print('the end')
        
