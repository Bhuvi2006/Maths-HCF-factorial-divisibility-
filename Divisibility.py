n=int(input("Enter the number: "))
n1=int(input("Enter the range: "))
print("The numbers that are divisible:-")
for i in range(n1+1):
    if i%n==0:
        print(i)
        
