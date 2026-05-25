# University Course Fee Calculator
# Number of modules
NM = int(input("Enter the number of modules: "))
# Fee per module
FPM = float(input("Enter the fee per module in LKR: "))
# Library fee
LF = float(input("Enter the library fee in LKR: "))
# Registration fee
RF = float(input("Enter the registration fee in LKR: "))

# Calculations
Total_Module_Fee = NM * FPM
Total_Semester_Fee = Total_Module_Fee + LF + RF

# Payment Summary
print("\n--- SEMESTER FEE PAYMENT SUMMARY ---")
print("Total Module Cost (", NM, "modules) : ", Total_Module_Fee, " LKR")
print("Library Fee                     : ", LF, " LKR")
print("Registration Fee                : ", RF, " LKR")
print("Total Semester Fee Amount       : ", Total_Semester_Fee, " LKR")