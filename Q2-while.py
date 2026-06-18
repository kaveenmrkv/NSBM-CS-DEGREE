#Plane Temp MGMT SYSTEM
"""
#engine count
ecount=int(input("Enter Engine Count : "))
safe_e=0
main_e=0
while ecount>0:
    tmp=int(input("Enter Engine Temp : "))
    if tmp>200:
        if tmp<800:
            print("Engine ", ecount ," :safe")
            safe_e=safe_e+1
            ecount=ecount-1
        else:
            print("Engine ", ecount ,":Maintainance Required")
            main_e=main_e+1
            ecount=ecount-1
    
    else:
        print("Engine ", ecount ,":Maintainance Required")
        main_e=main_e+1
        ecount=ecount-1

    
#Finale Output
print("Safe Engines : ", safe_e)
print("Maintenance Required : ", main_e)

"""
#----------------------------

#engine count
ecount=1
safe_e=0
main_e=0

while ecount<=4:
    tmp=float(input("Enter Engine Temp : "))
    if tmp>200 and tmp<850:
        print("Engine ", ecount ," :safe")
        safe_e=safe_e+1
    else:
        print("Engine ", ecount ,":Maintainance Required")
        main_e=main_e+1
    ecount=ecount+1

    
#Finale Output
print("Safe Engines : ", safe_e)
print("Maintenance Required : ", main_e)
