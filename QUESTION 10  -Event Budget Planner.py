# Event Budget Planner
# Fixed expenses
Hall_Rental = float(input("Enter the Hall Rental charge in LKR: "))
Deco_Cost = float(input("Enter the Decoration cost in LKR: "))
Sound_Rental = float(input("Enter the Sound System rental cost in LKR: "))

# Variable expenses based on attendance
Guests = int(input("Enter the total number of guests: "))
Food_Per_Person = float(input("Enter the food cost per person in LKR: "))

# Calculations
Total_Food_Cost = Guests * Food_Per_Person
Total_Budget = Hall_Rental + Deco_Cost + Sound_Rental + Total_Food_Cost

# Budget Breakdown Display
print("\n--- TOTAL EVENT BUDGET PLAN ---")
print("Hall Rental Cost           : ", Hall_Rental, " LKR")
print("Decoration Expenses        : ", Deco_Cost, " LKR")
print("Sound System Rental        : ", Sound_Rental, " LKR")
print("Total Catering Cost (x", Guests, ") : ", Total_Food_Cost, " LKR")
print("Estimated Total Event Cost : ", Total_Budget, " LKR")