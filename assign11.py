choice='y'
while choice.lower()=="yes" or choice.lower()=="y":
    a=(input("enter the student name"))
    mark1=float(input("enter the student mark in sub1"))
    mark2=float(input("enter the student mark in sub2"))
    mark3=float(input("enter the student mark in sub3"))
    if mark1<=100 and mark2<=100 and mark3<=100:
        total=(mark1+mark2+mark3)
        print("student name:-",a)
        print("total mark is:-",total)
        avg=total/3
        print("the avg is:-",avg)
        if avg<=100.0 and avg>=95.0:
            grade="A1"
            print("Your grade is A+")
        elif avg<95 and avg>90:
            grade="A2"
            print("Your grade is A")
        elif avg<90 and avg>80:
            grade="B1"
            print("Your grade is B+")
        elif avg<80 and avg>70:
            grade="B2"
            print("Your grade is B")
        elif avg<70 and avg>60:
            grade="C"
            print("Your grade is C")
        elif avg<60 and avg>45:
            grade="D"
            print("Your grade is D")
        elif avg<45 and avg>30:
            grade="E"
            print("Your grade is E")
        else:
            grade="F"
            print("Your grade is F")
        if grade=="F":
            print("Your status is :- Oops you just missed you are fail")
        else:
            print("your status is:- congrats you are pass")
        
    else:
        print("enter a valid mark,(each subject carry 100 mark)")

    choice=input("do want to continue(yes/y/no/y)")
else:
    print('you can go now')
print('the end')
