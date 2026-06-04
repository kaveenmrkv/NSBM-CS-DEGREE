#Electricity Bill Calculator

#V01


#Consumed Units
CU=int(input("Enter the Consumed Electricity Units:"))
float(CU)
if CU<=30:
    #total bill
    TC=CU*20
    print("Total Bill Amount is : " , TC , " LKR")
    print(CU, ": Units Consumed")
elif CU<=60:
    #total bill
    pt1=30*20
    RC=CU-30
    pt2=RC*40
    TC=pt1+pt2
    print("Total Bill Amount is : " , TC , " LKR")
    print(CU, ": Units Consumed")
else:
    #total bill
    pt1=30*20
    RC=CU-30
    pt2=RC*40
    RC=CU-60
    pt3=RC*60
    TC=pt1+pt2+pt3
    print("Total Bill Amount is : " , TC , " LKR")
    print(CU, ": Units Consumed")


#v02

#Consumed Units
CU=int(input("Enter the Consumed Electricity Units:"))
if CU<60:
    if CU<30:
        #total bill
        TC=CU*20
        print("Total Bill Amount is : " , TC , " LKR")
        print(CU, ": Units Consumed")
    else:
        #total bill
        pt1=30*20
        RC=CU-30
        pt2=RC*40
        TC=pt1+pt2
        print("Total Bill Amount is : " , TC , " LKR")
        print(CU, ": Units Consumed")
else:
    #total bill
    pt1=30*20
    pt2=30*40
    RC=CU-60
    pt3=RC*60
    TC=pt1+pt2+pt3
    print("Total Bill Amount is : " , TC , " LKR")
    print(CU, ": Units Consumed")

