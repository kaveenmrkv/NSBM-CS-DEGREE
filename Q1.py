#airport baggage weight extra charges calculator
#Baggage weight input
w=int(input("Enter The baggage weight amount : "))
if w>30 :
    print("The baggage is not allowed")
elif w>21:
    r=w-20
    c=200*r
    print("The charge is :", c, "LKR")
else:
    print("No charges Apply")

    
