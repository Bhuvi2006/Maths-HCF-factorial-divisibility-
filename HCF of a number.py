
#HCF of a number
n=int(input("Enter a number: "))
n1=int(input("Enter another number:"))
if n>n1:
    smallno=n1
else:
    smallno=n
for i in range(1,smallno+1):
    if((n%i==0) and(n1%i==0)):
        hcf=i
print("The HCF of",n,"and",n1,"is",hcf)
