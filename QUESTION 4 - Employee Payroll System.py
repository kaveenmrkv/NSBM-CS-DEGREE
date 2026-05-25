#Employee Payroll System
#Basic Salary
BS=float(input("Enter the Basic Salary Amount in LKR : "))
#OT Hours
OT=float(input("Enter the OT Hours Amount : "))
#OT Rate
OTR=float(input("Enter the OT Rate in LKR : "))
#Bonus
B=float(input("Enter the bonus amount in LKR : "))
#Tax
TAX=float(input("Enter the tax percentage : "))
TAX_amt=TAX/1000
#net salary
NS=(BS+(OT*OTR)+B)-((BS+(OT*OTR)+B)*TAX_amt)
print("The Net Salary is : ",NS)
