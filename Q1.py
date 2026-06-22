#electricity bill calculator
cus=5
tot=0 
while cus>0:
    uc=int(input("Enter the units consumed : "))
    if uc<100:
        cost=uc*10
    elif uc<200:
        cost1=100*10
        rc=uc-100
        cost2=rc*15
        tc=cost1+cost2
    else:
        cost1=100*10
        cost2=100*15
        rc=uc-200
        cost3=rc*20
        tc=cost1+cost2+cost3
    cus=cus-1
    print("The total bill amount is : ", tc , " LKR")
    tot=tot+tc
print("The total bill amount is of all customers : ", tot , " LKR")
        
