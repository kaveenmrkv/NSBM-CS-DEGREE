#SUM of 10 numbers
S=0
x=int(input("How many numbers do you want to find the sum of : "))
while x>0:
    N=int(input("Enter your Number : "))
    S=S+N
    x=x-1
print("The Sum of the numbers is :", S)
