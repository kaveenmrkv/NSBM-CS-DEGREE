#Online SHopping Discount
#Member Status
MS=str(input("Enter Customers Status :"))
PA=float(input("Enter The Purchase Amount in LKR :"))
if MS=="premium":
    if PA>=10000:
        print("20% Discount Applied")

    else:
        print("10% Discount Applied")
else:
    print("No discount Available")


    
#------------------------------ver02

#Member Status
MS=str(input("Enter Customers Status if premium (Y) Else (N):"))
PA=float(input("Enter The Purchase Amount in LKR :"))
if MS=="Y":
    if PA>=10000:
        print("20% Discount Applied")

    else:
        print("10% Discount Applied")
else:
    print("No discount Available")


