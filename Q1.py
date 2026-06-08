#Voting Eligibility Verification
#age
age=int(input("Enter Your Age : "))
cit=str(input("Are you a Citizen (Y/N)"))
nic=str(input("Is your NIC Vaild (Y/N)"))

if age>=18:
    if cit=="Y":
        if nic=="Y":
            print("You are Eligible to Vote")
        else:
            print("You are not Eligible to Vote")
    else:
        print("You are not Eligible to Vote")
        
else:
    print("You are not Eligible to Vote")
        
