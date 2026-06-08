#Grade Classification
RoomA=1
id=str(input("Is the ID VAILD (Y/N) :"))
ap=str(input("Is the Advanced payment done (Y/N) :"))
nights=int(input("Enter the nights count that the customer is staying : "))
if RoomA==1:
    if id=="Y":
        if ap=="Y":
            if nights>=1:
                print("Successfully Checked IN")
            else:
                print("Check IN Failed")
        else:
            print("Check IN Failed")
else:
    print("Successfully Checked IN")
