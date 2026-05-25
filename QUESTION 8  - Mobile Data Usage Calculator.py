# Mobile Data Usage Calculator
# Data usage in GB
DU = float(input("Enter the data usage in GB: "))
# Cost per GB
CPG = float(input("Enter the cost per GB in LKR: "))
# Additional service charges
ASC = float(input("Enter the additional service charges in LKR: "))

# Calculations
Data_Cost = DU * CPG
Final_Bill = Data_Cost + ASC

# Bill Details Display
print("\n--- INTERNET BILL SUMMARY ---")
print("Data Usage Cost (", DU, "GB)     : ", Data_Cost, " LKR")
print("Additional Service Charges    : ", ASC, " LKR")
print("Final Internet Bill Amount    : ", Final_Bill, " LKR")