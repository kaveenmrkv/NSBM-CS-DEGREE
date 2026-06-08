#ATM CAHS WITHDRAWAL
pin=str(input("Enter Your Bank Pin : "))
AB=20000
if pin=="1234":
    WA=int(input("Enter Withdrawal Amount : "))
    if WA<AB:
        print("You have Sufficient Balance for a withdrawal")
        rem=AB-WA
        print(WA, " LKR Withdrawn &", rem,  "LKR Remaining")
    else:
         print("Balance Insufficient for withdrawal")
else:
    print("Incorrect PIN")
    
