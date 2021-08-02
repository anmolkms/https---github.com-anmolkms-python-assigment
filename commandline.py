from sys import argv
print(type(argv),argv)
sum=0
for a in argv[1:]:
    sum+=eval(a)
print("sum of all CLA are",sum)
