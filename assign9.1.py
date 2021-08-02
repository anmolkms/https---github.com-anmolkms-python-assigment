n=int(input('Enter no. of tickets'))
n1=int(input('Enter no. of senior citizens'))
n2=int(input('Enter no. of childs'))
n3=int(input('Enter no. of minors'))
n4=n-(n1+n2+n3)                                                                 
p=int(input('Enter the price of single ticket'))                                   
print('Total price of tickets is :',p*n)
if n1<=n :
    d=20
    fp1=n1*(p-(p*d/100))
    print('senior citizen will get 20% discount.')      
    print('the price of tickets after discount is :',fp1)
    if n2<=(n-n1) :
        d=100
        fp2=n2*(p-(p*d/100))
        print('child will get 100% discount.')  
        print('the price of tickets after discount is :',fp2)
        if n3<=(n-(n1+n2)) :
            d=50
            fp3=n3*(p-(p*d/100))
            print('minors will get 50% discount.')     
            print('the price of tickets after discount is :',fp3)
            if n4!=0:                                                            
                d=0
                fp4=n4*(p-(p*d/100))
                print('adults will not get any discount.')           
                print('the price of tickets after discount is :',fp4)
                print('Final price of all the tickets is :',(fp1+fp2+fp3+fp4))
else: print('invalid entry')                                
