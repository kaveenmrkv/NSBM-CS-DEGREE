#Plane Temp MGMT SYSTEM

E_01=float(input("Enter Engine 1 Temp in Celecius: "))
E_02=float(input("Enter Engine 2 Temp in Celecius: "))
E_03=float(input("Enter Engine 3 Temp in Celecius: "))
E_04=float(input("Enter Engine 4 Temp in Celecius: "))
safe_e=0
main_e=0

#engine01

if E_01>200:
    if E_01<800:
        print("Engine 1:safe")
        safe_e=safe_e+1
    else:
        print("Engine 1:Maintainance Required")
        main_e=main_e+1

else:
     print("Engine 1:Maintainance Required")
     main_e=main_e+1

#engine02

if E_02>200:
    if E_02<800:
        print("Engine 2:safe")
        safe_e=safe_e+1
    else:
        print("Engine 2:Maintainance Required")
        main_e=main_e+1

else:
     print("Engine 2:Maintainance Required")
     main_e=main_e+1

#engine03

if E_03>200:
    if E_03<800:
        print("Engine 3:safe")
        safe_e=safe_e+1
    else:
        print("Engine 3:Maintainance Required")
        main_e=main_e+1

else:
     print("Engine 3:Maintainance Required")
     main_e=main_e+1

#engine04

if E_04>200:
    if E_04<800:
        print("Engine 4:safe")
        safe_e=safe_e+1
    else:
        print("Engine 4:Maintainance Required")
        main_e=main_e+1

else:
     print("Engine 4:Maintainance Required")
      main_e=main_e+1

#Finale Output
print("Safe Engines : ", safe_e)
print("Maintenance Required : ", main_e)


        
