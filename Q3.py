#Employee Promotion System
#Performance Score
EP=float(input("Enter the Employees Performance Score Percentage : "))
#Years of Service
YS=int(input("Enter the years of service : "))
if EP>=85:
    if YS>=3:
        print("Promotion Approved")
    else:
        print("More Expirience Needed")
else:
    print("Performance Improvement Required")
