n=int(input('Enter no. of tickets'))
print("So the total no of person is",n)
choice=input("yes,y/No,n")
choice=choice.strip()
if choice.lower()=="yes" or choice.lower()=="y":
    price=int(input('Enter price of the tickets'))
    n2=int(input('enter the age of 1st person'))
    if n2>=65:
        print("you are a senior citizen so we respect your age so you get 20% discount")
        price1=price-(price*0.2)
        print("After discount the price is",price1)
    elif n2<=5:
        print("you are a child  so you get 100% discount  means free")
        price1=0
        print("After discount the price is",price1)
    elif n2>5 and n2<=11:
        print("you are a minor  so you get 50% discount")
        price1=price-(price*0.5)
        print("After discount the price is",price1)
    elif n2>=18 and n2<65:
        print("you are a adult  so you get 0% discount  don't cry if you are adult now")
        price1=price
        print("After discount the price is",price1)
    else:
        print("invalid entry")
    n3=int(input('enter the age of 2nd person'))
    if n3>=65:
        print("you are a senior citizen so we respect your age so you get 20% discount")
        price2=price-(price*0.2)
        print("After discount the price is",price2)
    elif n3<=5:
        print("you are a child  so you get 100% discount  means free")
        price2=0
        print("After discount the price is",price2)
    elif n3>5 and n2<11:
        print("you are a minor  so you get 50% discount")
        price2=price-(price*0.5)
        print("After discount the price is",price2)
    elif n2>=18 and n2<65:
        print("you are a adult  so you get 0% discount  don't cry if you are adult now")
        price2=price
        print("After discount the price is",price2)
    else:
        print("invalid entry")
    n4=int(input('enter the age of 3rd person'))
    if n4>=65:
        print("you are a senior citizen so we respect your age so you get 20% discount")
        price3=price-(price*0.2)
        print("After discount the price is",price3)
    elif n4<=5:
        print("you are a child  so you get 100% discount  means free")
        price3=0
        print("After discount the price is",price3)
    elif n4>5 and n2<=11:
        print("you are a minor  so you get 50% discount")
        price3=price-(price*0.5)
        print("After discount the price is",price3)
    elif n4>=18 and n2<65:
        print("you are a adult  so you get 0% discount  don't cry if you are adult now")
        price3=price
        print("After discount the price is",price3)
    else:
        print("invalid entry")
    finalprice=0
    finalprice= price1+price2+price3
    print("Final price is",finalprice)

elif choice.lower()=="no" or choice.lower()=="n":
    print("you cannot go with out ticket ok i put you in jail get lost")
else:
    print("wrong entry")
    print("you can go now bye")
