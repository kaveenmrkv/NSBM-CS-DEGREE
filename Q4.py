#Average of marks
S=0
x=int(input("How many subjects do you want to find the Avg of : "))
while x>0:
    N=int(input("Enter your Mark : "))
    S=S+N
    x=x-1
Avg=S/10
if Avg<50:
    print("Fail")
else:
    print("Pass")
