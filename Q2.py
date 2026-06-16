#Bonus Calculator
#Salary AMT
S=float(input("Enter The Salary Amount :"))
if S>=100000:
    bonus=S*(15/100)
    print("Bonus Amount is :", bonus ,"LKR" )
elif S>50000:
    bonus=S*(10/100)
    print("Bonus Amount is :", bonus ,"LKR" )
else:
    bonus=S*(5/100)
    print("Bonus Amount is :", bonus ,"LKR" )
