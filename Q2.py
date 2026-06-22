#student attendance
count=10
ec=0
nec=0
tot=0
while count>0:
    att=int(input("Enter the attendance precentage : "))
    if att>=75:
        ec=ec+1
    else:
        nec=nec+1
    count=count-1
    tot=tot+att
avg=tot/10
    
print("The total number of eligible students is  : ", ec)
print("The total number of non-eligible students is  : ", nec)
print("The average student attendance perecentage is ", avg)
        
