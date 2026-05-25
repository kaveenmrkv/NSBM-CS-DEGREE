# Cinema Ticket Booking System
# Ticket quantities
Num_Adult = int(input("Enter the number of Adult tickets: "))
Num_Child = int(input("Enter the number of Child tickets: "))

# Ticket prices
Price_Adult = float(input("Enter the price of an Adult ticket in LKR: "))
Price_Child = float(input("Enter the price of a Child ticket in LKR: "))

# Snack package cost
Snack_Cost = float(input("Enter the total snack package cost in LKR: "))

# Calculations
Total_Adult_Price = Num_Adult * Price_Adult
Total_Child_Price = Num_Child * Price_Child
Total_Ticket_Cost = Total_Adult_Price + Total_Child_Price
Final_Payment = Total_Ticket_Cost + Snack_Cost

# Detailed Bill Display
print("\n--- CINEMA DETAILED BILL ---")
print("Adult Tickets (x", Num_Adult, ")       : ", Total_Adult_Price, " LKR")
print("Child Tickets (x", Num_Child, ")       : ", Total_Child_Price, " LKR")
print("Total Ticket Subtotal      : ", Total_Ticket_Cost, " LKR")
print("Snack Package Charges      : ", Snack_Cost, " LKR")
print("Total Booking Amount       : ", Final_Payment, " LKR")