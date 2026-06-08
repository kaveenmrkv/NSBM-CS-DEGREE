#Online Exam Access 
reg=str(input("IS the student Registered (Y/N): "))
EF=str(input("Exam Fee Paid or NOT (Y/N): "))
if reg=="Y":
    if EF=="Y":
        print("Eligible for the Exam")
    else:
         print("NOT Eligible for the Exam")
else:
    print("NOT Eligible for the Exam")
        
