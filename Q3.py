#Loan Approval System
sal=int(input("Enter Your Monthly Salary in LKR: "))
CS=float(input("Enter Your Credit Score: "))
if sal>=50000:
    if CS>=700:
        print("Eligible for the Loan")
    else:
         print("NOT Eligible for the Loan")
else:
    print("NOT Eligible for the Loan")
        
