#Grade Classification
SM=int(input("Enter the Student Marks: "))
if SM>=50:
    if SM>64:
        if SM>74:
              print("Grade A")
        else:
            print("Grade B")
    else:
        print("Grade C")
else:
    print("Failed")
            
