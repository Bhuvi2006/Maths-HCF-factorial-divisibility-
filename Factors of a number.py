n=int(input("Enter the number: "))
fact=1
print("The factors of",n,"are:".format(n))
while n>=1:
    if n%fact==0:
        print("{0}".format(fact))
        
    fact+=1
